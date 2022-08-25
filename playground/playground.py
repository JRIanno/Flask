from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return 'How are you today?'

@app.route("/play")
def play_render():
    return render_template('playground.html', times=3, color='lightblue')

@app.route("/play/<int:times>")
def play_num(times):
    return render_template('playground.html', times=times, color='lightblue')

@app.route("/play/<int:times>/<string:color>")
def play_color(times, color):
    return render_template('playground.html', times=times, color=color)

if __name__ == '__main__':
    app.run(debug=True)