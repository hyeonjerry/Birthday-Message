from django.shortcuts import render, redirect

from forms import MessageForm


def leave_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('web:leave_message')
    else:
        form = MessageForm()
    context = {'form': form}
    return render(request, 'leave_message.html', context)
