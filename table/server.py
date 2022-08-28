from flask import Flask, render_template

app = Flask(__name__)

headings = ("First Name", "Last Name", "Full Name")
users = [
    {'first_name': 'Shwan', 'last_name': 'Spencer'},
    {'first_name': 'Burton', 'last_name': 'Guster'},
    {'first_name': 'Juliet', 'last_name': 'OHara'},
    {'first_name': 'Carlton', 'last_name': 'Lassiter'},
]

@app.route("/")
def table():
    return render_template('table.html', headings = headings, users = users)

if __name__ == '__main__':
    app.run(debug=True)