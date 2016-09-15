import base64
import httplib2
from email.mime.text import MIMEText
from apiclient.discovery import build
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import run

def send_email():
    flow = flow_from_clientsecrets("client-secret.json", scope="https://mail.google.com")
    http = httplib2.Http()
    storage = Storage("gmail.storage")
    credentials = storage.get()
    if credentials is None or credentials.invalid:
        credentials = run(flow, storage, http=http)
    http = credentials.authorize(http)
    gmail_service = build('gmail', 'v1', http=http)
    message = MIMEText("BODY")
    message['to'] = "@gmail.com"
    message['from'] = "@gmail.com"
    message['subject'] = ""
    body = {'raw': base64.b64encode(message.as_string())}
    message = (gmail_service.users().messages().send(userId="me", body=body).execute())
