from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import View, ListView, DetailView
from . import models
from locations.models import State
from rivers.models import River
from river_subs.forms import AddSubForm
from river_subs.models import RiverSubscription
from rivers.update import runUpdate

from river_subs.sendmail import send_email

# Create your views here.

# class RiverListView(ListView):
#     model = models.River
#     template_name = "rivers/river_index.html"



def state_index(request, state_abrv):
    found_state = get_object_or_404(State, abbreviation=state_abrv)
    form = AddSubForm()
    #rivers = River.objects.filter(state = found_state)
    rivers = found_state.river.all().order_by('name')
    # runUpdate()
    if request.method == 'POST':
        if request.user.is_authenticated:

            level = request.POST['trigger_level']
            name = request.POST['riverName']
            foundRiver = River.objects.filter(name=request.POST['riverName']).first()
            if foundRiver:
                sub = RiverSubscription()
                sub.river = foundRiver
                sub.user = request.user
                sub.trigger_level = request.POST['trigger_level']
                existing_subs = RiverSubscription.objects.filter(user=sub.user, river=sub.river)
                if existing_subs:
                    print(existing_subs)
                    message = 'You are already subscribed to this river!'
                    messageClass = 'alert-danger'
                    return render(request, 'rivers/river_index.html', {'rivers': rivers, 'form': form, 'message': message, 'messageClass': messageClass})
                sub.save()
                message = 'Thanks for subscribing to {}!'.format(sub.river.name)
                messageClass = 'alert-success'
                return render(request, 'rivers/river_index.html', {'rivers': rivers, 'form': form, 'message': message, 'messageClass': messageClass})
            else:
                message: 'something went wrong...'
                messageClass = 'alert-danger'
                return render(request, 'rivers/river_index.html', {'rivers': rivers, 'form': form, 'message': message,  'messageClass': messageClass})
        else:
            message = 'You must be logged in to subscribe. Please login and try again.'
            messageClass = 'alert-danger'
            return render(request, 'rivers/river_index.html', {'state': found_state, 'rivers': rivers, 'form': form,'message': message,  'messageClass': messageClass})
    states = State.objects.all()
    return render(request, 'rivers/river_index.html', {'state': found_state, 'rivers': rivers, 'form': form, 'states': states})



def RiverDetail(request, state_abrv, pk):
    form = AddSubForm()
    river = get_object_or_404(River, pk=pk)
    if river is not None:
        if state_abrv == river.state.abbreviation:
            if request.method == 'POST':
                if request.user.is_authenticated:
                    level = request.POST['trigger_level']
                    sub = RiverSubscription()
                    sub.river = river
                    sub.user = request.user
                    sub.trigger_level = level
                    existing_subs = RiverSubscription.objects.filter(user=sub.user, river=sub.river)
                    if existing_subs:
                        print(existing_subs)
                        message = 'You are already subscribed to this river!'
                        return render(request, 'rivers/river_detail.html', {'river': river, 'form': form, 'message': message})
                    sub.save()
                    return redirect(reverse('user_admin'))
                else:
                    message = 'You must be logged in to subscribe. Please login and try again.'
                    return render(request, 'rivers/river_detail.html', {'river': river, 'form': form,'message': message})
            return render(request, 'rivers/river_detail.html', {'river': river, 'form': form})
        else:
            raise Http404
    else:
        raise Http404
