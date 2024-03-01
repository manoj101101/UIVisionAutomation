pipeline {
    agent { label "${NODE_LABEL_NAME}" }

    parameters {
        string(defaultValue: "health-UIVision", description: 'Enter Node Label Name Where You Want to Run UIVIsion', name: 'NODE_LABEL_NAME')
        string(defaultValue: "", description: 'Enter Macro Names', name: 'MACRO_LIST')
    }

    stages {
        stage('build') {
            steps {
                script {
                    def workspacePath = "${WORKSPACE}/src/main/core/"
                    def pythonExecutable = "/usr/bin/python3"
                    def scriptCommand = "${pythonExecutable} MacroRunner.py --macro ${MACRO_LIST}"
                    def errorLogFile = "${WORKSPACE}/health_error_logs.txt"
                    sh 'uivision export health_error_logs.html'

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
        always{
            publishHTML(target: [
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: '${WORKSPACE}/',
                reportFiles: 'myLogFile.html',
                reportName: 'UI Vision Report'
            ])
        }
        success {
            echo 'Pipeline Ran Successfully'
        }
        failure {
            echo 'Pipeline Failed'
        }
    }
}
