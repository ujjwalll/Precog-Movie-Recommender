#TODO: 1. List of 10 movie
#TODO: 2. Randomy select 4 movie
#TODO: 3. send 4 movie to ui
import random
import sqlite3
movie_list=[]
movie_list_full = ["Toy Story","Jumanji","Grumpier Old Men","Waiting to Exhale","Father of the Bride Part II","Heat","Sabrina","Tom and Huck","Sudden Death","GoldenEye (1995)"]
def make_final_data():
    con = sqlite3.connect("movies.db")
    cur = con.cursor()
    cur.execute("SELECT title, movieId FROM movies ORDER by random() LIMIT 1")
    row = cur.fetchall()
    movie_list = []
    for i in row:
        movie_list.append(i)
    print(movie_list)
    return {"movies": movie_list}

