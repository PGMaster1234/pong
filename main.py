import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1200, 650))
clock = pygame.time.Clock()
block_up = False
block_down = False
blockY = 200
block_image = pygame.image.load('block.png')
ball_image = pygame.image.load('ball.png')
ballX = 600
ballY = 325
ball_Y_momentum = random.randint(-5, 5)
ball_X_momentum = 10
border_image = pygame.image.load('border.png')
score = 0

#
#
#
#
top_score = 30  # ------------------------ Do you remember typing this
#
#
#
#

font = pygame.font.Font("freesansbold.ttf", 28)
game_over_font = pygame.font.Font("freesansbold.ttf", 50)
game_over = False
game_over_delay = 0
game_running = True
particles = []
ball_collision_with_blockX = []
ball_collision_with_blockY = []
ball_collision_with_block = False
ball_collision_with_barX = []
ball_collision_with_barY = []
ball_collision_with_bar = False
rect_particle_delay = 0
rect_particles = []
thickness_var = 10
boost = 0
using_boost = False


class Color:
    def __init__(self):
        pass

    white = (255, 255, 255)
    black = (0, 0, 0)
    dark_blue = (47, 141, 158)
    blue = (95, 215, 235)
    light_blue = (153, 242, 255)
    dark_brown = (235, 158, 94)
    light_brown = (158, 99, 32)
    orange = (255, 158, 66)
    dull_dark_blue = (97, 161, 179)
    dull_blue = (156, 221, 225)
    teal = (81, 148, 153)


class BlueColorSet:
    def __init__(self):
        pass

    dark_blue = (32, 78, 128)
    grey_dark_blue = (61, 93, 128)
    blue = (98, 149, 204)
    light_blue = (123, 186, 255)
    extra_light_blue = (191, 222, 255)


