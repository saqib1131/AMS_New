# Main File to run the application
from my_asset_project import app
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, session, redirect, url_for, request

from flask import request, redirect, url_for, session
from werkzeug.exceptions import HTTPException


log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
log_handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=1)
log_handler.setFormatter(log_formatter)
app.logger.addHandler(log_handler)
app.logger.setLevel(logging.DEBUG)

app.secret_key = '909b8f5c619322db13ef485cbc8104c2e99caf34b8ba639d9bf75065ebb641ed'


# Allow access to these routes without login
PUBLIC_ROUTES = {'/login', '/logout'}

@app.before_request
def require_login():
    # Allow static files (JS, CSS, etc.)
    if request.path.startswith('/static'):
        return

    # Skip for public routes
    if request.path in PUBLIC_ROUTES:
        return

    # Check if user is logged in
    if 'name' not in session:
        return redirect(url_for('users.login'))
    

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)


