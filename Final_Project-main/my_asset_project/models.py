from my_asset_project import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    
    __tablename__ = 'login_details'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    AIC_office = db.Column(db.String(100))
    domain_name = db.Column(db.String(100), unique=True, index=True)
    user_email = db.Column(db.String(100), unique=True, index=True)
    password_hash = db.Column(db.String(600))


    def __init__(self, AIC_office, user_email, domain_name, password_hash):
 
        self.AIC_office = AIC_office
        self.user_email = user_email
        self.domain_name = domain_name
        self.password_hash = generate_password_hash(password_hash)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    # def __repr__(self):
    #     return f"User_name {self.user_name}"
    

# class Asset_history(db.Model):
    # __tablename__ = 'asset_history'

    # asset_history_id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    # asset_id = db.Column(db.Integer, db.ForeignKey('asset_details.id'))
    # asset_status=db.Column(db.String(30))
    # employee_id = db.Column(db.String(30))
    # user_name = db.Column(db.String(20))
    # user_email = db.Column(db.String(30))
    # user_contact = db.Column(db.String(20))
    # company = db.Column(db.String(40))
    # other_company = db.Column(db.String(50))
    # location = db.Column(db.String(50))
    # other_location = db.Column(db.String(50))
    # retain_date = db.Column(db.Date)
    # retained_end_date = db.Column(db.Date)
    # retain_amount = db.Column(db.String(20))
    # transfer_date = db.Column(db.Date)
    # transferred_end_date = db.Column(db.Date)
    # in_stock_start_date=db.Column(db.Date)
    # in_stock_end_date=db.Column(db.Date)
    # assigned_start_date=db.Column(db.Date)
    # assigned_end_date=db.Column(db.Date)
    # not_working_start_date=db.Column(db.Date)
    # not_working_end_date=db.Column(db.Date)
    # end_of_life_start_date=db.Column(db.Date)
    # end_of_life_end_date=db.Column(db.Date)
    # transferred_amount = db.Column(db.Integer)
    # transferred_from = db.Column(db.String(50))
    # transferred_to = db.Column(db.String(50))
    # disposed_date=db.Column(db.Date)
    # disposed_end_date=db.Column(db.Date)
    # disposed_amount=db.Column(db.String(50))
    # record_insertion_date=db.Column(db.Date)
    # related_asset = db.relationship('Asset_Details', foreign_keys=[asset_id])
    
    # # assets = db.relationship('Asset_Details',backref='assigned_user', lazy=True)

    # def __init__(self,asset_id, asset_status,employee_id, record_insertion_date,user_name, user_email, user_contact, company,other_company,location, other_location, transferred_amount, transferred_from, transferred_to,transfer_date,transferred_end_date,in_stock_start_date,in_stock_end_date,not_working_start_date,not_working_end_date ,disposed_date,disposed_end_date,end_of_life_start_date,end_of_life_end_date,retain_date,retained_end_date,assigned_start_date,assigned_end_date,retain_amount,disposed_amount):
        
    #     self.asset_id=asset_id
    #     self.asset_status=asset_status
    #     self.employee_id = employee_id
    #     self.user_name = user_name
    #     self.user_email = user_email
    #     self.user_contact = user_contact
    #     self.company = company
    #     self.other_company=other_company
    #     self.location = location
    #     self.other_location = other_location  
    #     self.transferred_amount = transferred_amount
    #     self. transferred_from = transferred_from
    #     self.transferred_to = transferred_to
    #     self.in_stock_start_date=in_stock_start_date
    #     self.in_stock_end_date=in_stock_end_date
    #     self.assigned_start_date=assigned_start_date
    #     self.assigned_end_date=assigned_end_date
    #     self.retain_date=retain_date
    #     self.retain_end_date=retained_end_date
    #     self.end_of_life_start_date=end_of_life_start_date
    #     self.end_of_life_end_date=end_of_life_end_date
    #     self.transfer_date=transfer_date
    #     self.transferred_end_date=transferred_end_date
    #     self.disposed_end_date=disposed_end_date
    #     self.not_working_start_date=not_working_start_date
    #     self.not_working_end_date=not_working_end_date
    #     self. retain_amount = retain_amount
    #     self.disposed_date = disposed_date
    #     self. disposed_amount = disposed_amount
    #     self.record_insertion_date=record_insertion_date

