import smtplib
import functools
import requests
import os


# def send_info_email(user, acc_pass, mail_from, mail_to, mail_subject, mail_body):
#     message = """From: {}
# Subject: {}
# {}
# """.format(mail_from, mail_subject, mail_body)
#
#     try:
#         server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
#         server.ehlo()  # you need to say hello.
#         server.login(user, acc_pass)
#         server.sendmail(user, mail_to, message)
#         server.close()
#         print('Mail sent.')
#         return True
#
#     except:
#         print('Error sending mail')
#         return False
#
#
# with open(r'/home/darek/Projects/send', 'r') as file:
#     mail_to = [addresses[:-1] for addresses in file.readlines()]
# with open(r'/home/darek/Projects/send_1', 'r') as file:
#     acc_pass = file.readline()
#
# mail_from = 'Your automation system'
# mail_subject = "Processing finished successfully"
# mail_body = '''Hello!!!
# This mail confirms that processing has finished without problems.
#
# Have a nice day!!!'''
# user = mail_to[0]
#
# send_info_email_gmail = functools.partial(send_info_email, user, acc_pass,
#                                           mail_subject="Execution alert")
#
# send_info_email_gmail(mail_from=mail_from, mail_to=mail_to, mail_body=mail_body)
#
# # send_info_email(user, acc_pass, mail_from, mail_to, mail_subject, mail_body)

#  Lab


def save_url_file(url, dir_, file, msg):
    print(msg.format(file))

    r = requests.get(url, stream=True)
    file_path = os.path.join(dir_, file)

    with open(file_path, "wb") as f:
        f.write(r.content)


# msg = "Please wait - the file {} will be downloaded"

url = 'http://mobilo24.eu/spis'
# dir_ = '/tmp/'
file = 'spis.html'
# save_url_file(url, dir_, file, msg)


save_url_to_dir = functools.partial(save_url_file, dir_='/tmp/', msg="Please wait: {}")
save_url_to_dir(url=url, file=file)


url = 'https://www.mobilo24.eu/wp-content/uploads/2015/11/Mobilo_logo_kolko_512-565b1626v1_site_icon.png'
# dir_ = '/tmp/'
file = 'logo.png'
# save_url_file(url, dir_, file, msg)


save_url_to_dir(url=url, file=file)
