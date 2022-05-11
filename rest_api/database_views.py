import sqlite3

from flask import request, render_template
from rest_api import app


# A standard function for fetching database records
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


# Display a percentage of the database. Some or all records in the database.
@app.route('/api/v1/resources/view_database', methods=['GET', 'POST'])
def view_database():
    """
    This function displays a portion of the database.
    """

    db_name = "./weather_archive.db"

    try:
        # Establish a connection with database db_name
        connection = sqlite3.connect(db_name)
        connection.row_factory = dict_factory
        my_cursor = connection.cursor()

        # Fetch the value submitted by the user and assign it to a variable.
        data_limit = request.args.get('data_limit', 5)

        if request.method == 'POST':
            data_limit = request.form.get('data_limit')

        data_limit = float(data_limit)
        data_limit = round(data_limit)

        # Ensure the value submitted by the user is not greater than 100 percent.
        if data_limit > 100:
            data_limit = 100

        if data_limit < -100:
            data_limit = -100

        # Make query, read and display database
        view = "SELECT * FROM weather;"
        rows = my_cursor.execute(view).fetchall()

        total_records = len(rows)

        slice_number = round(data_limit/100 * total_records)

        records = []

        if slice_number < 0:
            for row in rows[:-slice_number]:
                records.append(row)

        if slice_number > 0:
            for row in rows[-slice_number:]:
                records.append(row)
            records = reversed(records)

        slice_number, data_limit = abs(slice_number), abs(data_limit)

        # Render the elements to the specified html template.
        return render_template("view.html", elements=[records, data_limit, total_records, slice_number])

    except sqlite3.Error as error:
        print('Failed to display sqlite database/table.', error)
