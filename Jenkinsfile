// Jenkinsfile

pipeline {
    agent any

    environment {
        // Define a variable for your Docker Hub credentials ID from Jenkins
        DOCKERHUB_CREDENTIALS_ID = 'dockerhub-credentials'
        // Define your Docker Hub username
        DOCKERHUB_USERNAME = 'jdhruv'
        // Define the name for your Docker image
        DOCKER_IMAGE_NAME = "${DOCKERHUB_USERNAME}/calculator-app"
    }

    stages {
        stage('1. Pull Code from GitHub') {
            steps {
                echo 'Pulling the latest code from the repository...'
                git 'https://github.com/JDhruvR/calculator_cicd.git'
            }
        }

        stage('2. Build and Test') {
            steps {
                echo 'Building and running tests...'
                // We use a python docker image to run the tests in a clean environment
                script {
                    docker.image('python:3.9-slim').inside {
                        sh 'python -m unittest discover'
                    }
                }
            }
        }

        stage('3. Build Docker Image') {
            steps {
                echo "Building the Docker image: ${DOCKER_IMAGE_NAME}:${BUILD_NUMBER}"
                // The 'true' argument in build() returns the image object
                script {
                    def customImage = docker.build(DOCKER_IMAGE_NAME, ".")
                    // We can tag it with the build number for versioning
                    customImage.tag("${BUILD_NUMBER}")
                }
            }
        }

        stage('4. Push Docker Image to Docker Hub') {
            steps {
                echo "Pushing the image to Docker Hub..."
                // Use the credentials stored in Jenkins
                script {
                    docker.withRegistry('https://registry.hub.docker.com', DOCKERHUB_CREDENTIALS_ID) {
                        // Push the 'latest' tag
                        docker.image(DOCKER_IMAGE_NAME).push('latest')
                        // Push the build number tag
                        docker.image(DOCKER_IMAGE_NAME).push("${BUILD_NUMBER}")
                    }
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished. Cleaning up workspace.'
            cleanWs() // Deletes the workspace to save disk space
        }
    }
}
