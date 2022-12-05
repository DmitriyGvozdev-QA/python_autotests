import requests

token = '4dfcf5c00263ed431a70673c951d778d'
response = requests.post('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token' : token}, json={
    "name": "Daimon",
    "photo": "https://static.wikia.nocookie.net/pokemon/images/2/21/001Bulbasaur.png"
})
print(response.text)


response_put = requests.put('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token' : token}, json={
    "pokemon_id": 1376 ,
    "name": "Daimond",
    "photo": "https://static.wikia.nocookie.net/pokemon/images/8/88/711Gourgeist.png/revision/latest?cb=20181021103054&path-prefix=ru"
})
print(response_put.text)


response_post = requests.post('https://pokemonbattle.me:5000/trainers/addPokebol', headers={'trainer_token' : token}, json={
  "pokemon_id": "1376"
})
print(response_post.text)

response_put = requests.put('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token' : token}, json={
    "pokemon_id": 1376 ,
    "name": "Daimond",
    "photo": "https://static.wikia.nocookie.net/pokemon/images/8/88/711Gourgeist.png/revision/latest?cb=20181021103054&path-prefix=ru"
})
print(response_put.text)


