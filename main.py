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
   driversold = [
    {
        "position": 1,
        "number": 16,
        "name": "Charles Leclerc",
        "team": "Ferrari",
        "color": "#E8002D",
        "time": "1:31.421"
    },
    {
        "position": 2,
        "number": 1,
        "name": "Max Verstappen",
        "team": "Red Bull Racing",
        "color": "#3671C6",
        "time": "1:31.489"
    },
    {
        "position": 3,
        "number": 44,
        "name": "Lewis Hamilton",
        "team": "Mercedes",
        "color": "#00D2BE",
        "time": "1:31.770"
    },
    {
        "position": 4,
        "number": 81,
        "name": "Oscar Piastri",
        "team": "McLaren",
        "color": "#FF8000",
        "time": "1:31.812"
    },
    {
        "position": 5,
        "number": 63,
        "name": "George Russell",
        "team": "Mercedes",
        "color": "#00D2BE",
        "time": "1:31.950"
    },
    {
        "position": 6,
        "number": 11,
        "name": "Sergio Pérez",
        "team": "Red Bull Racing",
        "color": "#3671C6",
        "time": "1:32.002"
    },
    {
        "position": 7,
        "number": 4,
        "name": "Lando Norris",
        "team": "McLaren",
        "color": "#FF8000",
        "time": "1:32.110"
    },
    {
        "position": 8,
        "number": 55,
        "name": "Carlos Sainz",
        "team": "Ferrari",
        "color": "#E8002D",
        "time": "1:32.140"
    },
    {
        "position": 9,
        "number": 14,
        "name": "Fernando Alonso",
        "team": "Aston Martin",
        "color": "#229971",
        "time": "1:32.230"
    },
    {
        "position": 10,
        "number": 18,
        "name": "Lance Stroll",
        "team": "Aston Martin",
        "color": "#229971",
        "time": "1:32.310"
    },
    {
        "position": 11,
        "number": 23,
        "name": "Alexander Albon",
        "team": "Williams",
        "color": "#005AFF",
        "time": "1:32.410"
    },
    {
        "position": 12,
        "number": 2,
        "name": "Logan Sargeant",
        "team": "Williams",
        "color": "#005AFF",
        "time": "1:32.500"
    },
    {
        "position": 13,
        "number": 24,
        "name": "Zhou Guanyu",
        "team": "Stake F1 Sauber",
        "color": "#52E252",
        "time": "1:32.620"
    },
    {
        "position": 14,
        "number": 77,
        "name": "Valtteri Bottas",
        "team": "Stake F1 Sauber",
        "color": "#52E252",
        "time": "1:32.700"
    },
    {
        "position": 15,
        "number": 20,
        "name": "Kevin Magnussen",
        "team": "Haas",
        "color": "#B6BABD",
        "time": "1:32.820"
    },
    {
        "position": 16,
        "number": 27,
        "name": "Nico Hülkenberg",
        "team": "Haas",
        "color": "#B6BABD",
        "time": "1:32.900"
    },
    {
        "position": 17,
        "number": 22,
        "name": "Yuki Tsunoda",
        "team": "RB F1 Team",
        "color": "#1430FF",
        "time": "1:33.010"
    },
    {
        "position": 18,
        "number": 40,
        "name": "Liam Lawson",
        "team": "RB F1 Team",
        "color": "#1430FF",
        "time": "1:33.090"
    },
    {
        "position": 19,
        "number": 3,
        "name": "Daniel Ricciardo",
        "team": "RB F1 Team (sub)",
        "color": "#1430FF",
        "time": "1:33.300"
    },
    {
        "position": 20,
        "number": 21,
        "name": "Oliver Bearman",
        "team": "Haas (reserve)",
        "color": "#B6BABD",
        "time": "1:33.500"
    }
   ]
   drivers = f1api.get_championship()
   return render_template("/results.html", drivers=drivers)


if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=5000)