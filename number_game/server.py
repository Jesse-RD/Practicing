from flask import Flask, render_template, session, request, redirect
import random
app = Flask(__name__)
app.secret_key = '123456789'



num = random.randint(1, 1000)

@app.route('/')
def home():
    session['num'] = num
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    session['guess'] = request.form['num_guess']
    return redirect('/guess')
    

@app.route('/guess')
def guess():
    guess = session['guess']
    num = session['num']
    if int(guess) < int(num):
        low = "Too Low!"
        return render_template('guess.html', answer = low)
    elif int(guess) > int(num):
        high = "Too High!"
        return render_template('guess.html', answer = high)
    elif int(guess) == int(num):
        return redirect('/correct')

@app.route('/correct')
def correct():
    return render_template('correct.html')

@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')



if __name__=="__main__":
    app.run(debug=True)
