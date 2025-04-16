import pygame
import sys

# Inicializando o Pygame
pygame.init()

# Definindo algumas cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Definindo as dimensões da janela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")


# Função para exibir o menu
def exibir_menu():
    screen.fill(BLACK)

    # Texto do título
    font_title = pygame.font.Font(None, 48)
    text_surface = font_title.render("SPACE INVADERS", True, WHITE)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 4))
    screen.blit(text_surface, text_rect)

    # Texto das opções do menu
    font_options = pygame.font.Font(None, 36)
    opcoes = ["JOGAR", "DIFICULDADE", "RANKING", "SAIR"]
    y = HEIGHT // 2
    botoes = []
    for opcao in opcoes:
        text_surface = font_options.render(opcao, True, WHITE)
        text_rect = text_surface.get_rect(center=(WIDTH // 2, y))
        screen.blit(text_surface, text_rect)
        botoes.append(text_rect)
        y += 50

    pygame.display.flip()
    return botoes


# Função para exibir a tela de seleção de dificuldade
def selecionar_dificuldade():
    screen.fill(BLACK)

    # Texto do título
    font_title = pygame.font.Font(None, 48)
    text_surface = font_title.render("SELECIONE A DIFICULDADE", True, WHITE)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 4))
    screen.blit(text_surface, text_rect)

    # Texto das opções de dificuldade
    font_options = pygame.font.Font(None, 36)
    opcoes = ["Fácil", "Médio", "Difícil"]
    y = HEIGHT // 2
    botoes = []
    for opcao in opcoes:
        text_surface = font_options.render(opcao, True, WHITE)
        text_rect = text_surface.get_rect(center=(WIDTH // 2, y))
        screen.blit(text_surface, text_rect)
        botoes.append(text_rect)
        y += 50

    pygame.display.flip()
    return botoes


# Função para o loop do jogo
def game_loop():
    screen.fill(BLACK)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return


# Função principal do jogo
def main():
    tela_atual = "menu"
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Verifica se o botão esquerdo do mouse foi pressionado
                    botoes = exibir_menu() if tela_atual == "menu" else selecionar_dificuldade()
                    mouse_pos = pygame.mouse.get_pos()
                    for botao in botoes:
                        if botao.collidepoint(mouse_pos):
                            if botao == botoes[0]:
                                tela_atual = "jogar"
                            elif botao == botoes[1]:
                                tela_atual = "dificuldade"
                            elif botao == botoes[3]:
                                sys.exit()

        if tela_atual == "jogar":
            game_loop()

    pygame.quit()


if __name__ == "__main__":
    main()
