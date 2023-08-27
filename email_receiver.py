import email
import imaplib

class Receiver:
    def authenticate():
        host = 'imap.gmail.com'
        username = '-email_address-'
        password = '-email-password-'
        
        #password must be generated google app password
        
        mail = imaplib.IMAP4_SSL(host)
        mail.login(username, password)
        return mail

    def get_inbox():
        mail = Receiver.authenticate()
        typ, data = mail.select('INBOX')
        num_msgs = int(data[0])
        _, search_data = mail.search(None, 'UNSEEN')  #type ALL to print all inbox mail or UNSEEN
        my_message = []
        for num in search_data[0].split():
            email_data = {}
            email_data["request_num"]=num.decode()
            _, data = mail.fetch(num, '(RFC822)')
            #print(data[0])
            _, b = data[0]
            email_message = email.message_from_bytes(b)
            for header in ['subject', 'to', 'from', 'date']:
                #print("{}: {}".format(header, email_message[header]))
                email_data[header] = email_message[header]
            for part in email_message.walk():
                if part.get_content_type() == "text/plain":
                    body = part.get_payload(decode=True)
                    #print('body:',body.decode('latin-1'))  #print body
                    email_data['body'] = body.decode('latin-1')      #encoding changes to allow microsoft messages
                elif part.get_content_type() == "text/html":
                    html_body = part.get_payload(decode=True)
                    email_data['html_body'] = html_body.decode('latin-1')
            my_message.append(email_data)
        return my_message
        
    
if __name__ == "__main__":
    data = get_inbox()
    for email in data:
        print("Email request number",email['request_num'])
        print(email['date'])
        print(email['body'])


