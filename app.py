from flask import Flask, render_template, request, send_from_directory
import mysql.connector
import config
from userlist import userlist_blueprint
from useradd import useradd_blueprint
from siteapply import siteapply_blueprint
from sitelist import sitelist_blueprint
from productlist import productlist_blueprint
from productapply import productapply_blueprint


app = Flask(__name__)

app.register_blueprint(userlist_blueprint, url_prefix='/users')
app.register_blueprint(useradd_blueprint, url_prefix='/users')
app.register_blueprint(siteapply_blueprint, url_prefix='/sites')
app.register_blueprint(sitelist_blueprint, url_prefix='/sites')
app.register_blueprint(productlist_blueprint, url_prefix='/products')
app.register_blueprint(productapply_blueprint, url_prefix='/products')

def get_db_connection():
    conn = mysql.connector.connect(**config.db_config)
    return conn

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')

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

        cursor.execute('UPDATE users_tab SET password = %s, email = %s WHERE username = %s',
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
    cursor.execute('SELECT * FROM users_tab WHERE username = %s', (username,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()

    return render_template('useredit.html', user=user)

@app.route('/download/<file_id>')
def download_file(file_id):
    # 파일 ID를 기반으로 파일 정보 조회
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM product_files_tab WHERE id = %s', (file_id,))
    file = cursor.fetchone()
    cursor.close()
    conn.close()

    if file:
        return send_from_directory(directory=app.config['UPLOAD_FOLDER'], path=file['file_name'], as_attachment=True)
    else:
        return "File not found", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
