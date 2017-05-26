node {
    String code
    String status_file = 'calculator_status.dat'

    stage('Load code') {
        dir('python-on-jenkins') {
            git(
                poll: false,
                url: 'https://github.com/ifireball/python-on-jenkins.git'
            )
            code = readFile 'jenkins/calculator_processor.py'
        }
    }
    stage('Load data') {
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
            "CALCULATOR_STATUS=$calculator_status"
        ]) {
            sh code
        }
    }
    stage('Save data') {
        archive status_file
    }
}
