// // JavaScript function to handle the delete confirmation for the invoice upload
// // document.querySelectorAll('.delete-link').forEach(function(link) {
// //     link.addEventListener('click', function(event) {
// //         event.preventDefault(); // Prevent the default link behavior
// //         if (confirm(link.getAttribute('data-confirm'))) {
// //             window.location.href = link.getAttribute('href'); // Follow the link's href
// //         }
// //     });
// // });

// $(document).ready(function()
// {
//     document.querySelectorAll('.delete-link').forEach(function(link) {
//         link.addEventListener('click', function(event) {
//             event.preventDefault(); // Prevent the default link behavior
//             if (confirm(link.getAttribute('data-confirm'))) {
//                 window.location.href = link.getAttribute('href'); // Follow the link's href
//             }
//         });
//     });
// }
// )

// // If Product Category = Desktop/Laptop then SystemHostName field will be visible
// function toggleSystemHostName() {
//     var productCategoryField = document.getElementById("{{ form.product_category.id }}");
//     var systemHostNameField = document.getElementById("systemHostNameField");

//     if (productCategoryField.value === "Desktop" || productCategoryField.value === "Laptop") {
//         systemHostNameField.style.display = "block";
//     } else {
//         systemHostNameField.style.display = "none";
//     }
// }

// // If insurance company = Others then OtherInsurance field will be visible
// $(document).ready(function toggleOtherInsurance() {
//     console.log("Function Called");
//     var insuranceCompanyField = document.getElementById("{{ form.insurance_company.id }}");
//     var otherInsuranceCompanyField = document.getElementById("otherInsuranceCompanyField");

//     if (insuranceCompanyField.value === "Others") {
//         otherInsuranceCompanyField.style.display = "block";
//     } else {
//         otherInsuranceCompanyField.style.display = "none";
//     }
// }
// )

// function toggleFieldVisibility(selectId, otherFieldId) {
//     var select = document.getElementById(selectId);
//     var otherField = document.getElementById(otherFieldId);

//     if (select.value === "others") {
//         otherField.style.display = "block";
//     } else {
//         otherField.style.display = "none";
//     }
// }

// // IPv4 Validator
// function validateIPv4(inputElement) {
//     // Regular expression to match a valid IPv4 address
//     var ipv4Pattern = /^(\d{1,3}\.){3}\d{1,3}$/;
    
//     var inputValue = inputElement.value;
    
//     if (ipv4Pattern.test(inputValue)) {
//         // Valid IPv4 address
//         inputElement.setCustomValidity('');
//     } else {
//         // Invalid IPv4 address
//         inputElement.setCustomValidity('Please enter a valid IPv4 address.');
//     }
// }


// // This function is used to toggle the enable/disable state of insurance-related input fields
// function toggleInsuranceFields() {
//     var insuranceCoverageField = document.getElementById("{{ form.insurance_coverage.id }}");
//     var insuranceFields = document.querySelectorAll(".insurance-field");

//     // Check if "Yes" is selected before enabling/disabling fields
//     var isEnabled = insuranceCoverageField.value === "Yes";

//     insuranceFields.forEach(function (field) {
//         field.disabled = !isEnabled;
//     });
// }


// // Call the function when the page loads and whenever insurance_coverage changes
// toggleInsuranceFields();

// var insuranceCoverageField = document.getElementById("{{ form.insurance_coverage.id }}");
// insuranceCoverageField.addEventListener("change", toggleInsuranceFields);


// // Define a function to fetch user details via AJAX
// function fetchUserDetails(userName) {
//     // Send an AJAX request to the server to get user details
//     $.ajax({
//         url: "{{ url_for('asset_blueprint.get_user_details') }}",
//         method: "POST",
//         data: { user_name: userName },
//         success: function (response) {
//             // Update the email and contact fields with the fetched data
//             $("#{{ form.user_email.id }}").val(response.user_email);
//             $("#{{ form.contact.id }}").val(response.user_contact);
//         },
//         error: function () {
//             console.error("Error fetching user details.");
//         }
//     });
// }

// $(document).ready(function () {
//     // Attach the fetchUserDetails function to the change event of the user_name field
//     $("#{{ form.user_name.id }}").change(function () {
//         var selectedUserName = $(this).val();
//         fetchUserDetails(selectedUserName);
//     });
// });

// // You can also call fetchUserDetails explicitly when needed
// function someOtherFunction() {
//     var userName = $("#{{ form.user_name.id }}").val(); // Get the user name from the field
//     fetchUserDetails(userName); // Call fetchUserDetails
// }


// // Function to show different Asset Status HTML forms based on asset status selection
// function showAssetDetails() {
//     console.log;
//     var statusForm = document.getElementById('statusForm');
//     var status = document.getElementById('{{ form.asset_status.id }}').value;
//     // Check if Asset Status is already selected, and show details if necessary

