import smtplib
import datetime
import time
from django.conf import settings
from email.mime.text import MIMEText
from email.header import Header


class EmailUtils():

    @staticmethod
    def send(destEmail, text):
        print('Start send email: ' + text)

        message = MIMEText(text+'   此邮件由系统自动发出,请勿回复!', 'plain', 'utf-8')
        message['Date'] = str(time.localtime())
        message['From'] = Header("openstack运维组", 'utf-8')
        message['To'] = Header(destEmail)
        nowdate = datetime.datetime.now().strftime("%Y-%m-%d")
        subject = '【'+nowdate + '】' + 'openstack服务器到期提醒'
        message['Subject'] = Header(subject, 'utf-8')

        try:
            smtpObj = smtplib.SMTP(settings.Email_host)
            smtpObj.login(settings.Email_user, settings.Email_pass)
            smtpObj.sendmail(settings.Email_sender, destEmail, message.as_string())
            print('邮件发送成功')
        except Exception:
            print('邮件发送失败')
        finally:
            smtpObj.close()
