from __future__ import print_function

import boto3
import os

client = boto3.client('cloudformation', region_name='eu-west-1')
sns = boto3.client('sns', region_name='eu-west-1')

def lambda_handler(event, context):

    if 'clickType' in event:
        if event['clickType'] == 'SINGLE':
            print("Single press - Deploy the CloudFormation"),
            printer_notworking()
            sns_notify()
           

        if event['clickType'] == 'DOUBLE':
            print ("Please fix the printer its not working"),
            build_stack()

        else:
            print("Long press - Delete the CloudFormation"),
            delete_stack()
    else:
        print("Something else initiated the Lambda")
    return 'end of function'   

def build_stack():
    response = client.create_stack(
        StackName=os.environ['stackName'],
        TemplateURL='https://s3-eu-west-1.amazonaws.com/cloudformation-templates-eu-west-1/WordPress_Single_Instance.template',
        Parameters=[
            {
                "ParameterKey": "DBName",
                "ParameterValue": "wordpressdb"
            },
            {
                "ParameterKey": "DBPassword",
                "ParameterValue": "xxxxxxxx"
            },
            {
                "ParameterKey": "DBRootPassword",
                "ParameterValue": "xxxxxxxx"
            },
            {
                "ParameterKey": "DBUser",
                "ParameterValue": "admin"
            },
            {
                "ParameterKey": "InstanceType",
                "ParameterValue": "t2.micro"
            },
            {
                "ParameterKey": "KeyName",
                "ParameterValue": os.environ['keyPair']
            },
            {
                "ParameterKey": "SSHLocation",
                "ParameterValue": "0.0.0.0/0"
            },
        ],
        Capabilities=[
            'CAPABILITY_IAM',
        ],
        OnFailure='ROLLBACK',
        EnableTerminationProtection=False
    )
    return(response)

def delete_stack():
    response = client.delete_stack(
        StackName=os.environ['stackName'],
    )
    return(response)

def printer_notworking():
    message = 'Please fix the printer its not working',
    response = sns.publish(TopicArn="arn:aws:sns:eu-west-1:xxxxxxxxxxxx:aws-iot-button-sns-topic-staffuniv",
    Subject="PrinterNotWorking", Message="Printer is not working")
    return(response)

def sns_notify():
    response = sns.publish(PhoneNumber="+441111111111", Message="Printer is Broken, Please help. Its urgent for my homework")
    return(response)
