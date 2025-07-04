from flask import app, render_template, url_for, request, redirect, Blueprint, flash, session
from sqlalchemy import desc

from my_asset_project import db
from my_asset_project.assets.forms import BulkUploadForm, AddNewAssetForm, AssetSearchForm,EditAssetForm, MasterDropdownForm, UserLifeCycle
import pandas as pd
from datetime import date
from my_asset_project.models import Asset_Details,Asset_Status_Details,Asset_User_Mapping,Asset_Trail,User_Details,MasterDropdown, Asset_log
from sqlalchemy import create_engine, or_
from my_asset_project import app
from flask import jsonify, request
from sqlalchemy.sql import column
import traceback



import os
from flask import send_from_directory

add_new_asset = Blueprint('add_asset', __name__)
asset_upload = Blueprint('assets', __name__)
asset_search = Blueprint('search_asset', __name__)
#edit_asset = Blueprint('edit_asset', __name__)
#Edit_asset = Blueprint('assets', __name__)
asset_blueprint = Blueprint('asset_blueprint', __name__)#####EDIT ASSET#######
view_asset=Blueprint('view_asset', __name__)
get_asset_number = Blueprint('get_asset_number', __name__)
asset_lifecycle = Blueprint('asset_lifecycle', __name__)
set_asset_id = Blueprint('set_asset_id', __name__)



#Bulk Upload
@asset_upload.route('/bulk_upload', methods=['POST', 'GET'])
def bulk_upload():
    form = BulkUploadForm()

    if form.validate_on_submit():
        excel_file = form.excel_file.data
        df = pd.read_excel(excel_file) #Using pandas to read excel file
        engine = create_engine('mysql+pymysql://root:santhu01@localhost/ams', echo=False) #Creates engine using sqlalchemy to insert data in mysql
        # Define the columns for table1 and table2
        table1_columns = ['asset_number', 'product_category', 'product_name', 'model_version', 'manufacturer', 'asset_status', 'user_name', 'employee_id', 'location', 'other_location', 'user_email', 'contact', 'company', 'other_company', 'assigned_start_date', 'in_stock_start_date', 'not_working_start_date', 'end_of_life_start_date', 'retain_date', 'retain_amount', 'transfer_date', 'record_insertion_date', 'transferred_amount', 'transferred_from', 'transferred_to', 'disposed_date', 'disposed_amount', 'asset_category', 'oem_serial_number', 'system_host_name', 'ip_address', 'AIC_office', 'oem_asset_warranty', 'oem_warranty_expiry_date', 'insurance_coverage', 'insurance_company',  'policy_number', 'insured_amount', 'start_date', 'end_date', 'supplier_name', 'supplier_contact', 'supplier_location', 'supplier_email', 'incident_id', 'remarks', 'payment_done', 'payment_date', 'voucher_number','device_type', 'desk_lap_os', 'desk_lap_hdd_type', 'desk_lap_hdd_size', 'desk_lap_ram_type', 'desk_lap_ram_size', 'desk_lap_ram_frequency', 'desk_lap_ram_expandable', 'desk_lap_ram_slots', 'desk_lap_hdmi_port', 'desk_lap_display_size', 'desk_lap_graphics_card_size', 'desk_lap_graphics_card_version', 'printer_type', 'printing_type', 'printer_toner_name', 'printer_connectivity', 'hdd_size', 'hdd_type', 'hdd_connectivity', 'tab_os', 'tab_storage', 'tab_ram_size', 'tab_display_size', 'tab_stylus', 'tab_connectivity', 'monitor_display_size', 'monitor_hdmi_port', 'monitor_speaker', 'ups_capacity', 'ups_amc', 'ups_start_date', 'ups_end_date', 'source_of_purchase', 'contract_id','invoice_id', 'invoice_amount', 'invoice_date', 'invoice_upload', 'other_insurance']
        table2_columns = ['asset_status', 'employee_id', 'user_name', 'user_email', 'user_contact', 'company', 'other_company', 'location', 'other_location', 'retain_date', 'retained_end_date', 'retain_amount', 'transfer_date', 'transferred_end_date', 'in_stock_start_date', 'in_stock_end_date', 'assigned_start_date', 'assigned_end_date', 'not_working_start_date', 'not_working_end_date', 'end_of_life_start_date', 'end_of_life_end_date', 'transferred_amount', 'transferred_from', 'transferred_to', 'disposed_date', 'disposed_end_date', 'disposed_amount', 'record_insertion_date']
        
        # Create DataFrames for table1 and table2
        table1_df = df[table1_columns]
        table2_df = df[table2_columns]

        # Insert data into table1
        table1 = "asset_details"
        table1_df.to_sql(table1, engine, if_exists='append', index=False)

        # Insert data into table2
        table2 = "asset_history"
        table2_df.to_sql(table2, engine, if_exists='append', index=False)

        engine.dispose()
    return render_template('bulk_upload.html', form=form)

@get_asset_number.route('/get_last_asset', methods=['GET'])
def get_last_asset():
    # Extract product_category and AIC_office from the request
    product_category = request.args.get('product_category')
    AIC_office = request.args.get('AIC_office')
    
    if AIC_office in ["Statesman House", "East Kidwai Nagar", "Parsvnath Capital Towers"]:
        # If AIC_office is one of the specified values, fetch the maximum asset number
        max_asset = Asset_Details.query.filter(Asset_Details.product_category == product_category, 
                                               or_(Asset_Details.AIC_office == "Statesman House",
                                                   Asset_Details.AIC_office == "East Kidwai Nagar",
                                                   Asset_Details.AIC_office == "Parsvnath Capital Towers"))\
                                      .order_by(Asset_Details.asset_number.desc())\
                                      .first()
        
        if max_asset:
            last_asset_number = int(max_asset.asset_number.split("/")[-1])
        else:
            last_asset_number = 0  # Handle cases where no previous asset exists
    else:
        # If AIC_office is not one of the specified values, fetch as before
        last_asset = Asset_Details.query.filter_by(product_category=product_category, AIC_office=AIC_office)\
                                       .order_by(Asset_Details.id.desc())\
                                       .first()

        if last_asset:
            last_asset_number = int(last_asset.asset_number.split("/")[-1])
        else:
            last_asset_number = 0  # Handle cases where no previous asset exists
    print(last_asset_number, "Last Asset")
    # Return the last asset number as JSON
    return jsonify({'lastNumber': last_asset_number})


