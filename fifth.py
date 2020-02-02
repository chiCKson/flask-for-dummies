from flask import Flask,render_template
app = Flask(__name__) 

@app.route('/<user>')
def home(user):
    return render_template("fourth.html",name=user)

if __name__ =="__main__":
    app.run(debug=True)