from flask import Blueprint, render_template, request
import mysql.connector
import config

sitelist_blueprint = Blueprint('sitelist', __name__)

def get_db_connection():
    conn = mysql.connector.connect(**config.db_config)
    return conn

@sitelist_blueprint.route('/sitelist')
def sitelist():
    return render_template('sitelist.html')