# Function to generate asset numbers
def generate_asset_number(product_category, AIC_office, AICOfficePrefixes, productCategoryPrefixes):
    with app.app_context():
        # Check if the provided AIC office and product category are in the prefixes dictionaries
        if AIC_office in AICOfficePrefixes and product_category in productCategoryPrefixes:
            AIC_prefix = AICOfficePrefixes[AIC_office]
            category_prefix = productCategoryPrefixes[product_category]

            if AIC_office in ["HO Statesman", "HO Kidwai Nagar", "HO Parsvnath"]:
                # If AIC_office is one of the specified values, fetch the maximum asset number
                max_asset = Asset_Details.query.filter(
                    Asset_Details.product_category == product_category,
                    or_(Asset_Details.AIC_office == "HO Statesman",
                        Asset_Details.AIC_office == "HO Kidwai Nagar",
                        Asset_Details.AIC_office == "HO Parsvnath")
                ).order_by(Asset_Details.asset_number.desc()).first()

                if max_asset:
                    # Extract the last asset number and increment it by 1
                    last_asset_number = int(max_asset.asset_number.split("/")[-1])
                    new_asset_number = last_asset_number + 1
                else:
                    # If no previous asset exists for this combination, start with 1
                    new_asset_number = 1
            else:
                # If AIC_office is not one of the specified values, fetch as before
                last_asset = Asset_Details.query.filter_by(product_category=product_category, AIC_office=AIC_office)\
                    .order_by(Asset_Details.id.desc()).first()

                if last_asset:
                    # Extract the last asset number and increment it by 1
                    last_asset_number = int(last_asset.asset_number.split("/")[-1])
                    new_asset_number = last_asset_number + 1
                else:
                    # If no previous asset exists for this combination, start with 1
                    new_asset_number = 1

            # Format the new asset number and construct the asset number string
            asset_number = f'AIC/{AIC_prefix}/{category_prefix}/{new_asset_number:02d}'
            return asset_number
        else:
            return None  # Handle cases where prefixes are not found


from sqlalchemy.sql import column

@app.route('/get_code', methods=['GET'])
def get_code():
    product_category = request.args.get('product_category')
    AIC_office = request.args.get('AIC_office')
    print(f"Product category: {product_category}")
    print(f"AIC Office: {AIC_office}")

    # Query the database to fetch the code based on the selected product_category
    result_product_category = MasterDropdown.query.filter_by(category='Product Category', choice=product_category).with_entities(column('code')).first()

    # Query for AIC Office
    result_AIC_office = MasterDropdown.query.filter_by(category='AIC Office', choice=AIC_office).with_entities(column('code')).first()

    # Unpack the result to get the actual value
    result_product_category = result_product_category[0] if result_product_category else None
    result_AIC_office = result_AIC_office[0] if result_AIC_office else None
    
    print(f"Result for Product category code: {result_product_category}")
    print(f"Result for AIC Office code: {result_AIC_office}")

    if result_product_category is not None and result_AIC_office is not None:
        response_data = {
            'code_product_category': result_product_category,
            'code_AIC_office': result_AIC_office
        }
        return jsonify(response_data)
    else:
        return jsonify({'error': 'No matching record found'})


