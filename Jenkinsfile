pipeline {
    agent { label ${NODE_LABEL_NAME} }

    parameters {
        string(defaultValue: "agent-uivision", description: 'Enter Node Label Name Where You Want to Run UIVIsion', name: 'NODE_LABEL_NAME')
        string(defaultValue: "", description: 'Enter Macro Names', name: 'MACRO_LIST')
    }

    stages {
        stage('build') {
            steps {
                script {
                    def workspacePath = "${WORKSPACE}/src/main/core/"
                    def pythonExecutable = "/usr/bin/python3"
                    def scriptCommand = "${pythonExecutable} MacroRunner.py --macro ${MACRO_LIST}"
                    def errorLogFile = "${WORKSPACE}/error_logs.txt"

                    catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
                        dir(workspacePath) {
                            def exitCode = sh(script: "${scriptCommand} 2> ${errorLogFile}", returnStatus: true)
                            if (exitCode != 0) {
                                error "Failure!!! : Macros did not pass : Check the logs for current run"
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
