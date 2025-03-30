import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = "otoojoe230@gmail.com"
password = "qgkvdymmfzchkuui"
receiver = "otoojoe230@gmail.com"
message = """"\
Subject: Appreciation!
Hi my world!,
Bebe girl, I would like to tell you that, I really love you.
I am grateful to God for having you in my life.
With you my life is perfect. 
You always gave me joy and peace.
Thank you for loving me babe girl.

Best regard,
Your love and husband
"""
my_context = ssl.create_default_context()
with smtplib.SMTP_SSL(host, port, context=my_context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)
