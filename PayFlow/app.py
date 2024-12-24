# app.py - Flask application to manage routes and logic
# PURPOSE - This file contains the main logic of the Flask application, including routes for logging in, viewing the dashboard, and generating paychecks

from flask import Flask, render_template, request, redirect, url_for, send_file
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from io import BytesIO
from datetime import datetime

app = Flask(__name__)

# Route for the home page (index)
@app.route('/')
def index():
    return render_template('index.html')

# Route for login (not fully implemented here for brevity)
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    # Add authentication logic here
    return redirect(url_for('dashboard', username=username))

# Route for the dashboard
@app.route('/dashboard/<username>')
def dashboard(username):
    return render_template('dashboard.html', username=username)

# Route for viewing paycheck details
@app.route('/paycheck_details/<username>', methods=['GET'])
def paycheck_details(username):
    # Define payroll data for different roles
    payroll_data = {
        'admin': {
            'salary': 5000,
            'tax_deductions': 1000,
            'net_pay': 4000,
            'role': 'Admin'
        },
        'employee': {
            'salary': 3000,
            'tax_deductions': 600,
            'net_pay': 2400,
            'role': 'Employee'
        },
        'manager': {
            'salary': 7000,
            'tax_deductions': 1500,
            'net_pay': 5500,
            'role': 'Manager'
        }
    }

    # Ensure username is lowercase to match data keys
    username_lower = username.lower()
    payroll = payroll_data.get(username_lower)  # Fetch payroll data for this user

    if payroll:
        # Pass the payroll data and username to the template
        return render_template('paycheck.html', username=username, payroll=payroll)
    else:
        return "Payroll data not found", 404

# Route for generating paycheck PDF
@app.route('/generate_paycheck/<username>', methods=['GET'])
def generate_paycheck(username):
    # Define payroll data for different roles
    payroll_data = {
        'admin': {
            'salary': 5000,
            'tax_deductions': 1000,
            'net_pay': 4000,
            'role': 'Admin'
        },
        'employee': {
            'salary': 3000,
            'tax_deductions': 600,
            'net_pay': 2400,
            'role': 'Employee'
        },
        'manager': {
            'salary': 7000,
            'tax_deductions': 1500,
            'net_pay': 5500,
            'role': 'Manager'
        }
    }

    # Ensure username is lowercase to match data keys
    username_lower = username.lower()
    payroll = payroll_data.get(username_lower)  # Fetch payroll data for this user

    if payroll:
        # Generate the PDF paycheck and send it to the client
        buffer = BytesIO()
        c = canvas.Canvas(buffer, pagesize=letter)
        width, height = letter  # Dimensions of letter size paper (612, 792)
        
        # Center the company name
        company_name = "NebulaWorks"
        c.setFont("Times-Bold", 16)
        text_width = c.stringWidth(company_name, "Times-Bold", 16)
        c.drawString((width - text_width) / 2, 750, company_name)
        
        # Paycheck Statement
        statement_text = "Paycheck Statement"
        c.setFont("Times-Roman", 12)
        statement_width = c.stringWidth(statement_text, "Times-Roman", 12)
        c.drawString((width - statement_width) / 2, 730, statement_text)
        
        # Paycheck Date (placed below "Paycheck Statement", aligned to the right)
        date_text = f"Date: {datetime.now().strftime('%Y-%m-%d')}"
        date_width = c.stringWidth(date_text, "Times-Roman", 12)
        c.drawString(width - date_width - 20, 720, date_text)  # Adjusted Y-coordinate for the date under the statement

        c.setStrokeColor(colors.grey)
        c.setLineWidth(1)
        c.line(50, 700, 550, 700)  # Adjusted position of the line separating sections

        # Employee Information Header (adjusted position)
        employee_info = "Employee Information"
        c.setFillColor(colors.lightblue)
        c.rect(50, 680, 500, 30, fill=1)
        c.setFillColor(colors.black)
        c.setFont("Times-Bold", 14)
        employee_info_width = c.stringWidth(employee_info, "Times-Bold", 14)
        c.drawString((width - employee_info_width) / 2, 690, employee_info)
        
        # Employee Details (Name, Role)
        c.setFont("Times-Roman", 12)
        c.drawString(60, 665, f"Name: {username}")
        c.drawString(60, 650, f"Role: {payroll['role']}")
        
        # Payroll Summary Header (adjusted position)
        payroll_summary = "Payroll Summary"
        c.setFillColor(colors.lightgreen)
        c.rect(50, 600, 500, 30, fill=1)
        c.setFillColor(colors.black)
        c.setFont("Times-Bold", 14)
        payroll_summary_width = c.stringWidth(payroll_summary, "Times-Bold", 14)
        c.drawString((width - payroll_summary_width) / 2, 610, payroll_summary)
        
        # Payroll Summary Details (Salary, Tax Deductions, Net Pay)
        c.setFont("Times-Roman", 12)
        c.drawString(60, 580, f"Salary: ${payroll['salary']:,}")
        c.drawString(60, 560, f"Tax Deductions: ${payroll['tax_deductions']:,}")
        c.drawString(60, 540, f"Net Pay: ${payroll['net_pay']:,}")
        
        # Footer text (adjusted position)
        c.setFont("Times-Italic", 10)
        footer_text = "Generated by NebulaWorks Payroll System"
        footer_width = c.stringWidth(footer_text, "Helvetica-Oblique", 10)
        c.drawString((width - footer_width) / 2, 50, footer_text)
        
        contact_text = "Contact: support@nebulaworks.com | www.nebulaworks.com"
        contact_width = c.stringWidth(contact_text, "Times-Italic", 10)
        c.drawString((width - contact_width) / 2, 35, contact_text)
        
        c.save()
        buffer.seek(0)
        return send_file(buffer, as_attachment=True, download_name=f"Paycheck_{username}.pdf", mimetype="application/pdf")
    else:
        return "Payroll data not found", 404

if __name__ == '__main__':
    app.run(debug=True)


