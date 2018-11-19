
install:
	virtualenv -p python2.7 venv
	venv/bin/python venv/bin/pip install -r requirements.txt

clean:
	rm -rf venv

