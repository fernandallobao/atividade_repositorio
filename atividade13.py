# 13. Crie um programa que automatize uma busca na Internet por videoaulas sobre Python no Youtube.
# importa bibliotecas
import pyautogui as auto
import time

# tempo que cada comando demora para executar
auto.PAUSE = 2

# instruções
auto.press('win')
auto.write('chrome')
auto.press('enter')

# espera 10 segundos para abrir o vscode e continuar com os comandos
time.sleep(1)

# continua as instruções=
auto.write('www.youtube.com')
auto.press('enter')

auto.press('tab')
auto.press('tab')
auto.press('tab')
auto.press('tab')

auto.write('videoaulas sobre Python')
auto.press('enter')

