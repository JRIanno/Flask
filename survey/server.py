from flask import Flask, render_template, request, redirect, session

app= Flask(__name__)

app.secret_key = 'bannanasinpajamas'

@app.route('/')
def index():
    print(request.form)
    return render_template('survey.html')

@app.route('/result', methods=['POST'])
def result():
    print('Get Post Info')
    print(request.form)
    name = request.form["name"]
    dojo_hall = request.form['Location']
    language_learned = request.form['language_learned']
    Comments = request.form['Comments']
    return render_template('result.html', name = request.form['name'], dojo_hall = request.form['Location'], language_learned = request.form['language_learned'], comments = request.form['Comments'])


if __name__ == '__main__':
    app.run(debug=True)
