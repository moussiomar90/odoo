node {
    stage('Step1') {
        if (env.BRANCH_NAME == 'DEV') {
            echo 'Hello from main DEV'
        } else {
            sh "echo 'Hello from ${env.BRANCH_NAME} branch!'"
        }
    }
}