//     if (status === 'Assigned') {
//                 statusForm.innerHTML = `
//     <div>
//         <div class="form-row">
// <div class="form-group col-md-4">
//     <label for="{{ form.user_name.id }}">Domain Name:</label>
//     {{ form.user_name(class="form-control", id=form.user_name.id, onchange="fetchUserDetails(this.value)") }}
// </div>

            
//             <div class="form-group col-md-4">
//                 <label for="{{ form.assigned_start_date.id }}">Assigned Date:<span style="color: red;">*</span></label>
//                 {{ form.assigned_start_date(class="form-control", id=form.assigned_start_date.id) }}
              
//             </div>
//             <div class="form-group col-md-4">
//                 <label for="{{ form.location.id }}">Location:<span style="color: red;">*</span></label>
//                 {{ form.location(class="form-control", id=form.location.id, onchange="toggleFieldVisibility('location', 'other_location')") }}
//             </div>
//             <div class="form-group col-md-4">
//                 <div id="otherLocationContainer" class="form-group" style="display: none;">
//                     <label for="{{ form.other_location.id }}">Other Location:</label>
//                     {{ form.other_location(class="form-control", id=form.other_location.id) }}
//                 </div>
//             </div>
//         </div>
//         <div class="form-row">
// <div class="form-group col-md-4">
//     <label for="{{ form.user_email.id }}">Email ID:</label>
//     {{ form.user_email(class="form-control", id=form.user_email.id, placeholder="Email ID", readonly="readonly") }}
// </div>
// <div class="form-group col-md-4">
//     <label for="{{ form.contact.id }}">Contact:</label>
//     {{ form.contact(class="form-control", id=form.contact.id, placeholder="Contact", readonly="readonly") }}
// </div>
// </div>

//             <div class="form-group col-md-4">
//                 <label for="{{ form.company.id }}">Company<span style="color: red;">*</span></label>
//                 {{ form.company(class="form-control", id=form.company.id, onchange="toggleFieldVisibility('company', 'other_company')" ) }}
//             </div>
//             <div class="form-group col-md-4">
//                 <div id="otherCompanyContainer" class="form-group" style="display: none;">
//                     <label for="{{ form.other_company.id }}">Other Company:</label>
//                     {{ form.other_company(class="form-control", id=form.other_company.id) }}
//                 </div>
//             </div>
//         </div>
//     </div>

//                 `;
//             }
//             else if (status === 'Retained') {
// statusForm.innerHTML = `
//     <div>
//         <div class="form-row">
            
//             <div class="form-group col-md-4">
//                 <label for="{{ form.retain_amount.id }}">Retain Amount:<span style="color: red;">*</span></label>
//                 {{ form.retain_amount(class="form-control", id=form.retain_amount.id) }}
//             </div>
//             <div class="form-group col-md-4">
//                 <label for="{{ form.retain_date.id }}">Retain Date:<span style="color: red;">*</span></label>
//                 {{ form.retain_date(class="form-control", id=form.retain_date.id) }}
//         </div>
//     </div>
//     <div>
//         <div class="form-row">
// <div class="form-group col-md-4">
//     <label for="{{ form.user_name.id }}">Domain Name:</label>
//     {{ form.user_name(class="form-control", id=form.user_name.id, onchange="fetchUserDetails(this.value)") }}
// </div>
           
//             <div class="form-group col-md-4">
//                 <label for="{{ form.location.id }}">Location:<span style="color: red;">*</span></label>
//                 {{ form.location(class="form-control", id=form.location.id, onchange="toggleFieldVisibility('location', 'other_location')") }}
//             </div>
//             <div class="form-group col-md-4">
//                 <div id="otherLocationContainer" class="form-group" style="display: none;">
//                     <label for="{{ form.other_location.id }}">Other Location:</label>
//                     {{ form.other_location(class="form-control", id=form.other_location.id) }}
//                 </div>
//             </div>
//         </div>
//         <div class="form-row">
// <div class="form-group col-md-4">
//     <label for="{{ form.user_email.id }}">Email ID:</label>
//     {{ form.user_email(class="form-control", id=form.user_email.id, placeholder="Email ID", readonly="readonly") }}
// </div>
// <div class="form-group col-md-4">
//     <label for="{{ form.contact.id }}">Contact:</label>
//     {{ form.contact(class="form-control", id=form.contact.id, placeholder="Contact", readonly="readonly") }}
// </div>
// </div>
//             <div class="form-group col-md-4">
//                 <label for="{{ form.company.id }}">Company<span style="color: red;">*</span></label>
//                 {{ form.company(class="form-control", id=form.company.id,  onchange="toggleFieldVisibility('company', 'other_company')") }}
//             </div>
//             <div class="form-group col-md-4">
//                 <div id="otherCompanyContainer" class="form-group" style="display: none;">
//                     <label for="{{ form.other_company.id }}">Other Company:</label>
//                     {{ form.other_company(class="form-control", id=form.other_company.id) }}
//                 </div>
//             </div>
//         </div>
//     </div>

