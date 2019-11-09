PYTHON?=python
VENV?=venv

export PYTHONPATH = .:$(VENV)

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

.PHONY: test
