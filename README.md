# Developer Operations Assignment 1 
By: Emmanuel Sedicol (20072377)

## Project Overview

The overall objective of this assignment is to automate using Python 3 the process of
creating, launching and monitoring a public-facing web server in the Amazon cloud. The web
server will run on an EC2 instance and display some static content that is stored in S3. 

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

## Main Menu
When you run the program you are prompted the main menu where you have multiple choices. Each choices have inner selections that do things about the choice.
It hard to get lost along the way as you browse through the program but if you do I have inserted options for users to go back to the main menu or exit the program itself.

![image](https://mawe.s3-eu-west-1.amazonaws.com/Screenshot+2019-09-01+at+23.12.32.png)
