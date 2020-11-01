from app import app
from app.models.player import *
from flask import render_template, request, redirect
from app.models.player_list import *


@app.route("/")
def index():
    return render_template("index.html", title="Home", players=players)

@app.route("/game")
def play():
    return render_template("game.html", title="Game Zone")

@app.route("/game", methods=["POST"])
def game_played():
    players_name1 = request.form["name1"]
    players_choice1 = request.form["choice1"]
    players_name2 = request.form["name2"]
    players_choice2 = request.form["choice2"]

    return f"{players_name1}  Played {players_choice1}  {players_name2} Played {players_choice2}"
    return f""


# @app.route("/add-player", methods=["POST"])
# def add_player():
#     players_name = request.form["name"]
#     players_choice = request.form["choice"]
#     new_player = Player(players_name, players_choice)
#     add_player()
#     return render_template("index.html", title="Home", players=players)