while game_running:
    ball_collision_with_block = False
    ball_collision_with_blockX = []
    ball_collision_with_blockY = []
    ball_collision_with_barX = []
    ball_collision_with_barY = []
    ball_collision_with_bar = False
    screen.fill(BlueColorSet.grey_dark_blue)
    pygame.draw.rect(screen, BlueColorSet.blue, (pygame.rect.Rect(0, 0, 1100, 50)))
    pygame.draw.rect(screen, BlueColorSet.blue, (pygame.rect.Rect(1100, 0, 100, 650)))
    pygame.draw.rect(screen, BlueColorSet.blue, (pygame.rect.Rect(0, 600, 1100, 50)))
    pygame.draw.rect(screen, BlueColorSet.dark_blue, (pygame.rect.Rect(1090, 50, 10, 550)))
    block_rect = pygame.rect.Rect(100, blockY, 50, 200)
    ball_rect = pygame.Rect(ballX, ballY, 20, 20)
    boost_text = font.render('Boost', True, BlueColorSet.dark_blue)
    screen.blit(boost_text, (400, 15))
    pygame.draw.rect(screen, BlueColorSet.dark_blue, pygame.rect.Rect(500, 20, int(boost), 20), 0)
    pygame.draw.rect(screen, BlueColorSet.light_blue, pygame.rect.Rect(499, 19, 502, 22), 1)
    top_score_text = font.render('Top Score: ' + str(top_score), True, BlueColorSet.dark_blue)
    screen.blit(top_score_text, (175, 15))
    score_text = font.render('Score: ' + str(score), True, BlueColorSet.dark_blue)
    screen.blit(score_text, (25, 15))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                block_up = True
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                block_down = True
            if event.key == pygame.K_g:
                if game_over:
                    if game_over_delay > 60:
                        boost = 0
                        using_boost = False
                        ballX = 600
                        ballY = 325
                        ball_Y_momentum = random.randint(-5, 5)
                        ball_X_momentum = 10
                        score = 0
                        game_over = False
            if event.key == pygame.K_SPACE:
                if boost > 0:
                    using_boost = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                using_boost = False
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                block_up = False
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                block_down = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                clicking = True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                clicking = False

    if using_boost:
        if boost < 1:
            using_boost = False
        if boost > -1:
            boost -= 5
    else:
        if boost < 500:
            if not game_over:
                boost += 1

    if not game_over:
        if block_down:
            if using_boost:
                blockY += 10
            else:
                blockY += 5
        if block_up:
            if using_boost:
                blockY -= 10
            else:
                blockY -= 5

    if blockY < 50:
        blockY = 50
    if blockY > 400:
        blockY = 400
    ballX += ball_X_momentum
    ballY += ball_Y_momentum
    if ballY > 585:
        ballY = 585
        ball_Y_momentum = -ball_Y_momentum
    if ballY < 65:
        ballY = 65
        ball_Y_momentum = -ball_Y_momentum
    if ballX > 1080:
        score += 1
        ball_collision_with_bar = True
        ball_collision_with_barX.append(ballX)
        ball_collision_with_barY.append(ballY)
        if top_score < score:
            top_score += 1
        ballX = 1080
        ball_X_momentum = -ball_X_momentum
    if ball_rect.colliderect(block_rect):
        ball_collision_with_blockX.append(ballX)
        ball_collision_with_blockY.append(ballY)
        ball_collision_with_block = True
        ballX = 150
        ball_X_momentum = -ball_X_momentum
        ball_X_momentum += 1
        random_bounce = random.randint(1, 2)
        if random_bounce == 1:
            ball_Y_momentum = random.randint(-10, -5)
        if random_bounce == 2:
            ball_Y_momentum = random.randint(5, 10)
    if ballX < 0:
        game_over = True
    if game_over:
        game_over_delay += 1
        game_over_text = game_over_font.render('GAME OVER', True, (255, 255, 255))
        press_g = font.render('(Press [g] to play again)', True, (255, 255, 255))
        screen.blit((font.render('Your score was: ' + str(score), True, (255, 255, 255))), (490, 350))
        screen.blit(game_over_text, (450, 300))
        if game_over_delay > 180:
            screen.blit(press_g, (445, 380))
    else:
        game_over_delay = 0

    if rect_particle_delay < 3:
        rect_particle_delay += 1
    else:
        rect_particle_delay = 0

    mx, my = pygame.mouse.get_pos()

    if using_boost:
        if rect_particle_delay == 2:
            rect_particles.append([[100, blockY], thickness_var, 0])

    for rect_particle in rect_particles:
        if rect_particle[1] > 3:
            rect_particle[0][0] -= 2.5
            rect_particle[0][1] -= 2.5
            rect_particle[2] += 5
            pygame.draw.rect(screen, BlueColorSet.extra_light_blue, pygame.rect.Rect(int(rect_particle[0][0]),
                                                                                     int(rect_particle[0][1]),
                                                                                     50 + rect_particle[2],
                                                                                     200 + rect_particle[2]),
                             rect_particle[1])
            if rect_particle_delay == 1:
                rect_particle[1] -= 1
        else:
            rect_particles.remove(rect_particle)
    if ball_collision_with_block:
        for i in range(50):
            particles.append([[(ball_collision_with_blockX[0] + 25), ball_collision_with_blockY[0]],
                              [random.uniform(-1, 1), random.uniform(-1, -3)], random.randint(4, 6)])
    if ball_collision_with_bar:
        for i in range(50):
            particles.append([[(ball_collision_with_barX[0] - 25), ball_collision_with_barY[0]],
                              [random.uniform(-1, 1), random.uniform(-1, -3)], random.randint(4, 6)])
    if score > 2:
        particles.append([[ballX, ballY], [random.uniform(-1, 1), random.uniform(-1, -3)], random.randint(4, 6)])
    for particle in particles:
        particle[0][0] += particle[1][0]
        particle[0][1] += particle[1][1]
        particle[2] -= 0.05
        particle[1][1] += 0.1
        if score < 3:
            pygame.draw.circle(screen, (255, 255, 255), (int(particle[0][0]), int(particle[0][1])), particle[2])
        if score > 2:
            pygame.draw.circle(screen, (201, 151, 32), (int(particle[0][0]), int(particle[0][1])), particle[2])
        if score > 4:
            pygame.draw.circle(screen, (201, 111, 32), (int(particle[0][0]), int(particle[0][1])), particle[2])
        if score > 9:
            pygame.draw.circle(screen, (201, 75, 32), (int(particle[0][0]), int(particle[0][1])), particle[2])
        if score > 14:
            pygame.draw.circle(screen, (201, 32, 32), (int(particle[0][0]), int(particle[0][1])), particle[2])
        if particle[2] <= 0:
            particles.remove(particle)
    if score < 3:
        pygame.draw.circle(screen, (255, 255, 255), (ballX, ballY), 15)
    if score > 2:
        pygame.draw.circle(screen, (201, 151, 32), (ballX, ballY), 15)
    if score > 4:
        pygame.draw.circle(screen, (201, 111, 32), (ballX, ballY), 15)
    if score > 9:
        pygame.draw.circle(screen, (201, 75, 32), (ballX, ballY), 15)
    if score > 14:
        pygame.draw.circle(screen, (201, 32, 32), (ballX, ballY), 15)

    pygame.draw.rect(screen, BlueColorSet.light_blue, (pygame.rect.Rect(100, blockY, 50, 200)))

    clock.tick(60)
    pygame.display.update()
