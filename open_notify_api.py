import requests


# people = requests.get('http://api.open-notify.org/astros.json')
# # print(people.text)

# people_json  = people.json()
# # print(people_json)

# #To print the number of people in space
# print("Number of people in space:",people_json['number'])
# #To print the names of people in space using a for loop
# for p in people_json['people']:
#     print(p['name'])

response = requests.get("https://wordsapiv1.p.rapidapi.com/words/?random=true",
  headers={
    "X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com",
    "X-RapidAPI-Key": "782ba449e5mshd7b6cca45ba21edp100f31jsna8f64ebe64a9"
  }
)


word = response.json()['word']
print(word)

