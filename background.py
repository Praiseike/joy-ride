import gameObject,pygame

class Background(gameObject.GameObject):

    images = []

    def __init__(self,background_filename="assets/background/double_spring.png",pos = pygame.Rect(0,0,0,0)):
        self.xvel = self.yvel= 1
        self.pos = pos
        self.x = 0
        self.scroll_speed = 10
        self.image = pygame.image.load(background_filename).convert_alpha()
        self.image = pygame.transform.scale(self.image,(1800,600))
        self.image_rect = self.image.get_rect()
       
        

    def move(self):
        #TODO 
        """ Custom movement implemetation """

    def draw(self,screen):
        self.move()
        if(self.x == -self.image_rect.width/2):
            self.x = 0
        self.x -= self.scroll_speed
        screen.blit(self.image,(self.x,0))


