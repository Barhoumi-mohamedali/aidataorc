pipeline {
 //environment {  PATH = "$PATH:/usr/local/bin" }
  //agent { docker { image 'python:3.6' args '-u 0:0' // solution for pemission denied sh scrip  }   }
 
  agent any
              
 stages{
    stage('Deploy Application to K8s Cluster') {
      steps {
       
        echo "Current step is deployement"
       kubernetesDeploy(
        configs: "DjangoPostgresql.yaml",
        kubeconfigId: 'KUBERNETES_CLUSTER_CONFIG',
         enableConfigSubstitution : true
         )
      }   
    }
    stage('Publish results (Slack)') {
      steps {
       script {
         try {
           echo "Current step is Publish results"
          slackSend color: "good", message: "Build successful: `${env.JOB_NAME}#${env.BUILD_NUMBER}` <${env.BUILD_URL}|Open in Jenkins>"
       }   
        catch (err) {
        slackSend color: "danger", message: "Build failed :face_with_head_bandage: \n`${env.JOB_NAME}#${env.BUILD_NUMBER}` <${env.BUILD_URL}|Open in Jenkins>"

        throw err
    }
         
       }
      }   
    }
  }
}  

 

     
         
     
