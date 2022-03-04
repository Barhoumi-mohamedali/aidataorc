pipeline {
  agent { docker { 
                  image 'python:3.7.2' 
                 } 
                 }
  stages {
    stage('build') {
      steps {
        sh  'virtualenv .venv'
        sh 'source .venv/bin/activate'
        sh  'pip install -r requirements.txt'
        sh 'python manage.py migrate'



      }
    }
    stage('test') {
      steps {
        sh 'python manage.py runserver 0.0.0.0:8001'
      }   
    }
  }
}
