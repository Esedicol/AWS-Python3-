import boto3
import sys
import os

# ------------------------- create Buckets -----------------------------
def create_bucket():
    os.system('clear')
    s3 = boto3.resource('s3')
    print ('''
     ===========================================
                 Creating Bucket
     ===========================================
     ''')
    print ("\nEnter new Bucket Name")
    name = input (" >>> ")

    try:
        response = s3.create_bucket(Bucket = name, CreateBucketConfiguration={'LocationConstraint': 'eu-west-1'})
        print ("\n< ----- !!! BUCKET CREATED !!! ----- >")
        print (response)
    except Exception as error:
        print('\n< ----- !!!!OPSIES something went wrong!!!!! ----- >')
        print(error)

# -------------------------- delete Buckets ----------------------------
def delete_buckets():
    os.system('clear')
    s3 = boto3.resource('s3')
    print ('''
     ===========================================
                 Listing Buckets
     ===========================================
     ''')
    bkts = []
    for b in s3.buckets.all():
        bkts.append(b)
    for x in range (0, len(bkts)):
        print (' Bucket: ', x + 1, '=>\tName:', bkts[x].name)

    print ("\n\nEnter bucket name to delete it!! => ")
    index = input (" >>> ")
    name = bkts[int(index) - 1].name

    bucket_name = s3.Bucket(name)
    try:
        response = bucket_name.delete()
        print ("\n< ------- Deleting ", name, "------- >")
        print ("< ------- Bucket Succesfully deleted !!!! ------ >")
    except Exception as error:
        print('\n< ----- !!!!OPSIES something went wrong!!!!! ----- >')
        print(error)


# ------------------- List all Buckets -----------------------------
def list_buckets():
    os.system('clear')
    s3 = boto3.resource('s3')
    print ('''
     ===========================================
                 Listing Buckets
     ===========================================
     ''')
    try:   
        bkts = []
        for b in s3.buckets.all():
            bkts.append(b)

        for x in range (0, len(bkts)):
            print("\nBucket Name => ", bkts[x].name)
    except Exception as error:
        print('\n< ----- !!!!OPSIES something went wrong!!!!! ----- >')
        print(error)

# ------------------------- add contents into bucket -----------------
import tkinter as tk
from tkinter import filedialog

def add_contents():
    os.system('clear')
    s3 = boto3.resource('s3')
    print ('''
     ===========================================
                 Adding to Buckets
     ===========================================
     ''')
    bkts = []
    for b in s3.buckets.all():
        bkts.append(b)
    for x in range (0, len(bkts)):
        print (' Bucket: ', x + 1, '=>\tName:', bkts[x].name)

    print ("\n\nEnter index of bucket to add files into it => ")
    index = input (" >>> ")
    i = int(index) -1 
    name = bkts[i].name

    print ("\nSelect one of the following => ")
    print ("1. Add existing files.")
    print ("2. Create new file.")
    file = input (" >>> ")
    newFile = ''

    if file == '1':
        print ("\nFile Dialog Opening .......")
        os.system('clear')
        file_path = filedialog.askopenfilename()
        os.system('clear')
        newFile = file_path 
        print(newFile)
        print(newFile.name)
        os.system('clear')


    elif file == '2':
        print ("\nEnter new file name => ")
        newFile = input (" >>> ")
        f = open(newFile, 'w')
        print ("New file ", f, " successfully created!!")
    else:
        print ("Invalid Input!!")
        add_contents()

    try:
        s3 = boto3.client('s3')
        s3.upload_file(newFile,name,newFile)
        print('file uploaded')
    except Exception as error:
        print (error)

    # try:
    #     s3.upload_file(newFile, )
    #     # response = s3.Object(name, newFile).put(Body=open(newFile, 'rb'), ACL='public-read')
    #     # print ("\nNew files successfully added into ", name)
    #     # print (json.load(response))
    # except Exception as error:
    #     print('\n< ----- !!!!OPSIES something went wrong!!!!! ----- >\n\n')
    #     print(error)


# ------------------- delete contents in a bucket -------------------------
def delete_contents():
    os.system('clear')
    s3 = boto3.resource('s3')
    print ('''
     ===========================================
                 Adding to Buckets
     ===========================================
     ''')
    bkts = []
    for b in s3.buckets.all():
        bkts.append(b)
    for x in range (0, len(bkts)):
        print (' Bucket: ', x + 1, '=>\tName:', bkts[x].name)
   

    print ("\n\nEnter index of bucket to delete files from it => ")
    index = input (" >>> ")
    name = bkts[int(index) -1].name
    bucket = s3.Bucket(name)
    for x in bucket.objects.all():
        try:
            response = x.delete()
            print ("\nBucket Contents sucessfully deleted!!")
        except Exception as error:
            print('\n< ----- !!!!OPSIES something went wrong!!!!! ----- >\n\n')
            print(error)









