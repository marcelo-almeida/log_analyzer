#!/usr/bin/env python3
# This Python file uses the following encoding: utf-8

import psycopg2

DBNAME = "news"

most_popular_articles = '"{article}" - {count} views"'


def execute_query(query):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    return c.fetchall()


def get_most_popular_articles():
    query = "SELECT articles.title, count(log.path) AS count FROM log " \
            "JOIN articles ON log.path = CONCAT('/article/', articles.slug)" \
            " GROUP BY path, title ORDER BY count DESC LIMIT 3"
    query_results = execute_query(query)
    article_list = []
    for result in query_results:
        article = most_popular_articles.format(
            article=result[0],
            count=str(result[1])
        )
        article_list.append(article)
    return article_list
