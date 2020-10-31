# IIT dep finder

![Screenshot](res/ss.png)

---------------

## Installation:
```
git clone https://github.com/Aniruddha-Deb/IIT_dep_finder.git
cd IIT_dep_finder
```
after this, the preferred way of doing it is to use `venv`:
```
virtualenv venv
echo "venv" > .gitignore
```
create a `logs` directory to store the logs, add `logs` to `.gitignore` and also
create two files, `gunicorn-access.log` and `gunicorn-error.log` to the log folder.
You can start gunicorn with the following commands:
```
gunicorn -c gunicorn.conf.py wsgi:app
```
And you'll need a web server to serve static content, so also set up NGINX.

## Usage:
go to \<site url\>/IIT\_dep\_finder to see the webpage, once the server setup 
is done.
