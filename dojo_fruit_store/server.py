from flask import Flask, render_template, request, redirect
import datetime
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.context_processor
def inject_today_date():
    return {'date': datetime.date.today(), 'time': datetime.datetime.utcnow()}

@app.route('/checkout', methods=['POST'])         
def checkout():
    firstName = request.form['firstName']
    lastName = request.form['lastName']
    student_id = request.form['student_id']
    strawberries = request.form['strawberries']
    raspberries = request.form['raspberries']
    apples = request.form['apples']
    items = int(request.form['strawberries']) + int(request.form['raspberries']) + int(request.form['apples'])
    print(request.form)
    print("Charging ", firstName, lastName, " for ", items, " fruits.")
    return render_template("checkout.html", firstName = firstName, lastName = lastName, student_id = student_id, strawberries = strawberries, raspberries = raspberries, apples = apples, items = items)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    