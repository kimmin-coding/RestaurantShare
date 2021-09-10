from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Create your views here.
def sendEmail(request):
    checked_res_list = request.POST.getlist('checks')
    inputReceiver=request.POST['inputReceiver']
    inputTitle=request.POST['inputTitle']
    inputContent=request.POST['inputContent']
    
    
    mail_html="hello"
    
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login("plantrevol2@gmail.com","vtoqinijxmnliyxf")
    
    msg=MIMEMultipart('alternative')
    msg['Subject']=inputTitle
    msg['from']="aaa@gmail.com"
    msg['To']=inputReceiver
    mail_html=MIMEText(mail_html,'html')
    msg.attach(mail_html)
    server.sendmail(msg['from'], msg['To'].split(','),msg.as_string())
    server.quit()
    
    #print(checked_res_list,"/",inputReceiver,"/",inputTitle,"/",inputContent)
    
    return HttpResponseRedirect(reverse('index'))

#"vtoqinijxmnliyxf"