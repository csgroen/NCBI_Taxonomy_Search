# NCBI Taxonomy Search
Search locally hosted NCBI Taxonomy using Flask

## How to use it:
1. Download and populate a MySQL database following these instructions:
https://github.com/giffordlabcvr/DIGS-for-EVEs/wiki/NCBI-taxonomy-database

2. Download Flask:
```
pip install Flask
```

3. Download this Python module:
https://pypi.python.org/pypi/mysql-connector-python/2.0.4  
Extract, then enter the downloaded directory in Terminal, then run:
```
python setup.py install
```

4. Download **this** directory from Github

5. Edit the MySQL database configuration in the `query.py`

6. Enter the root of **NCBI_Taxonomy** directory using Terminal

7. Run the app using:
```
FLASK_APP=query.py flask run
```
8. NCBI Taxonomy Search is available at `http://localhost:5000`
