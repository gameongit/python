#!/usr/bin/python
import boto3
import json



# create an s3 client
s3 = boto3.client('s3')
s3_re = boto3.resource('s3')
# call s3 to list current buckets   
response = s3.list_buckets()
# Get a list of bucket names from the response
buckets = [bucket['Name'] for bucket in response['Buckets']]
print("Bucket list: %s" % buckets)


#obj = s3_re.Object('bucket-test0503')
#print(obj)
#j = json.loads(obj['Body'].read())