//     </div>
// `;
// }
//             else if (status === 'Transferred') {
// statusForm.innerHTML = `
//     <div>
//         <div class="form-row">
//             <div class="form-group col-md-4">
//                 <label for="{{ form.transfer_date.id }}">Transfer Date:<span style="color: red;">*</span></label>
//                 {{ form.transfer_date(class="form-control", id=form.transfer_date.id) }}
              
//             </div>
//             <div class="form-group col-md-4">
//                 <label for="{{ form.transferred_from.id }}">Transferred From:<span style="color: red;">*</span></label>
//                 {{ form.transferred_from(class="form-control", id=form.transferred_from.id) }}
//             </div>
//             <div class="form-group col-md-4">
//                 <label for="{{ form.transferred_to.id }}">Transferred To:<span style="color: red;">*</span></label>
//                 {{ form.transferred_to(class="form-control", id=form.transferred_to.id) }}
//             </div>
//             <div class="form-group col-md-4">
//                 <label for="{{ form.transferred_amount.id }}">Transferred Amount:<span style="color: red;">*</span></label>
//                 {{ form.transferred_amount(class="form-control", id=form.transferred_amount.id) }}
//             </div>
//         </div>
//     </div>
//     <div>
//         <div class="form-row">
// <div class="form-group col-md-4">
//     <label for="{{ form.user_name.id }}">Domain Name:</label>
//     {{ form.user_name(class="form-control", id=form.user_name.id, onchange="fetchUserDetails(this.value)") }}
// </div>
           
//             <div class="form-group col-md-4">
//                 <label for="{{ form.location.id }}">Asset_Location:<span style="color: red;">*</span></label>
//                 {{ form.location(class="form-control", id=form.location.id,  onchange="toggleFieldVisibility('location', 'other_location')") }}
//             </div>
//             <div class="form-group col-md-4">
//                 <div id="otherLocationContainer" class="form-group" style="display: none;">
//                     <label for="{{ form.other_location.id }}">Other Location:</label>
//                     {{ form.other_location(class="form-control", id=form.other_location.id) }}
//                 </div>
//             </div>
//         </div>
//         <div class="form-row">
// <div class="form-group col-md-4">
//     <label for="{{ form.user_email.id }}">Email ID:</label>
//     {{ form.user_email(class="form-control", id=form.user_email.id, placeholder="Email ID", readonly="readonly") }}
// </div>
// <div class="form-group col-md-4">
//     <label for="{{ form.contact.id }}">Contact:</label>
//     {{ form.contact(class="form-control", id=form.contact.id, placeholder="Contact", readonly="readonly") }}
// </div>
// </div>
//             <div class="form-group col-md-4">
//                 <label for="{{ form.company.id }}">Company<span style="color: red;">*</span></label>
//                 {{ form.company(class="form-control", id=form.company.id,  onchange="toggleFieldVisibility('company', 'other_company')") }}
//             </div>
//             <div class="form-group col-md-4">
//                 <div id="otherCompanyContainer" class="form-group" style="display: none;">
//                     <label for="{{ form.other_company.id }}">Other Company:</label>
//                     {{ form.other_company(class="form-control", id=form.other_company.id) }}
//                 </div>
//             </div>
//         </div>
//     </div>

// `;
// }               else if (status === 'Disposed') {
// statusForm.innerHTML = `
//     <div>
//         <div class="form-row">
//             <div class="form-group col-md-4">
//                 <label for="{{ form.disposed_date.id }}">Disposed Date:<span style="color: red;">*</span></label>
//                 {{ form.disposed_date(class="form-control", id=form.disposed_date.id) }}
              
//             </div>
//             <div class="form-group col-md-4">
//                 <label for="{{ form.disposed_amount.id }}">Disposed Amount:<span style="color: red;">*</span></label>
//                 {{ form.disposed_amount(class="form-control", id=form.disposed_amount.id) }}
//             </div>
//         </div>
//     </div>
// `;
// }
//             else if (status === 'In Stock') {
// statusForm.innerHTML = `
    
//         <div class="form-row">
//             <label for="{{ form.in_stock_start_date.id }}">Instock Date:<span style="color: red;">*</span></label>
//                 {{ form.in_stock_start_date(class="form-control", id=form.in_stock_start_date.id) }}
              
//         </div>
// `;
// }
//             else if (status === 'Not Working') {
// statusForm.innerHTML = `
    
//         <div class="form-row">
//             <label for="{{ form.not_working_start_date.id }}">Not Working Start Date:<span style="color: red;">*</span></label>
//                 {{ form.not_working_start_date(class="form-control", id=form.not_working_start_date.id) }}
              
//         </div>
// `;
// }
//             else if (status === 'End Of Life') {
// statusForm.innerHTML = `
    
//         <div class="form-row">
//             <label for="{{ form.end_of_life_start_date.id }}">End Of Life Start Date:<span style="color: red;">*</span></label>
//                 {{ form.end_of_life_start_date(class="form-control", id=form.end_of_life_start_date.id) }}
              
//         </div>
// `;
// }
//     console.log("Show Asset Details: assetStatus =", status);
// }

