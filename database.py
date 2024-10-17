import sqlite3
import json

with open('mufradat.json', 'r', encoding='utf-8') as file:
    mufradat = json.load(file)

conn = sqlite3.connect('dictionaries.db')
conn.text_factory = str
cursor = conn.cursor()

cursor.execute('CREATE INDEX idx_normalized ON isfahani(normalized_word)')


# for normalized, words in mufradat.items():
#         cursor.execute('''
#                     INSERT INTO isfahani (normalized_word, word, definition)
#                     VALUES (?, ?, ?)
#                     ''', (normalized, words['word'], json.dumps(words['definition']).encode('utf-8').decode('unicode_escape')))






# cursor.execute('''
#                CREATE TABLE IF NOT EXISTS isfahani (
#                     id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     normalized_word TEXT,
#                    word TEXT,
#                    definition TEXT
#                )
#                ''')


conn.commit()
conn.close()

print('done')

