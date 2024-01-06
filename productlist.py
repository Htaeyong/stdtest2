from flask import Blueprint, render_template
import mysql.connector
import config

productlist_blueprint = Blueprint('productlist', __name__)

def get_db_connection():
    conn = mysql.connector.connect(**config.db_config)
    return conn

@productlist_blueprint.route('/productlist')
def productlist():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # 제품 정보와 연관된 파일 정보 가져오기
    cursor.execute('SELECT p.*, pf.id as file_id, pf.file_name, pf.file_path FROM products_tab p LEFT JOIN product_files_tab pf ON p.id = pf.product_id')
    products_temp = cursor.fetchall()
    
    # 제품별로 파일 정보 그룹화
    products = {}
    for item in products_temp:
        if item['id'] not in products:
            products[item['id']] = item
            products[item['id']]['files'] = []
        if item['file_id']:
            products[item['id']]['files'].append({
                'file_id': item['file_id'],
                'file_name': item['file_name'],
                'file_path': item['file_path']
            })

    cursor.close()
    conn.close()
    return render_template('productlist.html', products=products.values())