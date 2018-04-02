import os
import boto3
import time
import sys
from datetime import datetime

session=boto3.Session(profile_name='default')
s3=session.client('s3')
resource=boto3.resource('s3')

def download(s3, bucket, obj, local_file_path):
    s3.download_fileobj(bucket,obj,local_file_path)

def uploadto(s3,local_file_path,bucket, obj):
    s3.upload_file(local_file_path,bucket,obj)

def make_public_read(s3,bucket, key):
    s3.put_object_acl(ACL='public-read',Bucket=bucket,Key=key)

if len(sys.argv) <=3:
    print ("put extra options!")
    sys.exit

download=sys.argv[3]
makepublic=sys.argv[2]
uploadpath=sys.argv[1]

def upload(dirname):
    res=[]
    for root,dirs, files in os.walk(dirname):
        rootpath=os.path.join(os.path.abspath(dirname),root)
        for file in files:
            filepath = os.path.join(rootpath, file)
            uploadto(s3,filepath,bucket,year+'/'+today+'/'+file)
            if makepublic=='1': make_public_read(s3,bucket,year+'/'+today+'/'+file)


today="%02d-%02d" % (datetime.today().month,datetime.today().day)
year="%04d" % datetime.today().year


if __name__ == "__main__":
    bucket = "khu-bigdata-course-junhu"

    s3 = boto3.client('s3')
    
    if download=='1':
        for obj in s3.list_objects(Bucket='khu-bigdata-course-junhu')['Contents']:
            try:  
        		filename = obj['Key'].rsplit('/', 1)[1]
                
            except IndexError:
        		filename = obj['Key']

            localfilename = os.path.join('/home/junhukang/Downloads/', filename)

            s3.download_file(bucket, obj['Key'], localfilename)
    elif download=='0':
        upload(uploadpath)
       