###Add New Asset
@add_new_asset.route('/add_asset', methods=['POST', 'GET'])
def add_asset():
    print("iiiiiiiiiiiiiii")
    form = AddNewAssetForm()
    name=session.get('name')
    if request.method == 'POST':
        # try:
        new_asset = Asset_Details(asset_number= form.asset_number.data, product_category= form.product_category.data, 
                                product_name = form.product_name.data, 
                                model_version= form.model_version.data, manufacturer = form.manufacturer.data, 
                                asset_status = form.asset_status.data, user_name=form.user_name.data, domain_name=form.domain_name.data, location=form.location.data,
                                other_location=form.other_location.data, user_email=form.user_email.data, contact=form.contact.data, company=form.company.data, 
                                other_company=form.other_company.data, assigned_start_date=form.assigned_start_date.data,in_stock_start_date=form.in_stock_start_date.data,
                                record_insertion_date=datetime.today(),
                                    not_working_start_date=form.not_working_start_date.data,end_of_life_start_date=form.end_of_life_start_date.data,
                                retain_date=form.retain_date.data,retain_amount=form.retain_amount.data,transfer_date=form.transfer_date.data,
                                transferred_from=form.transferred_from.data, transferred_to=form.transferred_to.data,transferred_amount=form.transferred_amount.data,
                                disposed_date=form.disposed_date.data,disposed_amount=form.disposed_amount.data,
                                asset_category= form.asset_category.data, 
                                oem_serial_number = form.oem_serial_number.data, system_host_name = form.system_host_name.data, 
                                ip_address = form.ip_address.data, AIC_office=form.AIC_office.data,
                                oem_asset_warranty = form.oem_asset_warranty.data, oem_warranty_expiry_date = form.oem_warranty_expiry_date.data, 
                                insurance_coverage= form.insurance_coverage.data, insurance_company= form.insurance_company.data,
                                policy_number = form.policy_number.data, 
                                insured_amount = form.insured_amount.data, start_date = form.start_date.data, 
                                end_date= form.end_date.data, supplier_name = form.supplier_name.data, 
                                supplier_contact = form.supplier_contact.data, supplier_location = form.supplier_location.data, supplier_address=form.supplier_address.data,
                                supplier_email = form.supplier_email.data, having_issue=form.having_issue.data,
                                incident_id = form.incident_id.data, remarks = form.remarks.data, payment_done= form.payment_done.data, 
                                payment_date = form.payment_date.data, amount_paid=form.amount_paid.data,
                                voucher_number = form.voucher_number.data, device_type = form.device_type.data, 
                                desk_lap_os = form.desk_lap_os.data, desk_lap_hdd_type = form.desk_lap_hdd_type.data, 
                                desk_lap_hdd_size = form.desk_lap_hdd_size.data, desk_lap_ram_type = form.desk_lap_ram_type.data, desk_lap_ram_size = form.desk_lap_ram_size.data, 
                                desk_lap_ram_frequency = form.desk_lap_ram_frequency.data, desk_lap_ram_expandable = form.desk_lap_ram_expandable.data, 
                                desk_lap_ram_slots = form.desk_lap_ram_slots.data, desk_lap_hdmi_port = form.desk_lap_hdmi_port.data, 
                                desk_lap_display_size = form.desk_lap_display_size.data, desk_lap_graphics_card_size = form.desk_lap_graphics_card_size.data, 
                                desk_lap_graphics_card_version = form.desk_lap_graphics_card_version.data, printer_type = form.printer_type.data, printing_type= form.printing_type.data, 
                                printer_toner= form.printer_toner.data, printer_connectivity= form.printer_connectivity.data, hdd_size= form.hdd_size.data, 
                                hdd_type= form.hdd_type.data, hdd_connectivity= form.hdd_connectivity.data, tab_os= form.tab_os.data, tab_storage= form.tab_storage.data, 
                                tab_ram_size= form.tab_ram_size.data, tab_display_size= form.tab_display_size.data, tab_stylus= form.tab_stylus.data, 
                                tab_connectivity= form.tab_connectivity.data, monitor_display_size= form.monitor_display_size.data, monitor_screen_type=form.monitor_screen_type.data, 
                                ups_capacity= form.ups_capacity.data, ups_amc= form.ups_amc.data, ups_start_date= form.ups_start_date.data, 
                                ups_end_date= form.ups_end_date.data, source_of_purchase= form.source_of_purchase.data, contract_id= form.contract_id.data,
                                    invoice_id= form.invoice_id.data, 
                                invoice_amount= form.invoice_amount.data, invoice_date= form.invoice_date.data, invoice_upload= form.invoice_upload.data)
        #db.drop_all()
        db.session.add(new_asset)
        print("address new",new_asset.supplier_address)
        db.session.commit()
    
        new_asset_status=Asset_Status_Details(asset_id=new_asset.id,asset_status=form.asset_status.data)
        db.session.add(new_asset_status)
    
        #db.create_all()
    

        if new_asset.asset_status=="Assigned"   :
            user_name = request.form['user_name']
            domain_name = request.form['domain_name']
            user = User_Details.query.filter_by(user_name=user_name, domain_name=domain_name).first()
            if user:
                new_asset_user_mapping = Asset_User_Mapping(asset_id=new_asset.id, user_id=user.user_id)
            # Perform actions with new_asset_user_mapping
                db.session.add(new_asset_user_mapping)
                db.session.commit()  # Commit the changes to the database
            
            else: 
                return "User not found. Please check the provided user name and domain name.", 400
        
        
    
        if (form.asset_status.data=='In Stock'):

            in_stock_start_date_str = form.in_stock_start_date.data.isoformat()
            form.domain_name.data=None 
            form.user_name.data=None
            form.location.data=None
            form.user_email.data=None
            form.contact.data=None 
            form.company.data =None
            form.transferred_to.data=None
            form.transferred_from.data =None 
            form.retain_amount.data =None
            form.disposed_amount.data=None
            session.get('name'),datetime.today().strftime('%Y-%m-%d')
            current_date = datetime.today().strftime('%Y-%m-%d')

            asset_log_data = Asset_log(form.asset_status.data, new_asset.id,form.domain_name.data, form.user_name.data, in_stock_start_date_str, form.location.data, form.user_email.data, form.contact.data, form.company.data, form.transferred_to.data, form.transferred_from.data, form.retain_amount.data, form.disposed_amount.data, session.get('name'),current_date)

            #new_asset_trail=Asset_Trail(asset_id=new_asset.id,trails=Asset_Trail.generate_trail_data(form.asset_status.data,in_stock_start_date_str, name))
            db.session.add(asset_log_data)
        else :
            as_strt_date_str = form.assigned_start_date.data.isoformat()
            date=form.assigned_start_date.data
            form.transferred_to.data=None
            form.transferred_from.data =None 
            form.retain_amount.data =None
            form.disposed_amount.data=None
            new_trail_data = generate_asset_trail_data(form, 'Assigned')
            asset_log_data = Asset_log(form.asset_status.data, new_asset.id,form.domain_name.data, form.user_name.data, as_strt_date_str, form.location.data, form.user_email.data, form.contact.data, form.company.data, form.transferred_to.data, form.transferred_from.data, form.retain_amount.data, form.disposed_amount.data, session.get('name'),datetime.today().strftime('%Y-%m-%d'))

            #new_asset_trail=Asset_Trail(asset_id=new_asset.id,trails=Asset_Trail.generate_trail_data(form.asset_status.data,as_strt_date_str,AIC_office=form.AIC_office.data,user_name=user.user_name,user_email_id=user.user_email,user_contact=user.user_contact,user_domain_id=user.domain_name,company=form.company.data, name=name))
            db.session.add(asset_log_data)
        db.session.commit() 

    
        uploaded_files = request.files.getlist('invoiceFiles[]')
        # Initialize a list to store the file names
        saved_file_names = []

        # Create the asset folder based on asset ID
        asset_folder = create_asset_folder(new_asset.id)
        print("The length of uploaded file is: ", len(uploaded_files))
        for uploaded_file in uploaded_files:
            print("The upload File is", uploaded_file)

            # Check if the file is empty
            if uploaded_file.filename == '':
                continue

            # Secure the filename to prevent any malicious characters
            filename = secure_filename(uploaded_file.filename)

            # Define the path where the file will be saved within the asset folder
            file_path = os.path.join(asset_folder, filename)

            # Save the file to the specified path
            uploaded_file.save(file_path)

            # Append the saved file name to the list
            saved_file_names.append(filename)

        # Update the invoice_upload field in the asset object
        # Retrieve existing file names from asset.invoice_upload
        existing_file_names = new_asset.invoice_upload.split(',') if new_asset.invoice_upload else []

        # Concatenate the existing and newly uploaded file names
        combined_file_names = existing_file_names + saved_file_names

        # Join the combined file names into a single string
        new_asset.invoice_upload = ','.join(combined_file_names)

        db.session.commit()
        app.logger.info('New Asset added with Number: %s by %s', form.asset_number.data, session.get('name'))

        flash("Asset has been added successfully!", "info")

        return redirect(url_for('add_asset.add_asset'))
            # return render_template('add_asset.html', form=form)
        # except Exception as e:
        #     db.session.rollback()
        #     app.logger.error("Unexpected error: %s\n%s", str(e), traceback.format_exc())
        #     flash("Something went wrong. Please contact support.", "danger")
    form.set_choices()

    return render_template('add_asset.html', form=form)   


    

