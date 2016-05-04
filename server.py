from flask import Flask, session, redirect, request, render_template
import random, datetime
app = Flask(__name__)
app.secret_key = "I<3secrets"

@app.route('/')
def main():
	now = datetime.datetime.now()
	tformat = "%a %b %d, %Y %H:%M:%S"
	newTime = now.strftime(tformat)
	session["time"] = newTime
	if "score" not in session:
		session["score"] = 0
	if "text" not in session:
		session["text"] = []
	return render_template('main.html')

@app.route('/process_money', methods = ['POST'])
def money():
	if request.form["action"] == "farm":
		farmgold = random.randint(10,20)
		session["score"] += farmgold
		session["text"].insert(0,"Earned " + str(farmgold) + " golds from the farm! " + session["time"])
	elif request.form["action"] == "cave":
		cavegold = random.randint(5,10)
		session["score"] += cavegold
		session["text"].insert(0,"Earned " + str(cavegold) + " golds from the cave! " + session["time"])
	elif request.form["action"] == "house":
		housegold = random.randint(2,5)
		session["score"] += housegold
		session["text"].insert(0,"Earned " + str(housegold) + " golds from the farm! " + session["time"])
	elif request.form["action"] == "casino":
		housegold = random.randint(0,50)
		chance = random.randint(0,1)
		if chance == 0:
			session["score"] += housegold
			session["text"].insert(0,"Won " + str(housegold) + " golds from the Casino! " + session["time"])
		else:
			session["score"] -= housegold
			session["text"].insert(0,"Lost " + str(housegold) + " golds from the Casino! " + session["time"])
	return redirect('/')
@app.route('/reset')
def clear():
	del session["score"]
	del session["text"]
	return redirect('/')
app.run(debug=True)