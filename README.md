1. To run the test make sure you have installed requirements.txt
2. Run the command in the root directory `pytest test_pdf.py` this will run the pytest in standard mode
3. If you want see the `print` run `pytest -rP` or `pytest test_pdf.py -s`

**Running in Docker** 
1. Build the image with `docker build -t pytest:1.0 .`
2. Run the command in the root directory `docker run -it --rm pytest:1.0`