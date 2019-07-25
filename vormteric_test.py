#!/usr/bin/python

import os
import sys
import shutil
import rpm
import urllib2

LOCATION = "/tmp/Vormetric"
BKP_LOCATION = "/tmp/Vormetric_bkp"

DIR = rpm.TransactionSet()
PKGLST  = DIR.dbMatch()

def RpmPackages(pack):
   for line in PKGLST:
      if pack in line['name']:
         return line['name']

def PackageInstall(i):
#    for i in (a):
    RPMCheck = RpmPackages(i)
    if not RPMCheck:
        print(i+" is not installed")
        os.system(Install+" "+i)

if not os.path.isdir(LOCATION):
   os.mkdir(LOCATION)
   os.mkdir(BKP_LOCATION)

#lists = os.listdir(LOCATION)
#for content in lists:
   shutil.move(os.path.join(LOCATION, content), os.path.join(BKP_LOCATION, content))

if os.path.isfile("/etc/redhat-release"):
   OSV=(open('/etc/redhat-release','r').read().split(' ')[6].split('.')[0])
   PA="RHEL"+OSV
   OS="rh"+OSV
   OLDVER="older%20version"
   RPMV=(RpmPackages("vee-fs")[3]+"-"+RpmPackages("vee-fs")[4])
   Install="yum -y install"
#   print(RPMV)
   int_ver=RPMV.replace("-", ".")
   print (int_ver)
   import yum
   PackageInstall('poppler-utils')
else:
    for f in open("/etc/SuSE-release", "r"):
        if "VERSION" in f:
            OSV = (f.split(' ')[2])
    PA="SLES"
    OS="sles"+OSV
    OLDVER="older"
    RPMV=(RpmPackages("vee-fs")[3])
    print(RPMV)
    Install = "zypper -n install"
    PackageInstall('poppler-tools')


KERNEL=os.uname()[2]
#response = urllib2.urlopen('http://repository.adp.amadeus.net/repository/master-ops-vormetric/Compatibility/')
#f = open('/tmp/comp.txt', 'w')
#f.write(response.read())
#f.close()
#File=(open('/tmp/comp.txt','r'))
#for line in File:
#   if "Compatibility_Matrix" in line:
#      last=line
#PDF=(last.split('"')[1])
#PDF="2019-02-12-VDS_Compatibility_Matrix.pdf"
#print PDF
#VerName1=(PDF).split('_')[0]
#print VerName1
#url = ("http://repository.adp.amadeus.net/repository/master-ops-vormetric/Compatibility/"+PDF)
#os.system("wget "+url+" -P "+LOCATION )
#TXTFileName=(os.path.splitext(PDF)[0]+'.txt')
TXTFileName="test.txt"
#os.system("pdftotext "+LOCATION+"/"+PDF+" 2> /dev/null")
#TextFile=(open(LOCATION+"/"+TXTFileName,'r'))
TextFile="/tmp/Vormetric/test.txt"
second="VTE"

def latest_version(string_to_search, before, after, file_to_search, second_string):
    with open(file_to_search) as f:
        all_lines = f.readlines()
        last_line_number=len(all_lines)
        for current_line_no, current_line in enumerate(all_lines):
            if string_to_search in current_line:
                LEN=(len(current_line))
                start_line_no=max(current_line_no - before, 0)
                end_line_no=min(last_line_number, current_line_no+after+0)
                for i in range(current_line_no, end_line_no):
                    if LEN > 150:
                       YY=(all_lines[i].split(KERNEL)[1])
                    else:
                       YY=(all_lines[i])
                    if second_string in YY:
                       T=(YY.split('VTE')[1])
                       if len(T) > 1:
                          lat_ver=(T.split(')')[0].split('/')[-1].strip().split(' ')[0])
                          print (lat_ver)
                          break
                       else:
                          T=(all_lines[i+1])
                          lat_ver=(T.split(')')[0].split('/')[-1].strip().split(' ')[0])
                          print lat_ver
                          break
                             
latest_version(KERNEL, 0, 2, TextFile, second)

def install_pack()
    os.chmod(LOCATION, 0o744)
    os.system("sh "+ LOCATION +'/'+ '-e')
    os.listdir(LOCATION)
    os.system("rpm -Uvh " + LOCATION + '/' + '*.rpm')
    
if int_ver == lat_ver:
   print "Latest package is already installed"
else:
   response = urllib2.urlopen('http://repository.adp.amadeus.net/repository/master-ops-vormetric/'+PA+'/')
   if 
   testfile = urllib.URLopener()
   testfile.retrieve("http://randomsite.com/file.gz", "file.gz")


