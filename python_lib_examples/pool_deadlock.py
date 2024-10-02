# https://pythonspeed.com/articles/python-multiprocessing/

import logging
from logging.handlers import QueueHandler, QueueListener
from multiprocessing import Pool, set_start_method
from queue import Queue
from threading import Thread


def setup_logging():
    # Logs get written to a queue, and then a thread reads
    # from that queue and writes messages to a file:
    _log_queue = Queue()
    QueueListener(_log_queue, logging.FileHandler("out.log")).start()
    logging.getLogger().addHandler(QueueHandler(_log_queue))

    # Our parent process is running a thread that
    # logs messages:
    def write_logs():
        while True:
            logging.error("hello, I just did something")

    Thread(target=write_logs).start()


def runs_in_subprocess():
    print("About to log...")
    logging.error("hello, I did something")
    print("...logged")


if __name__ == '__main__':
    set_start_method('forkserver')
    setup_logging()

    set_start_method('spawn', force=True)
    # Meanwhile, we start a process pool that writes some
    # logs. We do this in a loop to make race condition more
    # likely to be triggered.
    while True:
        with Pool() as pool:  # every time it creates a new child process pool!
            pool.apply(runs_in_subprocess)
