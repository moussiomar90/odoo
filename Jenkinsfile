node {
    stage('Step1') {
        if (env.BRANCH_NAME == 'STAGING') {
            echo 'Hello from main STAGING'
        } else {
            sh "echo 'Hello from ${env.BRANCH_NAME} branch!'"
        }
    }
}
