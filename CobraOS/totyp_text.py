import os.path
import json



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

while end == False:

    increase = [0, 0, 0]
    decrease = [0, 0, 0]

    print('')
    print('Donuts:', donuts)
    print('')
    print('ingredients:', ingredients)
    print('Dough:', dough)
    print('')
    action = input('What would you like to do? ')
    
    if 'buy' in action:
        cost = int(action[4:len(action) - 1])
        if donuts >= cost:
            donuts = donuts - (cost - decrease[0])
            ingredients = ingredients + (cost + increase[0])
        else:
            print("You don't have enough donuts.")
    elif 'make' in action:
        cost = int(action[5:len(action) - 1])
        if ingredients >= (cost * 5):
            ingredients = ingredients - ((cost * 5) - decrease[1])
            dough = dough + (cost + increase[1])
        else:
            print("You don't have enough dough.")
    elif 'bake' in action:
        cost = int(action[5:len(action) - 1])
        if dough >= (cost * 5):
            dough = dough - ((cost * 5) - decrease[2])
            donuts = donuts + (cost + increase[2])
    elif action == 'beg':
        ingredients = ingredients + 1
        print('You beg a few scraps.')
    elif action == 'upgrades':
        print(upgrades)
    elif action == 'quit':
        end = True
        continue
    elif action == 'leaderboard':
        print('')
        print('Leaderboard:')
        print(leaderboardShow)
    elif action == 'help':
        print('')
        print("Type 'beg' to get 1 ingredient. Type 'make' to turn 5 ingredients into 1 dough.")
        print("Type 'bake' to turn 5 dough into 1 donut. Type 'buy' to turn 1 donut into 5 ingredients.")
        print("Type 'upgrades' to get a list of upgrades. Type the name of an upgrade to buy it.")
        print(r'The cost of an upgrade is its increase/decrease times 10.')
        print('')
    else:
        print("Not an action. Try: 'beg', 'buy', 'make', 'bake', 'upgrades', <upgrade-name>, leaderboard")
    
    if donuts > highscore:
        print('')
        print('New highscore!')
        highscore = donuts
        leaderboardShow.update({user:donuts})
    
newsave = {'donuts':donuts,'increase':increase,'decrease':decrease,'incUpgrades':incUpgrades,'decUpgrades':decUpgrades,
           'incupBought':incupBought,'decupBought':decupBought,'ingredients':ingredients,'dough':dough}
f = open(path, 'w')
f.write(json.dumps(newsave))

leaderboard = {}
#for i in leaderboardShow:
#    leaderboard.update({leaderboardShow.get(i): i})

f = open(r'TextFiles\totyp-leaderboard.json', 'w')
f.write(json.dumps(leaderboardShow))
f.close()
