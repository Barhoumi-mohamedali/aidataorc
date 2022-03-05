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
    stage('test') {
      steps {
        sh 'python3 -m manage runserver 0.0.0.0:8001'
      }   
    }
    stage('Deploy') {
      steps {
        echo "Current step is deployement"
      }   
    }
    stage('Publish results') {
      steps {
          echo "Current step is Publish results"
      }   
    }
  }
}
