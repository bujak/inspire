#!/usr/bin/env python3

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# me == my email address
# you == recipient's email address

def send_mail(email):
    me = "my@email.com"
    you = email

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Link"
    msg['From'] = me
    msg['To'] = you

    # Create the body of the message (a plain-text and an HTML version).
    text = "O kurwens ale super email z hackatonu"
    html = """\
    <html>
      <head></head>
      <body>
        <p>Joł<br>
           Co tam co tam?
        </p>
      </body>
    </html>
    """

    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)

    # # Send the message via local SMTP server.
    # server = smtplib.SMTP('smtp.gmail.com:587')
    # server.ehlo()
    #
    # server.starttls()
    # # sendmail function takes 3 arguments: sender's address, recipient's address
    # # and message to send - here it is sent as one string.
    # server.sendmail(me, you, msg.as_string())
    #


    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.ehlo()
    server.login("inspiredcodecooler@gmail.com", "hackatonjestspoko")
    server.sendmail(me, you, msg.as_string())
    server.quit()






