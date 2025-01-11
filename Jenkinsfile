pipeline {
    agent any
    
//    triggers {
//        pollSCM 'H/2 * * * *'
//    }

    options {
        ansiColor('xterm')
        timestamps()
        disableConcurrentBuilds()
        timeout(time: 1, unit: 'HOURS') 
        buildDiscarder(logRotator(artifactDaysToKeepStr: '5', artifactNumToKeepStr: '5', daysToKeepStr: '5', numToKeepStr: '5'))
    }
    
     stages {
        stage('#1') {
            steps {
                echo "run app"
                sh '''
                cd myapp
                python3 hw.py
                '''
            }
        }
    }
}
