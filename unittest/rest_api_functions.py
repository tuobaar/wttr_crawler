import sqlite3


# A standard function for fetching database records
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


# Find average, maximum, minimum temperature and wind speed for a single day/date. e.g. 2022-04-01)
def single_date_temp_wind(db_name, date):
    """
    This function computes and returns the average/maximum/minimum temperature and wind speed for a given date.

    :return: This function returns average/maximum/minimum temperature and wind speed for a given date.
    """

    try:
        # Establish a connection with database db_name

        connection = sqlite3.connect(db_name)

        # Create a cursor object to select records from the database

        my_cursor = connection.cursor()

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

        return avg_temp

    except sqlite3.Error as error:
        print('Failed to display temperature and wind speed', error)


# Find average, maximum, minimum temperature and wind speed for two or more consecutive dates (or a given interval)
# Example: 2 days interval - 2022-04-01 and 2022-04-02
# Example: 3 days interval - 2022-04-01 and 2022-04-03 - This includes 2022-04-02.
def interval_dates_temp_wind(db_name, start_date, end_date):
    """
    This function computes and returns the average/maximum/minimum temperature and wind speed within 2 interval dates.

    :return: This function returns average/maximum/minimum temperature and wind speed within 2 interval dates.
    """

    try:
        # Establish a connection with database db_name

        connection = sqlite3.connect(db_name)

        # Create a cursor object to select records from the database

        my_cursor = connection.cursor()

        params = [start_date, end_date]

        query_avg_temp = f"SELECT avg(Temperature) FROM weather WHERE Date BETWEEN (?) AND (?) "
        query_max_temp = f"SELECT max(Temperature) FROM weather WHERE Date BETWEEN (?) AND (?) "
        query_min_temp = f"SELECT min(Temperature) FROM weather WHERE Date BETWEEN (?) AND (?) "

        query_avg_wind = f"SELECT avg(Wind_Speed) FROM weather WHERE Date BETWEEN (?) AND (?) "
        query_max_wind = f"SELECT max(Wind_Speed) FROM weather WHERE Date BETWEEN (?) AND (?) "
        query_min_wind = f"SELECT min(Wind_Speed) FROM weather WHERE Date BETWEEN (?) AND (?) "

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

        return avg_temp

    except sqlite3.Error as error:
        print('Failed to display temperature and wind speed', error)


# Find average, maximum, minimum temperature and wind speed for one, two or several consecutive or
# non-consecutive different day(s)/date(s). Example: 2022-04-15, 2022-04-01, 2022-04-27, 2022-04-10
def multi_dates_temp_wind(db_name, dates):
    """
    This function computes and returns the average/maximum/minimum temperature and wind speed for one or more dates.

    :return: This function returns average temperature and wind speed for one or more dates.
    """

    try:
        # Establish a connection with database db_name

        connection = sqlite3.connect(db_name)

        # Create a cursor object to select records from the database

        my_cursor = connection.cursor()

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

        return avg_temp

    except sqlite3.Error as error:
        print('Failed to display temperature and wind speed', error)

