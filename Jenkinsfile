pipeline {
    agent any

    parameters {
        string(defaultValue: "ERROR*** :: INVALID MACRO NAME :: ENTER THE MACRO NAMES IN JENKINS PIPILINE", description: 'Enter macro names', name: 'MACRO_LIST')
    }

    stages {
        stage('build') {
            steps {
                script {
                    def workspacePath = "${WORKSPACE}/src/main/core/"
                    def pythonExecutable = "/usr/local/bin/python3.12"
                    dir(workspacePath) {
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