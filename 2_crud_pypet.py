line = ""
for i in range(0,53):
  line += '-'

print(line)
print('Welcome to Pypet!'.center(53))
print(line)

################## MODEL ##################

rank = {
  'star': [(0,'✰'),(1,'✰✰'),(2,'✰✰✰'),(3,'✰✰✰✰')],
  'circle': [(0,'ꔷ'),(1,'ꔷꔷ'),(2,'ꔷꔷꔷ'),(3,'ꔷꔷꔷꔷ')],
  'heart': [(0,'♥'),(1,'♥♥'),(2,'♥♥♥'),(3,'♥♥♥♥')]
}

food = {
  'va': {
    'name': 'Vitamin-A',
    'calories' : '4cal',
    'amount': '2kg'
  },
  'vb': {
    'name': 'Vitamin-B',
    'calories' : '2cal',
    'amount': '1.5kg'
  },
  'vc': {
    'name': 'Vitamin-C',
    'calories' : '1cal',
    'amount': '1kg'
  }
}

pettype = ['cat','mouse','fish']

cat = {
  'name': 'Garfy',
  'type': pettype[0],
  'hungry': True,
  'weight': 9.5,
  'age': 5,
  'rank': 'star',
  'level': rank['star'][2][0],
  'symbol': rank['star'][2][1],
  'food': food['va'],
  'photo': '(=^o.o^=)__',
}

mouse = {
  'name': 'Fluffy',
  'type': pettype[1],
  'age': 6,
  'weight': 1.5,
  'hungry': True,
  'rank': 'circle',
  'level': rank['circle'][1][0],
  'symbol': rank['circle'][1][1],
  'food': food['vb'],
  'photo': '<:3 )~~~~',
}

fish = {
  'name': 'Nemo',
  'type': pettype[2],
  'age': 7,
  'weight': 2.1,
  'hungry': True,
  'rank': 'heart',
  'level': rank['heart'][0][0],
  'symbol': rank['heart'][0][1],
  'food': food['vc'],
  'photo': '<`)))><',
}

pets = [cat, mouse, fish]

################## CTRLL ##################

def dashboard():
  sr = 0
  print('Please select pypet ...')
  for pet in pets:
    print('(' + str(sr+1) + ') ' + str(pet['name']))
    sr += 1
  pet_no = int(input())
  pet_no = pet_no - 1
  
  return pet_no
  
def create():
  new_rank = []
  new_rank_name = input('New Rank Name : ')
  new_rank_symbol = input('New Rank Symbol : ')
  for level in range(0,4):
    new_rank.append(tuple([level, new_rank_symbol * (level + 1)]))
  else:
    rank.update({new_rank_name: new_rank})

  new_food = {}
  new_food_code = input("New Food Code: ")
  new_food_name = input("New Food Name: ")
  new_food["name"] = new_food_name
  cal = input("New Food Calories: ")
  new_food["calories"] = cal + 'cal'
  amount = input("New Food Amount: ")
  new_food["amount"] = amount + 'kg'
  food.update({new_food_code: new_food})

  new_pet_type = input("New Pet Type Name: ")
  pettype.append(new_pet_type)

  new_pet = {}
  new_pet["name"] = input("New Pet Name : ")
  new_pet["type"] = new_pet_type
  new_pet["age"] = int(input("New Pet Age: "))
  new_pet["level"] = int(input("New Pet Level: "))
  new_pet["weight"] = float(input("New Pet Weight: "))
  new_pet["hungry"] = bool(input("New Pet Hungry: "))
  new_pet["photo"] = input("New Pet Photo: ")
  new_pet["symbol"] = rank[new_rank_name][new_pet["level"]][1]
  new_pet["food"] = food[new_food_code]
  pets.append(new_pet)

def delete(pet_no):
  delete_rank = pets[pet_no]['rank']
  food_name = str(pets[pet_no]['food']['name'])
  delete_food = str('v' + food_name[-1:]).lower()

  del rank[delete_rank]
  del food[delete_food]
  del pets[pet_no]
  
################## VIEW ##################

print('Please select your operation ...')
print('(1) Create Pypet')
print('(2) Update Pypet')
print('(3) Delete Pypet')
select = int(input())

if select is 3:
  pet_no = dashboard()
  delete(pet_no)
elif select is 2:
  pet_no = dashboard()
  delete(pet_no)
  create()
elif select is 1:
  n = int(input("Total Pet : "))
  while n > 0:
    n -= 1
    create()

print(line)
print('=== RANK LEVEL ==='.center(53))
print(line)

for name in rank:
  rank_str = ""
  for rank_item in rank[name]:
    rank_str += str(rank_item) + '|'
  print('| {} |{}'.format(name.ljust(7),rank_str))

print(line)
print('~~~ FOOD DETAIL ~~~'.center(53))
print(line)

for name in food:
  food_str = ""
  for key,value in food[name].items():
    food_str += str(value).ljust(14) + '|'
  print('| {}|{}'.format(name.ljust(5),food_str))

print(line)
print('^^^ CALORIES TYPE ^^^'.center(53))
print(line)

calories_type = set()
for food_code in food:
    calories_type.add(food[food_code]['calories'])
print(str(sorted(calories_type)).center(50))

print(line)
print('>>> RESULT LIST <<<'.center(53))
print(line)

for pet in pets:
  print('Hello ' + pet['name'] + '!')
  print(pet['photo'])
  print('Age: ' + str(pet['age']))
  print('Rank: ' + pet['symbol'])
  print('Weight: ' + str(pet['weight']))
  if pet['hungry'] and pet['level'] < 1:
    print(pet['name'] + ' is hungry!')
  elif pet['hungry'] and pet['level'] > 0:
    print(pet['name'] + ' is hungry!')
    print(pet['name'] + ' need food!')

    # get amount, calories
    ams = pet['food']['amount']
    amount = float(ams[:ams.find('k')])
    cals = pet['food']['calories']
    calories = float(cals[:cals.find('c')])
    ####
    
    level = pet['level']
    pet['weight'] += ((calories * amount ) * level) 

    print('Amount : ' + str(amount) + ' kg')
    print('Calories : ' + str(calories) + ' cal')
    print('Current Weight: ' + str(pet['weight']))
  else:
    print(pet['name'] + ' is not hungry!')
  
  print(line)