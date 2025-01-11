pipeline {
    agent any
    
//    triggers {
//        pollSCM 'H/2 * * * *'
//    }

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
