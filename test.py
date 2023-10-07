CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}
cities = ['chicago', 'new york', 'washington']
ways_to_filter = ['month', 'day', 'both', 'none']
months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
days = ['all','sunday', 'monday', 'tuesday',
        'wednesday', 'thursday', 'friday', 'saturday']

while True:
  city = input(
            "Would you like to see data for Chicago, New York or Washington?\n")
  if city.lower() in cities:
    break
  print('Please enter a valid city!')
while True:
  user_input = input(
            'Would you like to filter the data by month, day, both or not at all? Type "none" for no time filter.')
  if user_input.lower() in ways_to_filter:
    break
  print('Please enter a valid input!')
    
if user_input.lower() == 'both':
  while True:
    month = input(
                'Which month? January, February, March, April, May, June.\n\nYou can also see data for all months should you decide to.\n\nPlease type "all" if you would like to view data for all months')
    if month.lower() in months:
      break
    print('Please enter a valid month!')
  while True:
    day = input(
                    'Which day? (e.g Sunday,Monday e.t.c).\n \nYou can also view data for all days of the week.\n\nPlease type "all" if you would like to view data by all days.')
    
    if day in days:
      break
    print('Please enter a valid day!')
elif user_input.lower() == 'month':
  while True:
    month = input(
        'Which month? January, February, March, April, May, June.\n\nYou can also see data for all months should you decide to.\n\nPlease type "all" if you would like to view data for all months')
    if month.lower() in months:
      break
    print('Please enter a valid month!')
else:
  while True:
    day = input(
                    'Which day? (e.g Sunday, Monday e.t.c).\n\nYou can also view data for all days of the week.\n\nPlease type "all" if you would like to view data by all days.')
    
    if day in days:
      break
    print('Please enter a valid day!')