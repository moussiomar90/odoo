node {
   
        if (env.BRANCH_NAME == 'prod') {
           stage('ENv preparing...') {
        sh 'ssh -p 22 sama@192.168.1.6 "rm -rf /home/omar/addons/*" '
      
                    }
       
       stage ('Addons Install..'){
                 sh 'ssh -p 22 omar@192.168.1.6 "cd /home/sama/addons/ ; git clone --branch dev  https://github.com/moussiomar90/odoo.git  ./openacademy;" '
              }
         stage ('Test ok '){
                 echo ' Please check you website on this adress : 192.168.1.4:8080 '
              }
    }
        }
    else if (env.BRANCH_NAME == 'staging'){
        
        sh 'ssh -p 22 omar@192.168.1.6 "git clone --branch dev  https://github.com/moussiomar90/odoo ; cd odoo ; docker stop omar_web_1;  docker rm  omar_web_1; docker-compose up -d ;" '

    }
    else {
       stage('ENv preparing...') {
        sh 'ssh -p 22 omar@192.168.1.6 "rm -rf /home/omar/addons/*" '
      
                    }
       
       stage ('Addons Install..'){
                 sh 'ssh -p 22 omar@192.168.1.6 "cd /home/omar/addons/ ; git clone --branch dev  https://github.com/moussiomar90/odoo.git  ./openacademy;" '
              }
         stage ('Test ok '){
                 echo ' Please check you website on this adress : 192.168.1.6:8069 '
              }
    }
    
}
