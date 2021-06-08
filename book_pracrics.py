from datetime import datetime

odds = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,37,39,41,43,45,47,51,53,55,57,59]

right_this_minute= datetime.today().minute

if right_this_minute in odds:
    print("this minute seems a little dot.")
else:
    print("not an odd minute.")
