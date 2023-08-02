from flask import Flask, session, request, redirect, url_for

import os

from .extensions import db, migrate

from .functions import (
    get_units_from_beer, 
    get_units_from_spirits, 
    get_units_from_wines, 
    get_grams_of_alcohol, 
    get_grams_of_alcohol, 
    get_blood_alcohol
)


def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY=os.environ.get('SECRET_KEY'),
        SQLALCHEMY_DATABASE_URI=os.environ.get('DB_URI'),
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )

    db.init_app(app)
    migrate.init_app(app, db)


    @app.route('/start-drinking/', methods=['GET', 'POST'])
    def index():
        session.clear()
        session['bac'] = 0
        session['weight'] = float(request.form.get('weight'))
        session['gender'] = request.form.get('gender')

        print(session['weight'])
        print(session['gender'])
        print(session['bac'])

        return redirect(url_for('view_bac'))
    

    @app.route('/add-drink/', methods=['POST'])
    def add_drink():
        type_of_drink = request.args.get('type')

        if type_of_drink == 'beer':
            units = get_units_from_beer()
        elif type_of_drink =='spirits':
            units = get_units_from_spirits()
        elif type_of_drink == 'wines':
            units = get_units_from_wines()

        print(units)
        
        grams_of_alcohol = get_grams_of_alcohol(units)
        print(grams_of_alcohol)

        blood_alcohol = get_blood_alcohol(
            gender=session['gender'],
            weight=float(session['weight']),
            grams_of_alcohol=grams_of_alcohol
        )

        print(blood_alcohol)
        print([session['gender']])
        print([session['weight']])

        session['bac'] += blood_alcohol
    
        return redirect(url_for('view_bac'))


    @app.route('/view-bac/', methods=['GET'])
    def view_bac():
        bac = session['bac']
        if bac > 0.08:
            return f"You are intoxicated. Your blood alcohol is {bac:.5f}"
        else:
            return f"Your blood alcohol is {bac:.5f}. You are not intoxicated."
        

    return app