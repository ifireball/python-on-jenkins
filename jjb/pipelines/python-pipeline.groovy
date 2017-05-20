@Grab(group='org.python', module='jython-standalone', version='2.7.0')
import org.python.util.PythonInterpreter
import org.python.core.PyObject
import org.python.core.PyString
import org.python.core.adapter.ClassicPyObjectAdapter

def main() {
    PyObject pyfunc
    def out
    stage('load') {
        pyfunc = loadPython()
    }
    stage('call') {
        out = callPython(pyfunc, 'From Groovy to Python')
    }
    stage('report') {
        echo "From python:\n${out}"
        echo "this is: ${this.class}"
        steps.invokeMethod('echo', "steps is: ${steps.class}")
        // print "this.sleep: ${this.sleep}"
    }
}

@NonCPS
def loadPython() {
    PythonInterpreter interpreter = new PythonInterpreter()
    // interpreter.exec("from Building import Building");
    // buildingClass = interpreter.get("Building");
    //def hello = interpreter.eval("'Hello from python'")
    interpreter.exec """\
        def star_str(pipeline, steps, s):
            rv = "\\n".join(("*" * len(s), s, "*" * len(s)))
            pipeline.invokeMethod('echo', "Python printing:\\n{}".format(rv))
            # steps.echo("Python printing:\\n{}".format(rv))
            pipeline.print(repr(dir(pipeline)))
            pipeline.print(repr(dir(steps)))
            # pipeline.invokeMethod('sleep', 3)
            print("Stdout from Jython")
            return rv
    """.stripIndent()
    PyObject func = interpreter.get('star_str')
    return func
}

def callPython(PyObject pyfunc, String str) {
    def out = pyfunc.__call__(toPyObject(this), toPyObject(steps), new PyString(str))
    return out
}

@NonCPS
PyObject toPyObject(Object o) {
    ClassicPyObjectAdapter adapter = new ClassicPyObjectAdapter()
    return adapter.adapt(o)
}

main()
