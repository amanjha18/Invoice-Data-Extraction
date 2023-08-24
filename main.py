'''\s+: Matches one or more spaces. This is used to account for potential variations in spacing.
    \.: Matches a literal dot character. In some cases, the label might have a dot, so we need to escape it using \.
    (.*): This is a capturing group that matches and captures everything after the label. 
    .* matches any character (except newline) zero or more times.'''


import pytesseract
import re
''' 
The line from PIL import Image is used to import the Image class from the Pillow (PIL) library. Pillow is a popular Python 
Imaging Library that provides support for opening, manipulating, and saving various image file formats.
'''
from PIL import Image 

# Function to extract text from an image using Tesseract OCR
def extract_text_from_image(image_path):
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text
    except Exception as e:
        print("Error:", e)
        return ""

# Function to extract invoice fields using regular expressions
def extract_invoice_fields(text, patterns):
    extracted_fields = {}
    for field, pattern in patterns.items():
        # Using regular expression to find the pattern in the OCR'd text
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            # Extract the captured group from the regular expression match
            extracted_fields[field] = match.group(1).strip()
    return extracted_fields

# Define patterns for each field in the invoices

# Patterns for invoice sample 1
invoice1_patterns = {
    "Bill To": r"Bill\s+To:\s+(.*)",                    # Extracts the 'Bill To' information
    "Shipping To": r"Shipping\s+To:\s+(.*)",            # Extracts the 'Shipping To' information
    "Invoice Date": r"Invoice\s+Date:\s+(.*)",          # Extracts the 'Invoice Date' information
    "Payment Terms": r"Payment\s+Terms:\s+(.*)",        # Extracts the 'Payment Terms' information
    "Name of Rep.": r"Name\s+of\s+Rep.:\s+(.*)"         # Extracts the 'Name of Rep.' information
}

# Patterns for invoice sample 2
invoice2_patterns = {
    "Invoice No": r"Invoice\s+No\.:\s+(.*)",            # Extracts the 'Invoice No' information
    "Invoice Date": r"Invoice\s+Date:\s+(.*)",          # Extracts the 'Invoice Date' information
    "Payment Terms": r"Payment\s+Terms:\s+(.*)",        # Extracts the 'Payment Terms' information
    "Due Date": r"Due\s+Date:\s+(.*)",                  # Extracts the 'Due Date' information
    "Customer Number": r"Customer\s+Number:\s+(.*)"    # Extracts the 'Customer Number' information
}

# Process invoice 1
invoice1_text = extract_text_from_image("inv-sample-1.jpg")
print(invoice1_text)
invoice1_fields = extract_invoice_fields(invoice1_text, invoice1_patterns)
print("Invoice 1 Fields:", invoice1_fields)

# Process invoice 2
invoice2_text = extract_text_from_image("inv-sample-2.jpg")
invoice2_fields = extract_invoice_fields(invoice2_text, invoice2_patterns)
print("Invoice 2 Fields:", invoice2_fields)
