from django.shortcuts import render
from django.http import HttpResponse
import random

def play_game(request):
    if request.method == 'POST':
        moves = ['rock', 'paper', 'scissors']
        user_move = request.POST.get('move')
        computer_move = random.choice(moves)

        if user_move == computer_move:
            result = "It's a tie!"
        elif (user_move == 'rock' and computer_move == 'scissors') or (user_move == 'paper' and computer_move == 'rock') or (user_move == 'scissors' and computer_move == 'paper'):
            result = "You win!"
        else:
            result = "Computer wins!"

        return render(request, 'rpsgame/play_game.html', {'result': result, 'user_move': user_move, 'computer_move': computer_move})

    return render(request, 'rpsgame/play_game.html')

