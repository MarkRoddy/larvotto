
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
	$(PYTHON) setup.py -q sdist --format=zip

test:
	$(PYTHON) larvotto/tests/test_bot.py
	$(PYTHON) larvotto/tests/test_response.py
	$(PYTHON) larvotto/tests/test_commandline.py
	$(PYTHON) larvotto/tests/test_convsrc.py

clean:
	$(RM) -r  dist MANIFEST
	$(FIND) \( -name  \*.pyc -o -name \*~ \) -delete

