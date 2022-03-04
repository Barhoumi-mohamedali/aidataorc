pipeline {
  agent { docker { image 'python:3.7.2' } }
  stages {
    stage('build') {
      steps {
        sh 'pip3 freeze > requirements.txt && pip3 install -r  requirements.txt'
        sh 'pip install virtualenv && virtualenv --python=python3.7.2 env && source env/bin/activate'
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
