# Main File to run the application
from my_asset_project import app
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask

log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
log_handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=1)
log_handler.setFormatter(log_formatter)
app.logger.addHandler(log_handler)
app.logger.setLevel(logging.DEBUG)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)


