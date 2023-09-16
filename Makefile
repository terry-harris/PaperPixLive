venv:
	if [ ! -d "$(DIR1)" ]; then \
		python3 -m venv .venv; \
	fi

freeze:
	.venv/bin/pip freeze > requirements.txt

requirements:
	.venv/bin/pip install -r requirements.txt

run:
	.venv/bin/python gui.py
