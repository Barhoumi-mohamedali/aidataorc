pipeline {
 
  agent { docker { 
                  image 'python:3.6' 
                 } 
                 }
  
  stages {
    stage('build') {
      steps {
        withEnv(["HOME=${env.WORKSPACE}"]) { // hide user permission for /.local
        echo "Current workspace is ${env.WORKSPACE}"
          
        sh 'pip3  install  --default-timeout=100  virtualenv --user'
      
        sh 'python3 -m  virtualenv venv'
        sh '. venv/bin/activate'   
         sh  'pip3 freeze > requirements.txt'
        sh 'pip3 install -r requirements.txt'
       

           
        }
      }
    }
    stage('Test') {
      steps {
        echo "Current step is Test"
       sh 'python3 -m manage test'
        //sh 'python3 manage.py runserver 0.0.0.0:8001'
      }   
    }
    stage('Deploy') {
      steps {
        echo "Current step is deployement"
      }   
    }
    stage('Publish results') {
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
