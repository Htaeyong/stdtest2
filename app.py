from flask import Flask, render_template, request, jsonify
import mysql.connector
import config


app = Flask(__name__)

def get_db_connection():
    conn = mysql.connector.connect(**config.db_config)
    return conn

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/userlist', methods=['GET','POST'])
def userlist():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM Users')
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('userlist.html', users=users)

@app.route('/useradd', methods=['GET', 'POST'])
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
        cursor.execute('INSERT INTO Users (username, password, department, email, phone, role, memo) VALUES (%s, %s, %s, %s, %s, %s, %s)',
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

@app.route('/useredit/<username>', methods=['GET', 'POST'])
def useredit(username):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == 'POST':
        # 사용자 정보 수정 로직
        # 예: password, email 등을 업데이트
        updated_password = request.form['password']
        updated_email = request.form['email']
        # ... 다른 필드 업데이트

        cursor.execute('UPDATE Users SET password = %s, email = %s WHERE username = %s',
                       (updated_password, updated_email, username))
        conn.commit()
        
        cursor.close()
        conn.close()
        return '''
            <h1>사용자 수정 성공</h1>
            <p>사용자 정보가 수정되었습니다.</p>
            <a href="/"><button>홈으로</button></a>
        '''

    # GET 요청 시, 사용자 정보 로딩
    cursor.execute('SELECT * FROM Users WHERE username = %s', (username,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()

    return render_template('useredit.html', user=user)

@app.route('/siteapply', methods=['GET','POST'])
def siteapply():
    return render_template('siteapply.html')

@app.route('/sitelist', methods=['GET','POST'])
def sitelist():
    return render_template('sitelist.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
