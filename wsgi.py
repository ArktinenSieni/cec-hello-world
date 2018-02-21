import socket
import datetime
import logging
from flask import Flask

application = Flask(__name__)


def get_logfile():
    return "/mnt/important_logs"


def read_log():
    try:
        log_file = open(get_logfile, "r")
        logging = log_file.read()
        log_file.close()

        logging.info("Log reading successful")
    
    except Exception as e:
        logging.warning("Log reading failed: " + e)


def write_log():
    try:
        log_file = open(get_logfile(), "a")
        log_line = socket.gethostname + " " + str(datetime.datetime.now())

        log_file.write(log_line)
        log_file.close()

        logging.info("Logging successful")
    except Exception as e:
        logging.warning("Logging failed: " + e)



@application.route("/")
def hello():

    showed_output = str(
        "Hello World! Greetings from ",
        socket.gethostname(),
        "\n",
        read_log
    )
    
    return showed_output


if __name__ == "__main__":
    write_log()
    application.run()
