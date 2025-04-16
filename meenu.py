from PPlay.window import *
from PPlay.gameimage import *

janela = Window(800, 600)
janela.set_title("menu")
tela = GameImage("menu_principal.jpeg")
tela_dificuldade = GameImage("menu_dificuldade.jpeg")
mouse = Window.get_mouse()
teclado = Window.get_keyboard()

while True:
    if mouse.is_over_area([281, 220], [519, 270]):
        if mouse.is_button_pressed(1):
            tela_preta = Window(800, 600)
            tela_preta.set_background_color((0, 0, 0))
            while True:
                tela_preta.update()
                if teclado.key_pressed("ESC"):
                    break

    if mouse.is_over_area([281, 300], [519, 350]):
        if mouse.is_button_pressed(1):
            menu_dificuldade = Window(800, 600)
            while True:
                tela_dificuldade.draw()
                menu_dificuldade.update()
                if teclado.key_pressed("ESC"):
                    break

    if mouse.is_over_area([281, 380], [519, 430]):
        if mouse.is_button_pressed(1):
            janela.close()

    tela.draw()
    janela.update()