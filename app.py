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
	u = urllib2.urlopen("https://ghibliapi.herokuapp.com/films/12cfb892-aac0-4c5b-94af-521852e46d6a")
	s = u.read()
	d = json.loads(s)
	title = d['title']
	director = d['director']
	date = d['release_date']
	score = d['rt_score']
	return render_template("ghibli.html", title = title, director = director, date = date, score = score)
	
if __name__ == '__main__':
    app.debug = True
    app.run()