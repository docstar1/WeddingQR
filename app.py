from ordereddict import OrderedDict
from flask import Flask
from flask import render_template
import glob

app = Flask(__name__)

jsondict = {}
files = glob.glob("static/img/*.jpg")
for file in files:
    filename = file.split('/')[2].strip('.jpg')
    jsondict[filename.lower()] = {'name':filename,'photo':'%s.jpg' % filename, 'text':'%s.txt' % filename}
jsondictsorted = OrderedDict(sorted(jsondict.items(), key=lambda t: t[0]))

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title="Index", jsondict=jsondictsorted)

@app.route('/<target>')
def template(target):
    try:
        with open('static/text/%s' % jsondict[target.lower()]['text'], 'rb') as f:
            text = f.read().decode('utf-8')
    except IOError:
        text = "PLACEHOLDER TEXT"
    return render_template('template.html',
                           title=jsondict[target.lower()]['name'],
                           image=jsondict[target.lower()]['photo'],
                           text=text)



app.run()
