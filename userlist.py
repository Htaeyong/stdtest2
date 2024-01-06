from flask import Blueprint, render_template
import mysql.connector
import config

userlist_blueprint = Blueprint('userlist', __name__)

def get_db_connection():
    conn = mysql.connector.connect(**config.db_config)
    return conn

@userlist_blueprint.route('/userlist')
def user_list():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM users_tab')
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('userlist.html')

