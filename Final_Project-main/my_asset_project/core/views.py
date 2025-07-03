from flask import render_template, request, Blueprint, session, redirect, url_for
from my_asset_project.assets.forms import AssetSearchForm


core = Blueprint('core',__name__)

############################Core page for IT and Estb#########################
@core.route('/')
def index():
    #form = AssetSearchForm()
    log_content=""
    if 'name' not in session:
        return redirect(url_for('users.login'))
    else:
        alert_message = request.args.get('alert_message')
        log_file_path = 'app.log'  
        with open(log_file_path, 'r') as file:
            log_content = file.read()
            print(log_content)
        return render_template('index.html',alert_message=alert_message, log_content=log_content)
    return render_template('index.html')
     






