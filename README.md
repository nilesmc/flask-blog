A Flask Blog

to start the application

# python3 -m venv venv
# virtualenv -p python3 venv
# source venv/bin/activate
# pip install -r requirements.txt
# export FLASK_APP=flask-blog.py
# run flask

To turn on the smtp service needed for email alerts:
“python -m smtpd -n -c DebuggingServer localhost:25"
