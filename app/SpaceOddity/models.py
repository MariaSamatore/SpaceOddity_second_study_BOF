def create(db):
    class GameLog(db.Model):
        __tablename__ = "game_log"
        gameLogID = db.Column(db.Integer, primary_key=True, autoincrement=True)
        participantID = db.Column(db.Integer, db.ForeignKey('participant.participantID'))
        input = db.Column(db.String)
        submittedOn = db.Column(db.DateTime, nullable=False, default=db.func.now())

    class SpaceOddityDeath(db.Model):
        __tablename__ = "deathLog"
        condition = db.Column(db.String)
        gameLogID = db.Column(db.Integer, primary_key=True, autoincrement=True)
        participantID = db.Column(db.Integer, db.ForeignKey('participant.participantID'))
        timestamp = db.Column(db.String)
        levelID = db.Column(db.String)

    class LogSAM(db.Model):
        __tablename__ = "log_SAM"

        logSAMID = db.Column(db.Integer, primary_key=True, autoincrement=True)
        participantID = db.Column(db.Integer, db.ForeignKey('participant.participantID'))
        arousal = db.Column(db.Integer, nullable=False, default=0)
        valence = db.Column(db.Integer, nullable=False, default=0)
        dominance = db.Column(db.Integer, nullable=False, default=0)
        referrer = db.Column(db.String)


    return GameLog, SpaceOddityDeath, LogSAM
