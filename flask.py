from flask import Flask, render_template
import flask
#from flask import render_template
app = flask(__name__)  # , template_folder='templates'


@app.route('/')
def index():
    my_list = ["Wert 1", "Wert 2", "Wert 3"]
    return render_template('index.html', my_list=my_list)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')