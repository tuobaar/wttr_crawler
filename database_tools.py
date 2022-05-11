import sqlite3


def create_database():
    """
    This function creates a new database with table 'weather_archive' if it does not exist in the program directory.

    :return: This function returns no value.
    """
    db_name = 'weather_archive.db'

    # Connect to the given database db_name if it exists else create an instance with the same name.

    try:
        # Establish a connection with database db_name

        connection = sqlite3.connect(db_name)

        # Create a cursor object to create table and columns

        my_cursor = connection.cursor()

        create_table = """CREATE TABLE IF NOT EXISTS weather (
                                            Temperature INT, 
                                            Wind_Speed INT, 
                                            Date DATE,
                                            Time TIME                                             
                                            );"""

        my_cursor.execute(create_table)
        my_cursor.close()
        connection.close()

    except sqlite3.Error as error:
        print(f'Error connecting to the database {db_name}', error)

    finally:
        print("\nPreparing to crawl 'https://wttr.in/' ")
        print(f'\nConnection to the database {db_name} successful.\n')


def insert_update_database(temperature, wind_speed, crawl_date, crawl_time):
    """
    This function inserts/updates crawled information to the database db_name.
    It takes four parameters: temperature, wind_speed, crawl_date and crawl_time.

    Params: temperature - stores the current temperature information of crawled weather data.
            wind_speed - stores the wind speed information of crawled weather data.
            crawl_date - stores the date of crawled weather data.
            crawl_time - stores the time of crawled weather data.

    Returns: This function returns no value.

    """

    db_name = 'weather_archive.db'

    try:
        # Establish a connection with database db_name

        connection = sqlite3.connect(db_name)

        # Create a cursor object to insert data into the database

        my_cursor = connection.cursor()

        sqlite_insert_weather_data = """INSERT OR IGNORE INTO weather (Temperature, Wind_Speed,
        Date, Time) VALUES (?, ?, ?, ?)"""

        my_cursor.execute(sqlite_insert_weather_data, (temperature, wind_speed, crawl_date, crawl_time))
        connection.commit()
        my_cursor.close()
        connection.close()

    except sqlite3.Error as error:
        print('Failed to insert/update sqlite table', error)


def display_latest_entries():
    """
    This function displays the first 5 latest weather-entries in the database.

    :return: This function returns no value.
    """

    db_name = 'weather_archive.db'

    try:
        # Establish a connection with database db_name

        connection = sqlite3.connect(db_name)

        # Create a cursor object to select records from the database

        my_cursor = connection.cursor()

        # Printing the last 5 rows from 'weather_archive.db' database
        rows = my_cursor.execute("SELECT * FROM weather;").fetchall()
        print("\n\nThe latest weather-entries are: \n")
        for row in rows[-5:]:
            print(row, "\n")

        my_cursor.close()
        connection.close()

    except sqlite3.Error as error:
        print('Failed to display sqlite table', error)
