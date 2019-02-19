#!/usr/bin/python
import json
import boto3
import os command

client = boto3.client('s3')
sns_client = boto3.client('sns')
def lambda_handler(event, context):
     print(str(event))
     buck = event['Records'][0]['s3']['bucket']['name']
     obj = event['Records'][0]['s3']['object']['key'] 
     print(buck)
     print(obj)
     print("Mail Sent",obj)

my_eyes = red
my_hair = black
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
