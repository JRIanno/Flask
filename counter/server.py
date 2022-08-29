from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'qwertasdf'

@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 0
    else:
        session['count'] += 1
    
    return render_template('counter.html')

@app.route('/add', methods=['POST'])
def add():
    if request.form['plus'] == 'add':
        session['count'] += 3
    return redirect ('/')

@app.route('/pop')
def pop():
    session.pop('count')
    return redirect ('/')


if __name__ == '__main__':
    app.run(debug=True)