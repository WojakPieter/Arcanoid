import pygame, random

pygame.init()

height = 600
width = 900
x_pallette = random.randint(60, 750)
y_pallette = 480
x_ball = x_pallette - 50
y_ball = 350
x_vector = 1
y_vector = 1

rectangles = []
counter = 0

for i in range(0, 90):
    rectangles.append(True)


def get_rect_hit_side(x, y):
    global x_vector, y_vector
    x_rect = x*60
    y_rect = y*30
    if x_ball + 15 >= x_rect and x_ball <= x_rect + 50 and y_ball + 15 >= y_rect and y_ball <= y_rect + 20:
        if x_ball + 15 == x_rect or x_ball == x_rect + 50:
            return "leftright"
        elif y_ball == y_rect + 20 or y_ball + 15 == y_rect:
            return "updown"
    else:
        return None


window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Arcanoid")
game_over = pygame.image.load("lose_image.png")
win = pygame.image.load("win_image.jpg")
enabled = True
while enabled:
    pygame.time.delay(2)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            enabled = False
    window.fill((0, 0, 0))
    if y_ball >= height:
        window.fill((0, 0, 0))
        window.blit(game_over, (0, 0))
        enabled = False
    if counter >= 90:
        window.fill((0, 0, 0))
        window.blit(win, (0, 0))
        enabled = False
    keys = pygame.key.get_pressed()
    x_ball += x_vector
    y_ball += y_vector

    if x_ball + 20 >= width or x_ball <= 15:
        x_vector *= (-1)
    if y_ball <= 15:
        y_vector *= (-1)
    if y_ball + 15 <= y_pallette + 15 and y_ball + 15 >= y_pallette - 5 and \
        x_ball + 15 >= x_pallette - 5 and x_ball <= x_pallette + 105:
        y_ball = y_pallette - 30
        y_vector *= (-1)
    if keys[pygame.K_LEFT]:
        if x_pallette > 3:
            x_pallette -= 2
    if keys[pygame.K_RIGHT]:
        if x_pallette + 103 < width:
            x_pallette += 2
    reflected = False
    for x in range(0, 15):
        for y in range(0, 6):
            if rectangles[15*y + x] and not reflected:
                side = get_rect_hit_side(x, y)
                if side == "leftright":
                    x_vector *= (-1)
                if side == "updown":
                    y_vector *= (-1)
                if side is not None:
                    rectangles[15*y + x] = False
                    counter += 1
                    reflected = True
                    
    for m in range(0, 6):
        for i in range(0, 15):
            if rectangles[15*m + i] and enabled:
                pygame.draw.rect(window, (41, 99, 205), (i*60, m*30 + 3, 50, 20))
    if enabled:
        pygame.draw.circle(window, (255, 0, 0), (x_ball, y_ball), 15)
        pygame.draw.rect(window, (144, 144, 0), (x_pallette, y_pallette, 100, 10))
    pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
