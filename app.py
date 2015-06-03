from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title="Index")

jsondict = {'corsair':{'name':'Corsair','photo':'CORSAIR.jpg','text':'corsair.txt'}}

@app.route('/<target>')
def template(target):
    with open('static/text/%s' % jsondict[target.lower()]['text'], 'rb') as f:
        text = f.read().decode('utf-8')
    return render_template('template.html',
                           title=jsondict[target.lower()]['name'],
                           image=jsondict[target.lower()]['photo'],
                           text=text)



app.run(host='0.0.0.0', debug=True)
