from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.collision import *
from combates import *
#from MenuSolaris import *

def jogando():
    # Configuração da janela
    janela = Window(1000, 600)
    janela.set_background_color("Black")
    janela.set_title("Solaris")

    fundos = ["map (1).png","map (3).png", "map (9).png", "mapa10.png", "mapa11.png", "mapa12.png"]  # Lista de fundos com 4 mapas
    indice_fundo_atual = 0  # Índice do fundo atual
    fundo = GameImage(fundos[indice_fundo_atual])  # Inicializa o fundo
    fim_de_jogo = GameImage("game_win_solaris.png")
    # Controle de teclado
    controle = janela.get_keyboard()

    # Sprites dos personagens
    PabloD = Sprite("WalkfD.png", 8)
    PabloE = Sprite("WalkfE.png", 8)
    AliceD = Sprite("WalksD.png", 8)
    AliceE = Sprite("WalksE.png", 8)

    # Configuração da duração das animações
    PabloD.set_total_duration(1000)
    PabloE.set_total_duration(1000)
    AliceD.set_total_duration(1000)
    AliceE.set_total_duration(1000)

    # Posição inicial de Pablo
    PabloD.x = 50
    PabloD.y = 223
    PabloE.x = PabloD.x
    PabloE.y = 223

    # Posição inicial de Alice
    AliceD.x = 100
    AliceD.y = 223
    AliceE.x = AliceD.x
    AliceE.y = 223

    # Velocidade do movimento
    velocidade = 200  # pixels por segundo

    # Sprite atual de Pablo e Alice (direita por padrão)
    Pablo = PabloD
    Alice = AliceD

    # Variáveis de combate
    em_combate = False
    posicao_combate = 500

    cont1 = 0
    cont2 = 0
    cont3 = 0

    # Pontos de vida
    vida_pablo = 100
    vida_alice = 100
    vida_inimigo1 = 100

    # Dano de ataque
    dano_ataque = 10

    cont_mapa = 0
    cont_menu = 0

    def alterar_fundo():
        nonlocal indice_fundo_atual, fundo  # Torna a variável fundo acessível dentro da função
        fundo = GameImage(fundos[indice_fundo_atual])  # Altera o fundo da janela

    # Função para desenhar as informações de vida
    def desenhar_informacoes():
        janela.draw_text(f"Pablo HP: {vida_pablo}", 20, 520, size=20, color=(255,255,255))
        janela.draw_text(f"Alice HP: {vida_alice}", 20, 550, size=20, color=(255,255,255))
        janela.draw_text(f"Inimigo HP: {vida_inimigo1}", 800, 520, size=20, color=(255,255,255))

    # Loop principal do jogo
    while True:
        # Calcula o tempo decorrido desde a última atualização
        delta_time = janela.delta_time()

        fundo.draw()

        # Desenha os sprites dos personagens
        Pablo.draw()
        Alice.draw()


        # Controle de movimento do Pablo (fora de combate)
        if not em_combate:
            movendo = False

            if controle.key_pressed("D") and cont_mapa != 0 and cont_mapa!= 1 and cont_mapa != 2:
                if Pablo.x < 550:
                    Pablo.x += velocidade * delta_time
                    if Pablo != PabloD:
                        PabloD.x, PabloD.y = Pablo.x, Pablo.y
                        Pablo = PabloD
                        Alice = AliceD
                    movendo = True
                else:
                    if Pablo.y > 155:
                        Pablo.x += velocidade * delta_time
                        if Pablo != PabloD:
                            PabloD.x, PabloD.y = Pablo.x, Pablo.y
                            Pablo = PabloD
                            Alice = AliceD
                        movendo = True

            if controle.key_pressed("W") and Pablo.y > 50 and cont_mapa != 0 and cont_mapa!= 1 and cont_mapa != 2:
                if Pablo.x < 560:
                    Pablo.y -= velocidade * delta_time
                    movendo = True
                else:
                    if Pablo.y > 165:
                        Pablo.y -= velocidade * delta_time
                        movendo = True
                print(Pablo.x, Pablo.y)


            if controle.key_pressed("S") and cont_mapa != 0 and cont_mapa!= 1 and cont_mapa != 2:
                Pablo.y += velocidade * delta_time
                movendo = True
                #print(Pablo.y)

            if controle.key_pressed("A") and cont_mapa != 0 and cont_mapa!= 1 and cont_mapa != 2:
                Pablo.x -= velocidade * delta_time
                if Pablo != PabloE:
                    PabloE.x, PabloE.y = Pablo.x, Pablo.y
                    Pablo = PabloE
                    Alice = AliceE
                movendo = True


            if controle.key_pressed("D") and cont_mapa == 0:
                Pablo.x += velocidade * delta_time
                if Pablo != PabloD:
                    PabloD.x, PabloD.y = Pablo.x, Pablo.y
                    Pablo = PabloD
                    Alice = AliceD
                movendo = True

            if controle.key_pressed("W") and Pablo.y > 50  and cont_mapa == 0:
                    Pablo.y -= velocidade * delta_time
                    movendo = True

            if controle.key_pressed("S")  and cont_mapa == 0:
                Pablo.y += velocidade * delta_time
                movendo = True
                #print(Pablo.y)

            if controle.key_pressed("A") and cont_mapa == 0:
                Pablo.x -= velocidade * delta_time
                if Pablo != PabloE:
                    PabloE.x, PabloE.y = Pablo.x, Pablo.y
                    Pablo = PabloE
                    Alice = AliceE
                movendo = True


            if controle.key_pressed("D") and cont_mapa == 1:
                if Pablo.x < 550:
                    Pablo.x += velocidade * delta_time
                    if Pablo != PabloD:
                        PabloD.x, PabloD.y = Pablo.x, Pablo.y
                        Pablo = PabloD
                        Alice = AliceD
                    movendo = True
                else:
                    if Pablo.y > 155:
                        Pablo.x += velocidade * delta_time
                        if Pablo != PabloD:
                            PabloD.x, PabloD.y = Pablo.x, Pablo.y
                            Pablo = PabloD
                            Alice = AliceD
                        movendo = True

            if controle.key_pressed("W") and Pablo.y > 50 and cont_mapa == 1:
                if Pablo.x < 560:
                    Pablo.y -= velocidade * delta_time
                    movendo = True
                else:
                    if Pablo.y > 165:
                        Pablo.y -= velocidade * delta_time
                        movendo = True

            if controle.key_pressed("S") and cont_mapa == 1:
                Pablo.y += velocidade * delta_time
                movendo = True
                #print(Pablo.y)

            if controle.key_pressed("A") and cont_mapa == 1:
                Pablo.x -= velocidade * delta_time
                if Pablo != PabloE:
                    PabloE.x, PabloE.y = Pablo.x, Pablo.y
                    Pablo = PabloE
                    Alice = AliceE
                movendo = True



            if controle.key_pressed("D") and cont_mapa == 2:
                Pablo.x += velocidade * delta_time
                if Pablo != PabloD:
                    PabloD.x, PabloD.y = Pablo.x, Pablo.y
                    Pablo = PabloD
                    Alice = AliceD
                movendo = True

            if controle.key_pressed("W") and Pablo.y > 50 and cont_mapa == 2:
                if (Pablo.x > 180):
                    Pablo.y -= velocidade * delta_time
                    movendo = True
                else:
                    if(Pablo.y > 165):
                        Pablo.y -= velocidade * delta_time
                        movendo = True

            if controle.key_pressed("S") and cont_mapa == 2:
                Pablo.y += velocidade * delta_time
                movendo = True

            if controle.key_pressed("A") and cont_mapa == 2:
                if Pablo.x > 185:
                    Pablo.x -= velocidade * delta_time
                    if Pablo != PabloE:
                        PabloE.x, PabloE.y = Pablo.x, Pablo.y
                        Pablo = PabloE
                        Alice = AliceE
                    movendo = True

                else:
                    if(Pablo.y > 155):
                        Pablo.x -= velocidade * delta_time
                        if Pablo != PabloE:
                            PabloE.x, PabloE.y = Pablo.x, Pablo.y
                            Pablo = PabloE
                            Alice = AliceE
                        movendo = True

            #print(cont_mapa)



            # Checa se Pablo atingiu a extremidade esquerda
            if Pablo.x <= 0:
                if indice_fundo_atual > 0:
                    indice_fundo_atual -= 1
                    cont_mapa -= 1
                    alterar_fundo()
                    Pablo.x = janela.width - Pablo.width  # Reposiciona Pablo para o lado direito da tela
                    #print(Pablo.x)

                else:
                    Pablo.x = 0  # Impede de sair do primeiro mapa

            # Checa se Pablo atingiu a extremidade direita
            if Pablo.x + Pablo.width/2 >= janela.width:
                if indice_fundo_atual < len(fundos) - 1:
                    indice_fundo_atual += 1
                    cont_mapa += 1
                    alterar_fundo()
                    Pablo.x = 0  # Reposiciona Pablo para o lado esquerdo da tela
                    #print(Pablo.x)
                else:
                    Pablo.x = janela.width - Pablo.width/2   # Impede de sair do último mapa

                if indice_fundo_atual == 1 and cont1 == 0:
                    cont1 = 1
                    combate1()
                    janela.set_background_color("Black")

                if indice_fundo_atual == 3 and cont2 == 0:
                    cont2 = 1
                    combate2()
                    janela.set_background_color("Black")

                if indice_fundo_atual == 5 and cont3 == 0:
                    cont3 = 1
                    combate3()
                    janela.set_background_color("Black")



            if Pablo.y <= 0:
                Pablo.y = 0
            if Pablo.y + Pablo.height >= 380:
                Pablo.y = 380 - Pablo.height

            if indice_fundo_atual >= 4 and cont3 == 1:
                if Pablo.x > 650 and Pablo.x < 800 and Pablo.y > 150 and Pablo.y < 170 and controle.key_pressed("W"):
                    cont_menu +=1
                    #fim_de_jogo.draw()
            if cont_menu >= 1:
                fim_de_jogo.draw()

            # Apenas atualiza a animação se estiver se movendo
            if movendo:
                Pablo.update()
                Alice.update()
            else:
                Pablo.set_curr_frame(0)
                Alice.set_curr_frame(0)

            # Atualiza a posição de Alice em relação a Pablo
            Alice.x = Pablo.x - Pablo.width / 3
            Alice.y = Pablo.y

        janela.update()

# Chama a função jogando para iniciar o jogo
#jogando()