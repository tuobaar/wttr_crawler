import sqlite3

from flask import request, render_template
from rest_api import app


# Find average, maximum, minimum temperature and wind speed for one, two or several consecutive or
# non-consecutive different day(s)/date(s). Example: 2022-04-15, 2022-04-01, 2022-04-27, 2022-04-10
@app.route('/api/v1/resources/multi_dates_temp_wind', methods=['GET', 'POST'])
def multi_dates_temp_wind():
    """
    This function computes and returns the average/maximum/minimum temperature and wind speed for one or more dates.

    :return: This function returns average temperature and wind speed for one or more dates.
    """

    db_name = "./weather_archive.db"

    try:
        # Establish a connection with database db_name

        connection = sqlite3.connect(db_name)

        # Create a cursor object to select records from the database

        my_cursor = connection.cursor()

        # Fetch the dates submitted by the user and assign them to the respective variable.
        dates = request.args.get('dates', 'NO_DATE')

        if request.method == 'POST':
            dates = request.form.get('dates')

        items = [dates]
        params = items[0].split(',')

        factor = len(params)

        query_avg_temp = f"SELECT avg(Temperature) FROM weather WHERE Date in ({','.join(['?'] * factor)})"
        query_max_temp = f"SELECT max(Temperature) FROM weather WHERE Date in ({','.join(['?'] * factor)})"
        query_min_temp = f"SELECT min(Temperature) FROM weather WHERE Date in ({','.join(['?'] * factor)})"

        query_avg_wind = f"SELECT avg(Wind_Speed) FROM weather WHERE Date in ({','.join(['?'] * factor)})"
        query_max_wind = f"SELECT max(Wind_Speed) FROM weather WHERE Date in ({','.join(['?'] * factor)})"
        query_min_wind = f"SELECT min(Wind_Speed) FROM weather WHERE Date in ({','.join(['?'] * factor)})"

        avg_temp = my_cursor.execute(query_avg_temp, params).fetchall()
        max_temp = my_cursor.execute(query_max_temp, params).fetchall()
        min_temp = my_cursor.execute(query_min_temp, params).fetchall()

        avg_wind_speed = my_cursor.execute(query_avg_wind, params).fetchall()
        max_wind_speed = my_cursor.execute(query_max_wind, params).fetchall()
        min_wind_speed = my_cursor.execute(query_min_wind, params).fetchall()

        avg_temp, max_temp, min_temp = avg_temp[0][0], max_temp[0][0], min_temp[0][0]

        avg_wind_speed = avg_wind_speed[0][0]
        max_wind_speed = max_wind_speed[0][0]
        min_wind_speed = min_wind_speed[0][0]

        elements = [avg_temp, max_temp, min_temp, avg_wind_speed, max_wind_speed, min_wind_speed, dates]

        # Render the elements to the specified html template.
        return render_template("multi.html", elements=elements)

    except sqlite3.Error as error:
        print('Failed to display temperature and wind speed', error)

