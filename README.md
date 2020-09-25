# url_counter
Implement a job queue feature in a flask web app backed by a database.

### Steps to install and use the application

- Create a python virtual environment and install the dependencies in requirements.txt
    - ``` pip install -r requirements.txt```   
- You will need 3 different terminals to run different processes.
    1) ```redis-server``` to run redis 
    2) ```rqworker``` command to run redis queue to run the app asynchronously.
    3) python web_app.py to  run the Flask Application in development mode.

- After this you will be able to run the application at ```localhost:5000```
    - /url and / is used to submit url
    - /index is where we can see the urls with their respective count retrived from the database/