@add_new_asset.route('/upload_file/<int:asset_id>', methods=['POST'])
def upload_files(asset_id):
    asset = Asset_Details.query.get(asset_id)
    print("in upload section bro ")
    if asset:
        uploaded_files = request.files.getlist('invoiceFiles[]')
        saved_file_names = []

        # Create the asset folder based on asset ID
        asset_folder = create_asset_folder(asset.id)

        for uploaded_file in uploaded_files:
            if uploaded_file.filename == '':
                continue

            filename = secure_filename(uploaded_file.filename)
            file_path = os.path.join(asset_folder, filename)
            uploaded_file.save(file_path)
            saved_file_names.append(filename)

        existing_file_names = asset.invoice_upload.split(',') if asset.invoice_upload else []
        combined_file_names = existing_file_names + saved_file_names
        asset.invoice_upload = ','.join(combined_file_names)
        db.session.commit()

        flash('Files successfully uploaded.', 'success')
    else:
        flash('Asset not found.', 'error')

    return redirect(url_for('add_new_asset.add_asset', asset_number=asset.asset_number))



@add_new_asset.route('/download/<int:asset_id>/<filename>')
def download_file(asset_id, filename):
    # Construct the directory path with the asset ID
    directory_path = os.path.join(app.config['UPLOAD_FOLDER'], str(asset_id))
    print("d p " + directory_path)
    if os.path.exists(directory_path):
        return send_from_directory(directory_path, filename)
    else:
        return "File not found", 404


@add_new_asset.route('/delete_file/<int:asset_id>/<filename>', methods=['GET'])
def delete_file(asset_id, filename):
    asset_folder = os.path.join(app.config['UPLOAD_FOLDER'], str(asset_id))
    file_path = os.path.join(asset_folder, filename)

    if os.path.exists(file_path):
        os.remove(file_path)
        # Update the invoice_upload field in the asset object to remove the deleted file name
        asset = Asset_Details.query.get(asset_id)
        if asset.invoice_upload:
            files = asset.invoice_upload.split(',')
            files.remove(filename)
            asset.invoice_upload = ','.join(files)
            db.session.commit()
            flash(f"File '{filename}' has been deleted successfully.", "success")
        else:
            flash("File has been deleted successfully.", "success")
    else:
        flash(f"File '{filename}' not found.", "error")

    return redirect(url_for('add_new_asset.add_asset', asset_number=asset.asset_number))


@add_new_asset.route('/check_oem_serial_number', methods=['POST'])
def check_oem_serial_number():
    oem_serial_number = request.form.get('oem_serial_number')

    # Query the database to check if the oem_serial_number already exists
    existing_record =Asset_Details.query.filter_by(oem_serial_number=oem_serial_number).first()

    if existing_record:
        return jsonify({'exists': True})
    else:
        return jsonify({'exists': False})







@add_new_asset.route('/get_user_details', methods=['POST'])
def get_user_details():
    selected_domain_name = request.form['domain_name']
    print(f"Received domain_name: {selected_domain_name}")  # Add this line for logging
    user = User_Details.query.filter_by(domain_name=selected_domain_name).first()

    if user:
        user_details = {
            'user_name': user.user_name,
            'user_email': user.user_email,
            'user_contact': user.user_contact,
            'AIC_office': user.AIC_office
        }
        return jsonify(user_details)
    else:
        return jsonify(error='User not found'), 404










def get_start_date_attribute_for_status(asset_status):
    status_to_date_attribute = {
        'In Stock': 'in_stock_start_date',
        'Assigned': 'assigned_start_date',
        'Disposed': 'disposed_date',
        'Retained': 'retain_date',
        'Transferred': 'transfer_date',
        'End Of Life': 'end_of_life_start_date',
        'Not Working': 'not_working_start_date',
    }
    return status_to_date_attribute.get(asset_status, 'default_date_attribute')

def get_end_date_attribute_for_status(asset_status):
    status_to_end_date_attribute = {
        'In Stock': 'in_stock_end_date',
        'Assigned': 'assigned_end_date',
        'Disposed': 'disposed_end_date',
        'Retained': 'retained_end_date',
        'Transferred': 'transferred_end_date',
        'End Of Life': 'end_of_life_end_date',
        'Not Working': 'not_working_end_date',
    }
    return status_to_end_date_attribute.get(asset_status, 'default_end_date_attribute')

