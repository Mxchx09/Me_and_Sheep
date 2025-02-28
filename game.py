import pygame

WIN_WIDTH, WIN_HEIGHT = 1000, 800
RES = (WIN_WIDTH, WIN_HEIGHT)

class Game:
    
    WIN_HEIGHT = 980
    WIN_WIDTH = 980
    
    def __init__(self, FPS):
        self.title = "Cheesburger Game"
        self.RES = (WIN_WIDTH, WIN_HEIGHT)
        self.BACKGROUND_IMG  = pygame.transform.scale(pygame.image.load("Assets/background.png"), self.RES)
        self.FPS = FPS
        
    def draw_background(self, win):
        win.blit(self.BACKGROUND_IMG, (0, 0))



pygame.init()

game = Game(FPS=60)

screen = pygame.display.set_mode(game.RES)
pygame.display.set_caption(game.title)

def main(game):
    
    running = True
    clock = pygame.time.Clock()
    
    while running:
        
        clock.tick(game.FPS) # limits the fps
        # screen.blit("background.png", (0, 0)) -- background.png not defined yet
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        pygame.display.flip()
        
        game.draw_background(screen)
        
    pygame.quit()
    quit()
    
main(game=game)
