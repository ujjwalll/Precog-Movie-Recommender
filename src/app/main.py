from flask import Flask, render_template, request
import review
import recomend
import csv
import sqlite3
import sys
import datetime
import pytz
import thumbnail

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/review')
def take_review():
    html_data = review.make_final_data()
    return render_template('form.html', html_data=html_data)

@app.route('/handle_data', methods=['POST'])
def handle_data():
    movie_list = []
    con = sqlite3.connect("movies.db")
    cur = con.cursor()
    cur.execute("select userId from ratings order by userId DESC limit 1")
    row = cur.fetchall()
    user_id = int(row[0][0]) + 1
    for i in request.form.keys():
        print(user_id, i, request.form[i], datetime.datetime.now(tz=pytz.utc).timestamp(),)
        cur.execute("INSERT INTO ratings (userId,movieId,rating,timestamp) VALUES (?, ?, ?, ?);", (user_id, i, request.form[i], int(datetime.datetime.now(tz=pytz.utc).timestamp()),))
        con.commit()
        print(i)
    for i in request.form.keys():
        cur.execute("select title from movies WHERE movieId=?", (i, ))
        row = cur.fetchall()
        row = (row[0][0])
        movie_list.append(recomend.my_movie(row))
    con.close()
    movie = movie_list
    full_data = []
    con = sqlite3.connect("movies.db")
    cur = con.cursor()
    for i in movie:
        for j in i:
            try:
                cur.execute("SELECT * FROM movies WHERE title=?", (j, ))
                row = cur.fetchall()
                print(row)
                if len(row) > 0:
                    full_data.append(list(row[0]))
                    full_data[-1].append(thumbnail.get_thumbnail(row[0][0]))
            except Exception as e:
                con.commit()
                con.close()
                return "ERROR CONNECTING DB " + e
    con.commit()
    con.close()
    print(full_data)
    return render_template('index.html', movies=full_data)

@app.route('/populatedb')
def populatedb():
    try:
        con = sqlite3.connect("movies.db")
        cur = con.cursor()
        cur.execute("CREATE TABLE movies (movieId, title, genres);")

        with open('movies.csv','r') as fin: 
            dr = csv.DictReader(fin) 
            to_db = [(i['movieId'], i['title'],i['genres']) for i in dr]

        cur.executemany("INSERT INTO movies (movieId, title, genres) VALUES (?, ?, ?);", to_db)
        con.commit()
        con.close()
    except:
        print("Table movies already exists")
    try:
        con = sqlite3.connect("movies.db")
        cur = con.cursor()
        cur.execute("CREATE TABLE ratings (userId,movieId,rating,timestamp);") 

        with open('ratings.csv','r') as fin: 
            dr = csv.DictReader(fin) 
            to_db = [(i['userId'], i['movieId'],i['rating'], i['timestamp']) for i in dr]

        cur.executemany("INSERT INTO ratings (userId,movieId,rating,timestamp) VALUES (?, ?, ?, ?);", to_db)
        con.commit()
        con.close()
    except Exception as e:
        print(e)
    return render_template("home.html")


if __name__ == '__main__':
    app.run()