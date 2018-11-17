# AWSIoTButtonAutomation

This is for demo - Far from perfect but it works :) 

What it does : 

(a) Single Click - Send an email and text by using SNS
(b) Double Click - Create a wordpress environment 
(c) Long   Press - Delete the Wordpress stack 

Pre-Req :

(a) Please follow this link https://docs.aws.amazon.com/iot/latest/developerguide/iot-button-cloudformation.html to seup IoT button 
(b) Setup IAM Roles so that your lambda functions  have required permissions

Lambda Function Pre-req: 

(a) Create the lambda function, provide a name and select Python 2.7 runtime 
(b) Either create a new or existing IAM role and ensure you have permission to access various other services such as CFN 
(c) For this demo , Ensure you  define "EnvrionemtVariable" in Lambda and in our demo we define two "keyPair" which is your Key 
    and "stackName" the name of the stack.
    
    e.g : keyPair  :  Mydemoserveraccess
         stackName : Wordpress 
(d) Ensure you set up the "AWS IoT" trigger from the list for lambda and enable it with your right "Thing" 
(e) Change your SNS topics, WP password, Phone number etc in the lambda function


