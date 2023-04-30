import pygame
import sys

pygame.init()
WIN_WIDTH = 900
WIN_HEIGHT = 500
FPS = 60
RED = (255, 0, 0)
BLACK = (255, 255, 255)

window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
#window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Кибер лабиринт")
clock = pygame.time.Clock()
background = pygame.image.load("images\\kiber_fon.jpg")
#pygame.mixer.music.load("sounds\\fon_music.mp3")
#pygame.mixer.music.play()

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, speed, x, y, width, height, image):
        super().__init__()
        self.speed = speed
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.transform.scale(pygame.image.load(image), (width, height))

        self.image_r = self.image
        self.image_l = pygame.transform.flip(self.image, True, False)

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Hero(GameSprite):
    def __init__(self, speed, x, y, width, height, image):
        super().__init__(speed, x, y, width, height, image)
        self.can_move = True
    
    def update(self):
        if self.can_move == True:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP] and self.rect.y > 0:
                self.rect.y -= self.speed
            if keys[pygame.K_DOWN] and self.rect.y + self.rect.width + 1 < 500:
                self.rect.y += self.speed
            if keys[pygame.K_LEFT] and self.rect.x > 0:
                self.rect.x -= self.speed
                self.image = self.image_l
            if keys[pygame.K_RIGHT] and self.rect.x + self.rect.height + 1 < 900:
                self.rect.x += self.speed
                self.image = self.image_r
            if keys[pygame.K_w] and self.rect.y > 0:
                self.rect.y -= self.speed
            if keys[pygame.K_s] and self.rect.y + self.rect.width + 1 < 500:
                self.rect.y += self.speed
            if keys[pygame.K_a] and self.rect.x > 0:
                self.rect.x -= self.speed
                self.image = self.image_l
            if keys[pygame.K_d] and self.rect.x + self.rect.height + 1 < 900:
                self.rect.x += self.speed
                self.image = self.image_r
        window.blit(self.image, (self.rect.x, self.rect.y))

class Enemy(GameSprite):
    def __init__(self, speed, x, y, width, height, image, Finish_x, Finish_y, direction):
        super().__init__(speed, x, y, width, height, image)
        self.direction = direction
        self.start = (x, y)
        self.finish = (Finish_x, Finish_y)
        if self.direction == "left" or self.direction == "up":
            self.start, self.finish = self.finish, self.start

    def update(self):
        if self.rect.x >= self.finish[0]:
            self.direction = "left"
            self.image = self.image_l
        if self.rect.x <= self.start[0]:
            self.direction = "right"
            self.image = self.image_r

        if self.direction == "left" or self.direction == "right":
            if self.direction == "left":
                self.rect.x -= self.speed
            else:
                self.rect.x += self.speed
        
class Wall(pygame.sprite.Sprite):
    def __init__(self, color, x, y, width, height):
        super().__init__()
        self.color = color
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.Surface((width, height))
        self.image.fill(self.color)
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

test1 = Hero(5, 30, 400, 30, 30, "images\\cmert.png")
test2 = Enemy(3, 680, 300, 50, 50, "images\\enemy1.png", 840, 600, "right")
test3 = Enemy(3, 840, 200, 50, 50, "images\\enemy2.png", 680, 600, "left")
test4 = Enemy(3, 680, 100, 50, 50, "images\\enemy1.png", 840, 600, "right")
test5 = GameSprite(0, 730, 380, 150, 100, "images\\prize.png")

walls = pygame.sprite.Group()

wall1 = Wall(RED, 80, 0, 890, 10)
wall1.add(walls)
wall2 = Wall(RED, 890, 10, 10, 350)
wall2.add(walls)
wall3 = Wall(RED, 80, 10, 10, 420)
wall3.add(walls)
wall4 = Wall(RED, 80, 490, 650, 10)
wall4.add(walls)
wall5 = Wall(RED, 720, 400, 10, 90)
wall5.add(walls)
wall6 = Wall(RED, 670, 390, 60, 10)
wall6.add(walls)
wall7 = Wall(RED, 670, 60, 10, 380)
wall7.add(walls)
wall8 = Wall(RED, 560, 60, 120, 10)
wall8.add(walls)
wall9 = Wall(RED, 560, 60, 10, 355)
wall9.add(walls)
wall10 = Wall(RED, 615, 110, 10, 430)
wall10.add(walls)
wall11 = Wall(RED, 300, 405, 260, 10)
wall11.add(walls)
wall12 = Wall(RED, 350, 60, 130, 10)
wall12.add(walls)
wall13 = Wall(RED, 290, 58, 10, 100)
wall13.add(walls)
wall14 = Wall(RED, 290, 158, 140, 10)
wall14.add(walls)
wall15 = Wall(RED, 430, 158, 10, 140)
wall15.add(walls)
wall16 = Wall(RED, 360, 298, 80, 10)
wall16.add(walls)
wall17 = Wall(RED, 360, 298, 10, 50)
wall17.add(walls)
wall18 = Wall(RED, 360, 348, 130, 10)
wall18.add(walls)
wall19 = Wall(RED, 250, 205, 140, 10)
wall19.add(walls)
wall20 = Wall(RED, 300, 255, 90, 10)
wall20.add(walls)
wall21 = Wall(RED, 300, 255, 10, 160)
wall21.add(walls)
wall22 = Wall(RED, 480, 10, 10, 340)
wall22.add(walls)
wall23 = Wall(RED, 240, 88, 10, 410)
wall23.add(walls)
wall24 = Wall(RED, 80, 420, 110, 10)
wall24.add(walls)
wall25 = Wall(RED, 130, 340, 110, 10)
wall25.add(walls)
wall26 = Wall(RED, 80, 280, 110, 10)
wall26.add(walls)
wall27 = Wall(RED, 130, 220, 110, 10)
wall27.add(walls)
wall28 = Wall(RED, 130, 58, 10, 162)
wall28.add(walls)
wall29 = Wall(RED, 180, 10, 10, 162)
wall29.add(walls)

font_10 = pygame.font.SysFont("Comic Sans", 100, True)
txt_lose = font_10.render("YOU LOSE!", False, BLACK)
txt_win = font_10.render("YOU WIN!", False, BLACK)
txt_restart = font_10.render("Press r to restart", False, BLACK)

game = True

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                if test1.can_move == False:
                    test1.kill()
                    test1 = Hero(5, 30, 400, 30, 30, "images\\cmert.png")
                    test1.can_move = True

    window.blit(background, (0, 0))
    test1.update()
    test2.update()
    test2.reset()
    test3.update()
    test3.reset()
    test4.update()
    test4.reset()
    test5.reset()
    walls.draw(window)

    if pygame.sprite.spritecollide(test1, walls, False):
        window.blit(txt_lose, (100, 100))
        window.blit(txt_restart, (100, 250))
        test1.can_move = False
    
    if pygame.sprite.collide_rect(test1, test2):
        window.blit(txt_lose, (100, 100))
        window.blit(txt_restart, (100, 250))
        test1.can_move = False
    
    if pygame.sprite.collide_rect(test1, test3):
        window.blit(txt_lose, (100, 100))
        window.blit(txt_restart, (100, 250))
        test1.can_move = False
    
    if pygame.sprite.collide_rect(test1, test4):
        window.blit(txt_lose, (100, 100))
        window.blit(txt_restart, (100, 250))
        test1.can_move = False
    
    if pygame.sprite.collide_rect(test1, test5):
        window.blit(txt_win, (100, 100))
        window.blit(txt_restart, (100, 250))
        test1.can_move = False

    pygame.display.update()
    clock.tick(FPS)