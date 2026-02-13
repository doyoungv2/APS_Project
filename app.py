# app.py (이 코드로 덮어쓰세요)
from flask import Flask, render_template, request
import csv
import os
from datetime import datetime

os.chdir(os.path.dirname(os.path.abspath(__file__)))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        model = request.form.get('model', 'Not Selected') # 모델 선택 추가
        size = request.form['size']
        
        csv_file = 'orders.csv'
        file_exists = os.path.isfile(csv_file)
        
        try:
            with open(csv_file, 'a', newline='', encoding='utf-8-sig') as f:
                writer = csv.writer(f)
                if not file_exists:
                    writer.writerow(['주문일시', '이름', '전화번호', '이메일', '모델', '사이즈'])
                writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), name, phone, email, model, size])
        except Exception as e:
            print(f"에러: {e}")
            
        # [핵심 수정] _anchor='preorder'를 추가하여 폼 위치로 돌아오게 함
        return render_template('index.html', success=True, _anchor='preorder')

if __name__ == '__main__':
    app.run(debug=True, port=5000)