import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# Utilize an email account as multiple 'online' stacks distinguished by stack_id
class EmailStack:
    def __init__(self,
                 account: str,  # NOTE: these have to be the SAME to access the SAME stack
                 password: str,
                 stack_id: int = 0,
                 ):
        self.account = account
        self.password = password
        self.stack_id = stack_id
        self.mail_url = 'smtp.' + self.account.split('@')[-1]
        
        try:
            self.server = smtplib.SMTP(self.mail_url)
            self.server.starttls()
            self.server.login(self.account, self.password)
        except:
            raise RuntimeError('Email login failed')
        
    def push(self, stack_id: int, msg: str):
        pass

    def __send__(self, subject: str, body: str):
        message = MIMEMultipart()
        message['From'] = self.account
        message['To'] = self.account
        message['Subject'] = subject
        
        message.attach(MIMEText(body, 'plain'))
        text = message.as_string()
        try:
            self.server.sendmail(self.account, self.account, text)
        except:
            raise RuntimeError('Email account has become unaccessible')

    def __receive__(self):
        pass


if __name__ == '__main__':
    account = 'ipsync2@outlook.com'
    password = 'thisisawesome2'
    stack_id = 0
    
    estack = EmailStack(account, password, stack_id)