// // Function to show Asset Status details when editing a page
// function toggleAssetDetails() {
//     var statusForm = document.getElementById('statusForm');
//     if (statusForm.style.display === 'none' || statusForm.style.display === '') {
//         statusForm.style.display = 'block';
//     } else {
//         statusForm.style.display = 'none';
//     }
//     console.log("Toggle Asset Details: statusForm.style.display =", statusForm.style.display);
// }
// // Call the function to show Asset Status details when editing a page
// showAssetDetails();


// // Function to AutoPopulate oem_warranty_expiry_date
// const invoiceDateInput = document.getElementById('invoice_date');
// const oemWarrantyMonthsInput = document.getElementById('oem_asset_warranty');
// const oemWarrantyExpiryDateInput = document.getElementById('oem_warranty_expiry_date');
// const popupMessage = document.getElementById('popupMessage');
// const popupText = document.getElementById('popupText');

// // Function to calculate and set the oem_warranty_expiry_date
// function calculateWarrantyExpiryDate() {
//     const invoiceDate = invoiceDateInput.value;
//     const oemWarrantyMonths = oemWarrantyMonthsInput.value;

//     if (invoiceDate && oemWarrantyMonths) {
//         const date = new Date(invoiceDate);
//         date.setMonth(date.getMonth() + parseInt(oemWarrantyMonths));
//         const formattedDate = date.toISOString().substr(0, 10);
//         oemWarrantyExpiryDateInput.value = formattedDate;
//     } else {
//         oemWarrantyExpiryDateInput.value = '';
//     }
// }

// // Add event listeners for input fields
// invoiceDateInput.addEventListener('change', calculateWarrantyExpiryDate);
// oemWarrantyMonthsInput.addEventListener('change', calculateWarrantyExpiryDate);

// // Phone Number Validation
// function validateForm() {
    
//     const phoneNumberInput = document.getElementById('{{ form.supplier_contact.id }}');
  
//     if (!validatePhoneNumber(phoneNumberInput)) {
//         return false; // Prevent form submission
//     }

//     // If all validations pass, allow form submission
//     return true;
// }


// // Event listener for asset status select input to clear pervious status fields

// function openUserDetails() {
//     const status = document.getElementById('asset_status').value;
//     const statusForm = document.getElementById('statusForm');

//     statusForm.innerHTML = ''; // Clear previous content

//     if (status === 'Assigned') {
    
//         statusForm.innerHTML = `
// <div>
// <div class="form-row">
// <div class="form-group col-md-4">
// <label for="{{ form.user_name.id }}">Domain Name:</label>
// {{ form.user_name(class="form-control", id=form.user_name.id, onchange="fetchUserDetails(this.value)") }}
// </div>

   
//     <div class="form-group col-md-4">
//         <label for="{{ form.assigned_start_date.id }}">Assigned Date:<span style="color: red;">*</span></label>
//         {{ form.assigned_start_date(class="form-control", id=form.assigned_start_date.id) }}
      
//     </div>
//     <div class="form-group col-md-4">
//         <label for="{{ form.location.id }}">Location:<span style="color: red;">*</span></label>
//         {{ form.location(class="form-control", id=form.location.id,  onchange="toggleFieldVisibility('location', 'other_location')") }}
//     </div>
//     <div class="form-group col-md-4">
//         <div id="otherLocationContainer" class="form-group" style="display: none;">
//             <label for="{{ form.other_location.id }}">Other Location:</label>
//             {{ form.other_location(class="form-control", id=form.other_location.id) }}
//         </div>
//     </div>
// </div>
// <div class="form-row">
// <div class="form-group col-md-4">
// <label for="{{ form.user_email.id }}">Email ID:</label>
// {{ form.user_email(class="form-control", id=form.user_email.id, placeholder="Email ID", readonly="readonly") }}
// </div>
// <div class="form-group col-md-4">
// <label for="{{ form.contact.id }}">Contact:</label>
// {{ form.contact(class="form-control", id=form.contact.id, placeholder="Contact", readonly="readonly") }}
// </div>
// </div>
//     <div class="form-group col-md-4">
//         <label for="{{ form.company.id }}">Company<span style="color: red;">*</span></label>
//         {{ form.company(class="form-control", id=form.company.id, onchange="toggleFieldVisibility('company', 'other_company')") }}
//     </div>
//     <div class="form-group col-md-4">
//         <div id="otherCompanyContainer" class="form-group" style="display: none;">
//             <label for="{{ form.other_company.id }}">Other Company:</label>
//             {{ form.other_company(class="form-control", id=form.other_company.id) }}
//         </div>
//     </div>
// </div>
// </div>

//         `;
//     }
//    else if (status === 'Retained') {
// statusForm.innerHTML = `
// <div>
// <div class="form-row">
    
