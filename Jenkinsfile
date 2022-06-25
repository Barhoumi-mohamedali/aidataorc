pipeline {
 //environment {  PATH = "$PATH:/usr/local/bin" }
  //agent { docker { image 'python:3.6' args '-u 0:0' // solution for pemission denied sh scrip  }   }
 
  agent any
              
 stages {
    stage('Construction [Build]') {
      steps {
       withEnv(["PATH=$PATH:~/.local/bin"]){
        echo "Current workspace is $PATH:/usr/local/bin"
         sh "/usr/local/bin/docker-compose  -f docker-compose.yml build"
       
        }
      }
    }
    stage('Test') {
      steps {
        echo "L'étape actuelle est  Test"
       sh "/usr/local/bin/docker-compose up -d"
      }   
    }
    stage('Puch To Docker Hub Registry ') {
      steps {
       
            withCredentials([usernamePassword(credentialsId: 'DOCKER_HCREDENTIALS', passwordVariable: 'DockerPassword', usernameVariable: 'DockerUsername')]) {   
           
           echo "L'étape actuelle est Puch To Docker Hub Registry"
             sh 'echo $DockerPassword | docker login -u $DockerUsername --password-stdin'
          

        } 
       //You can push a new image to this repository using the CLI

//docker tag local-image:tagname new-repo:tagname
//docker push new-repo:tagname
     // myregistryhost  sh 'docker build -t barhoumimohamedalengineer/dataplaformai:latest -f docker-compose.yml'  
       sh  'docker image tag barhoumimohamedalengineer/dataplaformai:latest  myregistryhost:5000/barhoumimohamedalengineer/dataplaformai:latest   '
       sh 'docker image push barhoumimohamedalengineer/dataplaformai:latest'
      }   
    }
    stage('Déployer application sur K8s Cluster') {
      steps {
       
        echo "L'étape actuelle est deployement"
       kubernetesDeploy(
        configs: "DjangoPostgresql.yaml",
        kubeconfigId: 'KUBERNETES_CLUSTER_CONFIG',
         enableConfigSubstitution : true
         )
      }   
    }
    stage('Publier les résultats (Slack)') {
      steps {
       script {
         try {
           echo "L'étape actuelle est Publier le résultat"
          slackSend color: "good", message: "Construction avec succès: `${env.JOB_NAME}#${env.BUILD_NUMBER}` <${env.BUILD_URL}|Ouvrir dans Jenkins>"
       }   
        catch (err) {
        slackSend color: "danger", message: "Construction avec succès :face_with_head_bandage: \n`${env.JOB_NAME}#${env.BUILD_NUMBER}` <${env.BUILD_URL}|Ouvrir dans Jenkins>"

        throw err
    }
         
       }
      }   
    }
  }
     

 
}
     
         
     
