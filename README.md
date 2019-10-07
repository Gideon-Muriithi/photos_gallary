# Photos_Gallary
A personal gallery application to diplay photos

# Description
This is a Django application that allows users to view images based on the images categories and location. The admin is responsible for uploading, editing and deleting images. The users can search for images according to their categories.


# Setup/Installation Requirements

Ensure you have Python3.6 installed

Clone the project by running <git clone https://github.com/Gideon-Muriithi/photos_gallary>.

Create virtual environment by running <python3.6 -m venv pip virtual> while in the dirctory of the cloned project. Activate the virtual environment by running <source virtual/bin/activate>.

Install all the necessary dependencies necessarry for running the application using this command: pip install-r requirements.txt

Create a database: psql then create the databse using this command: CREATE DATABASE gallery

Run migrations using these respective commmands: python3.6 manage.py makemigrations images then: python3.6 manage.py migrate

Run the app using this command: python3.6 manage.py runserver on the terminal.You can then open the app on your browser

# Technologies Used

Python 3.6
Django
Bootstrap
HTML

# Support and Contact Details
Email : gideongakenge@gmail.com

# Licence
  ### MIT Licence
Copyright(c) 2019 Gideon Muriithi