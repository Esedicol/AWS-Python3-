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
    print ("7. SSH")
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
      instance.ssh()
    elif choice == '9':
      back()
    elif choice == '0':
      exit()
    else:
      instance_menu()

 


if __name__ == '__main__':
  main()