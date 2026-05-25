pipeline {
    agent any

    environment {
        DOCKER_IMAGE   = 'ashleylobo2001/devops-task-tracker'
        DOCKER_TAG     = "${BUILD_NUMBER}"
        REGISTRY_CREDS = credentials('dockerhub-credentials')
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
                echo "Checked out branch: ${env.BRANCH_NAME}"
            }
        }

        stage('Lint') {
            steps {
                echo 'Running flake8 linter...'
                sh '''
                    python3 -m pip install --upgrade pip
                    pip install flake8
                    flake8 app/ --max-line-length=120 --statistics
                '''
            }
        }

        stage('Test') {
            steps {
                echo 'Running pytest...'
                sh '''
                    pip install -r requirements.txt
                    python -m pytest tests/ -v --tb=short
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image: ${DOCKER_IMAGE}:${DOCKER_TAG}"
                sh """
                    docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} .
                    docker tag ${DOCKER_IMAGE}:${DOCKER_TAG} ${DOCKER_IMAGE}:latest
                """
            }
        }

        stage('Push to Docker Hub') {
            steps {
                echo 'Pushing image to Docker Hub...'
                sh """
                    echo \$REGISTRY_CREDS_PSW | docker login -u \$REGISTRY_CREDS_USR --password-stdin
                    docker push ${DOCKER_IMAGE}:${DOCKER_TAG}
                    docker push ${DOCKER_IMAGE}:latest
                    docker logout
                """
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo 'Deploying to Kubernetes...'
                sh """
                    kubectl apply -f k8s/deployment.yaml
                    kubectl apply -f k8s/service.yaml
                    kubectl rollout status deployment/devops-task-tracker --timeout=120s
                """
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check the logs above.'
        }
        always {
            sh 'docker system prune -f || true'
            cleanWs()
        }
    }
}
