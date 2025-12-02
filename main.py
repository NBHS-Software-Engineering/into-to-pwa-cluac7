from flask import Flask
from flask import render_template
from flask import request
import database_manager as dbHandler
import f1api

app = Flask(__name__)

@app.route('/index.html', methods=['GET'])
@app.route('/', methods=['POST', 'GET'])
def index():
   data = dbHandler.listExtension()
   return render_template('/index.html', content=data)

@app.route('/teams.html', methods=['GET'])
def teams():
   data = dbHandler.listExtension()
   return render_template('/teams.html', content=data)

# The main route for the F1 Starting Grid
@app.route('/results.html')
def results():
   drivers = f1api.get_championship()
   return render_template("/results.html", drivers=drivers)


if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=5000)