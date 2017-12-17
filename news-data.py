#python 3

import psycopg2

DBNAME = "news"


#used to connect to database and run queries
def run_queries(query):
	db = psycopg2.connect(database=DBNAME)
	c = db.cursor()
	c.execute(query)
	table = c.fetchall()
	return table
	db.close()

#runs first query and makes output more readable
def top_articles():
	'''

	thi query selects two columns from the view
	first_answer(view README)

	'''
	popular_articles = "select title, num from first_answer"
	top_articles = run_queries(popular_articles)
	print(' ')
	print('Most popular articles')
	print('******************************')
	for i in top_articles:
		print('  ' + i[0] + ' with: -- ' + str(i[1]) + " views")
		print('  ')
	print('******************************')

#runs second query and makes output readable
def best_authors():
	'''

	this query joins the best_author(view README) and
	authors table to show the best viewed 
	authors in order

	'''
	author_list = '''select authors.name, best_author.num
	               from authors, best_author
	               where authors.id = best_author.author;'''
	group = run_queries(author_list)
	print('Most popular authors')
	print('******************************')
	for i in group:
		print('  ' + i[0] + ' with ' + str(i[1]) + ' views' )
		print('  ')
	print('******************************')

#runs last query and makes output readable	
def errors():
	'''

	this query uses the view count_percent
	(view README) and returns the date 
	when the most error messages whhere 
	produced


	'''
	error_query = """select time, percentagefailed
            from count_percent
            where percentagefailed > 1;
            """
	errors_found = run_queries(error_query)
	print('Highest amount of errors')
	print('******************************')
	for day, percentagefailed in errors_found:
		print('  '"""{0:%B %d, %Y}
            -- {1:.2f} % errors""".format(day, percentagefailed))
	print('******************************')


#run functions

top_articles()
best_authors()
errors()