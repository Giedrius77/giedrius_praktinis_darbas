from django.shortcuts import render
from .models import WinLossCount 
from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _
import random

def play_game(request):
    if request.method == 'POST':
        moves = [_('rock'), _('paper'), _('scissors')]
        user_move = request.POST.get('move')
        computer_move = random.choice(moves)

        win_loss_count = WinLossCount.objects.first()
        if not win_loss_count:
            win_loss_count = WinLossCount.objects.create()

        if user_move == computer_move:
            result = _("it's a tie!").capitalize    
        elif (user_move == _('rock') and computer_move == _('scissors')) or (user_move == _('paper') and computer_move == _('rock')) or (user_move == _('scissors') and computer_move == _('paper')):
            result = _("you win!").capitalize
            win_loss_count.win_count += 1
        else:
            result = _("computer wins!").capitalize
            win_loss_count.loss_count += 1
        win_loss_count.save()
        return render(request, 'rpsgame/play_game.html', {'result': result, 'user_move': user_move, 'computer_move': computer_move, 'win_count': win_loss_count.win_count, 'loss_count': win_loss_count.loss_count})
    
    win_loss_count = WinLossCount.objects.first()
    if win_loss_count:
        win_loss_count.win_count = 0
        win_loss_count.loss_count = 0
        win_loss_count.save()

    return render(request, 'rpsgame/play_game.html')  
