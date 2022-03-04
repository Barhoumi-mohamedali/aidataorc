pipeline {
  agent { docker { image 'python:3.7.2' } }
  stages {
    stage('build') {
      steps {
        sh 'pip install -U pip-upgrader'
        sh 'pip-upgrader freeze > requirements.txt && pip-upgrader install -r  requirements.txt'
        sh 'pip-upgrader install -U --default-timeout=100  virtualenv && virtualenv env -p python3 && source env/bin/activate'
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
