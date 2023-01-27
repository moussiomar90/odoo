node {
    stage('Step1') {
        if (env.BRANCH_NAME == 'prod') {
            echo 'Hello from main prod'
        } else {
            sh "echo 'Hello from ${env.BRANCH_NAME} branch!'"
        }
    }
}
