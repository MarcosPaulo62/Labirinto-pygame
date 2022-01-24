import pygame

def main():
    #As definições da janela(variáveis)
    x = pygame.init() #Manda iniciar o pygame
    cj1 = pygame.image.load('cj.png')
    cj = pygame.transform.scale(cj1, (32,32))
    pygame.display.set_icon(cj)
    tela = pygame.display.set_mode([600, 450]) #Tamanho da tel larg x alt
    pygame.display.set_caption('My Game') #Título da janela
    relogio = pygame.time.Clock()
    cor_branca = (255, 255, 255)
    cor_azul = (108, 194, 236)
    cor_verde = (152, 231, 114)
    cor_vermelha = (200, 0, 0)
    cor_amarela = (241, 247, 43)

    espaco = pygame.image.load('espaco.jpg')
    sup = pygame.Surface((600, 450))  # Cria uma superficie
    sup.blit(espaco, (0, 0))
    pygame.mouse.set_pos(20, 20)

    ret = pygame.Rect(10, 10, 20, 20) #Rect(esquerda, topo, largura, altura) cria um retangulo
    ret2 = pygame.Rect(0, 40, 560, 20)
    ret3 = pygame.Rect(40, 120, 560, 20)
    ret4 = pygame.Rect(0, 200, 560, 20)
    ret5 = pygame.Rect(40, 280, 560, 20)
    ret6 = pygame.Rect(0, 360, 560, 20)
    ret7 = pygame.Rect(0, 380, 40, 100)
    ret8 = pygame.Rect(-1, 0, 1, 450)
    ret9 = pygame.Rect(600, 0, 1, 450)
    ret10 = pygame.Rect(0, 0, 600, 1)
    ret11 = pygame.Rect(0, 450, 600, 1)

    pygame.font.init()

    font_padrao = pygame.font.get_default_font()
    fonte_perdeu = pygame.font.SysFont(font_padrao, 45)
    fonte_ganhou = pygame.font.SysFont(font_padrao, 45)

    audio_explosao = pygame.mixer.Sound('bum.ogg')
    audio_gta = pygame.mixer.Sound('gta.ogg')

    sair = False
    while sair != True:
        for event in pygame.event.get(): #get captura o que entra

            if event.type == pygame.QUIT: #pygame.QUIT é o clique no X da janela, é um type
                sair = True
            '''if event.type == pygame.MOUSEBUTTONDOWN: #se clicar mouse
                pygame.mouse.set_pos(150,150)'''

        relogio.tick(120) #Quadros por segundo
        tela.fill(cor_branca) #fill = fundo de tela
        tela.blit(sup, [0, 0]) #Chama a superficie, entre colchetes a distancia da (esquerda da tela, do topo)

        (xant, yant) = (ret.left, ret.right)
        (ret.left, ret.top) = pygame.mouse.get_pos()
        ret.left -= ret.width/2
        ret.top -= ret.height/2
        if ret.colliderect(ret2) or ret.colliderect(ret3) or ret.colliderect(ret4) or ret.colliderect(ret5) or ret.colliderect(ret6):
            audio_explosao.play()
            audio_explosao.set_volume(0.5) #volume entre 0 e 1
            text = fonte_perdeu.render('PERDEU! :(', 1, cor_vermelha)
            tela.blit(text, [200, 200])
            pygame.display.update()
            pygame.time.wait(2000)
            (ret.left, ret.top) = (20, 20)
            pygame.mouse.set_pos(20, 20)
        if ret.colliderect(ret7):
            audio_gta.play()
            audio_gta.set_volume(0.5)
            text2 = fonte_ganhou.render('VENCEU! :)', 1, cor_amarela)
            tela.blit(text2, [200, 200])
            pygame.display.update()
            pygame.time.wait(4000) #Pausa o programa em milisegundos
            (ret.left, ret.top) = (20, 20)
            pygame.mouse.set_pos(20, 20)

        if ret.colliderect(ret8) or ret.colliderect(ret9) or ret.colliderect(ret10) or ret.colliderect(ret11):
            pygame.mouse.set_pos(20, 20)

        pygame.draw.rect(tela, cor_verde, ret)
        pygame.draw.rect(tela, cor_vermelha, ret2)
        pygame.draw.rect(tela, cor_vermelha, ret3)
        pygame.draw.rect(tela, cor_vermelha, ret4)
        pygame.draw.rect(tela, cor_vermelha, ret5)
        pygame.draw.rect(tela, cor_vermelha, ret6)
        pygame.draw.rect(tela, cor_verde, ret7)
        pygame.draw.rect(tela, cor_vermelha, ret8)
        pygame.draw.rect(tela, cor_vermelha, ret9)
        pygame.draw.rect(tela, cor_vermelha, ret10)
        pygame.draw.rect(tela, cor_vermelha, ret11)
        pygame.display.update() #Vai atualizando a janela a cada quadro
    pygame.quit()


main()
