node {
   
        if (env.BRANCH_NAME == 'prod') {
            echo 'Hello from  PROD'
        }
    else if (env.BRANCH_NAME == 'staging'){
        
           echo 'Hello from main staging'
    }
    else {
       sh 'ssh -p 22 omar@192.168.1.6 "git clone --branch dev  https://github.com/moussiomar90/odoo ; cd odoo ; docker-compose up -d ; docker stop omar_web_1;  docker rm  omar_web_1;" '
    }
    
}
