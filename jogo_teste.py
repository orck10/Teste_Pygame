import pygame, sys
from pygame.locals import *


#define cores
cor_branca = (255, 255, 255)
cor_azul = (90, 90, 255)
cor_verde = (90, 255, 90)
cor_vermelha = (255, 90, 90)

tamanho_tela = [640, 480]


def main():
    pygame.init()
    #cria tela e define o tamanho
    tela = pygame.display.set_mode(tamanho_tela)
    #coloca um titulo na tela
    pygame.display.set_caption('Tela de Teste')
    #cria um temporisador
    relogio = pygame.time.Clock()
    #cria superficie
    sup = pygame.Surface(tamanho_tela)
    #pinta a superficie de verde
    sup.fill(cor_branca)

    #cria retangulos
    ret = pygame.Rect(10, 10, 15 ,15)
    ret2 = pygame.Rect(5, 25, 600, 25)
    ret3 = pygame.Rect(35, 90, 600, 25)
    ret4 = pygame.Rect(5, 155, 600, 25)
    ret5 = pygame.Rect(600, 180, 30, 30)

    #cria fonte
    pygame.font.init()
    font_padrao = pygame.font.get_default_font()
    fonte_ganhou = pygame.font.SysFont(font_padrao, 30)

    #coloca o mouse na posição inicial
    pygame.mouse.set_pos(10, 10)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.mouse.set_pos(10, 10)
            if event.type == QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()

        #tempo de atualizar a tela
        relogio.tick(27)
        #coloca superficie na tela
        tela.blit(sup, [0, 0])
        #armazena pos anterior
        (xant, yant) = (ret.left, ret.top)
        #faz o retangulo seguir o mouse
        (ret.left, ret.top) = pygame.mouse.get_pos()
        #coloca o retangulo no centro do mouse
        ret.left -= ret.width/2
        ret.top -= ret.height/2

        #verifica colisão se colidir volta no começo
        if ret2.colliderect(ret):
            pygame.mouse.set_pos(10, 10)
        if ret3.colliderect(ret):
            pygame.mouse.set_pos(10, 10)
        if ret4.colliderect(ret):
            pygame.mouse.set_pos(10, 10)
        if ret5.colliderect(ret):
            sair = False
            while sair != True:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        exit()

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            exit()
                        if event.key == pygame.K_SPACE:
                            pygame.mouse.set_pos(10, 10)
                            sair = True
                text = fonte_ganhou.render('Você Ganhou aperte Espaço para jogar de novo e ESC para sair', 1, (0, 0, 0))
                tela.blit(text, (10, 200))
                pygame.display.update()
                
            
                
        #desenha os retangulos na tela        
        pygame.draw.rect(tela, cor_azul, ret2)
        pygame.draw.rect(tela, cor_azul, ret3)
        pygame.draw.rect(tela, cor_azul, ret4)
        pygame.draw.rect(tela, cor_vermelha, ret5)
        pygame.draw.rect(tela, cor_verde, ret)
        pygame.display.update()

main()
