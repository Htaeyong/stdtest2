from flask import Blueprint, render_template
import mysql.connector
import config

siteapply_blueprint = Blueprint('siteapply', __name__)

def get_db_connection():
    conn = mysql.connector.connect(**config.db_config)
    return conn

@siteapply_blueprint.route('/siteapply')
def siteapply():
    return render_template('siteapply.html')