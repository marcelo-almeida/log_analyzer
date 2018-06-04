#!/usr/bin/env python3
# This Python file uses the following encoding: utf-8

import datetime
from news_db import get_most_popular_articles, get_most_popular_authors, \
    get_failure_percentage


# print result in console
def print_question_and_answers():
    print(get_question_and_answers())


# Using the news_db get the answers for all questions
def get_question_and_answers():
    result = "What are the three most popular articles of all time?\n"
    articles = get_most_popular_articles()
    for article in articles:
        result += article + "\n"
    result += "Who are the authors of most popular articles of all time?\n"
    authors = get_most_popular_authors()
    for author in authors:
        result += author + "\n"
    result += "what days the errors resulted more than 1% of requests?\n"
    failures = get_failure_percentage()
    for failure in failures:
        result += failure + "\n"
    return result


# save result in a file
def save_question_and_answers():
    output_file = open('answers' +
                       datetime.datetime.now()
                       .strftime('%Y-%m-%d-%H-%M-%S-%f')
                       + '.txt', 'w')
    output_file.write(get_question_and_answers())
    output_file.close()


if __name__ == '__main__':
    print_question_and_answers()
    # save_question_and_answers()
