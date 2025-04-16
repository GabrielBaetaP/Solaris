import random
from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from random import randint

def combate1():
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

        vida_total, energia_total, esquiva_por = Alice_info(buff_vida_total, buff_energia_total, buff_esquiva)
        dano_Investida_Alice, rec_energia_Investida_Alice, critico_investida = Alice_Investida(buff_Investida, buff_rec_energia1, buff_critico_Investida)
        dano_QuebraNoz_Alice, rec_energia_QuebraNoz_Alice, critico_QuebraNoz = Alice_QuebraNoz(buff_QuebraNoz, buff_rec_energia2, buff_critico_QuebraNoz)
        dano_habilidade_dano_Alice, gasto_energia_habilidade_dano_Alice, critico_Habilidade = Alice_habilidade_dano(buff_habilidade_dano, buff_habilidade_dano_gasto, buff_critico_habilidade)
        rec_habilidade_vida_Alice, gasto_energia_habilidade_vida_Alice = Alice_habilidade_vida(buff_habilidade_vida, buff_habilidade_vida_gasto)

        dano_ataque_Ocultista, dano_habilidade_Ocultista, vida_Ocultista = Ocultista_info()

        while True:
            if vida_atual_Alice <= 0:
                print("Alice perdeu")
                break
            if vida_Ocultista <= 0:
                print("Ocultista perdeu")
                break

            if Controle.key_pressed("ESC"):
                break

            fundo.draw()
            Borda_preta.draw()
            Quadrado_preto.draw()
            Info_personagem.draw()

            janela.draw_text(f"{vida_atual_Alice}/{vida_total}",  210, 457, size = 25, color=(255,255,255), font_name = "m6x11")
            janela.draw_text(f"{energia_atual_Alice}/{energia_total}",  210, 555, size = 25, color=(255,255,255), font_name = "m6x11")
            janela.draw_text(f"{vida_Ocultista}",  760, 457, size = 25, color=(255,255,255), font_name = "m6x11")

            Alice.draw()
            Ocultista.draw()

            Ataque.draw()
            Habilidade.draw()
            Item.draw()

            if mouse.is_over_object(Ataque):
                Ataque_selec.draw()
                if mouse.is_button_pressed(1):
                    if mouse.is_over_object(Investida):
                        Investida_selec.draw()
                        if mouse.is_button_pressed(1):
                            if energia_atual_Alice >= rec_energia_Investida_Alice:
                                energia_atual_Alice -= rec_energia_Investida_Alice
                                vida_Ocultista -= dano_Investida_Alice
                                print(f"Alice usou Investida. Causou {dano_Investida_Alice} de dano.")
                            else:
                                Texto_energia()
                    elif mouse.is_over_object(QuebraNoz):
                        QuebraNoz_selec.draw()
                        if mouse.is_button_pressed(1):
                            if energia_atual_Alice >= rec_energia_QuebraNoz_Alice:
                                energia_atual_Alice -= rec_energia_QuebraNoz_Alice
                                vida_Ocultista -= dano_QuebraNoz_Alice
                                print(f"Alice usou Quebra-Noz. Causou {dano_QuebraNoz_Alice} de dano.")
                            else:
                                Texto_energia()
                    else:
                        Texto_ataques(dano_Investida_Alice, rec_energia_Investida_Alice, dano_QuebraNoz_Alice, rec_energia_QuebraNoz_Alice)

            if mouse.is_over_object(Habilidade):
                Habilidade_selec.draw()
                if mouse.is_button_pressed(1):
                    if mouse.is_over_object(Curse):
                        Curse_selec.draw()
                        if mouse.is_button_pressed(1):
                            if energia_atual_Alice >= gasto_energia_habilidade_dano_Alice:
                                energia_atual_Alice -= gasto_energia_habilidade_dano_Alice
                                vida_Ocultista -= dano_habilidade_dano_Alice
                                print(f"Alice usou Habilidade de Dano. Causou {dano_habilidade_dano_Alice} de dano.")
                            else:
                                Texto_energia()
                    elif mouse.is_over_object(Blessing):
                        Blessing_selec.draw()
                        if mouse.is_button_pressed(1):
                            if energia_atual_Alice >= gasto_energia_habilidade_vida_Alice and vida_atual_Alice < vida_total:
                                energia_atual_Alice -= gasto_energia_habilidade_vida_Alice
                                vida_atual_Alice += rec_habilidade_vida_Alice
                                if vida_atual_Alice > vida_total:
                                    vida_atual_Alice = vida_total
                                print(f"Alice usou Habilidade de Vida. Recuperou {rec_habilidade_vida_Alice} de vida.")
                            else:
                                if energia_atual_Alice < gasto_energia_habilidade_vida_Alice:
                                    Texto_energia()
                                if vida_atual_Alice == vida_total:
                                    Texto_vida_max()
                    else:
                        Texto_habilidades(dano_habilidade_dano_Alice, gasto_energia_habilidade_dano_Alice, rec_habilidade_vida_Alice, gasto_energia_habilidade_vida_Alice)

            janela.update()

    Combate(50, 10)

