#!/usr/bin/python3
'''
code structure implemented from:
https://www.bggofurther.com/2015/01/create-an-interactive-command-line-menu-using-python/
'''
import sys
import os
import boto3

 
# Main definition - constants
menu_actions  = {}  

# --------------------------------- main menu -----------------------------
def main_menu():
  os.system('clear')
  print('')
  print('''           \ \ \      /  __| 
          _ \ \ \ \  / \__ \  Amazon Web Services
        _/  _\ \_/\_/  ____/ ''')

  print ('''
  ================================================
         WELCOME to my AWS Automation System
  ================================================
  ''')
  print ("Select one the following to start:")
  print ("1. Instances")
  print ("2. Buckets")
  print ("3. File System")
  print ("4. NGINX")
  print ("5. Keys")
  print ("\n0. Quit")

  choice = input(" >>>  ")
  if (choice == '1'):
    instance_menu()
  elif choice == '2':
    bucket_menu()
  elif choice == '3':
    file()
  elif choice == '4':
    nginx_menu()
  elif choice == '5':
    key()
  elif choice == '0':
    sys.exit()
  else:
    main_menu()

  return

import instance
 # ------------------------------instance menu -------------------------------
def instance_menu():
  os.system('clear')
  while True:
    print ('''
     ===========================================
                      Instance
     ===========================================
     ''')
    print ("Select one the following to start:")
    print ("1. Create Instance")
    print ("2. List Instance")
    print ("3. Start Instance")
    print ("4. Stop Instance")
    print ("5. Terminate Instance")
    print ("6. Tags")
    print ("7. Open Instance")
    print ("\n9. Back")
    print ("\n0. Quit")

    choice = input(" >>>  ")

    if choice == '1':
      instance.create_instance()
    elif choice == '2':
      instance.list_instance()
    elif choice == '3':
      instance.start_instance()
    elif choice == '4':
      instance.stop_instance()
    elif choice == '5':
      instance.terminate_instance()
    elif choice == '6':
      instance.tags()
    elif choice == '7':
      instance.openInstance()
    elif choice == '9':
      back()
    elif choice == '0':
      exit()
    else:
      instance_menu()

 
import buckets
 # ------------------------------ bucket menu -------------------------------
def bucket_menu():
  os.system('clear')
  while True:  
    print ('''
     ===========================================
                      Buckets
     ===========================================
     ''')
    print ("Select one the following to start:")
    print ("1. Create Bucket")
    print ("2. Add Files into Bucket")
    print ("3. List Buckets")
    print ("4. Delete Bucket")
    print ("5. Delete Bucket Contents")
    print ("\n9. Back")
    print ("\n0. Quit")

    choice = input(" >>>  ")
    
    if choice == '1':
      buckets.create_bucket()
    elif choice == '2':
      buckets.add_contents()
    elif choice == '3':
      buckets.list_buckets()
    elif choice == '4':
      buckets.delete_buckets()
    elif choice == '5':
      buckets.delete_contents()
    elif choice == '9':
      back()
    elif choice == '0':
      exit()
    else:
      bucket_menu()


import nginx
# -------------------------- NGINX --------------------------------------
def nginx_menu():
  os.system('clear')
  while True:  
    print ('''
     ===========================================
                      NGINX
     ===========================================
     ''')
    print ("Select one the following to start:")
    print ("1. Check if NGINX is running")
    print ("2. Start NGINX")
    print ("\n9. Back")
    print ("\n0. Quit")

    choice = input (" >>> ")

    if choice == '1':
      nginx.checknginx()
    elif choice == '2':
      nginx.startnginx()
    elif choice == '9':
      back()
    elif choice == '0':
      exit()


# -------------------------- keys --------------------------------------
def key():
  os.system('clear')
  while True:  
    print ('''
     ===========================================
                      Keys
     ===========================================
     ''')
    print ("Select one the following to start:")
    print ("1. List all Keys")
    print ("2. Create new key (.pem)")
    print ("3. Delete key")
    print ("\n9. Back")
    print ("\n0. Quit")

    choice = input (" >>> ")

    if choice == '1':
      instance.list_keys()
    elif choice == '2':
      instance.new_key()
    elif choice == '3':
      instance.delete_keys()
    elif choice == '9':
      back()
    elif choice == '0':
      exit()

# -------------------------- file system --------------------------------------
def file():
  os.system('clear')
  while True:  
    print ('''
     ===========================================
                      File System
     ===========================================
     ''')
    print ("Select one the following to start:")
    print ("1. Add file into instance")
    print ("2. List all Files")
    print ("3. Create file")
    print ("4. Delete file")

    print ("\n9. Back")
    print ("\n0. Quit")

    choice = input (" >>> ")

    if choice == '1':
      instance.add_file()
    elif choice == '2':
      instance.list_file()
    elif choice == '3':
      instance.create_file()
    elif choice == '4':
      instance.del_file()
    elif choice == '9':
      back()
    elif choice == '0':
      exit()




 
# Back to main menu
def back():
  main_menu()
 
# Exit program
def exit():
  sys.exit()
 




def main():
  main_menu()

if __name__ == '__main__':
  main()