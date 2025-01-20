from flask import Flask, request, jsonify, render_template_string
import mysql.connector
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string(open('index.html').read())

@app.route('/add_data', methods=['POST'])
def add_data():
    data = request.json
    name = data['name']
    age = data['age']

    # Connect to MySQL server
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='mydatabase'
    )
    cursor = conn.cursor()
    
    # Insert data into the database
    query = "INSERT INTO users (name, age) VALUES (%s, %s)"
    cursor.execute(query, (name, age))
    conn.commit()
    
    cursor.close()
    conn.close()

    return jsonify({"message": "Data added successfully!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

