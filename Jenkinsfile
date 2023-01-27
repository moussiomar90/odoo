node {
   
        if (env.BRANCH_NAME == 'prod') {
            echo 'Hello from  PROD'
        }
    else if (env.BRANCH_NAME == 'staging'){
        
        sh 'ssh -p 22 omar@192.168.1.6 "git clone --branch dev  https://github.com/moussiomar90/odoo ; cd odoo ; docker stop omar_web_1;  docker rm  omar_web_1; docker-compose up -d ;" '

    }
    else {
       stage('GIT clone ') {
        sh 'ssh -p 22 omar@192.168.1.6 "rm -rf odoo ; git clone --branch dev  https://github.com/moussiomar90/odoo ; " '
                    }
       
        stage('Repo Init  ') {
           
        sh 'ssh -p 22 omar@192.168.1.6 "rm -rf /home/omar/addons/*; docker stop omar_web_1;docker rm  omar_web_1 -f; docker stop omar_db_1; docker rm omar_db_1 -f;  docker ps "'
                       
        }
        stage('Docker Compose ') {
           
        sh 'ssh -p 22 omar@192.168.1.6 "cd odoo ; docker-compose up -d ;  cp -r /home/omar/openacademy /home/omar/addons" '
                    
        
        }
       
       
       
    }
    
}
