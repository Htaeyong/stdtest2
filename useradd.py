from flask import Blueprint, render_template, request
import mysql.connector
import config

useradd_blueprint = Blueprint('useradd', __name__)

def get_db_connection():
    conn = mysql.connector.connect(**config.db_config)
    return conn

@useradd_blueprint.route('/useradd')
def useradd():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        department = request.form.get('department', '')
        email = request.form.get('email', '')
        phone = request.form.get('phone', '')
        role = request.form['role']
        memo = request.form.get('memo', '')

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users_tab (username, password, department, email, phone, role, memo) VALUES (%s, %s, %s, %s, %s, %s, %s)',
                       (username, password, department, email, phone, role, memo))
        conn.commit()
        cursor.close()
        conn.close()
        return '''
            <h1>사용자 등록 성공</h1>
            <p>새로운 사용자가 등록되었습니다.</p>
            <a href="/"><button>홈으로</button></a>
        '''
    return render_template('useradd.html')