import socket
import datetime
import logging
from flask import Flask

application = Flask(__name__)

log = logging.getLogger("mushroom-generator")


def get_logfile():
    return "/mnt/important_logs.txt"


def read_log():
    try:
        write_log()

        try:
            log_file = open(get_logfile(), "r")
        except IOError:
            log_file = open(get_logfile(), "w")

        log_data = log_file.read()
        log_file.close()

        log.info("Log reading successful")
        
        return log_data

    except Exception as e:
        log.warning("Log reading failed: " + str(e))
        
        return str(e)


def write_log():
    try:
        try:
            log_file = open(get_logfile(), "a")
        except IOError:
            log_file = open(get_logfile(), "w")


        log_line = "[ Hostname: " + str(socket.gethostname()) + "Datetime: " + str(datetime.datetime.now()) + " ]\n"
        log_file.write(log_line)

        log_file.close()

        log.info("Logging successful")
    except Exception as e:
        log.warning("Logging failed: " + str(e))



@application.route("/")
def hello():
    showed_output = "<body><h1>Hello World! Greetings from " + socket.gethostname() + "</h1><p>" + read_log() + "</p></body>"
    
    return showed_output


if __name__ == "__main__":
    write_log()
    application.run()
