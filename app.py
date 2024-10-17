from flask import Flask, render_template, request, jsonify
import sqlite3
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dictionaries.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)


def get_db_connection():
    conn = sqlite3.connect('/Users/muhammedozolcar/Desktop/Codespace/dictionary/dictionaries.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q', '').strip()
    if query:
        conn = get_db_connection()
        cursor = conn.cursor()
        # Use `normalized_word` for the search query
        cursor.execute("SELECT word, definition FROM isfahani WHERE normalized_word LIKE ? LIMIT 5", ('%' + query + '%',))
        results = cursor.fetchall()
        conn.close()
        # Prepare results to include both `word` and `definition`
        return jsonify([{'word': row['word'], 'definition': row['definition']} for row in results])
    return jsonify([])

if __name__ == '__main__':
    app.run(debug=True)

import sqlite3
