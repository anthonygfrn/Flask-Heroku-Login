import os
import psycopg2

conn = psycopg2.connect(
        host="localhost",
        database="resto_db",
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD'])

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute('DROP TABLE IF EXISTS restaurants;')
cur.execute('CREATE TABLE restaurants (restaurant_id serial PRIMARY KEY,'
                                 'name varchar (150) NOT NULL,'
                                 'area varchar (50) NOT NULL,'
                                 'rating integer NOT NULL,'
                                 'review text,'
                                 'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                 )

# Insert data into the table

cur.execute('INSERT INTO restaurants (name, area, rating, review)'
            'VALUES (%s, %s, %s, %s)',
            ('Pagi Sore',
             'Cipete',
             5,
             'One of the best padang cuisine , so tdelicious , spacious parking ,staff are responsif and helpful')
            )


cur.execute('INSERT INTO restaurants (name, area, rating, review)'
            'VALUES (%s, %s, %s, %s)',
            ('McDonald\'s Kemang Raya',
             'Leo Tolstoy',
             4,
             'The place is clean. Not really crowded even in the weekend. The food is affordable and has several variations.')
            )

conn.commit()

cur.close()
conn.close()