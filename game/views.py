
from django.shortcuts import render, redirect
import random

def index(request):
    if 'number' not in request.session:
        request.session['number'] = random.randint(1, 100)
    context = {'message': ''}
    return render(request, 'game/index.html', context)

def guess_number(request):
    if request.method == 'POST':
        user_guess = int(request.POST.get('guess'))
        actual_number = request.session.get('number')

        if user_guess < actual_number:
            message = 'Too low!'
        elif user_guess > actual_number:
            message = 'Too high!'
        else:
            message = f'Correct! The number was {actual_number}'
            request.session.pop('number')  # reset game

        return render(request, 'game/index.html', {'message': message})

    return redirect('index')
