import pygame

class Game:
    
    def __init__(self, FPS):
        self.WIN_WIDTH = 980
        self.WIN_HEIGHT = 980
        self.title = "Cheesburger Game"
        self.RES = (self.WIN_WIDTH, self.WIN_HEIGHT)
        self.BACKGROUND_IMG  = pygame.transform.scale(pygame.image.load("Assets/background.png"), self.RES)
        self.FPS = FPS
        
    def draw_background(self, win):
        win.blit(self.BACKGROUND_IMG, (0, 0))
        
pygame.init()

game = Game(FPS=60)

screen = pygame.display.set_mode(game.RES)
pygame.display.set_caption(game.title)

class Player:
    
    def __init__(self):
        self.VEL = 20
        self.SIZE = 80
        self.PLAYER_IMG = pygame.transform.scale(pygame.image.load("Assets/Cute_mouse.png"), (self.SIZE, self.SIZE))
        self.x = 200
        self.y = 200
        
    def draw_player(self, win):
        win.blit(self.PLAYER_IMG, (self.x, self.y))
        
    def movement(self, keys):
        if keys[pygame.K_w]:
            self.y -= self.VEL
        if keys[pygame.K_s]:
            self.y += self.VEL
        if keys[pygame.K_a]:
            self.x -= self.VEL
        if keys[pygame.K_d]:
            self.x += self.VEL
        
        

def main(game):
    
    running = True
    clock = pygame.time.Clock()
    
    player = Player()
    
    while running:
        
        clock.tick(game.FPS) # limits the fps
        
        print(clock.get_fps())
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        pygame.display.flip()
        
        game.draw_background(screen)
        
        player.draw_player(screen)
        player.movement(keys = pygame.key.get_pressed())
        
    pygame.quit()
    quit()
    
main(game=game)
