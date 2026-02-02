pipeline {
    // 'agent any' tells Jenkins to run this on the machine it is installed on (your Windows PC)
    agent any

    // Define tools if you have configured them in Jenkins (Optional, assuming PATH works)
    environment {
        // We set the path just in case, or rely on system PATH
        PATH = "${env.PATH}" 
    }

    stages {
        // STAGE 1: Get the Code
        stage('Checkout Code') {
            steps {
                // This replaces 'actions/checkout'
                // Use the HTTPS URL of your repo
                git branch: 'main', url: 'https://github.com/Rahul-saini-DS/CI_CD_PIPELINES.git'
            }
        }

        // STAGE 2: Build React (Frontend)
        stage('Build Frontend') {
            steps {
                script {
                    echo '--- Installing Node Dependencies ---'
                    // We use 'bat' for Windows Command Prompt commands
                    bat 'npm install'
                    
                    echo '--- Building React App ---'
                    bat 'npm run build'
                }
            }
        }

        // STAGE 3: Build EXE (Backend)
        stage('Build Windows EXE') {
            steps {
                script {
                    echo '--- Installing Python Dependencies ---'
                    bat 'pip install -r api/requirements.txt'
                    bat 'pip install pyinstaller'

                    echo '--- Creating EXE ---'
                    // The exact same command you used in GitHub Actions
                    // Note: In Groovy strings, use double quotes
                    bat 'pyinstaller --onefile --name MyApp --add-data "build;build" api/api.py'
                }
            }
        }
    }

    // STAGE 4: Archive (Save the file)
    post {
        success {
            echo 'Build Successful! Archiving artifacts...'
            // This replaces 'upload-artifact'. It saves the file in Jenkins dashboard.
            archiveArtifacts artifacts: 'dist/MyApp.exe', fingerprint: true
        }
        failure {
            echo 'Build Failed. Check logs.'
        }
    }
}
