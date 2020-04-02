# Developer Operations
By: Emmanuel Sedicol (20072377)

## Project Overview

The overall objective of this project is to create a cli tool for interacting with AWS. The tool offers the following functionalities:

1) creation, launching and monitoring a public-facing web server in the Amazon cloud. 
2) Create an Ec2 instance
3) Create and manage S3 Buckets
4) Create private keys

## Set up

Save your own AWS credentials on (~/.aws/credentials). This saves the use of credentials being stored in the program

* `$ python3 --version` - first verify if Python3 is installed
* `$ python3 menu.py` - enter the following command on the your terminal to run the program

## Project layout

        README.md           # This is the project information
        buckets.py          # This is where all the method related to S3 is located
        instance.py         # Contains basic scripts about EC2 instances and file mangement
        mawe-key.pem        # My default key
        menu.py             # Where the menu for is located
        nginx.py            # scripts to check if the server is running
        philippines.png     # test image file

