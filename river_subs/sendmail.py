from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import EmailMultiAlternatives
from river_subs.models import RiverSubscription
from django.contrib.auth.models import User

from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import get_template

def send_email():
    subject = "Your Update from RiverWatchr"
    from_email = 'aaronwright91@gmail.com'

    allUsers = User.objects.all()
    for us in allUsers:
        my_list = []
        #print(us)
        my_subs = RiverSubscription.objects.filter(user=us)
        for sub in my_subs:
            if(sub.trigger_level <= sub.river.current_level):
                my_list.append(sub)
                #print('email sent to {}! the River: {} is running. the current level is: {} and your trigger is {}'.format(us, sub.river, sub.river.current_level, sub.trigger_level))
        if(len(my_list) != 0):
            ctx = {
            'subs': my_list,
            'user': us
            }
            print(us)
            to = [us.email]
            message = get_template('river_subs/email_template.html').render(ctx)
            msg = EmailMessage(subject, message, to=to, from_email=from_email)
            msg.content_subtype = 'html'
            msg.send()
