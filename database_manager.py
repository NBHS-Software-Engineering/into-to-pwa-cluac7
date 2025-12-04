import sqlite3 as sql

def listExtension():
  con = sql.connect("database/data_source.db")
  cur = con.cursor()
  data = cur.execute('SELECT * FROM drivers').fetchall()
  con.close()
  return data


def search_drivers(q: str):
  con = sql.connect("database/data_source.db")
  cur = con.cursor()

  if not q:
    rows = cur.execute('SELECT * FROM drivers').fetchall()
    con.close()
    return rows

  qparam = f'%{q.lower()}%'
  rows = cur.execute(
    '''
    SELECT * FROM drivers
    WHERE LOWER(CAST(driverNum AS TEXT)) LIKE ?
       OR LOWER(name) LIKE ?
       OR LOWER(team) LIKE ?
    ''',
    (qparam, qparam, qparam)
  ).fetchall()

  con.close()
  return rows