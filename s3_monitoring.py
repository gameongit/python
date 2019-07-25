#!/usr/bin/python

import json
import boto3
import datetime
import time, re
from datetime import date, timedelta
import os
import subprocess
from dateutil.relativedelta import relativedelta

def lambda_handler():
    # create an s3 client
    Date = datetime.datetime.now()
    lastHourDateTime = Date - timedelta(hours = 1)
    TwoHourDateTime = Date - timedelta(hours = 2)
    FourHourDateTime = Date - timedelta(hours = 4)
    Yesterday = date.today() - timedelta(days=1)
    DayBeforeYesterday = date.today() - timedelta(days=2)
    DateTime = Date.strftime("%d-%m-%Y")
    DateTimeHour = Date.strftime("%Y-%m-%d-%H")
    lastmonthtimestamp = datetime.datetime.now() - relativedelta(months=1)

    # create an s3 client
    s3 = boto3.client('s3')
    response = s3.list_buckets()

    # Get a list of bucket names from the response
    BUCKET = [ bucket['Name'] for bucket in response['Buckets']]
    if "ama-s3-object-monitoring" not in BUCKET:
        try:
           s3.create_bucket(Bucket="ama-s3-object-monitoring", CreateBucketConfiguration={'LocationConstraint':'eu-central-1'})
        except:
           print ("Bucket ama-s3-object-monitoring creation has some issue")
    else:
        try:
           ObjectsContents = s3.list_objects(Bucket="ama-s3-object-monitoring")['Contents']
           for objects in ObjectsContents:
               def DelObject(OBjectName):
                   if OBjectName in objects['Key']:
                       DeleteObject = s3.delete_objects(Bucket="ama-s3-object-monitoring",
                                     Delete={
                                         'Objects': [
                                             {
                                                 'Key':OBjectName,
                                             }
                                          ]
                                     }
                                   )
               DelObject("Sv2Events")
               DelObject("Sv3Events")
        except:
           print ("Issue with deleting object SvEvent")


    if not os.path.exists('/tmp/bucketmonitoringfortheobjects'):
        os.makedirs('/tmp/bucketmonitoringfortheobjects')

    def FileDeletion(FileName):
         os.remove("/tmp/bucketmonitoringfortheobjects/"+FileName)
    FileDeletion("Sv2Events")
    FileDeletion("Sv3Events")

    CurrentBucketListwrite = open("/tmp/bucketmonitoringfortheobjects/BucketList-current", "w+")

    for item in BUCKET:
        CurrentBucketListwrite.write("%s\n" % item)
    CurrentBucketListwrite.close()

    ReadCurrentBucketList = open("/tmp/bucketmonitoringfortheobjects/BucketList-current", "r")
    CurrentBucketList = ReadCurrentBucketList.readlines()

    if os.path.exists("/tmp/bucketmonitoringfortheobjects/BucketList-previous"):
       ReadOLDbucketList = open("/tmp/bucketmonitoringfortheobjects/BucketList-previous", "r")
       OLDbucketList = ReadOLDbucketList.readlines()

       BUCKET = 0
       for bucketname in CurrentBucketList:
           if bucketname not in OLDbucketList:
               print("Bucket "+str(bucketname.strip())+" is added")
               BUCKET += 1

       for bucketname in OLDbucketList:
           if bucketname not in CurrentBucketList:
               print("Bucket "+str(bucketname.strip())+" is deleted")
               BUCKET += 1

       if BUCKET > 0:
           os.system("mv /tmp/bucketmonitoringfortheobjects/BucketList-current /tmp/bucketmonitoringfortheobjects/BucketList-previous")
    else:
       os.system("mv /tmp/bucketmonitoringfortheobjects/BucketList-current /tmp/bucketmonitoringfortheobjects/BucketList-previous")


    for bucket in response['Buckets']:
        tz_info = bucket['CreationDate'].tzinfo
        time_diff = (datetime.datetime.now(tz_info) - bucket['CreationDate']).total_seconds()
        if time_diff < 3600:
            print("Bucket %s is recently created" %bucket['Name'])

    FileforSv2AlerT = open("/tmp/bucketmonitoringfortheobjects/Sv2Events", "a+")
    FileforSv3AlerT = open("/tmp/bucketmonitoringfortheobjects/Sv3Events", "a+")

    def ObejctCheckSev2(objectpath, ObJECT):
        try:
           A = ("aws s3 ls s3://ama-tpe-src-amadeusftp/incoming/"+objectpath+ObJECT)
           AA = (subprocess.check_output(A, shell=True).strip())
           print AA
           if AA is None:
               FileforSv2AlerT.write("Object "+ObJECT+" is not present in "+"s3://ama-tpe-src-amadeusftp/incoming/"+objectpath+"\n")
        except:
           print("Object "+ObJECT+" is not present in "+"s3://ama-tpe-src-amadeusftp/incoming/"+objectpath)
           FileforSv2AlerT.write("Object "+ObJECT+" is not present in "+"s3://ama-tpe-src-amadeusftp/incoming/"+objectpath+"\n")

    def ObejctCheckSev3(objectpath, ObJECT):
        try:
           A = ("aws s3 ls s3://ama-tpe-src-amadeusftp/incoming/"+objectpath+ObJECT)
           AA = (subprocess.check_output(A, shell=True).strip())
           print AA
           if AA is None:
               FileforSv3AlerT.write("Object "+ObJECT+" is not present in "+"s3://ama-tpe-src-amadeusftp/incoming/"+objectpath+"\n")
        except:
           print("Object "+ObJECT+" is not present in "+"s3://ama-tpe-src-amadeusftp/incoming/"+objectpath)
           FileforSv3AlerT.write("Object "+ObJECT+" is not present in "+"s3://ama-tpe-src-amadeusftp/incoming/"+objectpath+"\n")

