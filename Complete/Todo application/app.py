import sqlite3
from datetime import date
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

class DB():
    """
CREATE TABLE "Todo" (
	"sno"	INTEGER,
	"title"	TEXT,
	"desc"	TEXT,
	"date"	TEXT,
	PRIMARY KEY("sno" AUTOINCREMENT)
);
"""

    database = sqlite3.connect('todo.db', check_same_thread=False)
    cursor = database.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Todo(
            "sno"	INTEGER,
            "title"	TEXT,
            "desc"	TEXT,
	        "date"	TEXT,
            PRIMARY KEY("sno" AUTOINCREMENT)
        )''')
    database.commit()
    def insert(title, desc):
        DB.cursor.execute(f"INSERT INTO Todo(title, desc, date) VALUES ('{title}', '{desc}', '{date.today()}')")
        DB.database.commit()
    def show_all():
        return (DB.cursor.execute("SELECT * FROM Todo").fetchall())
    def delete(sno):
        DB.cursor.execute(f"DELETE FROM Todo WHERE sno='{sno}'")
        DB.database.commit()
    def show(sno):
        return DB.cursor.execute(f"SELECT * FROM Todo WHERE sno='{sno}'").fetchall()[0]
    def update(sno, title, desc):
        DB.cursor.execute(f"UPDATE Todo SET title='{title}', desc='{desc}' WHERE sno='{sno}'")
        DB.database.commit()


@app.route('/', methods=['GET', 'POST'])
def index():
    #DB.insert(title="Learn JS", desc="Learn js today")
    if request.method == "POST":
        title = request.form.get('title')
        desc = request.form.get('desc')
        DB.insert(title, desc)
        return render_template('index.html', todo = DB.show_all())
    else:
        return render_template('index.html', todo = DB.show_all())

@app.route('/delete/<int:sno>')
def delete(sno):
    DB.delete(sno)
    return redirect(url_for('index'))

@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    if request.method == "POST":
        title = request.form.get('title')
        desc = request.form.get('desc')
        DB.update(sno, title, desc)
        return redirect(url_for('index'))
    else:
        return render_template('update.html', todo=DB.show(sno))

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run()