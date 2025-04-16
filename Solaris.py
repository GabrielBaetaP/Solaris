import random
from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.keyboard import *
from random import randint 

janela = Window(1000, 600)
janela.set_title("Solaris")
fundo = GameImage("map (1).png")

Alice = Sprite("WalksD(1).png", 8)
Alice.x, Alice.y = 120, 135

Ocultista = Sprite("Ocultista (2).png", 8)
Ocultista.x, Ocultista.y = 580, 110

Ocultist = Sprite("spritesheet (1).png", 10)
Ocultist.x, Ocultist.y = 300, 110

Ocultist.set_total_duration(1000)
Ocultista.set_total_duration(1000)

Controle = janela.get_keyboard()
mouse = janela.get_mouse()

Ataque = Sprite("ataque_nor.png")
Ataque.x, Ataque.y = 400, 400

Ataque_selec = Sprite("ataque_selec.png")
Ataque_selec.x, Ataque_selec.y = Ataque.x, Ataque.y

Habilidade = Sprite("habilidade_nor.png")
Habilidade.x, Habilidade.y = 400, 466

Habilidade_selec = Sprite("habilidade_selec.png")
Habilidade_selec.x, Habilidade_selec.y = Habilidade.x, Habilidade.y

Item = Sprite("item_nor.png")
Item.x, Item.y = 400, 532

Item_selec = Sprite("item_selec.png")
Item_selec.x, Item_selec.y = Item.x, Item.y

Borda_preta = Sprite("pretao_borda.png")
Borda_preta.x, Borda_preta.y = 400, 334

Quadrado_preto = Sprite("quadradin_pretaov2.png")
Quadrado_preto.x, Quadrado_preto.y = 700, 400

Curse = Sprite("curse_nor.png")
Curse.x, Curse.y = 700, 400

Curse_selec = Sprite("curse_selec.png")
Curse_selec.x, Curse_selec.y = Curse.x, Curse.y

Blessing = Sprite("blessing_nor.png")
Blessing.x, Blessing.y = 700, 500

Blessing_selec = Sprite("blessing_selec.png")
Blessing_selec.x, Blessing_selec.y = Blessing.x, Blessing.y

Investida = Sprite("investida_nor.png")
Investida.x, Investida.y = 700, 400

Investida_selec = Sprite("investida_selec.png")
Investida_selec.x, Investida_selec.y = Investida.x, Investida.y

QuebraNoz = Sprite("tamago_nor.png")
QuebraNoz.x, QuebraNoz.y = 700, 500

QuebraNoz_selec = Sprite("tamago_selec.png")
QuebraNoz_selec.x, QuebraNoz_selec.y = QuebraNoz.x, QuebraNoz.y

Info_personagem = Sprite("ver8_1.png")
Info_personagem.x, Info_personagem.y = 0, 334

Info_personagem_sangrando = Sprite("ver8_1_dano.png")
Info_personagem_sangrando.x, Info_personagem_sangrando.y = Info_personagem.x, Info_personagem.y

Quadrado1 = Sprite("quadrado1.png")
Quadrado1.x, Quadrado1.y = 0, 466

def Alice_info(buff_vida_total, buff_energia_total, buff_esquiva):
    vida_total = 50 + buff_vida_total
    energia_total = 10 + buff_energia_total
    esquiva_por = 20 + buff_esquiva

    return vida_total, energia_total, esquiva_por

def Alice_Investida(buff_Investida, buff_rec_energia1, buff_critico_Investida):
    dano_Investida_Alice = 8 + buff_Investida
    rec_energia_Investida_Alice = 3 + buff_rec_energia1
    critico_investida = 15 + buff_critico_Investida

    return dano_Investida_Alice, rec_energia_Investida_Alice, critico_investida

