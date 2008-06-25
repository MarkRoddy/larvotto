
PYTHON=/usr/bin/python
FIND=/usr/bin/find


install: setup.py
	$(PYTHON) setup.py install

installer:
	$(PYTHON) setup.py -q sdist --format=gztar

clean:
	$(RM) -r *~ dist MANIFEST
	$(FIND) -name  \*.pyc -delete