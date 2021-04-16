#This is my first sim
#First Pendulum Simulator

import pymunk, pygame, sys

successes, failures = pygame.init()
print("{0} successes and {1} failures".format(successes, failures))

def create_apple(space, pos):
    body = pymunk.Body(1, 100, body_type = pymunk.Body.DYNAMIC)
    body.position = pos
    shape = pymunk.Circle(body, 80)
    space.add(body, shape)
    return shape


def draw_apples(apples):
    for apple in apples:
        pos_x = int(apple.body.position.x)
        pos_y = int(apple.body.position.y)
        pygame.draw.circle(screen,(0,0,0), (pos_x, pos_y), 80)

def static_ball(space):
    body = pymunk.Body(body_type = pymunk.Body.STATIC)
    body.position = (400,400)
    shape = pymunk.Circle(body, 10)
    space.add(body, shape)
    return shape

def draw_static_ball(balls):
    for ball in balls:
        pygame.draw.circle(screen, (0, 0, 0), (400, 400), 10)

screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
space = pymunk.Space()
space.gravity = (0,50)
apples = []

balls = []
balls.append(static_ball(space))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            apples.append(create_apple(space, event.pos))

    screen.fill((217,217,217))
    draw_apples(apples)
    draw_static_ball(balls)
    space.step(1/50)
    pygame.display.update()
    clock.tick(120)


