import pygame
import time
import random

def main():
    # Need in every use of pygame
    pygame.init()

    display_width = 800
    display_height = 600
    title_of_game = "Jade Plant"

    # Initial setup with the display and title of the window
    # Also sets up the clock
    game_display = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption(title_of_game)
    clock = pygame.time.Clock()

    black = (0, 0, 0)
    white = (255, 255, 255)
    maroon = (140, 29, 64)
    gold = (255, 198, 39)

    jade_img = pygame.image.load("jade_plant.png")
    water_img = pygame.image.load("water.png")

    def things_dodged(count):
        font = pygame.font.SysFont(None, 25)
        text = font.render("Collected: " + str(count), True, gold)
        game_display.blit(text, (0,0))

    def draw_things(thingx, thingy, thingw, thingh, color):
        # First version - pygame.draw.rect(game_display, color, [thingx, thingy, thingw, thingh])
        # Water drop
        game_display.blit(water_img, (thingx, thingy))

    def text_objects(text, font):
        textSurface = font.render(text, True, white)
        return textSurface, textSurface.get_rect()

    def message_display(text):
        largeText = pygame.font.Font('freesansbold.ttf', 75)
        TextSurf, TextRect = text_objects(text, largeText)
        TextRect.center = ((display_width)/2, (display_height/2))
        game_display.blit(TextSurf, TextRect)

        pygame.display.update()

        time.sleep(2)

        game_loop()

    def crash():
        message_display("You hit the wall!")

    def jade(x, y):
        game_display.blit(jade_img, (x,y))

    def game_loop():
        x = (display_width * 0.2)
        y = (display_height * 0.4)

        x_change = 0
        y_change = 0
        speed = 1
        speed_change = 0
        plant_width = 312
        plant_height = 301

        dodged = 0

        # Draw rectangle
        thing_startx = random.randrange(0, display_width)
        thing_starty = -600
        thing_speed = 6
        thing_width = 300
        thing_height = 300
        collected = False

        # Sets up to handle when the user quits the game
        game_exit = False

        while not game_exit:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                # Controlling and moving the jade plant object
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x_change = -5*speed
                    elif event.key == pygame.K_RIGHT:
                        x_change = 5*speed
                    elif event.key == pygame.K_UP:
                        y_change = -5*speed
                    elif event.key == pygame.K_DOWN:
                        y_change = 5*speed
                    elif event.key == pygame.K_BACKSPACE:
                        speed_change = 1
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or \
                            event.key == pygame.K_RIGHT or \
                            event.key == pygame.K_UP or \
                            event.key == pygame.K_DOWN or \
                            event.key == pygame.K_BACKSPACE:
                        x_change = 0
                        y_change = 0
                        speed_change = 0

            x += x_change
            y += y_change
            speed += speed_change

            game_display.fill(maroon)
            jade(x, y)
            things_dodged(dodged)

            draw_things(thing_startx, thing_starty, thing_width, thing_height, black)
            thing_starty += thing_speed

            # Boundaries control
            if x > display_width - plant_width or x < 0:
                crash()
            if y > display_height - plant_height or y < 0:
                crash()

            # Once block leaves screen another one spawns
            if thing_starty > display_height:
                thing_starty = 0 - thing_height
                thing_startx = random.randrange(0, display_width)
                if collected:
                    dodged += 1
                    thing_speed += 1
                    # thing_width += (dodged * 1.2)
                    collected = False

            # Collision detection
            if y < thing_starty + thing_height:

                if (x > thing_startx and x < thing_startx + thing_width) or (x+plant_width > thing_startx and x+plant_width < thing_startx+thing_width):
                    collected = True

            pygame.display.update()
            clock.tick(60)

    game_loop()
    pygame.quit()
    quit()

if __name__ == "__main__":
    main()