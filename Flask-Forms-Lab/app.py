from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "siwarha"
password = "123"
facebook_friends=["Loai","Kenda","Avigail", "George", "Fouad", "Gi"]

@app.route('/',methods=['GET', 'POST'])
def login():
		if request.method=='GET':
			return render_template('login.html')
		else: 
			name1=request.form['username']
			password1=request.form['password']
			if name1==username and password1==password:
				return redirect(url_for('home'))
			else:
				return render_template('login.html')



			  # '/' for the default page
	
@app.route('/home',methods=['GET', 'POST'])
def home():
	return render_template('home.html')

  



if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)