//     <div class="form-group col-md-4">
//         <label for="{{ form.retain_amount.id }}">Retain Amount:<span style="color: red;">*</span></label>
//         {{ form.retain_amount(class="form-control", id=form.retain_amount.id) }}
//     </div>
//     <div class="form-group col-md-4">
//         <label for="{{ form.retain_date.id }}">Retain Date:<span style="color: red;">*</span></label>
//         {{ form.retain_date(class="form-control", id=form.retain_date.id) }}
// </div>
// </div>
// <div>
// <div class="form-row">
// <div class="form-group col-md-4">
// <label for="{{ form.user_name.id }}">Domain Name:</label>
// {{ form.user_name(class="form-control", id=form.user_name.id, onchange="fetchUserDetails(this.value)") }}
// </div>
    
//     <div class="form-group col-md-4">
//         <label for="{{ form.location.id }}">Location:<span style="color: red;">*</span></label>
//         {{ form.location(class="form-control", id=form.location.id,  onchange="toggleFieldVisibility('location', 'other_location')") }}
//     </div>
//     <div class="form-group col-md-4">
//         <div id="otherLocationContainer" class="form-group" style="display: none;">
//             <label for="{{ form.other_location.id }}">Other Location:</label>
//             {{ form.other_location(class="form-control", id=form.other_location.id) }}
//         </div>
//     </div>
// </div>
// <div class="form-row">
// <div class="form-group col-md-4">
// <label for="{{ form.user_email.id }}">Email ID:</label>
// {{ form.user_email(class="form-control", id=form.user_email.id, placeholder="Email ID", readonly="readonly") }}
// </div>
// <div class="form-group col-md-4">
// <label for="{{ form.contact.id }}">Contact:</label>
// {{ form.contact(class="form-control", id=form.contact.id, placeholder="Contact", readonly="readonly") }}
// </div>
// </div>
//     <div class="form-group col-md-4">
//         <label for="{{ form.company.id }}">Company<span style="color: red;">*</span></label>
//         {{ form.company(class="form-control", id=form.company.id,  onchange="toggleFieldVisibility('company', 'other_company')") }}
//     </div>
//     <div class="form-group col-md-4">
//         <div id="otherCompanyContainer" class="form-group" style="display: none;">
//             <label for="{{ form.other_company.id }}">Other Company:</label>
//             {{ form.other_company(class="form-control", id=form.other_company.id) }}
//         </div>
//     </div>
// </div>
// </div>

// </div>
// `;
// }
// else if (status === 'Transferred') {
// statusForm.innerHTML = `
// <div>
// <div class="form-row">
//     <div class="form-group col-md-4">
//         <label for="{{ form.transfer_date.id }}">Transfer Date:<span style="color: red;">*</span></label>
//         {{ form.transfer_date(class="form-control", id=form.transfer_date.id) }}
      
//     </div>
//     <div class="form-group col-md-4">
//         <label for="{{ form.transferred_from.id }}">Transferred From:<span style="color: red;">*</span></label>
//         {{ form.transferred_from(class="form-control", id=form.transferred_from.id) }}
//     </div>
//     <div class="form-group col-md-4">
//         <label for="{{ form.transferred_to.id }}">Transferred To:<span style="color: red;">*</span></label>
//         {{ form.transferred_to(class="form-control", id=form.transferred_to.id) }}
//     </div>
//     <div class="form-group col-md-4">
//         <label for="{{ form.transferred_amount.id }}">Transferred Amount:<span style="color: red;">*</span></label>
//         {{ form.transferred_amount(class="form-control", id=form.transferred_amount.id) }}
//     </div>
// </div>
// </div>
// <div>
// <div class="form-row">
// <div class="form-group col-md-4">
// <label for="{{ form.user_name.id }}">Domain Name:</label>
// {{ form.user_name(class="form-control", id=form.user_name.id, onchange="fetchUserDetails(this.value)") }}
// </div>
    
//     <div class="form-group col-md-4">
//         <label for="{{ form.location.id }}">Asset_Location:<span style="color: red;">*</span></label>
//         {{ form.location(class="form-control", id=form.location.id,  onchange="toggleFieldVisibility('location', 'other_location')") }}
//     </div>
//     <div class="form-group col-md-4">
//         <div id="otherLocationContainer" class="form-group" style="display: none;">
//             <label for="{{ form.other_location.id }}">Other Location:</label>
//             {{ form.other_location(class="form-control", id=form.other_location.id) }}
//         </div>
//     </div>
// </div>
// <div class="form-row">
// <div class="form-group col-md-4">
// <label for="{{ form.user_email.id }}">Email ID:</label>
// {{ form.user_email(class="form-control", id=form.user_email.id, placeholder="Email ID", readonly="readonly") }}
// </div>
// <div class="form-group col-md-4">
// <label for="{{ form.contact.id }}">Contact:</label>
// {{ form.contact(class="form-control", id=form.contact.id, placeholder="Contact", readonly="readonly") }}
// </div>
// </div>
  
