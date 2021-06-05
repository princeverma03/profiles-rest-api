# Profiles REST API

Profiles REST API code.

Project outcomes:

1. Creating and updating user profiles.
2. Login and authentication.
3. Posting status updates.
4. Viewing status update feeds.
5. Deploying API on AWS server


Commands for running the api on local development server.
1. python manage.py runserver 0.0.0.0:8000 ; # 8000 is the guest host port number
2. Open web browser -> 127.0.0.1:8000/api/ ; same port number as 8000

For superuser creation on dev server
python manage.py createsuperuser
email:...
name:...
password:...

Commands for deploying the api on AWS Server.
1. Create a account on AWS and login.
2. Add key-pair value from you local system to AWS. 
3. Configure the AWS EC2 free tier instance, choose ami-ubuntu Server 18.04 LTS , SSD Volume type.
4. Add HTTP access into the instance in Configure and security group and add the above ssh-key pair to it and launch the instance.

5. Open setup.sh in deploy folder. Modify this to your github profile. All codes are present here.
6. We clone project from the specified git to aws server SSD volume space. All the files from github to AWS are mounted into \usr\local\apps\profiles-rest-api.

7. In local bash: ssh ubuntu@<copy the EC2 instance public DNS IPV4 ID>.
8. Get a url of the rawfile of deploy.sh or update.sh from the github added in step 5.
9. $ubuntu@<>: curl -sL <step 8 url> | sudo bash -
10. Go to browser and enter : <copy the EC2 instance public DNS IPV4 ID>/api/ ex; ec2-18-4F..../api/

12. Same thing can be done with update.sh file also.

For super user creation on AWS.
1. on AWS, $ubuntu@<>: cd \usr\local\apps\profiles-rest-api;
2. sudo env\bin\python manage.py createsuperuser
email:...
name:...
password:...
