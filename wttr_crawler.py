import sys
import signal
import time
from database_tools import create_database, display_latest_entries
from crawl_parse_tools import crawler


# Catch KeyboardInterrupt errors and display the latest weather entries.
def keyboard_interrupt_handler(signal, frame):
    """
    This function handles KeyboardInterrupt errors and terminates the program.
    """
    print('\n\nTerminating program ...')
    time.sleep(1)
    display_latest_entries()
    print('\n\nProgram terminated.\n')
    sys.exit(0)


signal.signal(signal.SIGINT, keyboard_interrupt_handler)


def wttr_crawler():
    """
    This is the main function that crawls the URL.
    """
    print('\rData crawling in session.                                                          ', end='', flush=True)
    time.sleep(3)
    crawler()

    print("\r", end='', flush=True)
    print('\rSuccessfully inserted/updated new-entries to the database.                         ', end='', flush=True)
    time.sleep(3)
    print("\r", end='', flush=True)


create_database()

# Automatically run the main crawler every 30 minutes

while True:
    wttr_crawler()
    time.sleep(1)

    # Imitating a countdown timer to show program activity.
    for x in range(1800, -1, -1):
        time.sleep(1)
        print(f'\rWaiting to crawl data in the next 30 minutes. Working ... {x} '
              f'seconds remaining  ', end='', flush=True)
