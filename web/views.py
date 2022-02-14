from django.shortcuts import render, redirect

from forms import MessageForm
from web.models import Message


def _get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def leave_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            ip = _get_client_ip(request)
            form.ip_address = ip
            form.save()
            return redirect('web:message_list')
    else:
        form = MessageForm()
    context = {'form': form}
    return render(request, 'web/leave_message.html', context)


def message_list(request):
    messages = Message.objects.order_by('-create_date')
    context = {'messages': messages}
    return render(request, 'web/message_list.html', context)