class Asset_Details(db.Model):

    __tablename__ = 'asset_details'

    
    id = db.Column(db.Integer, primary_key= True, autoincrement=True)
    
    asset_number = db.Column(db.String(100), unique=True)
    product_category = db.Column(db.String(100))
    product_name = db.Column(db.String(100))
    model_version = db.Column(db.String(100))
    manufacturer = db.Column(db.String(100))
    asset_status = db.Column(db.String(100))
    user_name = db.Column(db.String(100))
    domain_name = db.Column(db.String(100))
    location = db.Column(db.String(100))
    other_location = db.Column(db.String(100))
    user_email = db.Column(db.String(100))
    contact = db.Column(db.String(100))
    company = db.Column(db.String(100))
    other_company = db.Column(db.String(100))
    assigned_start_date = db.Column(db.Date)
    in_stock_start_date = db.Column(db.Date)
    not_working_start_date = db.Column(db.Date)
    end_of_life_start_date = db.Column(db.Date)
    retain_date = db.Column(db.Date)
    retain_amount = db.Column(db.Float)
    transfer_date = db.Column(db.Date)
    record_insertion_date = db.Column(db.Date)
    transferred_amount = db.Column(db.Float)
    transferred_from = db.Column(db.String(100))
    transferred_to = db.Column(db.String(100))
    disposed_date = db.Column(db.Date)
    disposed_amount = db.Column(db.Float)
    asset_category = db.Column(db.String(100))
    oem_serial_number = db.Column(db.String(100), unique=True, nullable=False)
    system_host_name = db.Column(db.String(100))
    ip_address = db.Column(db.String(100))
    AIC_office = db.Column(db.String(100))
    oem_asset_warranty = db.Column(db.String(100))
    oem_warranty_expiry_date = db.Column(db.Date)
    insurance_coverage = db.Column(db.String(100))
    insurance_company = db.Column(db.String(100))
    other_insurance = db.Column(db.String(100))
    policy_number = db.Column(db.String(100))
    insured_amount = db.Column(db.Float, nullable=True)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    supplier_name = db.Column(db.String(100))
    supplier_contact = db.Column(db.String(100))
    supplier_location = db.Column(db.String(100))
    supplier_email = db.Column(db.String(100))
    supplier_address = db.Column(db.String(100))
    having_issue = db.Column(db.String(100))
    incident_id = db.Column(db.String(100))
    remarks = db.Column(db.String(100))
    payment_done = db.Column(db.String(100))
    payment_date = db.Column(db.Date)
    amount_paid = db.Column(db.Float)
    voucher_number = db.Column(db.String(100))
    device_type = db.Column(db.String(100))
    desk_lap_os = db.Column(db.String(100))
    desk_lap_hdd_type = db.Column(db.String(100))
    desk_lap_hdd_size = db.Column(db.String(100))
    desk_lap_ram_type = db.Column(db.String(100))
    desk_lap_ram_size = db.Column(db.String(100))
    desk_lap_ram_frequency = db.Column(db.String(100))
    desk_lap_ram_expandable = db.Column(db.String(100))
    desk_lap_ram_slots = db.Column(db.String(100))
    desk_lap_hdmi_port = db.Column(db.String(100))
    desk_lap_display_size = db.Column(db.String(100))
    desk_lap_graphics_card_size = db.Column(db.String(100))
    desk_lap_graphics_card_version = db.Column(db.String(100))
    printer_type = db.Column(db.String(100))
    printing_type = db.Column(db.String(100))
    printer_toner_name = db.Column(db.String(100))
    printer_connectivity = db.Column(db.String(100))
    hdd_size = db.Column(db.String(100))
    hdd_type = db.Column(db.String(100))
    hdd_connectivity = db.Column(db.String(100))
    tab_os = db.Column(db.String(100))
    tab_storage = db.Column(db.String(100))
    tab_ram_size = db.Column(db.String(100))
    tab_display_size = db.Column(db.String(100))
    tab_stylus = db.Column(db.String(100))
    tab_connectivity = db.Column(db.String(100))
    monitor_display_size = db.Column(db.String(100))
    monitor_screen_type = db.Column(db.String(100))
    ups_capacity = db.Column(db.String(100))
    ups_amc = db.Column(db.String(100))
    ups_start_date = db.Column(db.Date)
    ups_end_date = db.Column(db.Date)
    source_of_purchase = db.Column(db.String(100))
    contract_id = db.Column(db.String(100))
    invoice_id = db.Column(db.String(100))
    invoice_amount = db.Column(db.Float)
    invoice_date = db.Column(db.Date)
    invoice_upload = db.Column(db.String(100))
    asset_add_date = db.Column(db.Date, default=lambda: datetime.now().date())


    def __init__(self, asset_number, product_category, product_name, model_version, manufacturer,
                asset_status, user_name, domain_name, location, other_location, user_email, contact, company, other_company,
                retain_date,retain_amount,transfer_date,transferred_amount,transferred_from,transferred_to,disposed_date,disposed_amount,
                assigned_start_date,in_stock_start_date,not_working_start_date,end_of_life_start_date,
                asset_category, oem_serial_number, system_host_name, ip_address,AIC_office,
                oem_asset_warranty, oem_warranty_expiry_date, insurance_coverage, insurance_company,
                policy_number, insured_amount, start_date, end_date, supplier_name, supplier_contact,
                supplier_location, supplier_email,supplier_address,having_issue, incident_id, remarks, payment_done, payment_date,amount_paid,
                voucher_number,device_type, desk_lap_os, desk_lap_hdd_type,
                desk_lap_hdd_size, desk_lap_ram_type, desk_lap_ram_size, desk_lap_ram_frequency,
                desk_lap_ram_expandable, desk_lap_ram_slots, desk_lap_hdmi_port,
                desk_lap_display_size, desk_lap_graphics_card_size, desk_lap_graphics_card_version,
                printer_type, printing_type, printer_toner, printer_connectivity, hdd_size,
                hdd_type, hdd_connectivity, tab_os, tab_storage, tab_ram_size, tab_display_size,
                tab_stylus, tab_connectivity,monitor_display_size, monitor_screen_type,
                ups_capacity, ups_amc, ups_start_date, ups_end_date, source_of_purchase, contract_id,invoice_id,record_insertion_date,
                invoice_amount, invoice_date, invoice_upload):
        
        self.asset_number = asset_number
        self.product_category = product_category
        self.product_name = product_name
        self.model_version = model_version
        self.manufacturer = manufacturer
        self.record_insertion_date=record_insertion_date
        self.asset_status = asset_status
        self.user_name = user_name
        self.domain_name = domain_name
        self.location = location
        self.other_location = other_location
        self.user_email = user_email
        self.contact = contact
        self.company = company
        self.other_company = other_company
        self.assigned_start_date=assigned_start_date
        self.in_stock_start_date=in_stock_start_date
        self.not_working_start_date=not_working_start_date
        self.end_of_life_start_date=end_of_life_start_date
        self.retain_date=retain_date
        self.retain_amount=retain_amount
        self.transfer_date=transfer_date
        self.transfer_amount=transferred_amount
        self.transferred_from=transferred_from
        self.transferred_to=transferred_to
        self.disposed_date=disposed_date
        self.disposed_amount=disposed_amount
        self.asset_category = asset_category
        self.oem_serial_number = oem_serial_number
        self.system_host_name = system_host_name
        self.ip_address = ip_address
        self.AIC_office=AIC_office
        self.oem_asset_warranty = oem_asset_warranty
        self.oem_warranty_expiry_date = oem_warranty_expiry_date
        self.insurance_coverage = insurance_coverage
        self.insurance_company = insurance_company
        self.policy_number = policy_number
        self.insured_amount = insured_amount
        self.start_date = start_date
        self.end_date = end_date
        self.supplier_name = supplier_name
        self.supplier_contact = supplier_contact
        self.supplier_location = supplier_location
        self.supplier_email = supplier_email
        self.supplier_address=supplier_address
        self.having_issue=having_issue
        self.incident_id = incident_id
        self.remarks = remarks
        self.payment_done = payment_done
        self.payment_date = payment_date
        self.voucher_number = voucher_number
        self.amount_paid =amount_paid
        self.device_type = device_type
        self.desk_lap_os = desk_lap_os
        self.desk_lap_hdd_type = desk_lap_hdd_type
        self.desk_lap_hdd_size = desk_lap_hdd_size
        self.desk_lap_ram_type = desk_lap_ram_type
        self.desk_lap_ram_size = desk_lap_ram_size
        self.desk_lap_ram_frequency = desk_lap_ram_frequency
        self.desk_lap_ram_expandable = desk_lap_ram_expandable
        self.desk_lap_ram_slots = desk_lap_ram_slots
        self.desk_lap_hdmi_port = desk_lap_hdmi_port
        self.desk_lap_display_size = desk_lap_display_size
        self.desk_lap_graphics_card_size = desk_lap_graphics_card_size
        self.desk_lap_graphics_card_version = desk_lap_graphics_card_version
        self.printer_type = printer_type
        self.printing_type = printing_type
        self.printer_toner = printer_toner
        self.printer_connectivity = printer_connectivity
        self.hdd_size = hdd_size
        self.hdd_type = hdd_type
        self.hdd_connectivity = hdd_connectivity
        self.tab_os = tab_os
        self.tab_storage = tab_storage
        self.tab_ram_size = tab_ram_size
        self.tab_display_size = tab_display_size
        self.tab_stylus = tab_stylus
        self.tab_connectivity = tab_connectivity
        self.monitor_display_size = monitor_display_size
        self.monitor_screen_type=monitor_screen_type
        self.ups_capacity = ups_capacity
        self.ups_amc = ups_amc
        self.ups_start_date = ups_start_date
        self.ups_end_date = ups_end_date
        self.source_of_purchase = source_of_purchase
        self.contract_id = contract_id
        self.invoice_id = invoice_id
        self.invoice_amount = invoice_amount
        self.invoice_date = invoice_date
        self.invoice_upload = invoice_upload



