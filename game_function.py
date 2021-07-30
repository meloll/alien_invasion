import sys
import pygame
from bullet import Bullet
from alien import Alien

def check_keydown_events(event, ai_settings, screen,  ship, bullets):
    #Responde a pressionamento de tecla
        
        if event.key == pygame.K_RIGHT:
        #Move a nave para direita
            ship.moving_right = True

        elif event.key == pygame.K_LEFT:
            #Move a nave para esquerda
            ship.moving_left = True

        elif event.key == pygame.K_SPACE:
            #Cria um novo projétil e o adiciona ao grupo de projéteis
            fire_bullet(ai_settings, screen, ship, bullets)

        #Para sair do jogo quando pressionado a tecla "q"    
        elif event.key == pygame.K_q:
            sys.exit()

        
def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
                new_bullet = Bullet(ai_settings, screen, ship)
                bullets.add(new_bullet)


def check_keyup_events(event, ship):
    #Responde a solturas de tecla
        if event.key == pygame.K_RIGHT:
            ship.moving_right = False

        elif event.key == pygame.K_LEFT:
            ship.moving_left = False

def check_events(ai_settings, screen, ship,bullets):
    #Responde a eventos de pressionamento de teclas e de mouse

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen,ship ,bullets)
                    
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings,screen, ship, aliens, bullets):
    #Atualiza as imagens na tela e alterna para nova tela
    
     # Redesenha a tela a cada passagem pelo laço
        screen.fill(ai_settings.bg_color)

    #Redesenha todos os projéteis atrás da espaçonave e dos alienigenas
        for bullet in bullets.sprites():
            bullet.draw_bullet()
        ship.blitme()
        aliens.draw(screen)
        

        #Deixa a tela mais recente visível
        pygame.display.flip()

def update_bullets(bullets):

    #Atualiza as posições dos projéteis
    bullets.update()

    #Livra-se dos projéteis que desapareceram
    for bullet in bullets.copy():
        if bullet.rect.bottom <=0:
            bullets.remove(bullet)

def create_fleet(ai_settings,screen,aliens):
    #Cria uma frota completa de alienigenas

    #Cria um alienigena e calcula  o número de alienigenas em uma linha
    #O espaçamento entre os alienigenas é igual à larguraa de um alienigena 

    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x /(2*alien_width))

    #Cria a primeira linha de alienigenas
    for alien_number in range(number_aliens_x):
        alien = Alien(ai_settings,screen)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)