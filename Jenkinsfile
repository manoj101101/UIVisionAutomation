pipeline {
    agent any

    parameters {
        string(defaultValue: "", description: 'Enter Macro Names', name: 'MACRO_LIST')
    }

    stages {
        stage('build') {
            steps {
                script {
                    def workspacePath = "${WORKSPACE}/src/main/core/"
                    def pythonExecutable = "/usr/local/bin/python3.12"
                    def scriptCommand = "${pythonExecutable} MacroRunner.py --macro ${MACRO_LIST}"

                    catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
                        dir(workspacePath) {
                            def exitCode = sh(script: scriptCommand, returnStatus: true)
                            if (exitCode != 0) {
                                error "Failure!!!"
                                error "One of the macro did not pass"
                                error "Check the logs for current run"
                            }
                        }
                    }
                }
            }
        }
    }
    post {
        success {
            echo 'Pipeline Ran Successfully'
        }
        failure {
            echo 'Pipeline Failed'
        }
    }
}