//     <div class="form-group col-md-4">
//         <label for="{{ form.company.id }}">Company<span style="color: red;">*</span></label>
//         {{ form.company(class="form-control", id=form.company.id,  onchange="toggleFieldVisibility('company', 'other_company')") }}
//     </div>
//     <div class="form-group col-md-4">
//         <div id="otherCompanyContainer" class="form-group" style="display: none;">
//             <label for="{{ form.other_company.id }}">Other Company:</label>
//             {{ form.other_company(class="form-control", id=form.other_company.id) }}
//         </div>
//     </div>
// </div>
// </div>

// `;
// } else if (status === 'Disposed') {
// statusForm.innerHTML = `
// <div>
// <div class="form-row">
//     <div class="form-group col-md-4">
//         <label for="{{ form.disposed_date.id }}">Disposed Date:<span style="color: red;">*</span></label>
//         {{ form.disposed_date(class="form-control", id=form.disposed_date.id) }}
      
//     </div>
//     <div class="form-group col-md-4">
//         <label for="{{ form.disposed_amount.id }}">Disposed Amount:<span style="color: red;">*</span></label>
//         {{ form.disposed_amount(class="form-control", id=form.disposed_amount.id) }}
//     </div>
// </div>
// </div>
// `;
// }
// else if (status === 'In Stock') {
// statusForm.innerHTML = `

// <div class="form-row">
//     <label for="{{ form.in_stock_start_date.id }}">Instock Date:<span style="color: red;">*</span></label>
//         {{ form.in_stock_start_date(class="form-control", id=form.in_stock_start_date.id) }}
      
// </div>
// `;
// }
// else if (status === 'Not Working') {
// statusForm.innerHTML = `

// <div class="form-row">
//     <label for="{{ form.not_working_start_date.id }}">Not Working Start Date:<span style="color: red;">*</span></label>
//         {{ form.not_working_start_date(class="form-control", id=form.not_working_start_date.id) }}
      
// </div>
// `;
// }
// }

// // Function to validate an email address
// function validateEmail(emailInput) {
//     const email = emailInput.value;
//     const emailRegex = /^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}$/;

//     if (!emailRegex.test(email)) {
//         // Email is not valid, display an error message
//         alert('Please enter a valid email address.');
//         emailInput.focus(); // Set focus back to the email input field
//         return false; // Prevent form submission
//     }
//     return true; // Email is valid
// }

// // Function to validate a contact number
// function validateContact(contactInput) {
//     const contact = contactInput.value;
//     const contactRegex = /^\d{10}$/; // Assuming a 10-digit contact number

//     if (!contactRegex.test(contact)) {
//         // Contact number is not valid, display an error message
//         alert('Please enter a valid 10-digit contact number.');
//         contactInput.focus(); // Set focus back to the contact input field
//         return false; // Prevent form submission
//     }
//     return true; // Contact number is valid
// }

// function validateForm1() {
//     // Validate email and contact fields
//     const emailInput = document.getElementById('{{ form.user_email.id }}');
//     const contactInput = document.getElementById('{{ form.contact.id }}');
//     const supplier_emailInput = document.getElementById('{{ form.supplier_email.id }}');
//     const Supplier_contactInput = document.getElementById('{{ form.supplier_contact.id }}');

//     if (!validateEmail(emailInput) || !validateContact(contactInput)||!validateEmail(supplier_emailInput)||!validateContact(Supplier_contactInput) ) {
//         return false; // Prevent form submission
//     }

//     // Perform other form validations as needed
    
//     return true; // All validations pass, allow form submission
// }

// // Function to clear fields after status change
// $(document).ready(function() {
//     $('#asset_status').click(function() {
//         clearFieldsForStatusChange();
//     });

//     function clearFieldsForStatusChange() {
        
//         var selectedStatus = $('#asset_status').val();
//         // Clear fields based on the selected status
//         if (selectedStatus === 'In Stock') {

//             $('#in_stock_start_date').val('');
           

//         } else if (selectedStatus === 'Assigned') {
           
//             $('#assigned_start_date').val('');
//             $('#user_name').val('');
//             $('#contact').val('');
//             $('#user_email').val('');
//             $('#company').val('');
//             $('#location').val('');
          
//         } else if (selectedStatus === 'Transferred') {
//             $('#transfer_date').val('');
//             $('#transferred_amount').val('');
//             $('#transferred_from').val('');
//             $('#transferred_to').val('');
//             $('#user_name').val('');
//             $('#contact').val('');
//             $('#user_email').val('');
//             $('#company').val('');
//             $('#location').val('');
//         } else if (selectedStatus === 'Retained') {
//             $('#retain_date').val('');
//             $('#retain_amount').val('');
//             $('#user_name').val('');
//             $('#contact').val('');
//             $('#user_email').val('');
//             $('#company').val('');
//             $('#location').val('');
//         } else if (selectedStatus === 'Not Working') {
          
//             $('#not_working_start_date').val('');
//         } else if (selectedStatus === 'Disposed') {
          
//             $('#disposed_date').val('');
//             $('#disposed_amount').val('');
          
           
//         }
//     }
// });

// // Function to show device specifications as per selection.
// function showDeviceSpecifications() {
//     const deviceType = document.getElementById('device_type').value;
//     const specificationsForm = document.getElementById('specificationsForm');

