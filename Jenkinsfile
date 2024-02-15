pipeline {
    agent any

    parameters {
        string(defaultValue: "/Users/manoj.mathpal/Desktop/uivis/macros/AckoDrive/verifySuccessfulLogout", description: 'Enter macro names', name: 'MACRO_LIST')
        string(defaultValue: "/Users/manoj.mathpal/Desktop/uivis/macros/AckoDrive/verifySuccessfulLogout", description: 'Enter macro names', name: 'MACRO_DIR')
    }

    stages {
        stage('build') {
            steps {
                script {
                    def workspacePath = "${WORKSPACE}/src/main/core/"
                    def pythonExecutable = "/usr/local/bin/python3.12"
                    sh "${pythonExecutable} MacroRunner.py --macro ${MACRO_LIST}"
                    }
                }
            }
        }
    }

    post {
        success {
            echo '************************Pipeline ran successfully************************'
        }
        failure {
            echo '**************************Pipeline failed********************************'
        }
    }
}