pipeline {
    agent any

     stages {
        stage('Build') {
            steps {
                echo "Building.."
                sh '''
                cd myapp
                # pip install -r requirements.txt
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testing.."
                sh '''
                python3 hw.py
                '''
            }
        }
        stage('Deliver') {
            steps {
                echo 'Deliver....'
                sh '''
                echo "doing delivery stuff.."
                '''
            }
        }
    }
}
