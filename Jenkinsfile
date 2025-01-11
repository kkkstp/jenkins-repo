pipeline {
    agent any
    
    options {
        disableConcurrentBuilds()
        timeout(time: 1, unit: 'HOURS') 
        buildDiscarder(logRotator(artifactDaysToKeepStr: '5', artifactNumToKeepStr: '5', daysToKeepStr: '5', numToKeepStr: '5'))
    }
    parameters {
        text(name: 'value', defaultValue: '0', description: 'Enter the value')
    }
     stages {
        stage('#1 test') {
            steps {
                echo "run app"
                echo "${params.value}"
                sh '''
                cd myapp
                python3 calculate.py
                '''
            }
        }
    }
}
