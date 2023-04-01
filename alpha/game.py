import pygame as gaming
import random as random
import time as time

class game():

    def __init__(self):
        gaming.init()

        self.width = 900
        self.height = 500

        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.BLUE = (0, 0, 255)
        self.RED = (255, 0, 0)

        self.x = self.width / 2
        self.y = self.height / 2

        self.snake_block = 10

        self.food_block = 10

        self.Screen = gaming.display.set_mode((self.width, self.height))
        gaming.display.set_caption("2D game")

        self.stop = False

        self.x_change = 0
        self.y_change = 0

        self.speed_neg = -5
        self.speed_pos = 5

        self.Clock = gaming.time.Clock()
        self.FPS = 30

        self.bg = gaming.transform.scale(gaming.image.load('bg.png'), (self.width, self.height))

        self.x_food = round(random.randint(0, self.width - self.x - self.snake_block) // 10 ) * 10 
        self.y_food = round(random.randint(0, self.height - self.y - self.snake_block) // 10 ) * 10

        self.font = None
        self.Text_size = 50
        self.Text_score_size = 25

        self.Font = gaming.font.SysFont(self.font, self.Text_size)

        self.gameover = False

        self.score = 0

        self.block = 10

        self.score_font = gaming.font.SysFont(self.font, self.Text_score_size)

        self.eat_sound = gaming.mixer.Sound('food.mp3')

    def message(self, msg, COLOR):
        self.mesg = self.Font.render(msg, True, COLOR)
        self.Screen.blit(self.mesg, (self.width // 10, self.height // 3))

    def score_message(self, msg, COLOR):
        self.value = self.score_font.render(msg, True, COLOR)
        self.Screen.blit(self.value, [0, 0])
    def draw(self):
        self.Screen.blit(self.bg, (0, 0))
        gaming.draw.rect(self.Screen, self.RED, (self.x, self.y, self.snake_block, self.snake_block))
        gaming.draw.rect(self.Screen, self.BLACK, (self.x_food, self.y_food, self.food_block, self.food_block))
        if self.x <= -3 or self.x >= self.width or self.y <= 0 or self.y >= self.height:
            self.gameover = True
        if self.gameover:
            self.message("To play again click R or To quit click Q ", self.RED)
            gaming.display.update()
            for event in gaming.event.get():
                if event.type == gaming.KEYDOWN:
                    if event.key == gaming.K_q:
                        self.stop = True
                        self.gameover = False
                    if event.key == gaming.K_r:
                        game().gameloop()
        self.score_message("Your Score = " + str(self.score), self.BLUE)  
        gaming.display.update()
    def control(self):
        for event in gaming.event.get():
            if event.type == gaming.QUIT:
                self.stop = True
            if event.type == gaming.KEYDOWN:
                if event.key == gaming.K_w:
                    self.y_change = self.speed_neg
                    self.x_change = 0
                elif event.key == gaming.K_s:
                    self.y_change = self.speed_pos
                    self.x_change = 0
                elif event.key == gaming.K_a:
                    self.x_change = self.speed_neg
                    self.y_change = 0
                elif event.key == gaming.K_d:
                    self.x_change = self.speed_pos
                    self.y_change = 0
        self.x += self.x_change
        self.y += self.y_change
        if self.x == self.x_food and self.y == self.y_food:
            self.x_food = round(random.randint(0, self.width - self.snake_block - self.x) // 10 ) * 10 
            self.y_food = round(random.randint(0, self.height - self.snake_block - self.y) // 10 ) * 10
            self.score += 1
            gaming.mixer.Sound.play(self.eat_sound)
            gaming.mixer.music.stop()
    def gameloop(self):
        while not self.stop:
            self.control()
            self.Clock.tick(self.FPS)    
            self.draw()
        quit()

if __name__ == "__main__":
    game().gameloop()
