from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField, StringField, IntegerField, SelectField, DateField, TextAreaField,FloatField
from wtforms.validators import DataRequired, InputRequired, Email
from wtforms import SubmitField
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField, SelectField, DateField, IntegerField
from wtforms.validators import DataRequired, Email, InputRequired, Length, Regexp, ValidationError
from flask_wtf import FlaskForm
from my_asset_project.models import MasterDropdown,User_Details
from flask import session



class BulkUploadForm(FlaskForm):
    excel_file = FileField('Upload Excel File', validators=[FileRequired()])
    submit = SubmitField('Upload File')


class AddNewAssetForm(FlaskForm):
    asset_number = StringField('asset_number', validators=[DataRequired()])
    system_host_name = StringField("System Host Name")
    product_name = StringField('product_name', validators=[DataRequired()])
    model_version = StringField('model_version', validators=[DataRequired()])

    
    asset_status = SelectField("Asset Status", choices=[
        ("", "Select an option"),
        ("In Stock", "In Stock"),
        ("Assigned", "Assigned")
        
    ])
    user_name = StringField("user_name")
    domain_name=StringField("domain_name")
    
    location = SelectField("location", choices=[
        ("", "Select an location"),
        ("Residence", "Residence"),
        ("Ministry", "Ministry"),
        ("office", "office"),
        ("Others", "Others")
    ])
    other_location = StringField("other_location")
    user_email = StringField("email", validators=[Email()])
    contact = StringField("contact", validators=[InputRequired()])
    company = SelectField("company", choices=[
        ("", "Select a Company"),
        ("AIC", "AIC"),
        ("WIPRO", "WIPRO"),
        ("BHARAT IT", "BHARAT IT"),
        ("INTELLECT", "INTELLECT"),
        ("PROGILITY", "PROGILITY"),
        ("Others", "Others")
    ])
    other_company = StringField("other_company")
    in_stock_start_date=DateField("in_stock_start_date")
    assigned_start_date=DateField("assigned_start_date")
    not_working_start_date=DateField("not_working_start_date")
    end_of_life_start_date=DateField("end_of_life_start_date")
    retain_date=DateField("retain_date")
    retain_amount=FloatField("retain_amount")
    transfer_date=DateField("transfer_date")
    #record_insertion_date=DateField("record_insertion_date")
    transferred_from=StringField("transferred_from")
    transferred_to=StringField("transferred_to")
    
    transferred_amount =FloatField("transferred_amount")
    disposed_date=DateField("disposed_date")
    disposed_amount =FloatField("disposed_amount")


    asset_category = SelectField("Asset Category", choices=[
        ("", "Select asset category"),
        ("High", "High"),
        ("Medium", "Medium"),
        ("Low", "Low"),
    ])
    oem_serial_number = StringField('oem_serial_number', validators=[DataRequired()])
    ip_address = StringField('ip_address')
    oem_asset_warranty = SelectField("OEM asset Warranty(months)", choices=[
        ("", "Select a number"),
        *[(str(month), f"{month} months") for month in range(0, 61)],
    ])
    oem_warranty_expiry_date = DateField("OEM Warranty Expiry date")
    insurance_coverage = SelectField("Insurance Coverage", choices=[
        ("", "Select coverage"),
        ("Yes", "Yes"),
        ("No", "No"),
    ])
    insurance_company = SelectField("Insurance Company:", choices=[("", "Select company"), ("UIIC", "UIIC"), ("NICIL", "NICIL"), ("NIACL", "NIACL"), ("OICL", "OICL"),("Others","Others")], validators=[InputRequired()])
    other_insurance=StringField("other_insurance")
    policy_number = StringField("Policy Number")
    start_date = DateField("Start Date")
    end_date = DateField("End Date")
    insured_amount = FloatField("Insured Amount")
    source_of_purchase = SelectField("Source of Purchase", choices=[
        ("", "Select Source of Purchase"),
        ("GeM Direct Purchase", "GeM Direct Purchase"),
        ("GeM L-1 Purchase", "GeM L-1 Purchase"),
        ("GeM Bidding", "GeM Bidding"),
        ("Quotation Purchase", "Quotation Purchase"),
        ("Limited Tender", "Limited Tender"),
        ("Open Tender", "Open Tender"),
        ("Direct Purchase", "Direct Purchase"),
    ])
    contract_id = StringField("Contract ID")
    invoice_id = StringField("Invoice ID")
    invoice_amount = FloatField("Invoice Amount", validators=[DataRequired()])
    invoice_date = DateField("Invoice Date", validators=[InputRequired()])
    #invoice_upload = StringField('invoice_upload')
    invoice_upload = FileField('Invoice Upload', validators=[FileRequired()])
    supplier_name = StringField("Supplier Name:", validators=[InputRequired()])
    supplier_contact = StringField("Supplier Contact:", validators=[InputRequired()])
    supplier_email = StringField("Supplier Email:", validators=[Email()])
    
    supplier_address=StringField("Supplier Address:")
    
    having_issue=SelectField("Having Issue (Yes/No):", choices=[("", "Select"), ("Yes", "Yes"), ("No", "No")])
    incident_id = StringField("Incident ID:")
    remarks = TextAreaField("Remarks:")
    payment_done = SelectField("Payment Done (Yes/No):", choices=[("", "Select payment status"), ("Yes", "Yes"), ("No", "No")])
    payment_date = StringField("Payment Date" )
    voucher_number = StringField("FMS Invoice Number")
    amount_paid = FloatField('Amount paid')
    #disposal_date = StringField('disposal_date')
    #disposal_amount = IntegerField('disposal_amount')
    device_type = SelectField("Device Type", choices=[
        ("", "Select a device type"),
        ("laptopDesktop", "Laptop/Desktop"),
        ("printer", "Printer"),
        ("HDD Specs", "HDD Specs"),
        ("tabletMobile", "Tablet/Mobile"),
        ("monitor", "Monitor"),
        ("ups", "UPS")
    ], validators=[InputRequired()])
    # Desktop/Laptop
    desk_lap_os = StringField("desk_lap_os")
    desk_lap_hdd_type = SelectField("desk_lap_hdd_type", choices=[("", "Select HDD type"), ("SATA", "SATA"), ("SSD", "SSD"), ("SAS", "SAS"), ("Others", "Others")])
    desk_lap_hdd_size = SelectField("desk_lap_hdd_size", choices=[("", "Select HDD size"), ("128", "128"), ("256", "256"), ("512", "512"), ("1024", "1024"), ("2048", "2048"), ("4096", "4096"), ("Others", "Others")])
    desk_lap_ram_type = SelectField("desk_lap_ram_type", choices=[("", "Select RAM type"), ("DDR", "DDR"), ("DDR2", "DDR2"), ("DDR3", "DDR3"), ("DDR4", "DDR4"), ("Others", "Others")])
    desk_lap_ram_size = SelectField("desk_lap_ram_size", choices=[("", "Select RAM size"), ("0", "0 GB"), ("2", "2 GB"), ("4", "4 GB"), ("8", "8 GB"), ("16", "16 GB"), ("32", "32 GB"), ("64", "64 GB"), ("128", "128 GB"), ("Others", "Others")])
    desk_lap_ram_frequency = SelectField("desk_lap_ram_frequency", choices=[("", "Select RAM frequency"), ("3000", "3000 MHz"), ("3200", "3200 MHz"), ("3600", "3600 MHz"), ("4000", "4000 MHz"), ("4200", "4200 MHz"), ("4400", "4400 MHz"), ("2933", "2933 MHz"), ("2666", "2666 MHz"), ("2133", "2133 MHz"), ("1600", "1600 MHz"), ("1333", "1333 MHz"), ("1066", "1066 MHz"), ("800", "800 MHz"), ("1000", "1000 MHz"), ("667", "667 MHz"), ("533", "533 MHz"), ("400", "400 MHz"), ("200", "200 MHz"), ("266", "266 MHz"), ("300", "300 MHz"), ("333", "333 MHz"), ("Others", "Others")])
    desk_lap_ram_expandable = SelectField("desk_lap_ram_expandable", choices=[("", "RAM Expandable Upto"), ("0", "0 GB"), ("2", "2 GB"), ("4", "4 GB"), ("8", "8 GB"), ("16", "16 GB"), ("32", "32 GB"), ("64", "64 GB"), ("128", "128 GB"), ("Others", "Others")])
    desk_lap_ram_slots = SelectField("desk_lap_ram_slots", choices=[("", "Select RAM size"), ("0", "0 GB"), ("1", "1 GB"), ("2", "2 GB"), ("3", "3 GB"), ("4", "4 GB"), ("5", "5 GB"), ("Others", "Others")])
    desk_lap_hdmi_port = SelectField("desk_lap_hdmi_port", choices=[("Yes", "Yes"), ("No", "No")])
    desk_lap_display_size = IntegerField("desk_lap_display_size")
    desk_lap_graphics_card_size = SelectField("desk_lap_graphics_card_size", choices=[("", "Select Graphic card size"), ("0", "0 GB"), ("2", "2 GB"), ("4", "4 GB"), ("8", "8 GB"), ("16", "16 GB"), ("32", "32 GB"), ("64", "64 GB"), ("128", "128 GB"), ("Others", "Others")])
    desk_lap_graphics_card_version = SelectField("desk_lap_graphics_card_version", choices=[("", "Graphic Card Version"), ("Nvidia GeForce", "NVidia GeForce"), ("Intel Iris Xe", "Intel Iris Xe"), ("AMD Raedon", "AMD Raedon"), ("Others", "Others")])
    # Printer
    printer_type = StringField("printer_type")
    printing_type = SelectField("printing_type", choices=[("", "printer type"), ("color", "color"), ("Mono", "Mono"), ("Others", "Others")])
    printer_connectivity = SelectField("printer_connectivity", choices=[("", "Connectivity"), ("Wifi", "Wifi"), ("Ethernet", "Ethernet"), ("Both", "Both")])
    printer_toner = StringField("printer_toner")
    # HDD
    hdd_size = IntegerField("hdd_size")
    hdd_type = StringField("hdd_type")
    hdd_connectivity = SelectField("connectivity", choices=[("", "Connectivity"), ("USB", "USB"), ("Type C", "Type C"), ("Both", "Both")])
    # Tablet
    tab_os = StringField("tab_os")
    tab_storage = IntegerField("tab_storage")
    tab_ram_size = IntegerField("tab_ram_size")
    tab_display_size = IntegerField("tab_display_size")
    tab_stylus = SelectField("tab_stylus", choices=[("Yes", "Yes"), ("No", "No")])
    tab_connectivity = SelectField("tab_connectivity:", choices=[("", "Connectivity"), ("Wifi", "Wifi"), ("SIM", "SIM"), ("Both", "Both")])
    # Monitor
    monitor_display_size = IntegerField("display_size")
    monitor_screen_type = SelectField("screen_type", choices=[("LCD", "LCD"), ("LED", "LED"),("CRT", "CRT"),("OLED", "OLED"),("Plasma", "Plasma"),("HDR", "HDR"),("4K", "4K"),("Ultrawide", "Ultrawide"),("Curved", "Curved")])
   
    # UPS
    ups_capacity = IntegerField("ups_capacity")
    ups_amc = SelectField("amc", choices=[("Yes", "Yes"), ("No", "No")])
    ups_start_date = DateField("ups_start_date")
    ups_end_date = DateField("ups_end_date")

    domain_name = SelectField("domain_name")
    AIC_office = SelectField("AIC Office", validators=[DataRequired()])
    product_category = SelectField("Product Category", validators=[DataRequired()])
    manufacturer = SelectField("Manufacturer", validators=[DataRequired()])
    supplier_location = SelectField("Supplier Location")

    def set_choices(self):
        # Fetch choices from the database for product_category and manufacturer
        self.domain_name.choices = [(str(user.domain_name), user.domain_name) for user in User_Details.query.all()]
        self.product_category.choices = [(str(choice.choice), choice.choice) for choice in MasterDropdown.query.filter_by(category="Product Category").all()]
        self.manufacturer.choices = [(str(choice.choice), choice.choice) for choice in MasterDropdown.query.filter_by(category="Manufacturer").all()]
        if session.get('role')=="Normal":
            loc=session.get("location")
            self.AIC_office.choices = [(loc, loc)]   
        else:
            self.AIC_office.choices = [(str(choice.choice), choice.choice) for choice in MasterDropdown.query.filter_by(category="AIC Office").all()]   
        self.supplier_location.choices = [(str(choice.choice), choice.choice) for choice in MasterDropdown.query.filter_by(category="States").all()]

        self.domain_name.choices.insert(0, ("", "Select a Domain_name"))
        self.product_category.choices.insert(0, ("", "Select a Product Category"))
        self.manufacturer.choices.insert(0, ("", "Select a Manufacturer"))
        if session.get("role")!="Normal":
            self.AIC_office.choices.insert(0, ("", "Select a AIC Office"))
        self.supplier_location.choices.insert(0, ("", "Select a state"))


    
    def populate_obj(self, obj):
        super().populate_obj(obj)
        # Convert the selected product_category and manufacturer back to their names
        obj.domain_name = self.domain_name.data
        obj.product_category = self.product_category.data
        obj.manufacturer = self.manufacturer.data
       

    submit = SubmitField("Submit Asset")








