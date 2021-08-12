import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import game_function as gf 
from pygame.sprite import Group

def run_game():
    #Inicializa o jogo e cria um objeto para a tela

    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")


    #Criar a espaçonave
    ship = Ship(ai_settings, screen)
    
    #Criar um alienigena
        #alien = Alien(ai_settings, screen)

    #Cria um grupo de alienigenas
    aliens = Group()

    #Cria um grupo no qual serão armazenados os projéteis
    bullets = Group()

    #Cria uma frota de alienigenas
    gf.create_fleet(ai_settings,screen,ship,aliens)


    #Inicia o laço principal do jogo
    while True:

        #Observa eventos de teclado e de mouse
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        
        
        #print(len(bullets))
        
        #Atualiza as imagens na tela e alterna para nova tela
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
