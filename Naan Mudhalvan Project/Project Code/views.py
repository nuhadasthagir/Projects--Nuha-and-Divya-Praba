from django.views import View
from flask import Blueprint, jsonify,render_template,request,redirect,url_for
views=Blueprint(__name__,"views")
@views.route("/") 
def home():
    return render_template('index.html')
@views.route("/dashboard") 
def dashboard():
   return render_template('index-page.html')
@views.route("/report") 
def report():
     return render_template('report.html')
@views.route("/json") 
def get_json():
    return jsonify({'name':'div'})
@views.route("/data")
def get_data():
    data=request.json
    return jsonify(data)
@views.roue("/go-to-home")
def go_to_home():
    return redirect(url_for("views."))
