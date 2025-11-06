from flask import Flask
from flask import render_template
from flask import request
import database_manager as dbHandler

app = Flask(__name__)

@app.route('/index.html', methods=['GET'])
@app.route('/', methods=['POST', 'GET'])
def index():
   data = dbHandler.listExtension()
   return render_template('/index.html', content=data)

@app.route('/teams.html', methods=['GET'])
def teams():
   return render_template('/teams.html')

@app.route('/results.html', methods=['GET'])
def results():
   return render_template('/results.html')

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=5000)