def generate_asset_trail_data(form, status):
    # Get the common data for all statuses
    common_data = {
        'asset_status': status,
        'updated_by' : session.get('name')
    }

    if status == 'In Stock':
        common_data['start_date'] = form.in_stock_start_date.data.isoformat()

    elif status == 'Assigned':
        common_data['start_date'] = form.assigned_start_date.data.isoformat()

        assigned_data = {
            'AIC_office': form.AIC_office.data,
            'domain_name': form.domain_name.data,
            'user_name': form.user_name.data,
            'user_email_id': form.user_email.data,
            'user_contact': form.contact.data,
            'location': form.location.data,
            'company': form.company.data
        }
        common_data.update(assigned_data)

    elif status == 'Transferred':
        
        common_data['start_date'] = form.transfer_date.data.isoformat()

        transferred_data = {
            'transferred_from': form.transferred_from.data,
            'transferred_to': form.transferred_to.data,
            'transferred_amount': form.transferred_amount.data,
            'AIC_office': form.AIC_office.data,
            'user_name': form.user_name.data,
            'user_email_id': form.user_email.data,
            'user_contact': form.contact.data,
            'domain_name': form.domain_name.data,
            'company': form.company.data
        }
        common_data.update(transferred_data)

    elif status == 'Retained':
        print("retain date ")
        print(form.retain_date.data)
        #print(form.retained_amount.data)
        common_data['start_date'] = form.retain_date.data.isoformat()

        retained_data = {
            'retain_amount': form.retain_amount.data,
            'AIC_office': form.AIC_office.data,
            'user_name': form.user_name.data,
            'user_email_id': form.user_email.data,
            'user_contact': form.contact.data,
            'domain_name': form.domain_name.data,
            'company': form.company.data
        }
        common_data.update(retained_data)

    elif status == 'Disposed':
        common_data['start_date'] = form.disposed_date.data.isoformat()

        disposed_data = {
            'disposed_amount': form.disposed_amount.data
        }
        common_data.update(disposed_data)

    elif status == 'Not Working':
        common_data['start_date'] = form.not_working_start_date.data.isoformat()

    return common_data

from werkzeug.utils import secure_filename
from flask import  send_from_directory

#app.config['UPLOAD_FOLDER'] = 'C:\\Users\\mgtndl.appajisk\\Desktop\\invoices_upload'

