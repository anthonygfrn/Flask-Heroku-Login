import os
import psycopg2
from flask import Flask, render_template, request, url_for, redirect
from app import app

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='restaurant',
                            user=os.environ['DB_USERNAME'],
                            password=os.environ['DB_PASSWORD'])
    return conn

@app.route('/')
def index():
   return render_template("index.html")

@app.route('/restaurant/')
def restaurant():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM restaurants;')
    restaurants = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('restaurant.html', restaurants=restaurants)

@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        restaurant_name = request.form['restaurant_name']
        area = request.form['area']
        category = request.form['category']
        restaurant_visited = int(request.form['restaurant_visited'])
        average_rating = request.form['average_rating']
        ratings_count = int(request.form['ratings_count'])

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO restaurants (restaurant_name, area, category, restaurant_visited, average_rating, ratings_count)'
                    'VALUES (%s, %s, %s, %s, %s, %s)',
                    (restaurant_name, area, category, restaurant_visited, average_rating, ratings_count))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))
        
    return render_template('create.html')