from my_asset_project.models import MasterDropdown,User_Details


class EditAssetForm(FlaskForm):

    asset_number = StringField('asset_number', validators=[DataRequired()])
    product_category = SelectField("Product Category", validators=[DataRequired()])
    system_host_name = StringField("System Host Name")
    product_name = StringField('product_name', validators=[DataRequired()])
    model_version = StringField('model_version', validators=[DataRequired()])
    manufacturer = SelectField("Manufacturer", validators=[DataRequired()])
    editOptions = SelectField("Select Edit Option", choices=[
                                                      ("", "Select an Option"),
                                                      ("Assign / Change Asset Status", "Assign / Change Asset Status"), 
                                                    #   ("Edit Insurance / Warranty Details", "Edit Insurance / Warranty Details"),
                                                    #   ("Edit Payment Details", "Edit Payment Details"),
                                                    #   ("Report Issue", "Report Issue")
                                                      ])    

    location = SelectField("location", choices=[
        ("", "Select an location"),
        ("Residence", "Residence"),
        ("Ministry", "Ministry"),
        ("office", "office"),
        ("Others", "Others")
    ])
    other_location = StringField("other_location")
    user_email = StringField("email", validators=[Email()])
    domain_name=StringField("domain_name")
    user_name = StringField("user_name")
    contact = StringField("contact", validators=[InputRequired()])
    #contact = StringField("Contact", validators=[InputRequired(), validate_phone])
    assigned_start_date = DateField("Issue Date")
    company = SelectField("company", choices=[
        ("", "Select a Company"),
        ("AIC", "AIC"),
        ("WIPRO", "WIPRO"),
        ("BHARAT IT", "BHARAT IT"),
        ("INTELLECT", "INTELLECT"),
        ("PROGILITY", "PROGILITY"),
        ("Others", "Others")
    ])
    other_company = StringField("other_company")
    in_stock_start_date=DateField("in_stock_start_date")
    assigned_start_date=DateField("assigned_start_date")    
    not_working_start_date=DateField("not_working_start_date")
    end_of_life_start_date=DateField("end_of_life_start_date")
    
    retain_date=DateField("retain_date")
    #record_insertion_date=DateField("record_insertion_date")
    retain_amount=FloatField("retain_amount")
    transfer_date=DateField("transfer_date")
    #transferred_from=StringField("transferred_from")
    transferred_from=SelectField("Asset Category", choices=[
        ("", "Select AIC office location"),
        ("Ahmedabad", "Ahmedabad"),
        ("Bangalore", "Bangalore"),
        ("Bhopal", "Bhopal"), 
        ("Bhubaneswar", "Bhubaneswar"),
        ("Chandigarh", "Chandigarh"),
        ("Chennai", "Chennai"),
        ("Dehradun", "Dehradun"),
        ("Gujarat", "Gujarat"),
        ("Guntur", "Guntur"),
        ("Guwahati", "Guwahati"),
        ("HO Statesman", "HO Statesman"),
        ("HO Kidwai Nagar", "HO Kidwai Nagar"),
        ("HO Parsvnath", "HO Parsvnath"),
        ("Hyderabad", "Hyderabad"),
        ("Jaipur", "Jaipur"),
        ("Kolkata", "Kolkata"),
        ("Mumbai", "Mumbai"),
        ("Patna", "Patna"),
        ("Raipur", "Raipur"),
        ("Ranchi", "Ranchi"), 
        ("Thiruvananthapuram", "Thiruvananthapuram")  ])
    #transferred_to=StringField("transferred_to")
    transferred_to=SelectField("Asset Category", choices=[
        ("", "Select AIC office location"),
        ("Ahmedabad", "Ahmedabad"),
        ("Bangalore", "Bangalore"),
        ("Bhopal", "Bhopal"), 
        ("Bhubaneswar", "Bhubaneswar"),
        ("Chandigarh", "Chandigarh"),
        ("Chennai", "Chennai"),
        ("Dehradun", "Dehradun"),
        ("Gujarat", "Gujarat"),
        ("Guntur", "Guntur"),
        ("Guwahati", "Guwahati"),
        ("HO Statesman", "HO Statesman"),
        ("HO Kidwai Nagar", "HO Kidwai Nagar"),
        ("HO Parsvnath", "HO Parsvnath"),
        ("Hyderabad", "Hyderabad"),
        ("Jaipur", "Jaipur"),
        ("Kolkata", "Kolkata"),
        ("Mumbai", "Mumbai"),
        ("Patna", "Patna"),
        ("Raipur", "Raipur"),
        ("Ranchi", "Ranchi"), 
        ("Thiruvananthapuram", "Thiruvananthapuram")  ])
    transferred_amount =FloatField("transferred_amount")
    disposed_date=DateField("disposed_date")
    disposed_amount =FloatField("disposed_amount")
   # issue_date=DateField("disposed_date")
   # return_date=DateField("disposed_date")


    asset_category = SelectField("Asset Category", choices=[
        ("", "Select asset category"),
        ("High", "High"),
        ("Medium", "Medium"),
        ("Low", "Low"),
    ])
    oem_serial_number = StringField('oem_serial_number', validators=[DataRequired()])
    ip_address = StringField('ip_address')
    #transferred_to=StringField("transferred_to")
    transferred_to=SelectField("Asset Category", choices=[
        ("", "Select AIC office location"),
        ("Ahmedabad", "Ahmedabad"),
        ("Bangalore", "Bangalore"),
        ("Bhopal", "Bhopal"), 
        ("Bhubaneswar", "Bhubaneswar"),
        ("Chandigarh", "Chandigarh"),
        ("Chennai", "Chennai"),
        ("Dehradun", "Dehradun"),
        ("Gujarat", "Gujarat"),
        ("Guntur", "Guntur"),
        ("Guwahati", "Guwahati"),
        ("HO Statesman", "HO Statesman"),
        ("HO Kidwai Nagar", "HO Kidwai Nagar"),
        ("HO Parsvnath", "HO Parsvnath"),
        ("Hyderabad", "Hyderabad"),
        ("Jaipur", "Jaipur"),
        ("Kolkata", "Kolkata"),
        ("Mumbai", "Mumbai"),
        ("Patna", "Patna"),
        ("Raipur", "Raipur"),
        ("Ranchi", "Ranchi"), 
        ("Thiruvananthapuram", "Thiruvananthapuram")  ])
    transferred_amount =FloatField("transferred_amount")
    disposed_date=DateField("disposed_date")
    disposed_amount =FloatField("disposed_amount")
   # issue_date=DateField("disposed_date")
   # return_date=DateField("disposed_date")


    asset_category = SelectField("Asset Category", choices=[
        ("", "Select asset category"),
        ("High", "High"),
        ("Medium", "Medium"),
        ("Low", "Low"),
    ])
    oem_serial_number = StringField('oem_serial_number', validators=[DataRequired()])
    ip_address = StringField('ip_address')
    
    oem_asset_warranty = SelectField("OEM asset Warranty(months)", choices=[
        ("", "Select a number"),
        *[(str(month), f"{month} months") for month in range(0, 61)],
    ])
    oem_warranty_expiry_date = DateField("OEM Warranty Expiry date")
    oem_warranty_expiry_date= DateField("oem_warranty_expiry_date", render_kw={"class": "form-control"})
    insurance_coverage = SelectField("Insurance Coverage", choices=[
        ("", "Select coverage"),
        ("Yes", "Yes"),
        ("No", "No"),
    ])
    insurance_company = SelectField("Insurance Company:", choices=[("", "Select company"), ("UIIC", "UIIC"), ("NICIL", "NICIL"), ("NIACL", "NIACL"), ("OICL", "OICL"),("Others","Others")])
    policy_number = StringField("Policy Number", render_kw={"disabled": ""})
    start_date = DateField("Start Date")
    end_date = DateField("End Date")
    insured_amount = FloatField("Insured Amount")
    other_insurance=StringField("other_insurance")
    source_of_purchase = SelectField("Source of Purchase", choices=[
        ("", "Select Source of Purchase"),
        ("GeM Direct Purchase", "GeM Direct Purchase"),
        ("GeM L-1 Purchase", "GeM L-1 Purchase"),
        ("GeM Bidding", "GeM Bidding"),
        ("Quotation Purchase", "Quotation Purchase"),
        ("Limited Tender", "Limited Tender"),
        ("Open Tender", "Open Tender"),
        ("Direct Purchase", "Direct Purchase"),
    ])
    contract_id = StringField("Contract ID")
    invoice_id = StringField("Invoice ID")
    invoice_amount = FloatField("Invoice Amount", validators=[DataRequired()])
    invoice_date = DateField("Invoice Date", validators=[InputRequired()])
    invoice_upload = StringField('invoice_upload')
    supplier_name = StringField("Supplier Name:", validators=[InputRequired()])
    supplier_contact = StringField("Supplier Contact:", validators=[InputRequired()])
    supplier_email = StringField("Supplier Email:", validators=[Email()])
    
    supplier_address=StringField("Supplier Address:")
    having_issue=SelectField("Having Issue (Yes/No):", choices=[("", "Select"), ("Yes", "Yes"), ("No", "No")])
    incident_id = StringField("Incident ID:")
    remarks = TextAreaField("Remarks:")
    payment_done = SelectField("Payment Done (Yes/No):", choices=[("", "Select payment status"), ("Yes", "Yes"), ("No", "No")])
    payment_date = DateField("Payment Date", render_kw={"class": "form-control payment-field"})
    voucher_number = StringField("FMS Invoice Number", render_kw={"class": "form-control payment-field"})
    amount_paid = FloatField('Amount paid', validators=[DataRequired()])
    device_type = SelectField("Device Type", choices=[
        ("", "Select a device type"),
        ("laptopDesktop", "Laptop/Desktop"),
        ("printer", "Printer"),
        ("HDD Specs", "HDD Specs"),
        ("tabletMobile", "Tablet/Mobile"),
        ("monitor", "Monitor"),
        ("ups", "UPS")
    ], validators=[InputRequired()])
    # Desktop/Laptop
    desk_lap_os = StringField("desk_lap_os")
    desk_lap_hdd_type = SelectField("desk_lap_hdd_type", choices=[("", "Select HDD type"), ("SATA", "SATA"), ("SSD", "SSD"), ("SAS", "SAS"), ("Others", "Others")])
    desk_lap_hdd_size = SelectField("desk_lap_hdd_size", choices=[("", "Select HDD size"), ("128", "128"), ("256", "256"), ("512", "512"), ("1024", "1024"), ("2048", "2048"), ("4096", "4096"), ("Others", "Others")])
    desk_lap_ram_type = SelectField("desk_lap_ram_type", choices=[("", "Select RAM type"), ("DDR", "DDR"), ("DDR2", "DDR2"), ("DDR3", "DDR3"), ("DDR4", "DDR4"), ("Others", "Others")])
    desk_lap_ram_size = SelectField("desk_lap_ram_size", choices=[("", "Select RAM size"), ("0", "0 GB"), ("2", "2 GB"), ("4", "4 GB"), ("8", "8 GB"), ("16", "16 GB"), ("32", "32 GB"), ("64", "64 GB"), ("128", "128 GB"), ("Others", "Others")])
    desk_lap_ram_frequency = SelectField("desk_lap_ram_frequency", choices=[("", "Select RAM frequency"), ("3000", "3000 MHz"), ("3200", "3200 MHz"), ("3600", "3600 MHz"), ("4000", "4000 MHz"), ("4200", "4200 MHz"), ("4400", "4400 MHz"), ("2933", "2933 MHz"), ("2666", "2666 MHz"), ("2133", "2133 MHz"), ("1600", "1600 MHz"), ("1333", "1333 MHz"), ("1066", "1066 MHz"), ("800", "800 MHz"), ("1000", "1000 MHz"), ("667", "667 MHz"), ("533", "533 MHz"), ("400", "400 MHz"), ("200", "200 MHz"), ("266", "266 MHz"), ("300", "300 MHz"), ("333", "333 MHz"), ("Others", "Others")])
    desk_lap_ram_expandable = SelectField("desk_lap_ram_expandable", choices=[("", "RAM Expandable Upto"), ("0", "0 GB"), ("2", "2 GB"), ("4", "4 GB"), ("8", "8 GB"), ("16", "16 GB"), ("32", "32 GB"), ("64", "64 GB"), ("128", "128 GB"), ("Others", "Others")])
    desk_lap_ram_slots = SelectField("desk_lap_ram_slots", choices=[("", "Select RAM size"), ("0", "0 GB"), ("1", "1 GB"), ("2", "2 GB"), ("3", "3 GB"), ("4", "4 GB"), ("5", "5 GB"), ("Others", "Others")])
    desk_lap_hdmi_port = SelectField("desk_lap_hdmi_port", choices=[("Yes", "Yes"), ("No", "No")])
    desk_lap_display_size = IntegerField("desk_lap_display_size")
    desk_lap_graphics_card_size = SelectField("desk_lap_graphics_card_size", choices=[("", "Select Graphic card size"), ("0", "0 GB"), ("2", "2 GB"), ("4", "4 GB"), ("8", "8 GB"), ("16", "16 GB"), ("32", "32 GB"), ("64", "64 GB"), ("128", "128 GB"), ("Others", "Others")])
    desk_lap_graphics_card_version = SelectField("desk_lap_graphics_card_version", choices=[("", "Graphic Card Version"), ("Nvidia GeForce", "NVidia GeForce"), ("Intel Iris Xe", "Intel Iris Xe"), ("AMD Raedon", "AMD Raedon"), ("Others", "Others")])
    # Printer
    printer_type = StringField("printer_type")
    printing_type = SelectField("printing_type", choices=[("", "printer type"), ("color", "color"), ("Mono", "Mono"), ("Others", "Others")])
    printer_connectivity = SelectField("printer_connectivity", choices=[("", "Connectivity"), ("Wifi", "Wifi"), ("Ethernet", "Ethernet"), ("Both", "Both")])
    printer_toner = StringField("printer_toner")
    # HDD
    hdd_size = IntegerField("hdd_size")
    hdd_type = StringField("hdd_type")
    hdd_connectivity = SelectField("connectivity", choices=[("", "Connectivity"), ("USB", "USB"), ("Type C", "Type C"), ("Both", "Both")])
    # Tablet
    tab_os = StringField("tab_os")
    tab_storage = IntegerField("tab_storage")
    tab_ram_size = IntegerField("tab_ram_size")
    tab_display_size = IntegerField("tab_display_size")
    tab_stylus = SelectField("tab_stylus", choices=[("Yes", "Yes"), ("No", "No")])
    tab_connectivity = SelectField("tab_connectivity:", choices=[("", "Connectivity"), ("Wifi", "Wifi"), ("SIM", "SIM"), ("Both", "Both")])
    # Monitor
    monitor_display_size = IntegerField("display_size")
    monitor_screen_type = SelectField("screen_type", choices=[("LCD", "LCD"), ("LED", "LED"),("CRT", "CRT"),("OLED", "OLED"),("Plasma", "Plasma"),("HDR", "HDR"),("4K", "4K"),("Ultrawide", "Ultrawide"),("Curved", "Curved")])
   
    # UPS
    ups_capacity = IntegerField("ups_capacity")
    ups_amc = SelectField("amc", choices=[("Yes", "Yes"), ("No", "No")])
    ups_start_date = DateField("ups_start_date")
    ups_end_date = DateField("ups_end_date")

    domain_name = SelectField("domain_name")
    
    AIC_office = SelectField("AIC Office", validators=[DataRequired()])
    supplier_location = SelectField("Supplier Location")
    asset_status = SelectField("Asset Status", validators=[DataRequired()])
    def set_choices(self):
        # Fetch choices from the database for product_category and manufacturer
        self.domain_name.choices = [(str(user.domain_name), user.domain_name) for user in User_Details.query.all()]
        self.product_category.choices = [(str(choice.choice), choice.choice) for choice in MasterDropdown.query.filter_by(category="Product Category").all()]
        self.manufacturer.choices = [(str(choice.choice), choice.choice) for choice in MasterDropdown.query.filter_by(category="Manufacturer").all()]
        self.asset_status.choices = [(str(choice.choice), choice.choice) for choice in MasterDropdown.query.filter_by(category="Asset Status").all()]
        self.AIC_office.choices = [(str(choice.choice), choice.choice) for choice in MasterDropdown.query.filter_by(category="AIC Office").all()]
        self.supplier_location.choices = [(str(choice.choice), choice.choice) for choice in MasterDropdown.query.filter_by(category="States").all()]

        self.domain_name.choices.insert(0, ("", "Select a domain_name"))
        self.product_category.choices.insert(0, ("", "Select a Product Category"))
        self.manufacturer.choices.insert(0, ("", "Select a Manufacturer"))
        self.AIC_office.choices.insert(0, ("", "Select a AIC Office"))
        self.supplier_location.choices.insert(0, ("", "Select a state"))

        #self.user_name.choices = [(str(choice.user_name), choice.user_name) for choice in User_Details.query.filter_by(user_name="user_name").all()]
        
    def populate_obj(self, obj):
        super().populate_obj(obj)
        # Convert the selected product_category and manufacturer back to their names
        obj.domain_name = self.domain_name.data
        obj.product_category = self.product_category.data
        obj.manufacturer = self.manufacturer.data
      
       


    submit = SubmitField("Edit Asset")



   


