import os.path
import json
import tkinter


if os.path.isfile(r'TextFiles\user.json'):
    f = open(r'TextFiles\user.json', 'r')
    username = json.loads(f.read())
    f.close()
else:
    raise FileNotFoundError(r"File 'TextFiles\user.json', file current user, was not found.")

try:
    user = username.get('username')
except AttributeError:
    user = json.loads(username).get('username')

path = r'TextFiles\Saves\totyp-%s.json' % user
donuts = 0
increase = [0, 0, 0]
decrease = [0, 0, 0]
incUpgrades = {}
decUpgrades = {}
incupBought = {}
decupBought = {}
ingredients = 0
dough = 0
highscore = 0

end = False

incUpgrades = {'Bigger Donuts': increase[0] + 1, 'Better ingredients': increase[1] + 1, 'Hotter Oven': increase[2] + 1}
decUpgrades = {'Cheaper ingredients': decrease[0] + 1, 'Air Bubbles': decrease[1] + 1, 'Windwill Power': decrease[2] + 1}
incupBought = {'Bigger Donuts': 0, 'Better ingredients': 0, 'Hotter Oven': 0}
decupBought = {'Cheaper ingredients': 0, 'Air Bubbles': 0, 'Windwill Power': 0}
boughtUpgrades = {'Extra Keyboard': False, 'Extra Hand': False, 'Faster Proccessor': False}

if os.path.isfile(path) == False:
    f = open(path, 'x')
    f.close()
else:
    f = open(path, 'r')
    save = json.loads(f.read())
    upgrades = save['upgrades']
    donuts = save['donuts']
    boughtUpgrades = save['bUpgrades']
    ingredients = save['ingredients']
    dough = save['dough']
    f.close()
    
if os.path.isfile(r'TextFiles\totyp-leaderboard.json'):
    f = open(r'TextFiles\totyp-leaderboard.json', 'r')
    leaderboard = json.loads(f.read())
    f.close()
    lead = True
else:
    f = open(r'TextFiles\totyp-leaderboard.json', 'x')
    f.close()
    leaderboard = {}
    lead = False

if lead == True:
    leaderboardNum = {}
    sort = sorted(leaderboard.keys())
    for i in sort:
        leaderboardNum.update({leaderboard.get(i): i})
        
    if user in leaderboard:
        highscore = leaderboard.get(user)

    sort = sorted(leaderboardNum.keys())
    leaderboardShow = {}
    for i in sort:
        leaderboardShow.update({leaderboardNum.get(i): i})
else:
    leaderboardShow = {}

#Start Loop       

#End Loop
    
newsave = {'donuts':donuts,'increase':increase,'decrease':decrease,'incUpgrades':incUpgrades,'decUpgrades':decUpgrades,
           'incupBought':incupBought,'decupBought':decupBought,'ingredients':ingredients,'dough':dough}
f = open(path, 'w')
f.write(json.dumps(newsave))

f = open(r'TextFiles\totyp-leaderboard.json', 'w')
f.write(json.dumps(leaderboardShow))
f.close()