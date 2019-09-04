#!/usr/bin/python3

"""A tiny Python program to check that nginx is running.
Try running this program from the command line like this:
  python3 check_webserver.py
"""

import subprocess
import sys


def checknginx():
  cmd = 'ps -A | grep nginx | grep -v grep'

  (status, output) = subprocess.getstatusoutput(cmd)

  if status > 0:  
    print("\nNginx Server IS NOT running")
  else:
    print("\nNginx Server IS running")

def startnginx():
  try:
    cmd = 'sudo service nginx start'
    subprocess.run(cmd, check=True, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print("Nginx started")
   
  except subprocess.CalledProcessError:
    print("--- Error starting Nginx! ---")
    
# Define a main() function.
def main():
    if checknginx() == 1:
      startnginx()
      
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()