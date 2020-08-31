<h1 align = 'center'> Micro blogging website</h1>

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;[![](https://img.shields.io/badge/Made_with-Flask-blue?style=for-the-badge&logo=Flask)](https://flask.palletsprojects.com/en/1.1.x/)
&emsp;[![](https://img.shields.io/badge/IDE-Visual_Studio_Code-red?style=for-the-badge&logo=visual-studio-code)](https://code.visualstudio.com/ "Visual Studio Code")


<h4 align = 'center'> Preview app here - https://social-microblog.herokuapp.com/ </h4>

Project Structure
--------

  ```sh
  ├── Procfile   
  ├── README.md
  ├── config.py
  ├── microblog.py
  ├── test.py
  ├── requirements.txt
  ├── .gitignore
  ├── app
  │   ├── _init_.py
  │   ├── email.py
  │   ├── models.py
  │   ├── search.py
  │   ├── auth
  │   │   ├── _init_.py
  │   │   ├── email.py
  │   │   ├── forms.py
  │   │   ├── routes.py
  │   ├── errors
  │   │   ├── _init_.py
  │   │   ├── handlers.py
  │   ├── main
  │   │   ├── _init_.py
  │   │   ├── forms.py
  │   │   ├── routes.py
  │   └── templates
  │       ├── _post.html
  │       ├── base.html
  │       ├── edit_profile.html
  │       ├── index.html
  │       ├── messages.html
  │       ├── search.html
  │       ├── send_messages.html
  │       ├── user.html
  │       ├── user_popup.html
  │       ├── auth
  │       │   ├── login.html
  │       │   ├── register.html
  │       │   ├── reset_password.html
  │       │   ├── reset_password_request.html
  │       ├── email
  │       │   ├── reset_password.html
  │       │   ├── reset_password.txt
  │       └── errors
  │           ├── 404.html
  │           ├── 500.html
  └── migrations
  ```

### 📷 Screenshots

![LoginPage](https://github.com/tushargithub44/Flask-Blog/blob/master/Screenshots/Successfuly_Registered.PNG)

![ProfilePage](https://github.com/tushargithub44/Flask-Blog/blob/master/Screenshots/profilepage.PNG)

![ExplorePage](https://github.com/tushargithub44/Flask-Blog/blob/master/Screenshots/explore_section.PNG)



### 💻 Tech stack
`Backend` : Python ,Flask <br>
`Database` : SQLAlchemy <br>
`Frontend` : CSS , HTML , Bootstrap, Javascript, jQuery, Ajax  <br>
`Search Engine` : Elastic Search <br>


### 🚀 Features
- Create Post on any topic, share views regarding things you like.
- Explore new people from Explore sections.
- Get Feeds about people you follow in Home section.
- Update your Profile, status anytime.
- Follow/Unfollow Feature.
- Private Messaging service.
- Search about any post using search option (Not deployed due to Heroku Constraints but works fine locally).
- Last seen for Users to know their recent active state.

### 💨 Quick Start

1. Clone the repo
  ```
  $ git clone https://github.com/tushargithub44/Flask-Blog.git
  $ cd Microblog
  ```

2. Initialize and activate a virtualenv(For Windows):
  ```
  $ pip install virtualenv
  $ virtualenv --no-site-packages env
  $ cd env/Scripts
  $ activate.bat
  ```

3. Install the dependencies:
  ```
  $ pip install -r requirements.txt
  ```
  
4. Apply Migrations:
  ```
  $ flask db upgrade
  ```

5. Run the development server:
  ```
  $ flask run
  ```

6. Navigate to [http://localhost:5000](http://localhost:5000)

### :page_with_curl: Acknowledgments & References

* Documentation Flask https://flask.palletsprojects.com/en/1.1.x/
* Documentation Jinja https://jinja.palletsprojects.com/en/2.11.x/
* Documentation Flask-WTF https://flask-wtf.readthedocs.io/en/stable/
* Documentation Flask-SQLAlchemy https://flask-sqlalchemy.palletsprojects.com/en/2.x/
* Documentation Flask-Mail https://pythonhosted.org/Flask-Mail/
* Documentation Flask-BootStrap https://pythonhosted.org/Flask-Bootstrap/
* Mega Tutorial by Miguel Grinberg https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
* ElasticSearch Installation https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html
* Python Elasticsearch Client Docs https://elasticsearch-py.readthedocs.io/en/master/, https://www.elastic.co/guide/index.html

<h3 align="center"><b>Developed with :heart: by <a href="https://github.com/tushargithub44">Tushar</a></b></h1>
