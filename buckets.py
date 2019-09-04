import boto3
import sys
import os
import subprocess
import menu
import time
import webbrowser

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
        str = response.name
        print ("\n< ----- !!! New S3 Bucket <" + str + "> CREATED !!! ----- >")
        
    except Exception as error:
        print('\n< ----- !!!!OPSIES something went wrong!!!!! ----- >')
        print(error)
        

# -------------------------- delete Buckets ----------------------------
def delete_buckets():
    os.system('clear')
    s3 = boto3.resource('s3')
    print ('''
     ===========================================
                 Deleting Buckets
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
        print ("\n< --------- Deleting ", name, " .... --------- >")
        print('')
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


# ------------------- List all Buckets Contents -----------------------------
def list_contents():
    os.system('clear')
    s3 = boto3.resource('s3')
    print ('''
     ===========================================
                Listing Buckets Content
     ===========================================
     ''')

    for bucket in s3.buckets.all():
        for key in bucket.objects.all():
            try:
                print ('\n Bucket Object: ' + str(key))
            except Exception as error:
                print('\n< ----- !!!!OPSIES something went wrong!!!!! ----- >')
                print(error)



# ------------------------- add contents into bucket -----------------
def uploadImage():
    os.system('clear')
    s3 = boto3.resource('s3')
    print('')
    print ('''
     ===========================================
              Adding Image into Buckets
     ===========================================
     ''')
    print('')
    bkts = []
    for b in s3.buckets.all():
        bkts.append(b)
    for x in range (0, len(bkts)):
        print (' Bucket: ', x + 1, '=>\tName:', bkts[x].name)

    print ("\n\nSelect the Bucket you wish to add the new image to *_*")
    index = input (" >>> ")
    bucket_name = bkts[int(index) - 1].name

    print("\nEnter the image's file name along with its extension please :))")
    image = input(' >>> ')
    try:
        print('\n\nAdding ' + image + ' into ' + bucket_name + ' ........................')
        time.sleep(5)
        response = s3.Object(bucket_name, image).put(Body=open(image, 'rb'),  ACL='public-read')
        print('\nImage Successfully added to <' + bucket_name + '>')

        print('\nOpen image (yes or no)?')
        answer = input(' >>> ')

        if answer == 'yes':
            ec2 = boto3.resource('ec2')

            print ('''
             ===========================================
                         Listing instances
             ===========================================
             ''')

            ints = []
            for i in ec2.instances.all():
                ints.append(i)

            for x in range (0, len(ints)):
                print (' Index ', x + 1, '=>\t', ints[x].id, " is ", ints[x].state)
                print (' IP Adress : ' + ints[x].public_ip_address)
                print('\n\n')

            print ("\nEneter the index of desired instance:")
            index = input (' >>> ')
            instance = ints[int(index) - 1]

            open_image(instance, bucket_name, image)
            instance.start()
            print('\n\nInstance Starting ........')
            time.sleep(5)

            instance.wait_until_running()
            instance.load()

            print("Opening" + instance.public_dns_name + " on a new web browser :)")
            dns = instance.public_dns_name
            webbrowser.open("http://" + dns, new=2)

        elif answer =='no':
            menu.bucket_menu()

    except Exception as error:
        print('\n< ----- !!!!OPSIES something went wrong!!!!! ----- >')
        print(error)


def open_image(instance, bucket_name, image):
    os.system('clear')

    # the key used to make the instance selected
    print('\n Please enter the associated key')
    key = input(' >>> ')

    # Image title will display at the very top of the wep app
    print('\n Enter Image Title')
    title = input(' >>> ')

    # Creating a new html file where the title and image will be displated
    index_html = '<html><div align="center"><h1 style="color: "color: #3379b8; font-family: "Source Serif Pro", "serif"; font-size: 34px; padding: .2em 0; border-bottom: 1px solid #ddd;">' + title + '</h1><img src="https://s3-eu-west-1.amazonaws.com/'+ bucket_name + '/' + image +'" width="50%" ></img></div></html>'

    # were going to use the echo command to insert the index line of code into an file
    echo = "echo '"+ index_html + "' > index.html"
    subprocess.run(echo, check=True, shell=True)

    # We will use the ssh command to change the permission into readable, writtable and executable by using the chmod command
    change_permission = "ssh -t -o StrictHostKeyChecking=no -i "+ key +".pem ec2-user@" + instance.public_ip_address + " 'cd /usr/share/nginx/html/ ;sudo chmod 777 index.html' "

    # We will use the SCP file transfer protocol to replace the index.html file in the nginx/html dir
    scp = "scp -i " + key + ".pem index.html ec2-user@" + instance.public_ip_address + ":/usr/share/nginx/html/index.html"

    # Changing permision to read only
    closePermission = "ssh -t -o StrictHostKeyChecking=no -i "+ key +".pem ec2-user@" + instance.public_ip_address + " 'cd /usr/share/nginx/html ;sudo chmod 444 index.html '"


    try:
        os.system('clear')
        print('\nChanging index.html file permission ......')
        time.sleep(2)
        subprocess.run(change_permission, check=True, shell=True)
        print('Done!')


        print('\nReplacing index.html file ......') 
        time.sleep(2)      
        subprocess.run(scp, check=True, shell=True)
        print('Done!')


        print('\nChanging index.html file permission to READ ONLY......') 
        time.sleep(2)      
        subprocess.run(closePermission, check=True, shell=True)
        print('Done!')

    except Exception as error:
        print('\n< ----- !!!!OPSIES something went wrong!!!!! ----- >\n')
        print(error)



# ------------------- delete contents in a bucket -------------------------
def delete_contents():
    os.system('clear')
    s3 = boto3.resource('s3')
    print ('''
     ===========================================
                Deleting Bucket Contents
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









