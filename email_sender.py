import smtplib, ssl
class Sender:
    def send_email(message):
        smtp_server = "smtp.gmail.com"
        port = 587
        sender_email="scripting4server@gmail.com"
        recipient_email="email_address"
        password = "email_password"
        
        #password must be generated google app password
        
        context = ssl.create_default_context()

        try:
            server = smtplib.SMTP(smtp_server, port)
            server.starttls(context=context)
            server.login(sender_email, password)
            server.sendmail(sender_email, recipient_email, message)
        except Exception as e:
            print(e)
        finally:
            server.quit()

if __name__ == "__main__":
    Sender.send_email("Add a new user Bill")
    Sender.send_email("I need more privilege on server management.")

