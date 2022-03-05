pipeline {
  agent { docker { 
                  image 'python:3.7.2' 
                 } 
                 }
  stages {
    stage('build') {
      steps {
        withEnv(["HOME=${env.WORKSPACE}"]) { // hide user permission for /.local
        sh 'pip3  install  --default-timeout=100  virtualenv --user'
        sh 'virtualenv -p "which python3.6 " .venv'
        sh 'source .venv/bin/activate'
        sh 'pip install -r requirements.txt'
        sh 'python manage.py migrate'


        }
      }
    }
    stage('test') {
      steps {
        sh 'python manage.py runserver 0.0.0.0:8001'
      }   
    }
  }
}
