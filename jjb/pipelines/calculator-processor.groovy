node {
    String code
    String status_file = 'state/calculator_status.dat'

    stage('Load code') {
        dir('python-on-jenkins') {
            git(
                poll: false,
                url: 'https://github.com/ifireball/python-on-jenkins.git'
            )
            code = readFile 'scripts/calculator_processor.py'
        }
    }
    stage('Load data') {
        dir('state') { deleteDir(); touch(file: '_dummy_') }
        step([
            $class: 'CopyArtifact',
            filter: status_file,
            fingerprintArtifacts: true,
            projectName: env.JOB_NAME,
            optional: true,
        ])
    }
    stage('Run python') {
        withEnv([
            'PYTHONPATH=python-on-jenkins/scripts',
            "CALCULATOR_STATUS=$status_file"
        ]) {
            sh code
        }
    }
    stage('Save data') {
        archive status_file
    }
}
