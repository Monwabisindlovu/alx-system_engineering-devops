0x1A. Application server
Overview
This project focuses on setting up an application server to serve dynamic content for an Airbnb clone project. The application server will work alongside Nginx, which acts as a reverse proxy server. By following the tasks outlined in this project, you'll configure your server environment, set up Gunicorn as the WSGI server, and configure Nginx to serve dynamic content from your Flask application.

Concepts
Throughout this project, you'll explore the following concepts:

Web Server
Server
Web stack debugging
Background Context
The web infrastructure already includes Nginx, which serves static web pages. However, to handle dynamic content, an application server is needed. The goal of this project is to integrate the application server into the existing infrastructure, connecting it to Nginx and making it serve the Airbnb clone project.

Requirements
All Python-related tasks should be done using Python 3.
Config files must have comments for clarity.
Bash scripts must pass Shellcheck without any errors.
Servers must be running Ubuntu 16.04 LTS.
Tasks
Set up development with Python: Configure Flask to serve content from a specific route on port 5000.
Set up production with Gunicorn: Install Gunicorn and configure it to serve the same content as in task 1 on port 5000.
Serve a page with Nginx: Configure Nginx to serve the content from task 2 at the route /airbnb-onepage/.
Add a route with query parameters: Configure Nginx to proxy requests to a Gunicorn instance listening on port 5001 for a new route.
Serve your AirBnB clone: Configure Nginx to serve content from the AirBnB clone project, including handling static assets.
Deploy it!: Set up a systemd script to start the Gunicorn process automatically on system boot.
No service interruption: Write a Bash script to reload Gunicorn gracefully, ensuring no service interruption.
Resources
Application server vs web server
How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04
Running Gunicorn
Upstart documentation
Author
MOnwabisi Ndlovu
