pipeline {
  agent "devr"

  environment {
    DOCKER_REGISTRY = "https://registry.hub.docker.com"
    DOCKER_REPOSITORY = "thongngo3301/pastebin"
  }

  stages {
    stage('Build') {
      steps {
        cleanWs()
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
          """
          sh """
            docker push ${DOCKER_REPOSITORY}:${env.BUILD_NUMBER}
          """
        }
      }
    }

    stage('Deploy') {
      steps {
        script {
          // Restart containers
          sh "echo URI=`curl https://ifconfig.me/ip` > .env"
          sh """
            docker-compose down
          """
          sh """
            docker-compose up -d
          """
        }
      }
    }
  }
}