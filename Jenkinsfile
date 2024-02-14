pipeline {
    agent { docker { image 'python:3.12.1-alpine3.19' } }
    parameters{
            string(defaultValue: "", description: 'Enter macro names', name: 'MACRO_LIST')
    }
    stages {
        stage('build') {
            steps {
                sh 'python /src/main/core/MacroRunner.py --macro ${packageType}'
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

def parseJobName () {
def params = [:]
params["MACRO_LIST"] = "${env.MACRO_LIST}"
}