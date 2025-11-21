import fastf1
from fastf1.ergast import Ergast

def load_stats(year: int, race):
    event = fastf1.get_event(year, race)
    race = fastf1.get_session(year, event["EventName"], "R")
    race.load(laps=False, telemetry=False, weather=False, messages=False)
    print(race.results)

def list_events(year: int):
    schedule = fastf1.get_event_schedule(year)
    print(schedule["Country"])
    return int(input("Race: "))

def get_drivers_standings():
    ergast = Ergast()
    standings = ergast.get_driver_standings(season=2025, result_type="pandas")
    for position, driver in standings.content[0].iterrows():
        print(f'{position+1}: {driver["givenName"]} {driver["familyName"]} #{driver["driverNumber"]}')

# year = int(input("Year: "))
# load_stats(year, list_events(year))
# get_drivers_standings()

def fix_team_name(s):
    return s[0]

team_colours = {
    "Ferrari": "#FF2800",
    "Red Bull": "#4781D7",
    "Mercedes": "#00D7B6",
    "Williams": "#1868DB",
    "RB F1 Team": "#6C98FF",
    "Aston Martin": "#229971",
    "Haas F1 Team": "#9C9FA2",
    "Sauber": "#01C00E",
    "Alpine F1 Team": "#00A1E8",
    "McLaren": "#e4901b"
}    

def get_championship():
    ergast = Ergast()
    standings = ergast.get_driver_standings(season=2025, result_type="pandas")
    standings.content[0]['team'] = standings.content[0]['constructorNames'].apply(fix_team_name)
    standings.content[0]['colour'] = standings.content[0]['team'].apply(lambda x: team_colours[x])
    print(standings.content[0])
    print("")
    standingsDict = standings.content[0].to_dict(orient='records')
    
    return standingsDict

get_championship()