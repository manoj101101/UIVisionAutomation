pipeline {
agent any
    parameters{
            string(defaultValue: "", description: 'Enter macro names', name: 'MACRO_LIST')
    }

    stages {
        stage('build') {

            steps {

            script {
            echo "Running ${env.BUILD_ID} on ${env.JENKINS_URL}"
            def workspacePath = "${WORKSPACE}/src/main/core/"
            sh "cd ${workspacePath}"
            def pythonExecutable = sh(script: 'which python3.12', returnStdout: true).trim()
            sh "${pythonExecutable} MacroRunner.py --macro ${MACRO_LIST}"
            sh 'python3.12 --macro ${MACRO_LIST}'
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
