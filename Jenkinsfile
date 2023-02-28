pipeline {
  agent {
    node {
      label 'devr'
    }
  }

  environment {
    DOCKER_REGISTRY = "https://registry.hub.docker.com"
    DOCKER_REPOSITORY = "thongngo3301/pastebin"
  }

  stages {
    stage('Build') {
      steps {
        checkout scm
        sh """
          docker build -t ${DOCKER_REPOSITORY}:${env.BUILD_NUMBER} .
        """
      }
    }
    stage('Push') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'dockerhub-rw', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
          sh """
            docker login -u ${DOCKER_USERNAME} -p ${DOCKER_PASSWORD}
            docker push ${DOCKER_REPOSITORY}:${env.BUILD_NUMBER}
          """
        }
      }
    }
    stage('Deploy') {
      steps {
        script {
          sh """
            docker-compose rm -f
            docker-compose pull
            docker-compose up --build -d
          """
        }
      }
    }
    stage('Test') {
      steps {
        script {
          sh """
            /home/deployer/venv/bin/python3 tests/main.py ec2-3-239-51-189.compute-1.amazonaws.com
          """
        }
      }
    }
  }
  post {
    always {
      cleanWs()
    }
  }
}