def Alice_QuebraNoz(buff_QuebraNoz, buff_rec_energia2, buff_critico_QuebraNoz):
    dano_QuebraNoz_Alice = 6 + buff_QuebraNoz
    rec_energia_QuebraNoz_Alice = 5 + buff_rec_energia2
    critico_QuebraNoz = 20 + buff_critico_QuebraNoz

    return dano_QuebraNoz_Alice, rec_energia_QuebraNoz_Alice, critico_QuebraNoz

def Alice_habilidade_dano(buff_habilidade_dano, buff_habilidade_dano_gasto, buff_critico_habilidade):
    dano_habilidade_dano_Alice = 13 + buff_habilidade_dano
    gasto_energia_habilidade = 6 - buff_habilidade_dano_gasto
    critico_Habilidade = 10 + buff_critico_habilidade

    return dano_habilidade_dano_Alice, gasto_energia_habilidade, critico_Habilidade

def Alice_habilidade_vida(buff_habilidade_vida, buff_habilidade_vida_gasto):
    rec_habilidade_vida_Alice = 8 + buff_habilidade_vida
    gasto_energia_habilidade = 4 - buff_habilidade_vida_gasto

    return rec_habilidade_vida_Alice, gasto_energia_habilidade

def Ocultista_info():
    dano_ataque_Ocultista = 1
    dano_habilidade_Ocultista = 1
    vida_Ocultista = 100

    return dano_ataque_Ocultista, dano_habilidade_Ocultista, vida_Ocultista

def Sorte(minímo):
    x = randint(1,100)
    print(x)
    if x<=minímo:
        return True
    else:
        return False

def Texto_energia():
    janela.draw_text(f"Sem Energia para essa Habilidade", 485, 351, size = 35, color=(255,255,255), font_name = "m6x11")

def Texto_vida_max():
    janela.draw_text(f"Vida Cheia",  625, 351, size = 40, color=(255,255,255), font_name = "m6x11")

def Texto_ataques(dano_Investida_Alice, rec_energia_Investida_Alice, dano_QuebraNoz_Alice, rec_energia_QuebraNoz_Alice):
    janela.draw_text(f"{dano_Investida_Alice}",  955, 415, size = 35, color=(255,255,255), font_name = "m6x11")
    janela.draw_text(f"{rec_energia_Investida_Alice}",  955, 459, size = 35, color=(255,255,255), font_name = "m6x11")
    janela.draw_text(f"{dano_QuebraNoz_Alice}",  955, 515, size = 35, color=(255,255,255), font_name = "m6x11")
    janela.draw_text(f"{rec_energia_QuebraNoz_Alice}",  955, 559, size = 35, color=(255,255,255), font_name = "m6x11")

def Texto_habilidades(dano_habilidade_dano_Alice, gasto_energia_habilidade_dano_Alice, rec_habilidade_vida_Alice, gasto_energia_habilidade_vida_Alice):
    janela.draw_text(f"{dano_habilidade_dano_Alice}",  955, 415, size = 35, color=(255,255,255), font_name = "m6x11")
    janela.draw_text(f"{gasto_energia_habilidade_dano_Alice}",  955, 459, size = 35, color=(255,255,255), font_name = "m6x11")
    janela.draw_text(f"{rec_habilidade_vida_Alice}",  955, 515, size = 35, color=(255,255,255), font_name = "m6x11")
    janela.draw_text(f"{gasto_energia_habilidade_vida_Alice}",  955, 559, size = 35, color=(255,255,255), font_name = "m6x11")

