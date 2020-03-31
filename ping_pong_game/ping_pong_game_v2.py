import pygame
import sys
import random as rd

# Init Pygame Module
pygame.init()

# Game Setting
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Ball Class
class Ball(pygame.sprite.Sprite):
    # Setting
    VELOCITY = (5, 5)
    
    def __init__(self, init_x, init_y, resource, *groups):
        # Init parent class.
        super().__init__(*groups)

        # Override default settings.
        self.image = resource
        self.rect = self.image.get_rect()
        self.rect.center = (init_x, init_y)

        # Attributes
        self.direction = [rd.random() * rd.choice([1, -1]), rd.random() * rd.choice([1, -1])]

    def update(self, *args):
        global ball, objects, clock
        
        # Detect If Collide with wall
        if (self.rect.top <= 0 and self.direction[1] < 0) or (self.rect.bottom >= SCREEN_HEIGHT and self.direction[1] > 0):
            self.direction[1] *= -1
        
        if (self.rect.left <= 0 and self.direction[0] < 0) or (self.rect.right >= SCREEN_WIDTH and self.direction[0] > 0):
            # Remove last ball
            self.groups()[0].remove(ball)

            # Create new ball
            ball = Ball(int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2), r_ball, objects)

            # Delay 1 sec.
            clock.tick(1)

        # Test if collide with tab(args[0] is left tab, arg[1] is right tab)
        if (self.rect.colliderect(args[0].rect) and self.direction[0] < 0) or (self.rect.colliderect(args[1].rect) and self.direction[0] > 0):
            self.direction[0] *= -1

        self.rect.move_ip(self.VELOCITY[0] * self.direction[0], self.VELOCITY[1] * self.direction[1])

# Tab Class
class Tab(pygame.sprite.Sprite):
    # Setting
    VELOCITY = 10
    TAB_WIDTH = 10
    TAB_HEIGHT = 100

    def __init__(self, init_x, init_y, *groups):
        # Init parent class.
        super().__init__(*groups)

        # Override default settings.
        self.image = pygame.Surface((self.TAB_WIDTH, self.TAB_HEIGHT))
        self.image.fill(pygame.Color(0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (init_x, init_y)

        # Attributes
        self.is_up = False
        self.is_down = False

    def update(self, *args):
        # Move The Tab
        if self.is_up and self.rect.top > 0:
            self.rect.move_ip(0, self.VELOCITY * -1)
        
        elif self.is_down and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.move_ip(0, self.VELOCITY)

# Create display and initialize the screen with size of 800 x 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)

# Create clock
clock = pygame.time.Clock()

# Load resources
r_ball = pygame.image.load("basketball.png")

# Create Background
background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
background.fill(pygame.Color(255, 255, 255))

# Draw line and circle at background's center.
pygame.draw.line(
    background,
    pygame.Color(0, 0, 0),
    (SCREEN_WIDTH / 2, 0),
    (SCREEN_WIDTH / 2, SCREEN_HEIGHT),
    10
)

pygame.draw.circle(
    background,
    pygame.Color(0, 0, 0),
    (int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2)),
    50,
    8
)

screen.blit(background, (0, 0))

pygame.display.flip()

# Create groups
objects = pygame.sprite.RenderUpdates()

# Create ball
ball = Ball(int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2), r_ball, objects)

# Create two tabs
left_tab = Tab(int(Tab.TAB_WIDTH / 2), int(SCREEN_HEIGHT / 2), objects)
right_tab = Tab(int(SCREEN_WIDTH - Tab.TAB_WIDTH / 2), int(SCREEN_HEIGHT / 2), objects)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()

            elif event.key == pygame.K_r:
                # Reset Ball
                # Remove last ball
                objects.remove(ball)

                # Create new ball
                ball = Ball(int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2), r_ball, objects)

            elif event.key == pygame.K_w:
                left_tab.is_up = True
                left_tab.is_down = False
            
            elif event.key == pygame.K_s:
                left_tab.is_up = False
                left_tab.is_down = True

            elif event.key == pygame.K_UP:
                right_tab.is_up = True
                right_tab.is_down = False

            elif event.key == pygame.K_DOWN:
                right_tab.is_up = False
                right_tab.is_down = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                left_tab.is_up = False
            
            elif event.key == pygame.K_s:
                left_tab.is_down = False

            elif event.key == pygame.K_UP:
                right_tab.is_up = False

            elif event.key == pygame.K_DOWN:
                right_tab.is_down = False

    objects.clear(screen, background)
    objects.update(left_tab, right_tab, ball)

    # Draw All Object
    dirty_rect = objects.draw(screen)

    pygame.display.update(dirty_rect)

    clock.tick(60)
