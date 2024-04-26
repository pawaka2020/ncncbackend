This is a backend meant to be used together with the NCNC Flutter app

Libraries used to create this backend:
Flask
Mongodb

How to set up:

1. Download and install Mongodb https://www.mongodb.com/try/download/community
2. Change the IPV4_ADDRESS value in config.py to IPV4 address of the internet connection of local machine.
3. Make sure MONGODB_HOST value in models/mongodb/db.py is set to 'mongodb://localhost:27017/' or whichever value matches 
4. Make sure 'client' value in 
5. Type 'python app.py' on terminal to launch this backend.
6. If everything goes well, you should be able to see a webpage that shows 'NCNC Backend' on <IPV4_ADDRESS>:5000
(for example, http://192.168.1.40:5000)