#if __name__ == "__main__":
    #main()

import random

def combate2():
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

        vida_total, energia_total, esquiva_por = Alice_info(buff_vida_total, buff_energia_total, buff_esquiva)
        dano_Investida_Alice, rec_energia_Investida_Alice, critico_investida = Alice_Investida(buff_Investida, buff_rec_energia1, buff_critico_Investida)
        dano_QuebraNoz_Alice, rec_energia_QuebraNoz_Alice, critico_QuebraNoz = Alice_QuebraNoz(buff_QuebraNoz, buff_rec_energia2, buff_critico_QuebraNoz)
        dano_habilidade_dano_Alice, gasto_energia_habilidade_dano_Alice, critico_Habilidade = Alice_habilidade_dano(buff_habilidade_dano, buff_habilidade_dano_gasto, buff_critico_habilidade)
        rec_habilidade_vida_Alice, gasto_energia_habilidade_vida_Alice = Alice_habilidade_vida(buff_habilidade_vida, buff_habilidade_vida_gasto)

        dano_ataque_Ocultista, dano_habilidade_Ocultista, vida_Ocultista = Ocultista_info()

        while True:
            if vida_atual_Alice <= 0:
                print("Alice perdeu")
                break
            if vida_Ocultista <= 0:
                print("Ocultista perdeu")
                break

            if Controle.key_pressed("ESC"):
                break

            fundo.draw()
            Borda_preta.draw()
            Quadrado_preto.draw()
            Info_personagem.draw()

            janela.draw_text(f"{vida_atual_Alice}/{vida_total}",  210, 457, size = 25, color=(255,255,255), font_name = "m6x11")
            janela.draw_text(f"{energia_atual_Alice}/{energia_total}",  210, 555, size = 25, color=(255,255,255), font_name = "m6x11")
            janela.draw_text(f"{vida_Ocultista}",  760, 457, size = 25, color=(255,255,255), font_name = "m6x11")

            Alice.draw()
            Ocultista.draw()

            Ataque.draw()
            Habilidade.draw()
            Item.draw()

            if mouse.is_over_object(Ataque):
                Ataque_selec.draw()
                if mouse.is_button_pressed(1):
                    if mouse.is_over_object(Investida):
                        Investida_selec.draw()
                        if mouse.is_button_pressed(1):
                            if energia_atual_Alice >= rec_energia_Investida_Alice:
                                energia_atual_Alice -= rec_energia_Investida_Alice
                                vida_Ocultista -= dano_Investida_Alice
                                print(f"Alice usou Investida. Causou {dano_Investida_Alice} de dano.")
                            else:
                                Texto_energia()
                    elif mouse.is_over_object(QuebraNoz):
                        QuebraNoz_selec.draw()
                        if mouse.is_button_pressed(1):
                            if energia_atual_Alice >= rec_energia_QuebraNoz_Alice:
                                energia_atual_Alice -= rec_energia_QuebraNoz_Alice
                                vida_Ocultista -= dano_QuebraNoz_Alice
                                print(f"Alice usou Quebra-Noz. Causou {dano_QuebraNoz_Alice} de dano.")
                            else:
                                Texto_energia()
                    else:
                        Texto_ataques(dano_Investida_Alice, rec_energia_Investida_Alice, dano_QuebraNoz_Alice, rec_energia_QuebraNoz_Alice)

            if mouse.is_over_object(Habilidade):
                Habilidade_selec.draw()
                if mouse.is_button_pressed(1):
                    if mouse.is_over_object(Curse):
                        Curse_selec.draw()
                        if mouse.is_button_pressed(1):
                            if energia_atual_Alice >= gasto_energia_habilidade_dano_Alice:
                                energia_atual_Alice -= gasto_energia_habilidade_dano_Alice
                                vida_Ocultista -= dano_habilidade_dano_Alice
                                print(f"Alice usou Habilidade de Dano. Causou {dano_habilidade_dano_Alice} de dano.")
                            else:
                                Texto_energia()
                    elif mouse.is_over_object(Blessing):
                        Blessing_selec.draw()
                        if mouse.is_button_pressed(1):
                            if energia_atual_Alice >= gasto_energia_habilidade_vida_Alice and vida_atual_Alice < vida_total:
                                energia_atual_Alice -= gasto_energia_habilidade_vida_Alice
                                vida_atual_Alice += rec_habilidade_vida_Alice
                                if vida_atual_Alice > vida_total:
                                    vida_atual_Alice = vida_total
                                print(f"Alice usou Habilidade de Vida. Recuperou {rec_habilidade_vida_Alice} de vida.")
                            else:
                                if energia_atual_Alice < gasto_energia_habilidade_vida_Alice:
                                    Texto_energia()
                                if vida_atual_Alice == vida_total:
                                    Texto_vida_max()
                    else:
                        Texto_habilidades(dano_habilidade_dano_Alice, gasto_energia_habilidade_dano_Alice, rec_habilidade_vida_Alice, gasto_energia_habilidade_vida_Alice)

            janela.update()

    Combate(50, 10)

