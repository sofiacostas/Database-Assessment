# Import the libraries to connect to the database and present the information in tables
import sqlite3
from tabulate import tabulate

# This is the filename of the database to be used
DB_NAME = 'players_stats.db'
# This is the SQL to connect to all the tables in the database
TABLES = (" players_stats "
          "LEFT JOIN nations ON players_stats.nation_id = nations.nation_id "
          "LEFT JOIN positions ON players_stats.position_id = positions.position_id ")

def print_parameter_query(fields:str, where:str, parameter):
    """ Prints the results for a parameter query in tabular form. """
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    sql = ("SELECT " + fields + " FROM " + TABLES + " WHERE " + where)
    cursor.execute(sql,(parameter,))
    results = cursor.fetchall()
    print(tabulate(results,fields.split(",")))
    db.close()

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
    menu_choice = input('Welcome to the Tottenham Hotspurs players database from the 23/24 season\n\n'
                        'PLEASE NOTE: This database ONLY INCLUDES the following players\n'
                        ' - Players who are currently still in the club\n'
                        ' - Players who have played during this season\n'
                        ' - Players who did not go on loan for most/entire season\n'
                        ' - Loan players coming in do count\n\n'
                        'Please type the letter for the information that you want\n'
                        'To exit please type "Z"\n\n'
                        'A: All stats\n'
                        'B: Top 8 goalscorers\n'
                        'C: Most minutes played\n'
                        'D: Have had at least 1 goal and assist\n'
                        'E: What position players are\n'
                        'F: What nation players are\n'
                        'G: Games played and amount of yellow cards\n'
                        'H: Less than 2000 minutes played\n'
                        'I: Under 25 years old\n'
                        'J: Top 5 assisters\n'
                        'K: At least 25 games and 2500 mins played\n'
                        'L: Top 5 most games played by players 27years or older\n'

                        'Z: Exit\n\n''Type option here: ')

    menu_choice = menu_choice.upper()
    if menu_choice =='A':
        print_query('All information')
    elif menu_choice =='B':
        print_query('Top 8 goalscorers')
    elif menu_choice =='C':
        print_query('Most minutes played')
    elif menu_choice =='D':
        print_query('At least 1 goal and 1 assist')
    elif menu_choice =='E':
        print('Here are the following positions to choose from\n'
              '- Goalkeeper\n'
              '- Centre-Back\n'
              '- Right-Back\n'
              '- Left-Back\n'
              '- Attacking Midfield\n'
              '- Central Midfield\n'
              '- Defensive Midfield\n'
              '- Right Winger\n'
              '- Left Winger\n'
              '- Centre-Forward\n'
              '- Second Striker\n')
        position = input('Of what position do you want to see players of: ')
        print_parameter_query("name, age, games_played", "position = ? ORDER BY age DESC",position)
    elif menu_choice =='F':
        print('Here are the following nations to choose from\n'
              '- Italy\n'
              '- England\n'
              '- Argentina\n'
              '- Netherlands\n'
              '- Spain\n'
              '- Romania\n'
              '- Brazil\n'
              '- Colombia\n'
              '- Wales\n'
              '- Senegal\n'
              '- Mali\n'
              '- Uruguay\n'
              '- Denmark\n'
              '- Sweden\n'
              '- South Korea\n'
              '- Germany\n'
              '- Israel\n')
        nation = input('Of what nation do you want to see players of: ')
        print_parameter_query("name, age, games_played", "nation = ? ORDER BY age DESC",nation)
    elif menu_choice =='G':
        print_query('Games played and amount of yellow cards')
    elif menu_choice =='H':
        print_query('Under 2000 minutes played')
    elif menu_choice =='I':
        print_query('Age under 25')
    elif menu_choice =='J':
        print_query('Top 5 players most assists')
    elif menu_choice =='K':
        print_query('At least 25 games and 2500 mins played')
    elif menu_choice =='L':
        print_query('Top 5 players 27 or older most games played')






    
