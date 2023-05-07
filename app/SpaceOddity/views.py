import datetime
from flask import Blueprint, render_template
from BOFS.util import *
from BOFS.globals import db
from BOFS.admin.util import verify_admin

# The name of this variable must match the folder's name.
SpaceOddity = Blueprint('SpaceOddity', __name__,
                          static_url_path='/SpaceOddity',
                          template_folder='templates',
                          static_folder='static')


def handle_game_post():
    log = db.GameLog()
    log.participantID = session['participantID']
    log.input = request.form['input']

    db.session.add(log)
    db.session.commit()
    return ""


@SpaceOddity.route("/game_embed", methods=['POST', 'GET'])
@verify_correct_page
@verify_session_valid
def game_embed():
    if request.method == 'POST':
        return handle_game_post()
    return render_template("game_embed.html")


@SpaceOddity.route("/game_fullscreen", methods=['POST', 'GET'])
@verify_correct_page
@verify_session_valid
def game_fullscreen():
    if request.method == 'POST':
        return handle_game_post()
    return render_template("game_fullscreen.html")


@SpaceOddity.route("/game_custom", methods=['POST', 'GET'])
@verify_correct_page
@verify_session_valid
def game_custom():
    if request.method == 'POST':
        return handle_game_post()
    return render_template("game_custom.html")


@SpaceOddity.route("/index_NSE", methods=['POST', 'GET'])
@verify_correct_page
@verify_session_valid
def game_NSE():
    if request.method == 'POST':
        return handle_game_post()
    return render_template("index_NSE.html")


@SpaceOddity.route("/index_SE", methods=['POST', 'GET'])
@verify_correct_page
@verify_session_valid
def game_SE():
    if request.method == 'POST':
        return handle_game_post()
    return render_template("index_SE.html")


@SpaceOddity.route("/fetch_condition")
@verify_session_valid
def fetch_condition():
    return str(session['condition'])

#When the game ends, it redirects the user to the next page
@SpaceOddity.route("/end_game")
@verify_session_valid
def end_game():
    db.session.commit()
    return redirect("redirect_next_page")

#Logging functions
@SpaceOddity.route("/SpaceOddity", methods=['POST'])
@verify_session_valid
def game_data():
    if request.method == 'POST':
        log = db.SpaceOddityDeath()
        log.timestamp = request.form['timestamp']
        try:
            log.participantID = session['participantID']
        except:
            print("participantID exception, setting to -999")
            log.participantID = "-999"
        log.levelID = request.form['levelID']
        log.condition = session['condition']
        db.session.add(log)
        db.session.commit()
    return ""


