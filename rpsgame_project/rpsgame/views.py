from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _
import random

def play_game(request):
    if request.method == 'POST':
        moves = [_('rock'), _('paper'), _('scissors')]
        user_move = request.POST.get('move')
        computer_move = random.choice(moves)

        if user_move == computer_move:
            result = _("it's a tie!").capitalize    
        elif (user_move == _('rock') and computer_move == _('scissors')) or (user_move == _('paper') and computer_move == _('rock')) or (user_move == _('scissors') and computer_move == _('paper')):
            result = _("you win!").capitalize
        else:
            result = _("computer wins!").capitalize

        return render(request, 'rpsgame/play_game.html', {'result': result, 'user_move': user_move, 'computer_move': computer_move})

    return render(request, 'rpsgame/play_game.html') 
