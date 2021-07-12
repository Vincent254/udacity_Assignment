
# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv

message = Mail(
    from_email='info@aktech.co.ke',
    to_emails='vmwagiru@gmail.com',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')
try:
    print('=====================')
    load_dotenv('sendgrid.env')
    print(os.environ.get('SENDGRID_API_KEY'))
    print('=====================')
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    # sg = SendGridAPIClient(        "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")
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.__dict__)
