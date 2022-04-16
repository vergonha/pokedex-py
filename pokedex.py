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

        hp = todo['stats'][0]['base_stat']
        attack = todo['stats'][1]['base_stat']
        defense = todo['stats'][2]['base_stat']
        special_attack = todo['stats'][3]['base_stat']
        special_defense = todo['stats'][4]['base_stat']
        speed = todo['stats'][5]['base_stat']

        
        

        return type_primary, type_secondary, weight, height, sprite, hp, attack, defense, special_attack, special_defense, speed
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
    type_primary = infos[0].capitalize()
    type_secondary = infos[1].capitalize()
    weight = infos[2]
    height = infos[3]
    sprite = infos[4]

    hp = infos[5]
    attack = infos[6]
    defense = infos[7]
    special_attack = infos[8]
    special_defense = infos[9]
    speed = infos[10]

    if infos != "Pokemon não encontrado!":
        return render_template('pokemon.html', 
            type_primary=type_primary, 
            type_secondary=type_secondary, 
            weight=weight, 
            height=height, 
            pokeName=pokeName, 
            sprite=sprite,
            hp=hp,
            attack=attack,
            defense=defense,
            special_attack=special_attack,
            special_defense=special_defense,
            speed=speed,
            )
    else:
        return redirect(url_for('error'))

@app.route("/error")
def error():
    return render_template('error.html')

if __name__ == '__main__':
    app.run()