def Combate(vida_atual, energia_atual):
    vida_atual_Alice = vida_atual
    energia_atual_Alice = energia_atual

    buff_Investida = 0
    buff_rec_energia1 = 0
    buff_QuebraNoz = 0
    buff_rec_energia2 = 0
    buff_habilidade_dano = 0
    buff_habilidade_dano_gasto = 0
    buff_habilidade_vida = 0
    buff_habilidade_vida_gasto = 0
    buff_vida_total = 0
    buff_energia_total = 0
    buff_esquiva = 0
    buff_critico_Investida = 0
    buff_critico_QuebraNoz = 0
    buff_critico_habilidade = 0

    turno = "player"

    dano_Investida_Alice, rec_energia_Investida_Alice, critico_Investida = Alice_Investida(buff_Investida, buff_rec_energia1, buff_critico_Investida)
    dano_QuebraNoz_Alice, rec_energia_QuebraNoz_Alice, critico_QuebraNoz = Alice_QuebraNoz(buff_QuebraNoz, buff_rec_energia2, buff_critico_QuebraNoz)
    dano_habilidade_Alice, gasto_habilidade_dano_Alice, critico_Habilidade = Alice_habilidade_dano(buff_habilidade_dano, buff_habilidade_dano_gasto, buff_critico_habilidade)
    rec_habilidade_Alice, gasto_habilidade_vida_Alice = Alice_habilidade_vida(buff_habilidade_vida, buff_habilidade_vida_gasto)
    vida_total_Alice, energia_total_Alice, esquiva_total = Alice_info(buff_vida_total, buff_energia_total, buff_esquiva)


    dano_ataque_inimigo, dano_habilidade_inimigo, vida_atual_inimigo = Ocultista_info()

    Ataque_vis = False
    Habilidade_vis = False

    cont_energia = 0
    cont_vida = 0

    while True:
        fundo.draw()
        Quadrado1.draw()
        Ataque.draw()
        Borda_preta.draw()
        Quadrado_preto.draw()
        Habilidade.draw()
        Item.draw()
        Alice.draw()
        Ocultista.draw()
        Ocultista.update()


        if vida_atual_Alice < vida_total_Alice/3:
            Info_personagem_sangrando.draw()

        else:
            Info_personagem.draw()

        if cont_energia > 0:
            Texto_energia()

        if cont_vida > 0:
            Texto_vida_max()

        if turno == "player":
            if mouse.is_over_object(Ataque):
                Ataque_selec.draw()
                if mouse.is_button_pressed(1):
                    Ataque_vis = True
                    Habilidade_vis = False

            if mouse.is_over_object(Habilidade):
                Habilidade_selec.draw()
                if mouse.is_button_pressed(1):
                    Ataque_vis = False
                    Habilidade_vis = True

            if mouse.is_over_object(Item):
                Item_selec.draw()

            if Ataque_vis == True:
                Investida.draw()
                QuebraNoz.draw()
                Texto_ataques(dano_Investida_Alice, rec_energia_Investida_Alice, dano_QuebraNoz_Alice, rec_energia_QuebraNoz_Alice)

                if mouse.is_over_object(Investida):
                    Investida_selec.draw()
                    Texto_ataques(dano_Investida_Alice, rec_energia_Investida_Alice, dano_QuebraNoz_Alice, rec_energia_QuebraNoz_Alice)
                    if mouse.is_button_pressed(1):
                        critico = Sorte(critico_Investida)
                        if critico == False:
                            vida_atual_inimigo -= dano_Investida_Alice
                        else:
                            vida_atual_inimigo -= (dano_Investida_Alice*2)
                            print("CRITICO\n")
                        
                        energia_atual_Alice += rec_energia_Investida_Alice
                        turno = "inimigo"
                        Ataque_vis = False
                        cont_energia = 0
                        cont_vida = 0

                if mouse.is_over_object(QuebraNoz):
                    QuebraNoz_selec.draw()
                    Texto_ataques(dano_Investida_Alice, rec_energia_Investida_Alice, dano_QuebraNoz_Alice, rec_energia_QuebraNoz_Alice)
                    if mouse.is_button_pressed(1):
                        critico = Sorte(critico_QuebraNoz)
                        if critico == False:
                            vida_atual_inimigo -= dano_QuebraNoz_Alice
                        else:
                            vida_atual_inimigo -= (dano_QuebraNoz_Alice*2)
                            print("CRITICO\n")
                        
                        energia_atual_Alice += rec_energia_QuebraNoz_Alice
                        turno = "inimigo"
                        Ataque_vis = False
                        cont_energia = 0
                        cont_vida = 0

            if energia_atual_Alice > energia_total_Alice:
                energia_atual_Alice = energia_total_Alice

            if Habilidade_vis == True:
                Blessing.draw()
                Curse.draw()
                Texto_habilidades(dano_habilidade_Alice, gasto_habilidade_dano_Alice, rec_habilidade_Alice, gasto_habilidade_vida_Alice)
            
                if mouse.is_over_object(Curse):
                    Curse_selec.draw()
                    Texto_habilidades(dano_habilidade_Alice, gasto_habilidade_dano_Alice, rec_habilidade_Alice, gasto_habilidade_vida_Alice)
                    if mouse.is_button_pressed(1):
                        
                        if energia_atual_Alice < gasto_habilidade_dano_Alice:
                            cont_energia = 1
                            cont_vida = 0
                    
                        else:
                            critico = Sorte(critico_Habilidade)
                            if critico == False:
                                vida_atual_inimigo -= dano_habilidade_Alice
                                print("Alice causou", dano_habilidade_Alice, "de dano")
                            else:
                                vida_atual_inimigo -= dano_habilidade_Alice*2
                                print("Alice causou", dano_habilidade_Alice*2, "de dano")
                                
                            energia_atual_Alice -= gasto_habilidade_dano_Alice
                            turno = "inimigo"
                            Habilidade_vis = False
                            cont_energia = 0
                            cont_vida = 0

                if mouse.is_over_object(Blessing):
                    Blessing_selec.draw()
                    Texto_habilidades(dano_habilidade_Alice, gasto_habilidade_dano_Alice, rec_habilidade_Alice, gasto_habilidade_vida_Alice)
                    if mouse.is_button_pressed(1):    
                        if vida_atual_Alice == vida_total_Alice:
                            cont_vida = 1
                            cont_energia = 0

                        if energia_atual_Alice < gasto_habilidade_vida_Alice:
                            cont_energia = 1
                            cont_vida = 0

                        if vida_atual_Alice < vida_total_Alice and cont_energia != 1:
                            energia_atual_Alice -= gasto_habilidade_vida_Alice
                            if vida_atual_Alice + rec_habilidade_Alice > vida_total_Alice:
                                vida_atual_Alice = vida_total_Alice
                            else:
                                vida_atual_Alice += rec_habilidade_Alice
                            print("Alice recuperou", rec_habilidade_Alice, "de vida")
                            turno = "inimigo"
                            Habilidade_vis = False
                            cont_energia = 0
                            cont_vida = 0
        
        if vida_atual_Alice <= 0:
            print("Você perdeu!")
            break
        elif vida_atual_inimigo <= 0:
            print("Você venceu!")
            break

        if turno == "inimigo":
            tipo_dano = random.choice(["ataque", "habilidade"])
            esquivou = Sorte(esquiva_total)
            
            if esquivou == False:
                if tipo_dano == "ataque":
                    print("Inimigo causou", dano_ataque_inimigo, "de dano")
                    vida_atual_Alice -= dano_ataque_inimigo
            
                else:
                    print("Inimigo causou", dano_habilidade_inimigo, "de dano")
                    vida_atual_Alice -= dano_habilidade_inimigo

            else:
                print("Você esquivou")
            
            turno = "player"

        if vida_atual_Alice <= 0:
            print("Você perdeu!")
            break
        elif vida_atual_inimigo <= 0:
            print("Você venceu!")
            break

        
        janela.draw_text(f"{vida_atual_Alice}/{vida_total_Alice}", 180, 358, size = 35, color=(255,255,255), font_name = "m6x11")
        janela.draw_text(f"{energia_atual_Alice}/{energia_total_Alice}", 226, 401, size = 35, color=(255,255,255), font_name = "m6x11")
        
        
        janela.draw_text(f"{vida_atual_inimigo}", 226, 500, size = 35, color=(255,255,255), font_name = "m6x11")

        janela.update()
        janela.delay(100)


Combate(30, 10)
