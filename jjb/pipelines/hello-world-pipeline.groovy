node {
    stage('Say hello') {
        sh """\
            echo 'Hello world!'
        """
    }
}
