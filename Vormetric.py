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
         return "%s.%s" % (line['version'], line['release'])

def PackageInstall(i):
#    for i in (a):
    RPMCheck = RpmPackages(i)
    if not RPMCheck:
        print(i+" is not installed")
        os.system(Install+" "+i)

if not os.path.isdir(LOCATION):
   os.mkdir(LOCATION)
   os.mkdir(BKP_LOCATION)

lists = os.listdir(LOCATION)
for content in lists:
   shutil.move(os.path.join(LOCATION, content), os.path.join(BKP_LOCATION, content))

if os.path.isfile("/etc/redhat-release"):
   OSV=(open('/etc/redhat-release','r').read().split(' ')[6].split('.')[0])
   PA="RHEL"+OSV
   OS="rh"+OSV
   OLDVER="older%20version"
   RPMV=(RpmPackages("vee-fs"))
   print RPMV
   Install="yum -y install"
   int_ver=RPMV
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
#    RPMV=(RpmPackages("vee-fs")[3])
    RPMV=(RpmPackages("vee-fs"))
    print RPMV
    int_ver=RPMV
    Install = "zypper -n install"
    PackageInstall('poppler-tools')

def file_write():
   f = open('/tmp/comp.txt', 'w')
   f.write(response.read())
   f.close()
#   File=(open('/tmp/comp.txt','r'))

KERNEL=os.uname()[2]
#KERNEL="3.0.101-108.84-default"
URL="http://repository.adp.amadeus.net/repository/master-ops-vormetric"
print KERNEL
response = urllib2.urlopen(URL+'/Compatibility/')
file_write()
File=(open('/tmp/comp.txt','r'))
for line in File:
   if "Compatibility_Matrix" in line:
      last=line
PDF=(last.split('"')[1])
#PDF="2019-02-12-VDS_Compatibility_Matrix.pdf"
print PDF
VerName1=(PDF).split('_')[0]
print VerName1
url = (URL+"/Compatibility/"+PDF)
os.system("wget "+URL+"/Compatibility/"+PDF+" -P "+LOCATION )
TXTFileName=(os.path.splitext(PDF)[0]+'.txt')
#TXTFileName="test.txt"
os.system("pdftotext "+LOCATION+"/"+PDF+" 2> /dev/null")
#TextFile=(open(LOCATION+"/"+TXTFileName,'r'))
TextFile=(LOCATION+"/"+TXTFileName)
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
                          return (lat_ver)
                          break
                       else:
                          T=(all_lines[i+1])
                          lat_ver=(T.split(')')[0].split('/')[-1].strip().split(' ')[0])
                          return lat_ver
                          break
        else:
            print (KERNEL+" is not present in the doc")
            exit()

lat_ver=latest_version(KERNEL, 0, 2, TextFile, second)
lat_v=((lat_ver[::-1]).replace(".", "-", 1)[::-1])
binary=(("vee-fs-"+lat_v+"-"+OS).strip())
URL_NEW=(URL+'/'+PA+'/')
URL_OLDER=(URL+'/'+PA+'/older/')

def binary_package_search(urL):
    response = urllib2.urlopen(urL)
    f = open('/tmp/comp.txt', 'w')
    f.write(response.read())
    f.close()
    File=(open('/tmp/comp.txt','r'))
    for line in File:
      if binary in line:
         BIN=(line.split('"')[1])
         return BIN

def install_pack():
    os.chmod(LOCATION, 0o744)
    os.system("cd "+LOCATION+" ; sh "+ LOCATION +'/'+binary_pack+' -e')
    os.listdir(LOCATION)
    os.system("rpm -Uvh " + LOCATION + '/' + '*.rpm')

if int_ver == lat_ver:
   print "Latest package is already installed"
else:
   binary_pack=binary_package_search(URL_NEW)
   if binary_pack:
      os.system("wget "+URL_NEW+"/"+binary_pack+" -P "+LOCATION )
      print binary_pack
      install_pack()
   else:
     binary_pack=binary_package_search(URL_OLDER)
     os.system("wget "+URL_OLDER+"/"+binary_pack+" -P "+LOCATION )
     print binary_pack
     install_pack()

