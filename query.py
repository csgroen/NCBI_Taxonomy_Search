from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
import mysql.connector
app = Flask('teste')

@app.route('/')
def hello():
	return render_template('index.html')

@app.route('/search', methods = ['GET', 'POST'])
def search():
	if request.method == 'POST':
		name = request.form['name']
		tax = request.form['tax']
		# name = 'Vibrio'

		if name == "" and tax == "":
			return render_template('index.html')
		if tax == "":
			id_type = 'name'
		else:
			id_type = 'tax_id'

		cols = request.form.getlist("columns")
		# cols = ['tax_id', 'parent_tax_id', 'rank', 'comments']

		cnx = mysql.connector.connect(user='user', password='password', host='localhost', database='NCBI_Taxonomy')
		cursor = cnx.cursor()

		if id_type == 'name':
			name_org = "'%" + name + "%'"
			query = "SELECT tax_id, name_txt FROM ncbi_names WHERE name_txt LIKE " + name_org + ";"
			cursor.execute(query)
			tax = []
			names = []
			for tax_id in cursor:
				tax.append("'" + str(tax_id[0]) + "'")
				names.append("'" + str(tax_id[1]) + "'")

		columns = ", ".join(cols)

		if len(tax) > 1:
			tax_str = ", ".join(tax)
			tax_str = "(" + tax_str + ")"
			query = "SELECT " + columns + " FROM ncbi_nodes WHERE tax_id IN " + tax_str + ";"
		else:
			tax_str = str(tax[0])
			query = "SELECT " + columns + " FROM ncbi_nodes WHERE tax_id = " + tax_str + ";"

		cursor.execute(query)
		f_table = []

		results = list(cursor)

		i = 0
		for result in results:
			f_table.append([])
			for col in result:
				f_table[i].append(col)
			i += 1

		i = 0
		for hit in f_table:
			hit.append(names[i])
			i += 1

		cols.append('names')

		return(render_template("results.html", f_table = f_table, colnames = cols))

	else:
		return render_template('index.html')
