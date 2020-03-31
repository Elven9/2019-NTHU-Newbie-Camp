import pygame
import sys

# Init Pygame Module
pygame.init()

# Game Setting
Screen_width = 800
Screen_height = 600

# Clock
clock = pygame.time.Clock()

# Create display and initialize the screen with size of 800 x 600
screen = pygame.display.set_mode((Screen_width, Screen_height), pygame.FULLSCREEN)

# Two Tabs Y Position
Tab_length = 100
Tab_width = 10
Tab_speed = 20

tab_left_y = int(Screen_height / 2 - Tab_length / 2)
tab_right_y = int(Screen_height / 2 - Tab_length / 2)

# Create ball and define its position and velocity
ball = pygame.image.load("basketball.png")
ball_width = ball.get_width()
ball_height = ball.get_height()

ball_x = int(Screen_width / 2) - 20
ball_y = int(Screen_height / 2)

ball_velocity_x = 10
ball_velocity_y = 10

# Loop
while True:
    print(clock.get_fps())

    # Dirty Rect
    dirty_rect = []

    # Process Event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            # Detect which key.
            if event.key == pygame.K_w:
                if tab_left_y - Tab_speed > 0: tab_left_y -= Tab_speed

            elif event.key == pygame.K_s:
                if tab_left_y + Tab_speed < Screen_height - Tab_length: tab_left_y += Tab_speed

            elif event.key == pygame.K_UP:
                if tab_right_y - Tab_speed > 0: tab_right_y -= Tab_speed

            elif event.key == pygame.K_DOWN:
                if tab_right_y + Tab_speed < Screen_height - Tab_length: tab_right_y += Tab_speed
            
            elif event.key == pygame.K_q:
                sys.exit()
            
            # Append left tab to dirty rect list.
            dirty_rect.append(pygame.Rect(0, tab_left_y, Tab_width, Tab_length))
            dirty_rect.append(pygame.Rect(Screen_width - Tab_width, tab_right_y, Tab_width, Tab_length))

    # Clear surface and fill background color with white.
    screen.fill(pygame.Color(255, 255, 255))

    # Draw line and circle at screen's center.
    pygame.draw.line(
        screen,
        pygame.Color(0, 0, 0),
        (Screen_width / 2, 0),
        (Screen_width / 2, Screen_height),
        10
    )

    pygame.draw.circle(
        screen,
        pygame.Color(0, 0, 0),
        (int(Screen_width / 2), int(Screen_height / 2)),
        50,
        8
    )

    # Draw two Tab
    pygame.draw.polygon(
        screen,
        pygame.Color(0, 0, 0),
        [(0, tab_left_y), (Tab_width, tab_left_y), (Tab_width, tab_left_y + Tab_length), (0, tab_left_y + Tab_length)]
    )

    pygame.draw.polygon(
        screen,
        pygame.Color(0, 0, 0),
        [(Screen_width - Tab_width, tab_right_y), (Screen_width, tab_right_y), (Screen_width, tab_right_y + Tab_length), (Screen_width - Tab_width, tab_right_y + Tab_length)]
    )

    # Logic of ball
    # Bounce between wall
    if ball_x + ball_width / 2 + ball_velocity_x >= Screen_width and ball_velocity_x > 0:
        # The ball touches right-side wall
        ball_velocity_x *= -1

    elif ball_x - ball_width - ball_velocity_x / 2 <= 0 and ball_velocity_x < 0:
        # The ball touches left-side wall
        ball_velocity_x *= -1
    
    if ball_y + ball_height / 2 + ball_velocity_y >= Screen_height or ball_y - ball_height / 2 + ball_velocity_y <= 0:
        ball_velocity_y *= -1
    
    # Add original rect to dirty rect list.
    dirty_rect.append(pygame.Rect(ball_x - ball_width / 2, ball_y + ball_height / 2, ball_width, ball_height))
    
    ball_x += ball_velocity_x
    ball_y += ball_velocity_y

    # Add new rect to dirty rect list
    dirty_rect.append(pygame.Rect(ball_x - ball_width / 2, ball_y + ball_height / 2, ball_width, ball_height))
    
    # Draw Ball
    screen.blit(ball, (ball_x - ball_width / 2, ball_y - ball_height / 2))

    # Update Content to display
    pygame.display.update(dirty_rect)

    clock.tick()