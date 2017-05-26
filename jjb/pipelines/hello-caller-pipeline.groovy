node {
    stage('Run python') {
        sh '''\
            #!/usr/bin/env python
            from __future__ import print_function
            from os import environ
            import json

            first_name = environ.get('FIRST_NAME', 'small')
            last_name = environ.get('LAST_NAME', 'world')
            name = ' '.join([first_name, last_name])

            build_spec = dict(
                job='hello-world-with-params',
                parameters=[{
                '$class': 'StringParameterValue',
                'name': 'YOUR_NAME',
                'value': name,
                }]
            )
            with open('build_spec.json', 'w') as f:
                json.dump(build_spec, f)
        '''.stripIndent()
    }
    stage('Launch Job') {
        build readJSON(file: 'build_spec.json')
    }
}

