#!/usr/bin/env python3
# This Python file uses the following encoding: utf-8

from news_db import get_most_popular_articles, get_most_popular_authors, \
    get_failure_percentage


# Using the news_db prints the answers for all questions
def print_question_and_answers():
    print("What are the three most popular articles of all time?")
    articles = get_most_popular_articles()
    for article in articles:
        print(article)
    print("Who are the authors of most popular articles of all time?")
    authors = get_most_popular_authors()
    for author in authors:
        print(author)
    print("what days the errors resulted more than 1% of requests?")
    failures = get_failure_percentage()
    for failure in failures:
        print(failure)


print_question_and_answers()
