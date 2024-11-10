import json
import os

with open('quiz_data.json', 'r', encoding='utf-8') as file:
    quiz_data = json.load(file)


class Colors:
    WHITE = "\033[37m"
    GREEN = "\033[32m"
    RED = "\033[31m"
    CYAN = "\033[36m"
    YELLOW = "\033[33m"


def start():
    messages = {
        'welcome': f'{Colors.CYAN}------- Bem-vindo ao nosso Quiz de Matemática!',
        'start_question': f'{Colors.WHITE}~ Deseja iniciar o quiz? "{Colors.GREEN}sim{Colors.WHITE}, {Colors.RED}não{Colors.WHITE} ou {Colors.CYAN}sair{Colors.WHITE}".',
        'exit': f'{Colors.WHITE}~ Entendido! Até a próxima e obrigado por participar!',
        'invalid_response': f'{Colors.WHITE}~ Resposta inválida! Por favor, digite "{Colors.GREEN}sim{Colors.WHITE}, {Colors.RED}não{Colors.WHITE} ou {Colors.CYAN}sair{Colors.WHITE}.'
    }

    clear_screen()

    print(messages['welcome'])

    while True:
        start_or_not = input(f'{messages["start_question"]}\n{Colors.YELLOW}$ ').lower()

        if start_or_not in ['sim', 'si', 's', 'yes', 'ye', 'yep', 'y']:
            run_quiz(quiz_data)
            break
        elif start_or_not in ['não', 'nao', 'n', 'no', 'nope', 'nop']:
            print(messages['exit'])
            break
        elif start_or_not in ['sair', 'close', 'exit']:
            return
        else:
            print(messages['invalid_response'])


def clear_screen():
    system = os.name
    if system == 'nt':  # windows
        os.system('cls')
    else:
        os.system('clear')


def run_quiz(quiz_db):
    clear_screen()

    score = 0
    total_answers = len(quiz_db)

    messages = {
        'correct_answer': f'{Colors.GREEN}~ Você acertou!',
        'incorrect_answer': f'{Colors.RED}~ Você errou, {Colors.CYAN}resposta: {Colors.GREEN}',
        'final_message': f'{Colors.WHITE}~ Você acertou {Colors.GREEN}{score} {Colors.WHITE}de {Colors.CYAN}{total_answers}{Colors.WHITE} questões. até mais!'
    }

    for quiz_key, quiz_value in quiz_db.items():
        print(f'{Colors.CYAN}{quiz_key}: {Colors.WHITE}{quiz_value["question"]}')
        print(f'{Colors.WHITE}{quiz_value["answers"]}')
        user_answer = input(f'{Colors.WHITE}Resposta? {Colors.YELLOW}').lower()

        if user_answer == quiz_value['correct_answer']:
            print(f'{messages["correct_answer"]}\n')
            score += 1
        else:
            print(f'{messages["incorrect_answer"]} {quiz_value["correct_answer"]}\n')

    print(messages['final_message'])


start()
