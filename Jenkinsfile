#!groovy

pipeline{
    agent any

    stages{
        stage('Clone repository'){
            steps{
                echo "Starting clone..."
                sh("git init .")
                sh("git remote rm origin")
                sh("git remote add origin https://github.com/froOst23/parsing_hh")
                sh("git pull origin master")
                echo "Git clone success!"
            }
        }
        stage('Build project') {
            steps{
                echo "Starting build..."
                echo "Install requirements..."
                sh("pip3.7 install -r requirements.txt")
                echo "Try to lunch project..."
                sh("python3.7 parser.py")
                echo "Build success!"
            }
        }
    }
}
