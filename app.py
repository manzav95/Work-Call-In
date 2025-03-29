from flask import Flask, render_template, request, flash
from flask_mail import Mail, Message
import os

from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Email Configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'zavalamanuel95@gmail.com'
app.config['MAIL_PASSWORD'] = 'zahr pbja ayyq qymo'
mail = Mail(app)

# Editable Employee Names
EMPLOYEE_NAMES = ["Ahmad Abuhmaid", "Cristoval Aguirre", "Wyatt Ashton", "Miguel Bac", "Cole Bartolo", "Roberto Guzman", "Mingrui Chen", "Chris Francis", "David Fuller", "Alex Gutierrez", "Eric Hayes", "Julian Hitchcock", "Thomas Jackson", "Dilong Liu", "Mustafa Mohammadi", "Isaac Nuñez", "Evan Pung", "Antonio Reyes", "Gustavo Sanchez", "Jimena Sandoval", "Desmond Tofoya", "Anthony Torres", "Alyssa Trent", "Manuel Zavala"]

@app.route('/')
def home():
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Format timestamp
    return render_template('index.html', employees=EMPLOYEE_NAMES, now=current_time)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('employee_name')
    reason = request.form.get('reason')
    additional_info = request.form.get('additional_info')
    date = request.form.get('date')  # New field
    timestamp = request.form.get('timestamp')

    if not name or not reason or not date:
        flash("Please fill out all required fields.", "error")
        return render_template('index.html', employees=EMPLOYEE_NAMES)

    # Send Email
    subject = f"Work Call-In Notification - {name}"
    body = f"""
    Employee: {name}
    Date of Call-In: {date}
    Reason: {reason}
    Additional Info: {additional_info}
    Timestamp: {timestamp}
    """
    try:
        msg = Message(subject, sender=app.config['MAIL_USERNAME'], recipients=['manuel@ronbow.com, ahmad@ronbow.com'])
        msg.body = body
        mail.send(msg)
        flash("Form submitted successfully. Email sent.", "success")
    except Exception as e:
        flash(f"Error sending email: {e}", "error")

    return render_template('index.html', employees=EMPLOYEE_NAMES)

if __name__ == '__main__':
    app.run(debug=True)
 