@asset_blueprint.route('/edit_asset', methods=['GET', 'POST'])
def edit_asset_page():
    asset1 = Asset_Details.query.get(session.get('asset_id'))
    print(session.get('asset_id'))
    asset_number=asset1.asset_number
    asset = Asset_Details.query.filter_by(asset_number=asset_number).first()
    form = EditAssetForm(obj=asset)
  
    
    if request.method == 'POST' :
        try:
            new_asset_status=Asset_Status_Details(asset_id=asset.id,asset_status=form.asset_status.data)
            db.session.add(new_asset_status)
            
            domain_name = form.domain_name.data
            user = User_Details.query.filter_by(domain_name=domain_name).first()
            if user:
                user_id = user.user_id
            else:
                user_id = None  # Handle the case when user doesn't exist

            # Check if Asset_User_Mapping entry exists for the asset
            asset_user_mapping = Asset_User_Mapping.query.filter_by(asset_id=asset.id).first()
            asset_status = form.asset_status.data

            should_remove_mapping = asset_status in ["In Stock", "Not Working", "Disposed"]

            if should_remove_mapping:
                # If the asset_status is one of the specified values, remove the mapping
                if asset_user_mapping:
                    db.session.delete(asset_user_mapping)  # Delete the mapping entry
            else:
                # Update or create the Asset_User_Mapping entry
                if not asset_user_mapping:
                    # Create a new Asset_User_Mapping entry if it doesn't exist
                    new_asset_user_mapping = Asset_User_Mapping(asset_id=asset.id, user_id=user_id)
                    db.session.add(new_asset_user_mapping)
                elif asset_user_mapping.user_id != user_id:
                    # Update user_id in the Asset_User_Mapping entry if it has changed
                    asset_user_mapping.user_id = user_id
        
            # Check if the asset_status has changed
            
            # Check if the asset_status remains either assigned or transferred and if any user details have changed
            if asset.asset_status != form.asset_status.data or asset.asset_status in ['Assigned', 'Transferred'] and any(
                [
                    asset.user_name != form.user_name.data,
                    asset.domain_name != form.domain_name.data,
                    asset.location != form.location.data,
                    asset.transfer_date != form.transfer_date.data,
                    asset.transferred_from != form.transferred_from,
                    asset.transferred_to != form.transferred_to,
                ]
            ):
                new_trail_data={}
                global date
                previous_details = Asset_Details.query.filter_by(id=session.get('asset_id')).first()


                if form.asset_status.data == 'In Stock':
                    logEntry=Asset_log.query.filter_by(Asset_ID=session.get('asset_id')).order_by(desc(Asset_log.Date)).first()
                    date=form.in_stock_start_date.data
                    logEntry.EndDate=date
                    form.domain_name.data=None 
                    form.user_name.data=None
                    form.location.data=None
                    form.user_email.data=None
                    form.contact.data=None 
                    form.company.data =None
                    form.transferred_to.data=None
                    form.transferred_from.data =None 
                    form.retain_amount.data =None
                    form.disposed_amount.data=None
                    previous_details.asset_status=None

                    session.get('name'),datetime.today().strftime('%Y-%m-%d')
                    new_trail_data = generate_asset_trail_data(form, 'In Stock')
                elif form.asset_status.data == 'Assigned':                    
                    date=form.assigned_start_date.data
                    logEntry=Asset_log.query.filter_by(Asset_ID=session.get('asset_id')).order_by(desc(Asset_log.Date)).first()
                    logEntry.EndDate=date
                    previous_details.asset_status=None
                    form.transferred_to.data=None
                    form.transferred_from.data =None 
                    form.retain_amount.data =None
                    form.disposed_amount.data=None
                    new_trail_data = generate_asset_trail_data(form, 'Assigned')
                elif form.asset_status.data == 'Transferred':
                    form.retain_amount.data =None
                    form.disposed_amount.data=None
                    date=form.transfer_date.data
                    logEntry=Asset_log.query.filter_by(Asset_ID=session.get('asset_id')).order_by(desc(Asset_log.Date)).first()
                    logEntry.EndDate=date
                    new_trail_data = generate_asset_trail_data(form, 'Transferred')
                elif form.asset_status.data == 'Retained':                
                    form.transferred_to.data=None
                    form.transferred_from.data =None 
                    form.disposed_amount.data=None
                    date=form.retain_date.data
                    logEntry=Asset_log.query.filter_by(Asset_ID=session.get('asset_id')).order_by(desc(Asset_log.Date)).first()
                    logEntry.EndDate=date
                    new_trail_data = generate_asset_trail_data(form, 'Retained')
                elif form.asset_status.data == 'Disposed':
                    form.transferred_to.data=None
                    form.transferred_from.data =None 
                    form.retain_amount.data =None
                    date=form.disposed_date.data
                    logEntry=Asset_log.query.filter_by(Asset_ID=session.get('asset_id')).order_by(desc(Asset_log.Date)).first()
                    logEntry.EndDate=date
                    new_trail_data = generate_asset_trail_data(form, 'Disposed')
                elif form.asset_status.data == 'Not Working':
                    date=form.not_working_start_date.data
                    form.domain_name.data=None 
                    form.user_name.data=None
                    form.location.data=None
                    form.user_email.data=None
                    form.contact.data=None 
                    form.company.data =None
                    form.transferred_to.data=None
                    form.transferred_from.data =None 
                    form.retain_amount.data =None
                    form.disposed_amount.data=None
                    logEntry=Asset_log.query.filter_by(Asset_ID=session.get('asset_id')).order_by(desc(Asset_log.Date)).first()
                    logEntry.EndDate=date
                    new_trail_data = generate_asset_trail_data(form, 'Not Working')

    # Create the Asset_Trail instance with the generated trail data
                new_asset_trail = Asset_Trail(asset_id=asset.id, trails=new_trail_data)
                existing_trail = Asset_Trail.query.filter_by(asset_id=asset.id).first()
                print(date)
                
                asset_log_data = Asset_log(form.asset_status.data, asset.id,form.domain_name.data, form.user_name.data, date, form.location.data, form.user_email.data, form.contact.data, form.company.data, form.transferred_to.data, form.transferred_from.data, form.retain_amount.data, form.disposed_amount.data, session.get('name'),datetime.today().strftime('%Y-%m-%d'))
                if existing_trail:
                        # Concatenate the new trail entry with the existing asset trail
                        updated_trail = existing_trail.trails + ',' + new_asset_trail.trails
                        existing_trail.trails = updated_trail
                else :
                    existing_trail=new_asset_trail
                db.session.add(existing_trail) 
                db.session.add(asset_log_data)             
            print("aip " + str(asset.invoice_upload))
            form.populate_obj(asset)  # Update the asset object with form data
            print("aip after " + str(asset.invoice_upload))
            # Retrieve existing file names from asset.invoice_upload
            existing_file_names = asset.invoice_upload.split(',') if asset.invoice_upload else []
    # Concatenate the existing and newly uploaded file names
    # Join the combined file names into a single string
            db.session.commit()
            #flash('Successfully submitted', 'success')
            
            # Redirect to a success page or back to the edit page
            flash("Asset has been Edited Sucessfully!", "info")

            
        except Exception as e:
            alert_message = f'Error: {str(e)}'
            print(alert_message)
            return render_template('edit_asset.html', asset=asset, form=form)
    form.set_choices()
    uploaded_file_names = os.listdir(create_asset_folder(asset.id))

    return render_template('edit_asset.html', asset=asset, form=form)




@asset_blueprint.route('/upload_file/<int:asset_id>', methods=['POST'])
def upload_file(asset_id):
    asset = Asset_Details.query.get(asset_id)
    print("in upload section bro ")
    if asset:
        uploaded_files = request.files.getlist('invoiceFiles[]')
        saved_file_names = []

        # Create the asset folder based on asset ID
        asset_folder = create_asset_folder(asset.id)

        for uploaded_file in uploaded_files:
            if uploaded_file.filename == '':
                continue

            filename = secure_filename(uploaded_file.filename)
            file_path = os.path.join(asset_folder, filename)
            uploaded_file.save(file_path)
            saved_file_names.append(filename)

        existing_file_names = asset.invoice_upload.split(',') if asset.invoice_upload else []
        combined_file_names = existing_file_names + saved_file_names
        asset.invoice_upload = ','.join(combined_file_names)
        db.session.commit()

        flash('Files successfully uploaded.', 'success')
    else:
        flash('Asset not found.', 'error')

    return redirect(url_for('asset_blueprint.edit_asset', asset_number=asset.asset_number))



@asset_blueprint.route('/download/<int:asset_id>/<filename>')
def download_file(asset_id, filename):
    # Construct the directory path with the asset ID
    directory_path = os.path.join(app.config['UPLOAD_FOLDER'], str(asset_id))
    print("d p " + directory_path)
    if os.path.exists(directory_path):
        return send_from_directory(directory_path, filename)
    else:
        return "File not found", 404


@asset_blueprint.route('/delete_file/<int:asset_id>/<filename>', methods=['GET'])
def delete_file(asset_id, filename):
    asset_folder = os.path.join(app.config['UPLOAD_FOLDER'], str(asset_id))
    file_path = os.path.join(asset_folder, filename)

    if os.path.exists(file_path):
        os.remove(file_path)
        # Update the invoice_upload field in the asset object to remove the deleted file name
        asset = Asset_Details.query.get(asset_id)
        if asset.invoice_upload:
            files = asset.invoice_upload.split(',')
            files.remove(filename)
            asset.invoice_upload = ','.join(files)
            db.session.commit()
            flash(f"File '{filename}' has been deleted successfully.", "success")
        else:
            flash("File has been deleted successfully.", "success")
    else:
        flash(f"File '{filename}' not found.", "error")

    return redirect(url_for('asset_blueprint.edit_asset', asset_number=asset.asset_number))


