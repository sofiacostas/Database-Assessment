# Import the libraries to connect to the database and present the information in tables
import sqlite3
from tabulate import tabulate

# This is the filename of the database to be used
DB_NAME = 'players_stats.db'

def print_query(view_name:str):
    ''' Prints the specified view from the database in a table '''
    # Set up the connection to the database
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    # Get the results from the view
    sql = "SELECT * FROM '" + view_name + "'"
    cursor.execute(sql)
    results = cursor.fetchall()
    # Get the field names to use as headings
    field_names = "SELECT name from pragma_table_info('" + view_name + "') AS tblInfo"
    cursor.execute(field_names)
    headings = list(sum(cursor.fetchall(),()))
    # Print the results in a table with the headings
    print(tabulate(results,headings))
    db.close()

menu_choice =''
while menu_choice != 'Z':
    menu_choice = input('Welcome to the Tottenham Hotspurs players database for the 23/24 season\n\n'
                        'Please type the letter for the information you want\n'
                        'A: All information\n'
                        'B: Top 8 goalscorers\n'
                        'C: Most minutes played\n'
                        'D: Players with at least 1 goal and 1 assist\n'
                        'E: Centre-Forward players stats\n'
                        'F: All non England players\n'
                        'G: Games played and amount of yellow cards\n'
                        'H: Players with under 2000 minutes played\n'
                        'I: Players under 25\n'
                        'J: Top 5 players with the most assists\n'
                        'K: Players with at least 25 games and 2500 mins played\n'
                        'Z: Exit\n\n Type option here: ')