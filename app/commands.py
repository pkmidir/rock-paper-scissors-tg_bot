import app.keyboards as kb

from aiogram.filters.command import Command
from aiogram.types import Message
from aiogram import F, Router
from app.rsp_game import play_game 
from app.rsp_game import get_computer_choice
router = Router()


player_choice = None


@router.message(Command('start'))
async def cmd_start(message: Message):
    await message.answer('Напишите /game чтобы начать игру')


@router.message(Command('game'))
async def game_cmd(message: Message):
    await message.answer('Выберите: ', reply_markup=kb.rsp)


@router.callback_query(F.data == 'rock')
async def rock_cmd(message: Message):
    global player_choice
    player_choice = 'камень' 
    computer_choice = get_computer_choice()  
    result_of_game = play_game(player_choice, computer_choice)  
    await message.message.answer(f'Вы выбрали: {player_choice}, Бот выбрал: {computer_choice}, Итог игры: {result_of_game}')
    
    
@router.callback_query(F.data == 'scissors')
async def scissors_cmd(message: Message):
    global player_choice
    player_choice = 'ножницы'
    computer_choice = get_computer_choice()  
    result_of_game = play_game(player_choice, computer_choice)  
    await message.message.answer(f'Вы выбрали: {player_choice}, Бот выбрал: {computer_choice}, Итог игры: {result_of_game}')
    
    
@router.callback_query(F.data == 'paper')
async def paper_cmd(message: Message):
    global player_choice
    player_choice = 'бумага' 
    computer_choice = get_computer_choice()  
    result_of_game = play_game(player_choice, computer_choice)  
    await message.message.answer(f'Вы выбрали: {player_choice}, Бот выбрал: {computer_choice}, Итог игры: {result_of_game}')
   
# сложна очень