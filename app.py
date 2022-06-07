from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def index():
    
    writer = open("viewers.txt","a")
    
    writer.write(str(request.user_agent)+"\n")
    return render_template("index.html")

app.run(debug=True)