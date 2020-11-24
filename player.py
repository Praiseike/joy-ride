import gameObject

class player(gameObject.GameObject):
    

    def __init__self(self,image,name,pos=(0,0)):
        self.speed = 3
        super.__init__(image,speed,pos)
        self.player_id = ""
        self.play_name = ""
        self.play_health = 100
        self.play_lives = 3
        print("Created play")
    
    def __del__(self):
        print("Player "+self.play_name+" is dead")

