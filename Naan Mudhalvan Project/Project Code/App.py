from flask import Flask, render_template
from views import views
app=Flask(__name__)
app.register_blueprint(views,url_prefix="/views")
app.secret_key='divnuha'



@app.route('/', methods=["GET", "POST"])
def home(): 
    return render_template('index.html')

@app.route('/dashboard', methods=["GET", "POST"])
def dashboard():
   return render_template('index-page.html')

@app.route('/report', methods=["GET", "POST"]) 
def report():
     return render_template('report.html')

@app.route('/story', methods=["GET", "POST"])
def story():
    return render_template('portfolio-details.html')



if __name__=="__main__": 
    app.run(debug=True)