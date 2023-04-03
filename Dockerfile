FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN python3 -m venv venv; \
	. venv/bin/activate; \
	pip install --no-cache-dir -r requirements.txt

ADD . .

CMD . venv/bin/activate; pytest test_pdf.py -s