//     specificationsForm.innerHTML = ''; // Clear previous content
        
//                     if (deviceType === 'laptopDesktop') {
//                         specificationsForm.innerHTML = `
                            
// <div class="form-row">
//     <div class="form-group col-md-4">
//         <label for="{{ form.desk_lap_os.id }}">Operating System:</label>
//         {{ form.desk_lap_os(class="form-control", id=form.desk_lap_os.id, placeholder="Enter Operating System") }}
//     </div>
//     <div class="form-group col-md-4">
//         <label for="{{ form.desk_lap_hdd_type.id }}">HDD Type:</label>
//         {{ form.desk_lap_hdd_type(class="form-control", id=form.desk_lap_hdd_type.id) }}
//     </div>
//     <div class="form-group col-md-4">
//         <label for="{{ form.desk_lap_hdd_size.id }}">HDD Size (GB):</label>
//         {{ form.desk_lap_hdd_size(class="form-control", id=form.desk_lap_hdd_size.id) }}
//     </div>
// </div>
// <div class="form-row">
//     <div class="form-group col-md-4">
//         <label for="{{ form.desk_lap_ram_type.id }}">RAM Type:</label>
//         {{ form.desk_lap_ram_type(class="form-control", id=form.desk_lap_ram_type.id) }}
//     </div>
//     <div class="form-group col-md-4">
//         <label for="{{ form.desk_lap_ram_size.id }}">RAM Size:</label>
//         {{ form.desk_lap_ram_size(class="form-control", id=form.desk_lap_ram_size.id) }}
//     </div>
//     <div class="form-group col-md-4">
//         <label for="{{ form.desk_lap_ram_frequency.id }}">RAM Frequency (MHz):</label>
//         {{ form.desk_lap_ram_frequency(class="form-control", id=form.desk_lap_ram_frequency.id) }}
//     </div>
// </div>
// <div class="form-row">
//     <div class="form-group col-md-4">
//         <label for="{{ form.desk_lap_ram_expandable.id }}">RAM Expandable Upto (GB):</label>
//         {{ form.desk_lap_ram_expandable(class="form-control", id=form.desk_lap_ram_expandable.id) }}
//     </div>
//     <div class="form-group col-md-4">
//         <label for="{{ form.desk_lap_ram_slots.id }}">Number of RAM Slots:</label>
//         {{ form.desk_lap_ram_slots(class="form-control", id=form.desk_lap_ram_slots.id) }}
//     </div>
//     <div class="form-group col-md-4">
//         <label for="{{ form.desk_lap_hdmi_port.id }}">HDMI Port (Yes/No):</label>
//         {{ form.desk_lap_hdmi_port(class="form-control", id=form.desk_lap_hdmi_port.id) }}
//     </div>
// </div>
// <div class="form-row">
//     <div class="form-group col-md-4">
//         <label for="{{ form.desk_lap_display_size.id }}">Display Size (Inch):</label>
//         {{ form.desk_lap_display_size(class="form-control", id=form.desk_lap_display_size.id, placeholder="Enter Display Size") }}
//     </div>
//     <div class="form-group col-md-4">
//         <label for="{{ form.desk_lap_graphics_card_size.id }}">Graphics Card Size (GB):</label>
//         {{ form.desk_lap_graphics_card_size(class="form-control", id=form.desk_lap_graphics_card_size.id) }}
//     </div>
//     <div class="form-group col-md-4">
//         <label for="{{ form.desk_lap_graphics_card_version.id }}">Graphics Card Version:</label>
//         {{ form.desk_lap_graphics_card_version(class="form-control", id=form.desk_lap_graphics_card_version.id) }}
//     </div>
// </div>

                            
//                         `;

//                     } else if (deviceType === 'printer') {
//                         specificationsForm.innerHTML = `
                        
                        
                            
// <div class="form-row">
// <div class="form-group col-md-4">
//     <label for="{{ form.printer_type.id }}">Printer Type:</label>
//     {{ form.printer_type(class="form-control", id=form.printer_type.id, placeholder="Enter Printer Type") }}
// </div>
// <div class="form-group col-md-4">
//     <label for="{{ form.printing_type.id }}">Printing Type:</label>
//     {{ form.printing_type(class="form-control", id=form.printing_type.id) }}
// </div>
// <div class="form-group col-md-4">
//     <label for="{{ form.printer_connectivity.id }}">Connectivity:</label>
//     {{ form.printer_connectivity(class="form-control", id=form.printer_connectivity.id) }}
// </div>
// </div>
// <div class="form-row">
// <div class="form-group col-md-4">
//     <label for="{{ form.printer_toner.id }}">Printer Toner Name:</label>
//     {{ form.printer_toner(class="form-control", id=form.printer_toner.id, placeholder="Enter Printer Toner Name") }}
// </div>
// </div>


                
//                         `;
//             }else if (deviceType === 'HDD Specs') {
//                         specificationsForm.innerHTML = `
                            
                        
// <div class="form-row">
//     <div class="form-group col-md-4">
//         <label for="{{ form.hdd_size.id }}">HDD Size (GB):</label>
//         {{ form.hdd_size(class="form-control", id=form.hdd_size.id, placeholder="Enter HDD Size") }}
//     </div>
//     <div class="form-group col-md-4">
//         <label for="{{ form.hdd_type.id }}">HDD Type:</label>
//         {{ form.hdd_type(class="form-control", id=form.hdd_type.id, placeholder="Enter HDD Type") }}
//     </div>
//     <div class="form-group col-md-4">
//         <label for="{{ form.connectivity.id }}">Connectivity:</label>
//         {{ form.connectivity(class="form-control", id=form.connectivity.id) }}
//     </div>
// </div>

                            
//                         `;
//                     } else if (deviceType === 'tabletMobile') {
//                         specificationsForm.innerHTML = `
                    
