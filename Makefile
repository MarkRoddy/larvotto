
PYTHON=/usr/bin/python
FIND=/usr/bin/find


all:
	@echo "make install - Install on local system"
	@echo "make installer - Generate a source installer"
	@echo "make test - Run all unit tests"
	@echo "make clean - Get rid of scratch and byte files"

install: setup.py
	$(PYTHON) setup.py install

installer:
	$(PYTHON) setup.py -q sdist --format=gztar

test:
	$(PYTHON) larvotto/tests/bot.py
	$(PYTHON) larvotto/tests/response.py
	$(PYTHON) larvotto/tests/commandline.py
	$(PYTHON) larvotto/tests/convsrc.py

clean:
	$(RM) -r *~ dist MANIFEST
	$(FIND) -name  \*.pyc -delete