# On Count of Object basis
    MMPDedicated = ("aws s3 ls s3://ama-tpe-src-amadeusftp/incoming/MMPDedicated/"+lastHourDateTime.strftime('%Y-%m-%d-%H')+" | wc -l")
    count = (subprocess.check_output(MMPDedicated, shell=True).strip())
    print count
    if int(count) < 150:
       FileforSv2AlerT.write("Proper Object count is not present in s3://ama-tpe-src-amadeusftp/incoming/MMPDedicated/\n")

# Hourly
    ObejctCheckSev3("CleansedFQlogs/", TwoHourDateTime.strftime('%Y%m%d%H')+"_cleansedData_ti_search_analysis_1.0.0.csv.bz2")
    ObejctCheckSev3("EchoOptim/", FourHourDateTime.strftime('%Y%m%d%H')+"_spark_price_benchmark_1.0.0.csv.gz")

# For Daily before 12:00
    if int(Date.strftime("%H")) >= 12 and int(Date.strftime("%H")) < 14:
        ObejctCheckSev2("midt/1a/", "PRD.NBC.AIRFMI01.RAW.D"+Yesterday.strftime("%y%m%d")+".gz")
        ObejctCheckSev2("midt/1a/", "PRD.NBC.GDSFMI01.RAW.D"+Yesterday.strftime("%y%m%d")+".gz")
        ObejctCheckSev2("midt/1b/", "aba_midt_"+Yesterday.strftime("%d%m%Y")+".txt.gz")
        ObejctCheckSev2("midt/1e/", "travelsky_midt_"+DayBeforeYesterday.strftime("%Y%m%d")+".Z")
        ObejctCheckSev2("midt/1g/", "GALILEO_DAILY_"+Yesterday.strftime("%Y%m%d")+".gz")
        ObejctCheckSev2("midt/1g/", "GALILEO_DAILY_UNMSK_"+Yesterday.strftime("%Y%m%d")+".gz")
        ObejctCheckSev2("midt/1p/", "1P.MIDT.DAILY."+Yesterday.strftime("%Y%m%d")+".GZIP")
        ObejctCheckSev2("midt/1p/", "1P.MIDT.FILTER.DAILY."+Yesterday.strftime("%Y%m%d")+".GZIP")
        ObejctCheckSev2("midt/1s/", "sabre_daily_"+Date.strftime("%Y%m%d")+".txt.gz")
        ObejctCheckSev2("midt/1s/", "sabre_daily_unmsk_"+Date.strftime("%Y%m%d")+".txt.gz")
        ObejctCheckSev3("sidt/1a/", "PRD.NBC.GDSFMI01.OFF.M"+lastmonthtimestamp.strftime("%Y%m"))
        ObejctCheckSev3("sidt/1b/", "aba_1bsidt_"+lastmonthtimestamp.strftime("%m%Y"))
        ObejctCheckSev3("sidt/1f/", "SLD.NH."+lastmonthtimestamp.strftime('%m%Y')+".zip")
        ObejctCheckSev3("midt/1p/", "1P.MIDT.DAILY."+Yesterday.strftime('%Y%m%d')+".GZIP")
        ObejctCheckSev3("midt/1p/", "1P.MIDT.FILTER.DAILY."+Yesterday.strftime('%Y%m%d')+".GZIP")
        ObejctCheckSev3("midt/1p/", "1P_MIDT_MONTHLY_UNMASK_"+lastmonthtimestamp.strftime('%Y%m')+".gz")
        ObejctCheckSev3("cabin_class_rules/", "EXP_CABReport_"+Date.strftime('%Y%m%d'))
#        ObejctCheck("sidt/1a/", "")


# For Daily before 22:00
    if int(Date.strftime("%H")) >= 22:
        ObejctCheckSev2("midt/1f/", "DMIDT.NH."+Yesterday.strftime("%d%m%Y")+".zip")
        ObejctCheckSev2("midt/1j/", "AXESS.D.MIDT.U.AMADEUS."+Yesterday.strftime("%Y%m%d"))
        ObejctCheckSev3("sidt/1j/", "AXESS.SLD.U.AMADEUS."+lastmonthtimestamp.strftime('%Y%m'))
#        ObejctCheck("sidt/1a/", "")

    FileforSv2AlerT.close()
    FileforSv3AlerT.close()

    def ObJectwriting(FileObjectname):
        FileRead = open("/tmp/bucketmonitoringfortheobjects/"+FileObjectname, "r")
        Content = FileRead.read()
        num_lines = sum(1 for line in open('/tmp/bucketmonitoringfortheobjects/'+FileObjectname))
        if int(num_lines) > 0:
            OBJECTEVENTCREATION = s3.put_object(Body=str(Content), Bucket="ama-s3-object-monitoring", Key=FileObjectname)
        print(FileRead.read())
    ObJectwriting("Sv2Events")
    ObJectwriting("Sv3Events")

lambda_handler()

