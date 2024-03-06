from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

# Configure Flask-Mail settings
app.config['MAIL_SERVER'] = 'smtp.mail.yahoo.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'ncnctest@yahoo.com'
app.config['MAIL_PASSWORD'] = 'nocoffeenocure123!!'  # Make sure to keep this secure, perhaps use environment variables
app.config['MAIL_DEFAULT_SENDER'] = 'ncnctest@yahoo.com'

mail = Mail(app)

@app.route('/send_email')
def send_email():
    print("Email has been sent")
    msg = Message('Hello from Flask-Mail', recipients=['rinor85@gmail.com'])
    try:
        # Create message object
       
        #msg.body = 'This is a test email sent from Flask-Mail'

        # Send the email
        #mail.send(msg)
        print("Email has been sent222")
        return 'Email sent successfully!'
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
