node {
   
        if (env.BRANCH_NAME == 'prod')
   {
              stage('ENv preparing...') {
        sh 'ssh -p 22 sama@192.168.1.4 "rm -rf /home/sama/addons/*" '
      
                    }
       
       stage ('Addons Install..'){
                 sh 'ssh -p 22 sama@192.168.1.4 "cd /home/sama/addons/ ; git clone --branch dev  https://github.com/moussiomar90/odoo.git  ./openacademy;" '
              }
         stage ('Test ok '){
                 echo ' Please check you website on this adress : 192.168.1.4:8069 '
              }
   
       
           
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
