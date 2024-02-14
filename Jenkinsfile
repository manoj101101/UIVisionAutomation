pipeline {
agent any
    parameters{
            string(defaultValue: "", description: 'Enter macro names', name: 'MACRO_LIST')
            string(defaultValue: "/usr/local/bin/", description: 'Enter macro names', name: 'PYTHON_PATH')
            string(defaultValue: "", description: 'Enter macro names', name: 'SCRIPT_PATH')
    }

        environment {
        PYTHON_PATH = '/usr/local/bin/python3.12'
        SCRIPT_PATH = '/Users/manoj.mathpal/Documents/GitHub/UIVisionAutomation/src/main/core/MacroRunner.py'
       }

    stages {
        stage('build') {

            steps {

            script {

            sh '${PYTHON_PATH}  ${SCRIPT_PATH} --macro ${MACRO_LIST}'

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