def create_asset_folder(asset_id):
    # Create a folder with the asset ID if it doesn't exist
    asset_folder = os.path.join(app.config['UPLOAD_FOLDER'], str(asset_id))
    if not os.path.exists(asset_folder):
        os.makedirs(asset_folder)
    return asset_folder     
            
          

from flask import jsonify



@asset_blueprint.route('/get_user_details', methods=['POST'])
def get_user_details():
    selected_domain_name = request.form['domain_name']
    print(f"Received domain_name: {selected_domain_name}")  # Add this line for logging
    user = User_Details.query.filter_by(domain_name=selected_domain_name).first()

    if user:
        user_details = {
            'user_name': user.user_name,
            'user_email': user.user_email,
            'user_contact': user.user_contact,
            'AIC_office': user.AIC_office
        }
        return jsonify(user_details)
    else:
        return jsonify(error='User not found'), 404



    

# #####################################Search Asset####################################

@asset_search.route('/search_assets', methods=['GET', 'POST'])
def search_assets():
    form = AssetSearchForm()
    form.set_choices()
    print("inside search asset")
    print("aic ofc",form.AIC_office.data)
    if request.method == 'POST':
        # Get the form data
        asset_number = request.form.get('asset_number')
        oem_serial_number = request.form.get('oem_serial_number')
        asset_status = request.form.get('asset_status')
        domain_name = request.form.get('domain_name')
        product_category = request.form.get('product_category')
        AIC_office = request.form.get('AIC_office')
        date_added_from = form.date_added_from.data
        date_added_to = form.date_added_to.data
        # Build the query or fetch data from the database
        # Your code to fetch and filter data goes here
        query = Asset_Details.query
        if asset_number:
            query = query.filter(Asset_Details.asset_number == asset_number)
        if oem_serial_number:
            query = query.filter(Asset_Details.oem_serial_number == oem_serial_number)
        if asset_status:
            query = query.filter(Asset_Details.asset_status == asset_status)
        if domain_name:
            query = query.filter(Asset_Details.domain_name == domain_name)
            
        
        if product_category:
            query = query.filter(Asset_Details.product_category == product_category)
        if AIC_office:
            query = query.filter(Asset_Details.AIC_office == AIC_office)

        if date_added_from:
            query = query.filter(Asset_Details.asset_add_date >= date_added_from)
        if date_added_to:
            query = query.filter(Asset_Details.asset_add_date <= date_added_to)
        
        
        results = query.all()
        if not results:
            flash('No assets found with the specified criteria.', 'error')
            return render_template('search-it-asset.html', form=form)

        return render_template('search-it-asset.html', results=results, form=form)
    
    return render_template('search-it-asset.html', form=form)



@asset_search.route('/check_number', methods=['POST'])
def check_duplicate_asset():
    data = request.get_json()
    serial_number = data.get('serial_number')
    print("serial_number89",serial_number)
 
    if not serial_number:
        return jsonify({'status':400, 'message': 'OEM number is required'}), 400
    
    exists = Asset_Details.query.filter_by(oem_serial_number=serial_number).first()
 
    print("exists 988889",exists)
    if exists is not None:
        return jsonify({'status':403, 'message': 'OEM number already exists'})
    else:
        return jsonify({'status':200, 'message': 'OEM number is available'})


import json

from flask import render_template
from flask import request
from my_asset_project.assets.forms import AssetLifeCycle


#Custom function to split the trails
def split_trails(trails_str):
    return [trail.strip() for trail in trails_str.split('#')]

@asset_lifecycle.route('/asset_life_cycle', methods=['GET', 'POST'])
def get_asset_life_cycle():
    form = AssetLifeCycle()
    asset_id = None
    result = None
    if form.validate_on_submit():
        asset_number = form.asset_number.data
        asset1 = Asset_Details.query.filter_by(asset_number=asset_number).first()
        if asset1 is None:
            flash("No Asset Exists with the entered Asset ID", "info")
            return render_template('lifecycle.html', form=form)
        asset_status=Asset_Status_Details.query.filter_by(asset_id=asset1.id)
        asset_id = asset1.id
        log_asset = Asset_log.query.filter_by(Asset_ID=asset_id).all()
        result=log_asset
        if result is None:
            flash("No Asset Exists with the entered Asset ID", "info")
            return render_template('lifecycle.html', form=form)
        return render_template('lifecycle.html', asset_cycle=result, status=asset_status, form=form)

    return render_template('lifecycle.html', form=form)


######################## Master Drop down ###################################

from flask import render_template, redirect, url_for

from flask import Blueprint, render_template, redirect, url_for, request

master_dropdown = Blueprint('master_dropdown', __name__)

