from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

def search_books(query):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM books WHERE title LIKE ? OR author LIKE ?", (f'%{query}%', f'%{query}%'))
    results = cur.fetchall()
    conn.close()
    return results

@app.route('/', methods=['GET'])
def index():
    q = request.args.get('q', '')
    results = search_books(q) if q else []
    return render_template('index.html', results=results, query=q)

if __name__ == '__main__':
    app.run()

