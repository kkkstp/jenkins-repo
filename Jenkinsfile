pipeline {
    agent any
    
    options {
        disableConcurrentBuilds()
        timeout(time: 1, unit: 'HOURS') 
        buildDiscarder(logRotator(artifactDaysToKeepStr: '5', artifactNumToKeepStr: '5', daysToKeepStr: '5', numToKeepStr: '5'))
    }
    parameters {
        text(name: 'first_val', defaultValue: '5', description: 'Enter the first value')
        text(name: 'second_val', defaultValue: '2', description: 'Enter the second value')
    }
     stages {
        stage('#1 test') {
            steps {
                echo "run app"
                echo "${params.first_val} ${params.second_val}"
                sh '''
                ls -l
                cd myapp
                python3 calculate.py ${params.first_val} ${params.second_val}
                '''
            }
        }
    }
}