@master_dropdown.route('/master_dropdown', methods=['GET', 'POST'])
def master_dropdown_view():
    form = MasterDropdownForm()

    # Fetch distinct categories from the database
    categories = db.session.query(MasterDropdown.category).distinct().all()
    
    # Set default choices for the category field
    choices_category = [("Select a Category", "Select a Category")]
    choices_category.extend((category[0], category[0]) for category in categories)
    form.category.choices = choices_category

    # Get the selected category from the request's query parameters
    selected_category = request.args.get('category')
    choices_for_selected_category = db.session.query(MasterDropdown.choice).filter_by(category=selected_category).distinct().all()

    # Add a default choice to the beginning of the list
    choices_delete_choice = [("Select a Choice to Delete", "Select a Choice to Delete")]
    choices_delete_choice.extend((delete_choice[0], delete_choice[0]) for delete_choice in choices_for_selected_category)
    form.delete_choice.choices = choices_delete_choice


    # Initialize an empty list for choices
    choices = []

    # Message to display when no category is selected
    no_category_message = None
    print(f"Debugging: choices_for_selected_category: {choices_for_selected_category}")
    # If a category is selected, fetch the choices for that category
    if selected_category:
        choices = db.session.query(MasterDropdown.choice).filter_by(category=selected_category).all()

    # Handle POST requests
    if request.method == 'POST':
        selected_category_post = request.form.get('category')  # Get the selected category from the form data
        new_choice = request.form.get('new_choice')
        delete_choice = request.form.get('delete_choice')
        code = request.form.get('code', None)

        # Debugging: Print POST data
        print(f"Debugging: new_choice: {new_choice}, delete_choice: {delete_choice}, selected_category: {selected_category_post}, code: {code}")

        if not selected_category_post:
            no_category_message = "Please select a category before adding or deleting a choice."
        else:
            # Add a new choice to the database
            if new_choice:
                flash('Choice Added Successfully!', 'success')  # 'success' is the category (could be 'error', 'info', etc.)
                db.session.add(MasterDropdown(category=selected_category_post, choice=new_choice, code=code))
                db.session.commit()
            # Delete a choice from the database
            elif delete_choice:
                flash('Choice Deleted Successfully!', 'success')  # 'success' is the category (could be 'error', 'info', etc.)
                print("deleting")
                db.session.query(MasterDropdown).filter_by(category=selected_category_post, choice=delete_choice).delete()
                db.session.commit()

            # Debugging: Print a message before redirecting
            print("Debugging: Redirecting after POST")

            # Redirect to the same page after handling the POST request
            return redirect(url_for('master_dropdown.master_dropdown_view', category=selected_category_post))

    # Debugging: Print a message before rendering the template
    print("Debugging: Rendering template")

    # Render the HTML template with the categories, choices, and messages
    return render_template('master_dropdown_view.html', categories=categories, choices=choices, selected_category=selected_category, no_category_message=no_category_message, form=form)

from flask import request, render_template

# import necessary modules and dependencies

from flask import Blueprint, render_template, request, redirect, url_for, flash
from sqlalchemy.exc import SQLAlchemyError


import openpyxl
from datetime import datetime

from openpyxl import load_workbook

#User Life Cycle
u_lifecycle = Blueprint('u_lifecycle', __name__)

@u_lifecycle.route('/user-lifecycle', methods=['GET', 'POST'])
def lifecycle():
    form=UserLifeCycle()
    form.initFuntion()
    userName=form.domainName.data
    assetID=Asset_Details.query.all()
    assetMapping=Asset_Details.query.filter_by(domain_name=userName).all()
    previousAssets=Asset_log.query.filter_by(DomainName=userName)
    AssetIdNameMapping = {}
    for item in previousAssets:
        for asset_item in assetID:
            if item.Asset_ID == asset_item.id:
                AssetIdNameMapping[item.Asset_ID] = asset_item.product_category
                break  # Assuming Asset_ID is unique and only one match is needed

    print(AssetIdNameMapping)
    return render_template("user-lifecycle.html", form=form, assetMap=assetMapping, pAsset=previousAssets, assetIDname=AssetIdNameMapping)



#view asset
@view_asset.route('/view_asset', methods=['GET'])
def view_asset_page():
    asset1  =  Asset_Details.query.get(session.get('asset_id'))
    asset_number=asset1.asset_number
    asset = Asset_Details.query.filter_by(asset_number=asset_number).first()  # Assuming id is the primary key
    form = EditAssetForm(obj=asset)
    form.populate_obj(asset)
    form.set_choices()
    if asset:
        #return redirect(url_for('view_asset.html'), form=form)
        return render_template('view_asset.html', form=form)
    else:
        return render_template('asset_not_found.html')
############################ remove asset id from url###################
@set_asset_id.route('/set_asset_id', methods=['GET','POST'])
def set_asset():
    asset_id = request.form.get('asset_id')
    session['asset_id'] = asset_id
    return "OK"


@app.route('/get_choices')
def get_choices():
    selected_category = request.args.get('category')
    choices = db.session.query(MasterDropdown.choice).filter_by(category=selected_category).all()
    choices = [choice[0] for choice in choices]
    return jsonify({'choices': choices})


  
########################### Error pages#################################
from flask import render_template
from sqlalchemy.exc import DatabaseError, IntegrityError, OperationalError,DataError
from my_asset_project  import app, db

# Other imports and view functions...

# Custom error handler for all database-related errors
@app.errorhandler(DatabaseError)
def handle_database_error(error):
    db.session.rollback()  # Rollback the database session to avoid leaving the database in an inconsistent state
    
    # Check for specific database error types and provide custom messages
    if isinstance(error.orig, IntegrityError):
        return render_template('error_pages/database_error.html', error=error), 500
    elif isinstance(error.orig, OperationalError):
        return render_template('error_pages/database_error.html', error=error), 500
    elif "'NoneType' object has no attribute 'isoformat'" in str(error.orig):
        return render_template('error_pages/none_type_isoformat_error.html', error=error), 500
  
    else:
        return render_template('error_pages/database_error.html', error=error), 500

# Your other views and routes...
@app.route('/api/check-duplicate-asset', methods=['POST'])
def check_duplicate_asset():
    data = request.get_json()
    asset_number = data.get('asset_number')
 
    if not asset_number:
        return jsonify({'status': 'error', 'message': 'Asset number is required'}), 400
 
    exists = Asset_Details.query.filter_by(asset_number=asset_number).first()
 
    if exists:
        return jsonify({'status': 'duplicate', 'message': 'Asset number already exists'})
    else:
        return jsonify({'status': 'ok', 'message': 'Asset number is available'})





