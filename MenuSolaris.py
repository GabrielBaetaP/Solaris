from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from jogo import jogando
from PPlay.sound import *

janela = Window(1000, 600)
janela.set_background_color("Black")
background_01 = GameImage("menu.png")
background_02 = GameImage("menu.png")
parte = GameImage("parte.png")
solaris = GameImage("solaris.png")

musicamenu = Sound("musicamenu.ogg")
musicamenu.set_volume(50)
musicamenu.stop()
musicamenu.loop = True
musicamenu.play()

# mouse #
mouse = Window.get_mouse()

background_01.x = 0
background_02.x = -background_02.width

background_roll_speed = 60

# botoes #
start = Sprite("botoes\\start.png")
exit = Sprite("botoes\\exit.png")

# botoes selecionados #
start_selec = Sprite("botoes_selec\\start_selecionado.png")
exit_selec = Sprite("botoes_selec\\exit_selecionado.png")

def scrolling(bg_bottom, bg_top, roll_speed, janela):
    bg_bottom.x += roll_speed * janela.delta_time()
    bg_top.x += roll_speed * janela.delta_time()

    if bg_top.x >= 0:
        bg_bottom.x = 0
        bg_top.x = -bg_top.width
    bg_bottom.draw()
    bg_top.draw()

while True:
    # fundo #
    scrolling(background_01, background_02, background_roll_speed, janela)
    parte.draw()
    solaris.draw()

    # botoes #
    start.draw()
    exit.draw()

    if mouse.is_over_area([110, 250], [370, 300]):
        start = start_selec
        if mouse.is_button_pressed(1):
            musicamenu.stop()
            musicafundo = Sound("musicafundo.ogg")
            musicafundo.set_volume(25)
            musicafundo.stop()
            musicafundo.loop = True
            musicamenu.play()
            jogando()
    else:
        start = Sprite("botoes\\start.png")

    if mouse.is_over_area([150, 340], [320, 385]):  # Nova posição do botão "exit"
        exit = exit_selec
        if mouse.is_button_pressed(1):
            janela.close()
    else:
        exit = Sprite("botoes\\exit.png")

    janela.update()