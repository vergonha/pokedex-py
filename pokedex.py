from flask import Flask, redirect, render_template, url_for, request
import requests
import json
import findpokebyname

app = Flask(__name__, template_folder='templates', static_folder='static')



@app.route("/")
def index():
    return render_template('index.html')


@app.route(f"/pokemon", methods=["POST", "GET"])
def pokemon():
    pokeName = request.form.get('pokemon')
    pokeName = pokeName.capitalize()
    try:
        pokemon = findpokebyname.findPokeByName(pokeName)
        nomePokemon = pokemon.nomePokemon
        type_primary = pokemon.type_primary
        type_secondary = pokemon.type_secondary
        weight = pokemon.weight
        height = pokemon.height
        sprite = pokemon.sprite
        hp = pokemon.hp
        attack = pokemon.attack
        defense = pokemon.defense
        special_attack = pokemon.special_attack
        special_defense = pokemon.special_defense
        speed = pokemon.speed
    except:
        pokemon = None


    if pokemon == None:
        return redirect(url_for('error'))
    else:
        return render_template('pokemon.html', 
            nomePokemon=nomePokemon.capitalize(),
            type_primary=type_primary.capitalize(), 
            type_secondary=type_secondary.capitalize(), 
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

@app.route("/error")
def error():
    return render_template('error.html')

if __name__ == '__main__':
    app.run()