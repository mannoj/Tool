def send_mail(msg):
    from datetime import datetime
    now_date = datetime.now()

    # don't send mail on the weekend
    if not now_date.isoweekday() in range(1, 6):
        return
    
    sender = 'k4w-mailbot@amazon.com'
    receivers = ['mtahil@amazon.com', 'mtahil@amazon.com']

    from email.mime.text import MIMEText
#     body = cat 'http://karena-1.desktop.amazon.com:8080/job/KCRv2_bb/cucumber-html-reports/EndPage.feature.html
    import urllib2

    url = 'http://karena-1.desktop.amazon.com:8080/job/KP_BVT_Official/cucumber-html-reports/'

    response = urllib2.urlopen(url)
    webContent = response.read().replace("<head>", "<head> <base href=""http://karena-1.desktop.amazon.com:8080/job/KP_BVT_Official/254/cucumber-html-reports/"" target=""_blank"">")
#     webContent = webcontent.replace("<head>", "<head> <base href=""http://www.w3schools.com/images/"" target=""_blank"">")
    
    import os
    print ("Build Number #")
    print os.environ['BUILD_NUMBER']    
 
    print webContent

    message = MIMEText(webContent, 'html')
    message['From'] = sender
#     message['To'] = receivers

    # http://stackoverflow.com/questions/15568583/php-mail-priority-types
    # set priority to low
    message['X-Priority'] = "5"

    message['Subject'] = "Bagels queue for " + now_date.strftime("%Y-%m-%d")
    try:
        import smtplib
        smtp_obj = smtplib.SMTP('smtp.amazon.com')
        smtp_obj.sendmail(sender, receivers, message.as_string())
#         smtp_obj.sendmail(sender, receivers, webContent)
        print "Successfully sent email"
    except Exception as err:
        print str(err)
        print "Error: unable to send email"


def get_html(url):
    import urllib2
    response = urllib2.urlopen(url)
    return response.read()


def bagels_mail():
 
    # format the message
    msg = ""

    print msg
    send_mail(msg)


bagels_mail()
