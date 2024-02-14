pipeline {
agent any
    parameters{
            string(defaultValue: "", description: 'Enter macro names', name: 'MACRO_LIST')
    }
    stages {
        stage('build') {
            steps {
                sh '/usr/local/bin/python3.12 /src/main/core/MacroRunner.py --macro ${MACRO_LIST}'
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