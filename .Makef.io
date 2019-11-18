PYTHON?=python
VENV?=venv

export PYTHONPATH = .:$(VENV)

TRAVIS_SKEL?=travisci/.travis.skel.yml
TRAVIS_YML=.travis.yml
MAKEFILE?=Makefile

test: compile	
	mkdir -p $(VENV)
	$(PYTHON) -m pytest $(TEST)

integ: compile	
	$(PYTHON) -m pytest -o pytest.integ.ini $(TEST)

compile: $(VENV)
$(VENV): requirements.txt requirements/*.txt
	# download pip
	$(PYTHON) -m pip install -q -t $(VENV) -r requirements.txt
	touch $(VENV)
clean:	
	find . -name "*.pyc" -delete
	rm -rf `find . -name __pycache__`
	rm -rf $(VENV)

travisci: .travis.yml
.travis.yml: $(MAKEFILE)
	@cat $(TRAVIS_SKEL) > $(TRAVIS_YML)
	@echo "script:" >> $(TRAVIS_YML)
	@grep "[a-z]*:.*#cicd" Makefile  | cut -d: -f1 | sed -e "s/^/- make /" >> $(TRAVIS_YML)
	echo "updated $(TRAVIS_YML)"

.PHONY: test
