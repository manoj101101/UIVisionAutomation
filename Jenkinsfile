pipeline {
    agent any

    parameters {
        string(defaultValue: "/Users/manoj.mathpal/Desktop/uivis/macros/AckoDrive/verifySuccessfulLogout", description: 'Enter macro names', name: 'MACRO_LIST')
    }

    stages {
        stage('build') {
            steps {
                script {
                    def workspacePath = "${WORKSPACE}/src/main/core/"
                    echo "--------1>${workspacePath}"
                    def pythonExecutable = "/usr/local/bin/python3.12"
                    echo "--------2>${pythonExecutable}"
                    dir(workspacePath) {
                        echo "==========="
                        echo "${pythonExecutable} MacroRunner.py --macro ${MACRO_LIST}"
                        sh "${pythonExecutable}" MacroRunner.py --macro "${MACRO_LIST}"
                    }
                }
            }
        }
    }

    post {
        always {
            echo 'This will always run'
        }
        success {
            echo 'This will run only if successful'
        }
        failure {
            echo 'This will run only if failed'
        }
        unstable {
            echo 'This will run only if the run was marked as unstable'
        }
        changed {
            echo 'This will run only if the state of the Pipeline has changed'
            echo 'For example, if the Pipeline was previously failing but is now successful'
        }
    }
}