# JOWIYE-BLOGS
## Author
Lucy Chimoly
Yegon C Johnstone
Ibrahim Kiprotich
Ebrahim Kamau
Tamminga Budds


# Description
This  is a flask application that allows writers to post blogs, edit and delite blogs. It also allows users who have signed up to comment on the blogs that has been posted by a writer. It also allows a person to subscribed to recieve email everytime a new blog is posted by a writer.

## Live Link
[View Site]()

## Screenshots

## User Story

* A user can view the most recent posts.
* View and comment the blog posts on the site.
* A user should an email alert when a new post is made by joining a subscription.
* Register to be allowed to log in to the application
* A user sees random quotes on the site
* A writer can create a blog from the application and update or delete blogs I have created.

## BDD
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Load the page | **On page load** | Get all blogs, Select between signup and login|
| Select SignUp| **Email**,**Username**,**Password** | Redirect to login|
| Select Login | **Username** and **password** | Redirect to page with blogs that have been posted by writes and be able to subscribe to the blog|
| Select comment button | **Comment** | Form that you input your comment|
| Click on submit |  | Redirect to all comments tamplate with your comment and other comments|
|Subscription | **Email Address**| Flash message "Succesfully subsbribed to D-Blog"|





## Development Installation
To get the code..

1. Cloning the repository:
  ```bash
  https://github.com/chimolirgb/Dynamo-fitness.git
  ```
2. Move to the folder and install requirements
  ```bash
  cd Dynamo
  pip install -r requirements.txt
  ```
3. Exporting Configurations
  ```bash
  export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name}
  ```
4. Running the application
  ```bash
  python manage.py server
  ```
5. Testing the application
  ```bash
  python manage.py test
  ```
Open the application on your browser `127.0.0.1:5000`.


## Technology used

* [Python3.8](https://www.python.org/)
* [Flask](http://flask.pocoo.org/)
* [Heroku](https://heroku.com)


## Known Bugs
* There are no known bugs currently but pull requests are allowed incase you spot a bug

## Contact Information 

If you have any question or contributions, please email me at [johnstoneshylock@gmail.com,ibrakipz7@gmail.com,chimolirgb@gmail.com,ephraim.kamau@student.moringaschool.com,budds300@gmail.com]

## License
* *MIT License:*
* Copyright (c) 2021 ****