class AssetSearchForm(FlaskForm):
    asset_number = StringField('Asset number')
    oem_serial_number = StringField('OEM Serial number')
    domain_name = SelectField("domain_name")
    product_category = SelectField("Product Category")
    AIC_office = SelectField("AIC Office")
    date_added_from = DateField('date_added_from')
    date_added_to = DateField('date_added_to')
    submit = SubmitField('Search')
    asset_status = SelectField("Asset Status")
   
    def set_choices(self):
        # Fetch choices from the database for product_category and manufacturer
        if session.get('role')=="Normal":
            loc=session.get("location")
            self.AIC_office.choices=[(loc, loc)]
        else:
            self.AIC_office.choices = [(str(choice.choice), choice.choice) for choice in MasterDropdown.query.filter_by(category="AIC Office").all()]
        self.product_category.choices = [(str(choice.choice), choice.choice) for choice in MasterDropdown.query.filter_by(category="Product Category").all()]
        self.asset_status.choices = [(str(choice.choice), choice.choice) for choice in MasterDropdown.query.filter_by(category="Asset Status").all()]
        self.domain_name.choices = [(str(user.domain_name), user.domain_name) for user in User_Details.query.all()]

        self.product_category.choices.insert(0, ("", "Select a Product Category"))
        if session.get('role')!="Normal":
            self.AIC_office.choices.insert(0, ("", "Select a AIC Office"))
        self.asset_status.choices.insert(0, ("", "Select an option"))
        self.domain_name.choices.insert(0, ("", "Select a domain_name"))
    def populate_obj(self, obj):
        super().populate_obj(obj)
    
        obj.domain_name = self.domain_name.data   




class AssetLifeCycle(FlaskForm):
    asset_number = StringField('Asset Number', validators=[DataRequired()])
    submit = SubmitField('View Life Cycle')
    
class UserLifeCycle(FlaskForm):
    
    domainName = SelectField("Select User", choices=[], default="Select the User")
    submit = SubmitField('View User Details')
    def initFuntion(self):
        self.domainName.choices=[(str(user.domain_name), user.domain_name) for user in User_Details.query.all()]


class MasterDropdownForm(FlaskForm):
    category = SelectField('Select a Category', choices=[], default='Select a Category')
    delete_choice = SelectField('Select a Choice to Delete', choices=[], default='Select a Choice to Delete')
    new_choice = StringField('New Choice')
    code = StringField('Code')
    
    # You can use SubmitField for buttons
    delete_button = SubmitField('Delete')
    add_button = SubmitField('Add')


