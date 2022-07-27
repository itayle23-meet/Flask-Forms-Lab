from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "itay"
password = "123"
facebook_friends=["Loai","Yonathan","Adan", "George", "Fouad", "Celina"]


@app.route('/' , methods = ['GET', 'POST'])  # '/' for the default page
def login():
	if request.method == 'GET':
		return render_template('login.html')
	else:
		username = request.form['username']
		password = request.form['password']
		if username == "itay" and password == '123':
			return render_template('home.html', u = username, p = password , facebook_friends = facebook_friends)
  
@app.route('/home')
def home():
	return render_template('home.html' , facebook_friends = facebook_friends)

@app.route('/friend_exists', methods = ['GET', 'POST'])
def friend_exists():
	return render_template('friend_exists.html')

if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)