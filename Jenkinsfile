pipeline {
    agent any
     
    stages {
        if (env.BRANCH_NAME == "DEV")
        stage("DEV ....") {
            steps {
               sh 'echo from ' +env.BRANCH_NAME
            }
        }
    }
        stage("Satging ...") {
            steps {
                sh 'echo staging'
            }
        }
        
        
    }   
}
