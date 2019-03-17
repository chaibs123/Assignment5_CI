from flask import Flask, request
app = Flask(__name__)

#@app.route("/")
#def hello():
#    jdata = request.get_json()
#    return jdata["username"]

    
@app.route("/", methods=['POST'])
def login():
	jdata = request.get_json()
	if request.method == 'POST':
		if (jdata["password"]=="aA"):
			svar = jdata["password"], 200
			return svar
		else:
			svar = "Invalid username/password", 403
			return svar
