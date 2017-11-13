from flask import Flask, render_template, request, session, redirect, url_for, flash
import urllib2, json

app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def root():
	u = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=EaY9DuwzNdvTDJNTAAjNNhTDqQ9v415uVpKq3jWk")
	s = u.read()
	d = json.loads(s)
	type = d['media_type']
	image = d['url']
	title = d['title']
	return render_template("index.html", type = type, image = image, title = title)
	
@app.route('/chucknorris', methods = ['GET','POST'])
def chuck():
	u = urllib2.urlopen("https://api.chucknorris.io/jokes/random")
	#s = u.read()
	#d = json.loads(s)
	#joke = d['value']
	return render_template("chuck.html")
	
if __name__ == '__main__':
    app.debug = True
    app.run()