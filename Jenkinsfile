// Jenkinsfile

pipeline {
    agent any

    environment {
        // Define a variable for your Docker Hub credentials ID from Jenkins
        DOCKERHUB_CREDENTIALS_ID = 'dockerhub-credentials'
        // Define your Docker Hub username
        DOCKERHUB_USERNAME = 'jdhruvr'
        // Define the name for your Docker image
        DOCKER_IMAGE_NAME = "${DOCKERHUB_USERNAME}/calculator-app"
    }

    stages {
        stage('2. Build and Test') {
            steps {
                echo 'Building and running tests using a direct docker run command...'
                /*
                 * This is a more robust way to run tests. Here's the breakdown:
                 * 'docker run':  Execute a command in a new container.
                 * '--rm':        Automatically remove the container when it exits. Keeps things clean.
                 * '-v "$WORKSPACE":/app': Mount the Jenkins workspace directory (where your code is)
                 *                         into a folder named '/app' inside the container.
                 * '-w /app':     Set the working directory inside the container to '/app'.
                 * 'python:3.9-slim': The image to use.
                 * 'python -m unittest discover': The command to run inside the container.
                 *
                 * Because we set the working directory to /app where the code lives,
                 * Python will correctly find both test_calculator.py and calculator.py.
                 */
                sh 'docker run --rm -v "$WORKSPACE":/app -w /app python:3.9-slim python -m unittest discover'
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
