node {
    stage('Say hello') {
        sh """\
            #!/usr/bin/env python
            from __future__ import print_function

            print('Hello world!')
        """.stripIndent()
    }
}
