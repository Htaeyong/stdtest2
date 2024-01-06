from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.utils import secure_filename
import os
import mysql.connector
import config

productapply_blueprint = Blueprint('productapply', __name__)

def get_db_connection():
    conn = mysql.connector.connect(**config.db_config)
    return conn

@productapply_blueprint.route('/productapply')
def productapply():
    if request.method == 'POST':
        product_name = request.form['product_name']
        manufacturer = request.form['manufacturer']
        eos = request.form['eos']
        eol = request.form['eol']
        product_category = request.form['product_category']
        product_specifications = request.form['product_specifications']

        # 데이터베이스 연결 및 커서 생성
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # 제품 정보 삽입
        try:
            cursor.execute('''
                INSERT INTO products_tab (product_name, manufacturer, eos, eol, product_category, product_specifications) 
                VALUES (%s, %s, %s, %s, %s, %s)
            ''', (product_name, manufacturer, eos, eol, product_category, product_specifications))
            conn.commit()
            
            # 삽입된 제품의 ID를 가져온다
            product_id = cursor.lastrowid

            # 파일 업로드 처리
            files = request.files.getlist('certificate_files')
            for file in files:
                if file and file.filename:
                    filename = secure_filename(file.filename)
                    file_path = os.path.join(config['UPLOAD_FOLDER'], filename)
                    file.save(file_path)

                    # 파일 정보를 product_files_tab 테이블에 삽입
                    cursor.execute('''
                        INSERT INTO product_files_tab (product_id, file_path, file_name) 
                        VALUES (%s, %s, %s)
                    ''', (product_id, file_path, filename))
                    conn.commit()

        except mysql.connector.Error as err:
            conn.rollback()  # 에러 발생 시 롤백
            flash(f'An error occurred: {err}', 'danger')  # 사용자에게 오류 메시지 표시
        finally:
            cursor.close()
            conn.close()

        return redirect(url_for('productlist'))  # 제품 목록 페이지로 리디렉션
    return render_template('productapply.html')  # 제품 등록 페이지 렌더링