#if __name__ == "__main__":
    #main()

def combate3():
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

        vida_total, energia_total, esquiva_por = Alice_info(buff_vida_total, buff_energia_total, buff_esquiva)
        dano_Investida_Alice, rec_energia_Investida_Alice, critico_investida = Alice_Investida(buff_Investida, buff_rec_energia1, buff_critico_Investida)
        dano_QuebraNoz_Alice, rec_energia_QuebraNoz_Alice, critico_QuebraNoz = Alice_QuebraNoz(buff_QuebraNoz, buff_rec_energia2, buff_critico_QuebraNoz)
        dano_habilidade_dano_Alice, gasto_energia_habilidade_dano_Alice, critico_Habilidade = Alice_habilidade_dano(buff_habilidade_dano, buff_habilidade_dano_gasto, buff_critico_habilidade)
        rec_habilidade_vida_Alice, gasto_energia_habilidade_vida_Alice = Alice_habilidade_vida(buff_habilidade_vida, buff_habilidade_vida_gasto)

        dano_ataque_Ocultista, dano_habilidade_Ocultista, vida_Ocultista = Ocultista_info()

        while True:
            if vida_atual_Alice <= 0:
                print("Alice perdeu")
                break
            if vida_Ocultista <= 0:
                print("Ocultista perdeu")
                break

            if Controle.key_pressed("ESC"):
                break

            fundo.draw()
            Borda_preta.draw()
            Quadrado_preto.draw()
            Info_personagem.draw()

            janela.draw_text(f"{vida_atual_Alice}/{vida_total}",  210, 457, size = 25, color=(255,255,255), font_name = "m6x11")
            janela.draw_text(f"{energia_atual_Alice}/{energia_total}",  210, 555, size = 25, color=(255,255,255), font_name = "m6x11")
            janela.draw_text(f"{vida_Ocultista}",  760, 457, size = 25, color=(255,255,255), font_name = "m6x11")

            Alice.draw()
            Ocultista.draw()

            Ataque.draw()
            Habilidade.draw()
            Item.draw()

            if mouse.is_over_object(Ataque):
                Ataque_selec.draw()
                if mouse.is_button_pressed(1):
                    if mouse.is_over_object(Investida):
                        Investida_selec.draw()
                        if mouse.is_button_pressed(1):
                            if energia_atual_Alice >= rec_energia_Investida_Alice:
                                energia_atual_Alice -= rec_energia_Investida_Alice
                                vida_Ocultista -= dano_Investida_Alice
                                print(f"Alice usou Investida. Causou {dano_Investida_Alice} de dano.")
                            else:
                                Texto_energia()
                    elif mouse.is_over_object(QuebraNoz):
                        QuebraNoz_selec.draw()
                        if mouse.is_button_pressed(1):
                            if energia_atual_Alice >= rec_energia_QuebraNoz_Alice:
                                energia_atual_Alice -= rec_energia_QuebraNoz_Alice
                                vida_Ocultista -= dano_QuebraNoz_Alice
                                print(f"Alice usou Quebra-Noz. Causou {dano_QuebraNoz_Alice} de dano.")
                            else:
                                Texto_energia()
                    else:
                        Texto_ataques(dano_Investida_Alice, rec_energia_Investida_Alice, dano_QuebraNoz_Alice, rec_energia_QuebraNoz_Alice)

            if mouse.is_over_object(Habilidade):
                Habilidade_selec.draw()
                if mouse.is_button_pressed(1):
                    if mouse.is_over_object(Curse):
                        Curse_selec.draw()
                        if mouse.is_button_pressed(1):
                            if energia_atual_Alice >= gasto_energia_habilidade_dano_Alice:
                                energia_atual_Alice -= gasto_energia_habilidade_dano_Alice
                                vida_Ocultista -= dano_habilidade_dano_Alice
                                print(f"Alice usou Habilidade de Dano. Causou {dano_habilidade_dano_Alice} de dano.")
                            else:
                                Texto_energia()
                    elif mouse.is_over_object(Blessing):
                        Blessing_selec.draw()
                        if mouse.is_button_pressed(1):
                            if energia_atual_Alice >= gasto_energia_habilidade_vida_Alice and vida_atual_Alice < vida_total:
                                energia_atual_Alice -= gasto_energia_habilidade_vida_Alice
                                vida_atual_Alice += rec_habilidade_vida_Alice
                                if vida_atual_Alice > vida_total:
                                    vida_atual_Alice = vida_total
                                print(f"Alice usou Habilidade de Vida. Recuperou {rec_habilidade_vida_Alice} de vida.")
                            else:
                                if energia_atual_Alice < gasto_energia_habilidade_vida_Alice:
                                    Texto_energia()
                                if vida_atual_Alice == vida_total:
                                    Texto_vida_max()
                    else:
                        Texto_habilidades(dano_habilidade_dano_Alice, gasto_energia_habilidade_dano_Alice, rec_habilidade_vida_Alice, gasto_energia_habilidade_vida_Alice)

            janela.update()

    Combate(50, 10)

if __name__ == "__main__":
    main()

