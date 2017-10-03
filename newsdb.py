#!/usr/bin/env python3
import psycopg2

DBNAME = "news"

query1 = '''Select title, count(*) as views
        from articles, log
        where log.path = concat('/article/', articles.slug)
        group by articles.title
        order by views desc limit 3;'''

query2 = '''Select name,
        sum(views) as views
        from articles, pop, authors
        where pop.title = articles.title
        and articles.author = authors.id
        group by authors.name order by views desc;'''

query3 = '''select to_char(date, 'Mon DD,YYYY') as date,
        Error from (select date(log.time) as date,
        round(100.0*sum(case log.status when '200 OK' then 0 else 1 end)/
        count(log.status),2) as Error from log
        group by date order by Error desc) as errdays
        where Error > 1;'''


def get_query_results(query):
    db = psycopg2.connect(database="news")
    c = db.cursor()
    c.execute(query)
    result = c.fetchall()
    db.close()
    return result


def pop_3_articles(query):
    data = get_query_results(query)
    for a, b in data:
        a = str(a)
        b = int(b)
        print('"{}" - {} {}'.format(a, b, 'views'))


def pop_authors(query):
    data = get_query_results(query)
    for a, b in data:
        a = str(a)
        b = int(b)
        print('{} - {} {}'.format(a, b, 'views'))


def errors(query):
    data = get_query_results(query)
    for a, b in data:
        a = str(a)
        b = float(b)
        if b > 1:
            print('{} - {}{} {}'.format(a, b, '%', 'errors'))


if __name__ == "__main__":
    pop_3_articles(query1)
    pop_authors(query2)
    errors(query3)
