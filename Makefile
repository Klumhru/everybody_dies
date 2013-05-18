test:
	../venv/bin/nosetests --with-coverage
	../venv/bin/python test_generate.py 20 20 rooms 15

clean:
	find . -name "*.pyc" |xargs rm
