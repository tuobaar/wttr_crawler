import sqlite3

from flask import request, render_template
from rest_api import app


# Find average, maximum, minimum temperature and wind speed for a single day/date. e.g. 2022-04-01)
@app.route('/api/v1/resources/single_date_temp_wind', methods=['GET', 'POST'])
def single_date_temp_wind():
    """
    This function computes and returns the average/maximum/minimum temperature and wind speed for a given date.

    :return: This function returns average/maximum/minimum temperature and wind speed for a given date.
    """

    db_name = "./weather_archive.db"

    try:
        # Establish a connection with database db_name

        connection = sqlite3.connect(db_name)

        # Create a cursor object to select records from the database

        my_cursor = connection.cursor()

        # Fetch the date submitted by the user, assign it to the respective variable.

        date = request.args.get('date', None)

        if request.method == 'POST':
            date = request.form.get('date')

        query_avg_temp = "SELECT avg(Temperature) FROM weather WHERE Date = ?"
        query_max_temp = "SELECT max(Temperature) FROM weather WHERE Date = ?"
        query_min_temp = "SELECT min(Temperature) FROM weather WHERE Date = ?"
        query_avg_wind = "SELECT avg(Wind_Speed) FROM weather WHERE Date = ?"
        query_max_wind = "SELECT max(Wind_Speed) FROM weather WHERE Date = ?"
        query_min_wind = "SELECT min(Wind_Speed) FROM weather WHERE Date = ?"

        avg_temp = my_cursor.execute(query_avg_temp, (date,)).fetchall()
        max_temp = my_cursor.execute(query_max_temp, (date,)).fetchall()
        min_temp = my_cursor.execute(query_min_temp, (date,)).fetchall()

        avg_wind_speed = my_cursor.execute(query_avg_wind, (date,)).fetchall()
        max_wind_speed = my_cursor.execute(query_max_wind, (date,)).fetchall()
        min_wind_speed = my_cursor.execute(query_min_wind, (date,)).fetchall()

        avg_temp, max_temp, min_temp = avg_temp[0][0], max_temp[0][0], min_temp[0][0]

        avg_wind_speed = avg_wind_speed[0][0]
        max_wind_speed = max_wind_speed[0][0]
        min_wind_speed = min_wind_speed[0][0]

        elements = [avg_temp, max_temp, min_temp, avg_wind_speed, max_wind_speed, min_wind_speed, date]

        # Render the elements to the specified html template.
        return render_template("single.html", elements=elements)

    except sqlite3.Error as error:
        print('Failed to display temperature and wind speed', error)

