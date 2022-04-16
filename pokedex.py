from flask import Flask, redirect, render_template, url_for, request
import requests
import json
import os

app = Flask(__name__, template_folder='templates', static_folder='static')

def findPokeByName(pokeName):
    try:
        pokemonName = pokeName.lower()
        request = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemonName}")
        todo = json.loads(request.content)

        spriteTodo = todo['sprites']
        sprite = spriteTodo["front_default"]
        type_primary = todo['types'][0]['type']['name']
        try:
            type_secondary = todo['types'][1]['type']['name']
        except:
            type_secondary = "Nenhum"
        weight = todo['weight']/10
        height = todo['height']/10
        

        return type_primary, type_secondary, weight, height, sprite
    except:
        return "Pokemon não encontrado!"

@app.route("/")
def index():
    return render_template('index.html')


@app.route(f"/pokemon", methods=["POST", "GET"])
def pokemon():
    pokeName = request.form.get('pokemon')
    pokeName = pokeName.capitalize()
    infos = findPokeByName(pokeName)
    type_primary = infos[0]
    type_secondary = infos[1]
    weight = infos[2]
    height = infos[3]
    sprite = infos[4]

    if infos != "Pokemon não encontrado!":
        return render_template('pokemon.html', 
            type_primary=type_primary, 
            type_secondary=type_secondary, 
            weight=weight, 
            height=height, 
            pokeName=pokeName, 
            sprite=sprite)
    else:
        return "Pokemon não encontrado!"

if __name__ == '__main__':
    app.run()