from easygui import *
msgbox("Hello World!")

msg = "Pick a position"
title = "Positions"
choices = ["Goalkeeper", "Centre-Back", "Right-Back", "Left-Back", "Attacking Midfield", "Central Midfield", "Defensive Midfield", "Right Winger", "Left Winger", "Centre-Forward", "Second Striker"]
choice = choicebox(msg, title, choices)