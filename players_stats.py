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
                        'I: Players under 25 years old\n'
                        'J: Top 5 players with the most assists\n'
                        'K: Players with at least 25 games and 2500 mins played\n'
                        'Z: Exit\n\n Type option here: ')

    menu_choice = menu_choice.upper()
    if menu_choice == 'A':
        print_query('All information')
    elif menu_choice == 'B':
        print_query('Top 8 goalscorers')
    elif menu_choice == 'C':
        print_query('Most minutes played')
    elif menu_choice == 'D':
        print_query('Players with at least 1 goal and 1 assist')
    elif menu_choice == 'E':
        print_query('Centre-Forward players stats')
    elif menu_choice == 'F':
        print_query('All non England players')
    elif menu_choice == 'G':
        print_query('Games played and amount of yellow cards')
    elif menu_choice == 'H':
        print_query('Players with under 2000 minutes played')
    elif menu_choice == 'I':
        print_query('Players under 25')
    elif menu_choice == 'J':
        print_query('Top 5 players with most assists ')
    elif menu_choice == 'K':
        print_query('Players with at least 25 games and 2500 mins played')






    
