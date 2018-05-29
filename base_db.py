#!/usr/bin/env python3
# This Python file uses the following encoding: utf-8

import psycopg2

DBNAME = 'news'


# execute a query passed by parameter in postgreSQL database
def execute_query(query):
    # connect to database
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    return c.fetchall()
