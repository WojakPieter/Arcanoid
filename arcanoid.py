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

enabled = []
counter = 0

for i in range(0, 90):
    enabled.append(True)


def is_hit(x, y):
    global x_vector, y_vector
    x_rect = x*60
    y_rect = y*30
    if x_ball + 15 >= x_rect and x_ball <= x_rect + 50 and y_ball + 15 >= y_rect and y_ball <= y_rect + 20:
        if x_ball + 15 == x_rect or x_ball == x_rect + 50:
            return "bok"
        elif y_ball == y_rect + 20 or y_ball + 15 == y_rect:
            return "sufit/dol"
    else:
        return False


okno = pygame.display.set_mode((width, height))
pygame.display.set_caption("Arcanoid")
game_over = pygame.image.load("lose_image.png")
win = pygame.image.load("win_image.jpg")
done = True
while done:
    pygame.time.delay(2)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
    keys = pygame.key.get_pressed()
    x_ball += x_vector
    y_ball += y_vector

    if x_ball + 20 >= width or x_ball <= 15:
        x_vector *= (-1)
    if y_ball <= 15 or ((y_ball + 15) <= y_pallette+15 and y_ball + 15 >=
                        y_pallette - 5 and x_ball + 15 >= x_pallette - 5 and x_ball <= x_pallette + 105):
        y_vector *= (-1)
    if keys[pygame.K_LEFT]:
        if x_pallette > 3:
            x_pallette -= 2
    if keys[pygame.K_RIGHT]:
        if x_pallette + 103 < width:
            x_pallette += 2
    odbity = False
    for x in range(0, 15):
        for y in range(0, 6):
            if is_hit(x, y) == "bok" and odbity == False:
                if enabled[15*y + x]:
                    enabled[15*y + x] = False
                    counter += 1
                    x_vector *= (-1)

                    odbity = True
            elif is_hit(x, y) == "sufit/dol" and odbity == False:
                if enabled[15*y + x]:
                    enabled[15*y + x] = False
                    counter += 1
                    y_vector *= (-1)
                    odbity = True
    okno.fill((0, 0, 0))
    if y_ball >= height:
        okno.fill((0, 0, 0))
        okno.blit(game_over, (0, 0))
        done = False
    if counter >= 90:
        okno.fill((0, 0, 0))
        okno.blit(win, (0, 0))
        done = False
    for m in range(0, 6):
        for i in range(0, 15):
            if enabled[15*m + i] and done:
                pygame.draw.rect(okno, (41, 99, 205), (i*60, m*30 + 3, 50, 20))
    if done:
        pygame.draw.circle(okno, (255, 0, 0), (x_ball, y_ball), 15)
        pygame.draw.rect(okno, (144, 144, 0), (x_pallette, y_pallette, 100, 10))
    pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
