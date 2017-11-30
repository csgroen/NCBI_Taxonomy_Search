# NCBI Taxonomy Search
Search locally hosted NCBI Taxonomy using Flask

## How to use it:
1. Download and populate a MySQL database following these instructions:
https://github.com/giffordlabcvr/DIGS-for-EVEs/wiki/NCBI-taxonomy-database

2. Download Flask:
```
pip install Flask
```

3. Download and install this Python module:
https://pypi.python.org/pypi/mysql-connector-python/2.0.4

3. Download this directory

4. Edit the MySQL database configuration in the `query.py`

5. Enter the root of this directory using Terminal

6. Run the app using:
```
FLASK_APP=query.py flask run
```
7. NCBI Taxonomy Search is available at `http://localhost:5000`
