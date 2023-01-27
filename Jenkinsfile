node {
    stage('Step1') {
        if (env.BRANCH_NAME == 'PROD') {
            echo 'Hello from main PROD'
        } else {
            sh "echo 'Hello from ${env.BRANCH_NAME} branch!'"
        }
    }
}
