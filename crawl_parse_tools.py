import datetime
import requests
import time
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from requests.exceptions import SSLError
from requests.packages.urllib3.util.retry import Retry
from database_tools import insert_update_database


def requests_retry_session(
        retries=3,
        backoff_factor=0.3,
        status_force_list=(429, 500, 502, 503, 504),
        # method_whitelist=("HEAD", "GET", "PUT", "POST", "DELETE", "OPTIONS", "TRACE")
        # allowed_methods=("HEAD", "GET", "PUT", "POST", "DELETE", "OPTIONS", "TRACE")
        session=None,
):
    """
    This function handles subtle irregularities when making requests to the URL.
    It retries requests to the URL.
    """
    session = session or requests.Session()
    retry_strategy = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_force_list,
        # method_whitelist= method_whitelist,
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session


def crawler():
    """
    This function crawls much older weather data from the URL 'https://wttr.in'.
    It calls the function insert_update_database(temperature, wind_speed, crawl_date, crawl_time) which
    then inserts the crawled information into the database.

    :return: This function returns no value.
    """

    url = 'https://wttr.in/?format=%c+%t+%w\n'
    headers = {"user-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/96.0.4664.45 Safari/537.36'}

    # Handling request errors, connection errors or network disconnections.

    source_code = ''

    while source_code == '':
        try:
            source_code = requests_retry_session().get(url, headers=headers, timeout=5)

        except SSLError:
            source_code = requests_retry_session().get(url, headers=headers, verify=False, timeout=5)

        except requests.exceptions.ConnectionError:
            print('\rConnection error. Connection to server denied or network problem.            ', end='', flush=True)
            time.sleep(3)
            print("\r", end='', flush=True)
            print('\rPlease check internet/network connection.                                    ', end='', flush=True)
            time.sleep(3)
            print("\r", end='', flush=True)
            print('\rIn the meantime, will keep trying until connection is established. Trying ...', end='', flush=True)
            time.sleep(3)
            print("\r", end='', flush=True)
            continue

    # print(f'Status code: {source_code.status_code}\n')

    soup = ''
    while soup == '':
        try:
            plain_text = source_code.text
            soup = BeautifulSoup(plain_text, 'html.parser')

            data = soup.encode('ascii', errors='ignore').decode('unicode-escape')

            # Cleaning and processing the crawled data.
            characters = ['+', 'C', 'km/h']
            for character in characters:
                data = data.replace(character, '')

            data.strip()
            temperature = int(data.split()[0])
            wind_speed = int(data.split()[1])

            download_time = str(datetime.datetime.now())
            crawl_date = download_time.split()[0]
            crawl_time = download_time.split()[1]
            insert_update_database(temperature, wind_speed, crawl_date, crawl_time)

        # Handling possible ValueErrors due to unknown errors at the url 'https://wttr.in/'
        except ValueError:
            print('\rValue error. There is an unknown error at the url "https://wttr.in/"         ', end='', flush=True)
            time.sleep(3)
            print("\r", end='', flush=True)
            print('\r Checking back in a few seconds to resume crawling the data.                 ', end='', flush=True)
            time.sleep(3)
            print("\r", end='', flush=True)
            print('\rIn the meantime, will keep trying until errors are resolved. Trying ...      ', end='', flush=True)
            time.sleep(3)
            print("\r", end='', flush=True)
            continue
