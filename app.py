from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Database connection function
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Aman@950898",   # apna MySQL password daalo
        database="mydb"
    )

# Route to display the form
@app.route('/')
def index():
    return render_template('form.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    try:
        # Get data from form
        name = request.form['name']
        fathername = request.form['fathername']
        email = request.form['email']
        phone = request.form['phone']

        # Database connection
        db = get_db_connection()
        cursor = db.cursor()

        # Insert data into MySQL
        sql = "INSERT INTO users (name, fathername, email, phone) VALUES (%s, %s, %s, %s)"
        values = (name, fathername, email, phone)
        cursor.execute(sql, values)
        db.commit()

        cursor.close()
        db.close()

        return "✅ Data inserted successfully!"

    except Exception as e:
        return f"❌ Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
