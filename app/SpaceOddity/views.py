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


@SpaceOddity.route("/task_sam", methods=['GET', 'POST']) #This is for the pre game SAM
@SpaceOddity.route("/task_sam2", methods=['GET', 'POST']) #This is for the post game SAM
@verify_session_valid
@verify_correct_page
def self_assessment_manikin():
    return render_template("task_sam.html")


@SpaceOddity.route("/log_sam", methods=['POST'])
def log_sam():
    print(request.referrer)

    message = request.form['message']
    if message == "logSAM":
        log_entry = db.LogSAM()
        pid = request.form['pid']
        #if db.session.query(db.LogSAM).filter(db.LogSAM.participantID == pid).first() is not None:
        #    print("There is already a SAM db entry for pid={pid}".format(pid=pid))
        #    return ""
        log_entry.participantID = session['participantID']
        log_entry.participantID = pid
        log_entry.arousal = request.form['arousal']
        log_entry.valence = request.form['valence']
        log_entry.dominance = request.form['dominance']
        log_entry.referrer = request.referrer

        db.session.add(log_entry)
        db.session.commit()
    return ""

