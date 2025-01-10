pipeline {
    agent any
    
    triggers {
        pollSCM 'H/2 * * * *'
    }

     stages {
        stage('Build') {
            steps {
                echo "Building.."
                sh '''
                cd myapp
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testing.."
                sh '''
                cd myapp
                python3 hw.py
                '''
            }
        }
        stage('Deliver') {
            agent {
                docker {
                    image 'alpine'
                }
            }
            steps {
                echo 'Deliver....'
                sh 'hostname'
            }
        }
    }
}
