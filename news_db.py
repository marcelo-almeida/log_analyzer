#!/usr/bin/env python3
# This Python file uses the following encoding: utf-8

import psycopg2

DBNAME = 'news'

# template for queries of the most popular
most_popular_template = '"{data}" - {count} views"'
# template for queries of the failure percentage
failure_percentage_template = '{date} - {percentage}% errors'


# execute a query passed by parameter in postgreSQL database
def execute_query(query):
    # connect to database
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    return c.fetchall()


# return the three firsts most popular articles in a list
def get_most_popular_articles():
    query = "SELECT articles.title, count(log.path) AS count FROM log " \
            "JOIN articles ON log.path = CONCAT('/article/', articles.slug)" \
            " GROUP BY path, title ORDER BY count DESC LIMIT 3"
    query_results = execute_query(query)
    article_list = []
    # processing result of query
    for result in query_results:
        article = most_popular_template.format(
            data=result[0],
            count=str(result[1])
        )
        article_list.append(article)
    return article_list


# return the authors in order by most popular to less popular in a list
def get_most_popular_authors():
    query = "SELECT authors.name, SUM(items.count) FROM " \
            "(SELECT articles.author AS author_fk, count(log.path) AS count" \
            " FROM log JOIN articles " \
            "ON log.path = CONCAT('/article/', articles.slug) " \
            "GROUP BY path, author) items JOIN authors " \
            "ON items.author_fk = authors.id " \
            "GROUP BY authors.id ORDER BY SUM(items.count) DESC"
    query_results = execute_query(query)
    author_list = []
    # processing result of query
    for result in query_results:
        author = most_popular_template.format(
            data=result[0],
            count=str(result[1])
        )
        author_list.append(author)
    return author_list


# return a list with days that occurs more than 1% of failure in requests
def get_failure_percentage():
    query = "SELECT requests.date AS date_requisitions, " \
            "failures.miss/CAST(requests.total AS FLOAT) * 100 AS percentage" \
            " FROM (SELECT CAST(time AS DATE) AS date, " \
            "count(*) AS total FROM log GROUP BY CAST(time AS DATE) " \
            ")requests JOIN (SELECT CAST(time AS DATE)  AS date, " \
            "count(*) AS miss FROM log WHERE status != '200 OK' " \
            "GROUP BY CAST(time AS DATE))failures " \
            "ON requests.date = failures.date WHERE " \
            "failures.miss/CAST(requests.total AS FLOAT) >= 0.01"
    query_results = execute_query(query)
    failure_list = []
    # processing result of query
    for result in query_results:
        failure = failure_percentage_template.format(
            date=result[0].strftime('%B %d, %Y'),
            percentage="{0:.2f}".format(result[1])
        )
        failure_list.append(failure)
    return failure_list