// <div class="form-row">
// <div class="form-group col-md-4">
//     <label for="{{ form.tab_os.id }}">Operating System:</label>
//     {{ form.tab_os(class="form-control", id=form.tab_os.id, placeholder="Enter Operating System") }}
// </div>
// <div class="form-group col-md-4">
//     <label for="{{ form.tab_storage.id }}">Storage (ROM) GB:</label>
//     {{ form.tab_storage(class="form-control", id=form.tab_storage.id, placeholder="Enter Storage (ROM) GB") }}
// </div>
// <div class="form-group col-md-4">
//     <label for="{{ form.tab_ram_size.id }}">RAM Size (GB):</label>
//     {{ form.tab_ram_size(class="form-control", id=form.tab_ram_size.id, placeholder="Enter RAM Size") }}
// </div>
// </div>
// <div class="form-row">
// <div class="form-group col-md-4">
//     <label for="{{ form.tab_display_size.id }}">Display Size (Inch):</label>
//     {{ form.tab_display_size(class="form-control", id=form.tab_display_size.id, placeholder="Enter Display Size") }}
// </div>
// <div class="form-group col-md-4">
//     <label for="{{ form.tab_stylus.id }}">Stylus (Yes/No):</label>
//     {{ form.tab_stylus(class="form-control", id=form.tab_stylus.id) }}
// </div>
// <div class="form-group col-md-4">
//     <label for="{{ form.tab_connectivity.id }}">Connectivity:</label>
//     {{ form.tab_connectivity(class="form-control", id=form.tab_connectivity.id) }}
// </div>
// </div>

        
                            
//                         `;
//                     } else if (deviceType === 'monitor') {
//                         specificationsForm.innerHTML = `
                            
                        
                            
// <div class="form-row">
//     <div class="form-group col-md-4">
//         <label for="{{ form.display_size.id }}">Display Size (Inch):</label>
//         {{ form.display_size(class="form-control", id=form.display_size.id, placeholder="Enter Display Size") }}
//     </div>
//     <div class="form-group col-md-4">
//         <label for="{{ form.hdmi_port.id }}">HDMI Port (Yes/No):</label>
//         {{ form.hdmi_port(class="form-control", id=form.hdmi_port.id) }}
//     </div>
//     <div class="form-group col-md-4">
//         <label for="{{ form.speaker.id }}">Speaker (Yes/No):</label>
//         {{ form.speaker(class="form-control", id=form.speaker.id) }}
//     </div>
// </div>
                            
//                         `;
//                     } else if (deviceType === 'ups') {
//                         specificationsForm.innerHTML = `
                            
                
//                                 <!-- Add UPS fields here -->
// <div class="form-row">
// <div class="container mt-4">
//     <label for="{{ form.ups_capacity.id }}">UPS Capacity (Kva):</label>
//     {{ form.ups_capacity(class="form-control", id=form.ups_capacity.id, placeholder="Enter UPS Capacity (Kva)") }}
// </div>
// <div class="container mt-4">
//     <label for="{{ form.amc.id }}">AMC (Yes/No):</label>
//     {{ form.amc(class="form-control", id=form.amc.id) }}
// </div>
// </div>
// <div class="form-row">
// <div class="container mt-4">
    
//     <label for="{{ form.ups_start_date.id }}">UPS Start Date:</label>
//     {{ form.ups_start_date(class="form-control", id=form.ups_start_date.id, ) }}
    
   
// </div>
// <div class="container mt-4">
   
//     <label for="{{ form.ups_end_date.id }}">UPS End Date:</label>
//     {{ form.ups_end_date(class="form-control", id=form.ups_end_date.id, ) }}
        
// </div>
// </div>
                        
//                         `;

//                     }
                    
//                 }

//                 var coll = document.getElementsByClassName("collapsible");
//                 var i;
        
//                 for (i = 0; i < coll.length; i++) {
//                 coll[i].addEventListener("click", function() {
//                     this.classList.toggle("active");
//                     var content = this.nextElementSibling;
//                     if (content.style.display === "block") {
//                     content.style.display = "none";
//                     } else {
//                     content.style.display = "block";
//                     }
//                 });
//                 }
