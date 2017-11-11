from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from rivers.models import River
from locations.models import State

from river_subs.models import RiverSubscription
from river_subs.forms import AddSubForm
from django.core.mail import EmailMessage
from django.contrib.auth.models import User
from django.template import Context
from django.template.loader import get_template


# Create your views here.


@login_required
def UserAdmin(request):
    subscriptions = RiverSubscription.objects.filter(user=request.user)
    form = AddSubForm()
    if request.method == 'POST':
        if request.POST.get('deleteForm', None) is not None:
            river = River.objects.get(name=request.POST['riverName'])
            river_sub = RiverSubscription.objects.filter(river=river.id, user=request.user)
            river_sub.delete()
            for sub in subscriptions:
                if(sub.river.current_level >= sub.trigger_level):
                    sub.addedClass = 'rivers-running'
                    sub.icon = 'fa-thumbs-o-up'
                else:
                    sub.addedClass = 'rivers-low'
                    sub.icon = 'fa-thumbs-o-down'
            states = State.objects.all()
            return render(request, 'river_subs/user_admin.html', {'subscriptions': subscriptions, 'form': form, 'states':states})
        trigger = request.POST.get('trigger_level', None)
        if trigger is not None:
            river = River.objects.get(name=request.POST['riverName'])
            river_sub = RiverSubscription.objects.filter(river=river.id, user=request.user)
            if river_sub is None:
                print('couldnt find the river subscription')
                message = 'Sorry, something went wrong...'
                return render(request, 'river_subs/user_admin.html', {'subscriptions': subscriptions, 'form': form, 'message': message})
            river_sub.update()
            for sub in river_sub:
                sub.trigger_level = request.POST['trigger_level']
                sub.save()
            for sub in subscriptions:
                if(sub.river.current_level >= sub.trigger_level):
                    sub.addedClass = 'rivers-running'
                    sub.icon = 'fa-thumbs-o-up'
                else:
                    sub.addedClass = 'rivers-low'
                    sub.icon = 'fa-thumbs-o-down'
            return render(request, 'river_subs/user_admin.html', {'subscriptions': subscriptions, 'form': form})
        else:
            print('delete!!!!')
            return render(request, 'river_subs/user_admin.html', {'subscriptions': subscriptions, 'form': form})
    for sub in subscriptions:
        if(sub.river.current_level >= sub.trigger_level):
            sub.addedClass = 'rivers-running'
            sub.icon = 'fa-thumbs-o-up'
        else:
            sub.addedClass = 'rivers-low'
            sub.icon = 'fa-thumbs-o-down'
    states = State.objects.all()
    return render(request, 'river_subs/user_admin.html',
    {'subscriptions': subscriptions, 'form': form, 'states':states})


@login_required
def RiverSubscribe(request, state_abrv, pk):
    form = AddSubForm()
    river = get_object_or_404(River, pk=pk)
    if request.method == 'POST':
        sub = RiverSubscription()
        sub.river = river
        sub.user = request.user
        sub.trigger_level = request.POST['trigger_level']
        existing_subs = RiverSubscription.objects.filter(user=sub.user, river=sub.river)
        if existing_subs:
            print(existing_subs)
            message = 'You are already subscribed to this river!'
            return render(request, 'river_subs/subscribe.html', {'river': river, 'form': form, 'message': message})
        sub.save()
        return redirect(reverse('user_admin'))

    return render(request, 'river_subs/subscribe.html', {'river': river, 'form': form})



def SendEmail(request):
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

    return HttpResponse('email sent!')






    for u in allUsers:
        print('waaaaaaa')
        my_list = []
        #print(u)
        my_subs = RiverSubscription.objects.filter(user=u)
        for sub in my_subs:
            if(sub.trigger_level <= sub.river.current_level):
                my_list.append(sub)
                #print('email sent to {}! the River: {} is running. the current level is: {} and your trigger is {}'.format(u, sub.river, sub.river.current_level, sub.trigger_level))
        if(len(my_list) != 0):
            ctx = {
            'subs': my_list,
            'user': u
            }
            to = [u.email]
            message = get_template('river_subs/email_template.html').render(ctx)
            msg = EmailMessage(subject, message, to=to, from_email=from_email)
            msg.content_subtype = 'html'
            # msg.send()


    # for user in users:
    #     my_list = []
    #     print(user)
    #     my_subs = RiverSubscription.objects.filter(user=user)
    #     for sub in my_subs:
    #         if(sub.trigger_level <= sub.river.current_level):
    #             my_list.append(sub)
                #print('email sent to {}! the River: {} is running. the current level is: {} and your trigger is {}'.format(u, sub.river, sub.river.current_level, sub.trigger_level))