#asset_status 

class Asset_Status_Details(db.Model):
    __tablename__ = 'asset_status_details'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    asset_id = db.Column(db.Integer, db.ForeignKey('asset_details.id'), nullable=True)
    asset_status = db.Column(db.String(255), nullable=True)
    
    def __init__(self, asset_id, asset_status):
        self.asset_id = asset_id
        self.asset_status = asset_status


class Asset_User_Mapping(db.Model):
    __tablename__ = 'asset_user_mapping'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    asset_id = db.Column(db.Integer, db.ForeignKey('asset_details.id'), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user_details.user_id'), nullable=True)

    def __init__(self, asset_id, user_id):
        self.asset_id = asset_id
        self.user_id = user_id


import json 
class Asset_log(db.Model):
    __tablename__ ='asset_log'
    ID = db.Column(db.Integer, primary_key=True)
    Asset_ID = db.Column(db.Integer, db.ForeignKey('asset_details.id'))
    AssetStatus=db.Column(db.String(255))
    DomainName = db.Column(db.String(255))
    UserName = db.Column(db.String(255))
    Date = db.Column(db.Date)
    EndDate = db.Column(db.Date)
    Location = db.Column(db.String(255))
    EmailId = db.Column(db.String(255))
    Contact = db.Column(db.String(20))
    Company = db.Column(db.String(255))
    TransferTo = db.Column(db.String(255))
    TransferFrom = db.Column(db.String(255))
    RetainAmount = db.Column(db.DECIMAL(10, 2))
    DisposedAmount = db.Column(db.DECIMAL(10, 2))
    UpdatedDate = db.Column(db.Date)
    Updated_By = db.Column(db.String(255))
    def __init__(
        self, AS, Asset_ID, DomainName, UserName, Date,Location, EmailId,
        Contact, Company, TransferTo, TransferFrom, RetainAmount,
        DisposedAmount, Updated_By, UpdatedDate
    ):
        self.AssetStatus=AS
        self.Asset_ID = Asset_ID
        self.DomainName = DomainName
        self.Date=Date
        self.UserName = UserName
        self.Location = Location
        self.EmailId = EmailId
        self.Contact = Contact
        self.Company = Company
        self.TransferTo = TransferTo
        self.TransferFrom = TransferFrom
        self.RetainAmount = RetainAmount
        self.DisposedAmount = DisposedAmount
        self.UpdatedDate = UpdatedDate
        self.Updated_By = Updated_By

class Asset_Trail(db.Model):
    __tablename__ = 'asset_trail'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    asset_id = db.Column(db.Integer, db.ForeignKey('asset_details.id'), nullable=True)
    trails = db.Column(db.Text, nullable=True)

    def __init__(self, asset_id, trails):
        self.asset_id = asset_id
        self.trails = json.dumps(trails) 
         # Convert Python list to JSON string when initializing

    @classmethod
    def generate_trail_data(cls, status, start_date, name, **kwargs):
        # Generate JSON data based on status and additional information
        data = {
            'asset_status': status,
            'start_date': start_date,
            'updated_by': f"{name} ({datetime.today().strftime('%d-%m-%Y')})"
        }
        if status == 'In Stock' :
            pass
        elif status == 'Assigned':
            data.update({
                'user_id': kwargs.get('user_id', None),
                'AIC_office': kwargs.get('AIC_office', None),
                'user_name': kwargs.get('user_name', None),
                'user_email_id': kwargs.get('user_email_id', None),
                'user_contact': kwargs.get('user_contact', None),
                'user_domain_id': kwargs.get('user_domain_id', None),
                'company': kwargs.get('company', None)
            })
        elif status == 'Transferred':
            data.update({
                'user_id': kwargs.get('user_id', None),
                'transferred_from': kwargs.get('transferred_from', None),
                'transferred_to': kwargs.get('transferred_to', None),
                'transferred_amount': kwargs.get('transferred_amount', None),
                'AIC_office': kwargs.get('AIC_office', None),
                'user_name': kwargs.get('user_name', None),
                'user_email_id': kwargs.get('user_email_id', None),
                'user_contact': kwargs.get('user_contact', None),
                'user_domain_id': kwargs.get('user_domain_id', None),
                'company': kwargs.get('company', None)
            })
        elif status == 'Retained':
            data.update({
                'user_id': kwargs.get('user_id', None),
                'retained_amount': kwargs.get('retained_amount', None),
                'AIC_office': kwargs.get('AIC_office', None),
                'user_name': kwargs.get('user_name', None),
                'user_email_id': kwargs.get('user_email_id', None),
                'user_contact': kwargs.get('user_contact', None),
                'user_domain_id': kwargs.get('user_domain_id', None),
                'company': kwargs.get('company', None)
            })
        elif status == 'Disposed':
            data.update({
                'disposed_amount': kwargs.get('disposed_amount', None)
            })
        elif status == 'Not Working':
            # Handle 'Not Working' status data here, if needed
            pass

        return json.dumps(data)

class MasterDropdown(db.Model):
    __tablename__ = 'master_dropdown'  # Replace with your actual table name

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category = db.Column(db.String(255), nullable=False)
    choice = db.Column(db.String(255), nullable=False)
    code = db.Column(db.String(55))

    def __init__(self, category, choice, code):
        self.category = category
        self.choice = choice
        self.code = code
    
class User_Details(db.Model):
    __tablename__ = 'user_details'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    domain_name = db.Column(db.String(255), nullable=False)
    user_name = db.Column(db.String(255), nullable=False)
    user_email = db.Column(db.String(255), nullable=False)
    user_contact = db.Column(db.String(20), nullable=True)
    company = db.Column(db.String(255), nullable=True)
    Designation = db.Column(db.String(100), nullable=True)
    AIC_office = db.Column(db.String(100), nullable=False)

    def __init__(self, domain_name, user_name, user_email, AIC_office, Designation=None, user_contact=None, company=None):
        self.domain_name= domain_name
        self.user_name = user_name
        self.user_email = user_email
        self.user_contact = user_contact
        self.company = company
        self.Designation = Designation
        self.AIC_office = AIC_office


