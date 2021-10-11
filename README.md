## bengallery
Is an application that allows users to  view different photos, click on a single photo and view its details, search for different categories of photos, copy link of the photo and also view based on location.
## Author
Bernard Opiyo

## Installation
Use the following command to install all the requirement applications. pip freeze -r requirements.txt

## setup
* Run git clone https://github.com/Bernard2030/bengallery or download the zip file from github.

After extracting the files,

* Navigate to the project folder cd into it.

* Creating a virtual environment virtualenv virtual.

* Activating the virtual environment source virtual/bin/activate.

* Running the application python3 manage.py runserver

* Running tests python3 manage.py test.

* create database
    You will need to create a database a new postgress database by typing the following command to access postgress
        $ psql
    Then run below query to create a new database named bengallery
        
* create Database migrations
    make migrations on postgres using django
        python3.8 manage.py makemigrations 
    then run the below command.
        python3.8 manage.py migrate

## Technologies used
* Python3.8
* Django  
* HTML5  
* Bootstrap4

user story

* View different photos that interest me.
* Click on a single photo to expand it and also view the details of the photo. The photo details must * appear on a modal within the same route as the main page.
* Search for different categories of photos. (ie. Travel, Food)
* Copy a link to the photo to share with my friends.
* View photos based on the location they were taken.


## pictorial Discription
<img src="image/image1.png" alt="landing"/>
<img src="image/image2.png" alt="landing"/>
<img src="image/image3.png" alt="landing"/>
<img src="image/image4.png" alt="landing"/>
<img src="image/image5.png" alt="landing"/>
	
	
	
	
	
	
## Known Bugs
There are no known bugs at the moment if you find any reach out through brobernard.254@gmail.com

## Collaboration
To contribute on the application you can do so by reaching me on brobernard.254@gmail.com

## LICENSE
This project is under [MIT](LICENSE).