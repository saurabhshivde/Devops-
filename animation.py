import pygame

pygame.init()

# set up the window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Train Animation")

# set up the train image and position
train_image = pygame.image.load('train.png')
train_rect = train_image.get_rect()
train_x = -train_rect.width

# set up the background image and position
background_image = pygame.image.load('background.png')
background_rect = background_image.get_rect()

# set up the clock
clock = pygame.time.Clock()

# main game loop
running = True
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # update the train position
    train_x += 5
    if train_x > WINDOW_WIDTH:
        train_x = -train_rect.width
    
    # draw the background and train
    window.blit(background_image, background_rect)
    window.blit(train_image, (train_x, WINDOW_HEIGHT - train_rect.height))
    
    # update the display
    pygame.display.update()
    
    # limit the frame rate
    clock.tick(60)

# clean up
pygame.quit()

