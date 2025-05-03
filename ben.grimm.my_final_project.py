# Ben Grimm
# Period 4
# Final Project: The Best Clicker Game Ever Conceived by Man
# The user clicks a cookie and buys upgrades!
# Upgrades correspond with each other and each click

import pygame
import time

def main():
    """
    The main function that runs the game
    """

    pygame.init()

    name = input("Name your cookie: ")

    ### VARIABLES, SCREEN, AND TEXT SETUP ###

    HEIGHT = 720
    WIDTH = 720

    SIZE = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(SIZE)

    clock = pygame.time.Clock()

    running = True

    size = 5
    score = 3000
    multiplier = 1
    multiplier_price = 50

    tophat_price = 100000000
    tophat_bought = False
    auto_click_bought = False

    autoclick = 0
    auto_click_amount = 250
    autoclick_price = 1000

    autoclick_speed = 0
    auto_click_speed_amount = 0.9
    autoclick_speed_price = 2500

    score_font = pygame.font.SysFont(None, 45)
    multiplier_font = pygame.font.SysFont(None, 20)
    autoclick_font = pygame.font.SysFont(None, 20)
    regular_font = pygame.font.SysFont(None, 40)

    class Text:
        """
        A text class that can create the text for the game

        """

        def __init__(self, font, text, x, y):
            """
            Constructor, all the values for the text to be created as its own unique text

            :param font: The font and size of the text
            :param text: The actual text in it
            :param x: The x position of the text
            :param y: The y position of the text
            """
            self.__font = font
            self.__text = text
            self.__x = x
            self.__y = y

        ## GETTER AND SETTERS ##

        def get_font(self):
            return self.__font

        def set_font(self, font):
            self.__font = font

        def get_text(self):
            return self.__text

        def set_text(self, text):
            self.__text = text

        ## END OF GETTER AND SETTERS ##

        def update_text(self):
            """
            This function creates and allows for updates to the text

            :return: rendered_text and text_rect - The entire text object itself and its rect that are needed to create the text
            """
            rendered_text = self.__font.render(self.__text, True, (0, 0, 0), None)
            text_rect = rendered_text.get_rect()
            text_rect.center = (self.__x, self.__y)
            return rendered_text, text_rect

    score_text = Text(score_font, "Clicks: " + str(score), WIDTH // 2, 50)
    multiplier_text = Text(multiplier_font, "Multiplier " + str(multiplier * 2) + "x: $" + str(multiplier_price), 80 , 195)
    autoclick_text = Text(autoclick_font, "Autoclick " + str(autoclick + 1) + ": $" + str(autoclick_price), 640 , 195)
    autoclick_speed_text = Text(autoclick_font, "Need: Autoclick", 640 , 295)
    reset_text = Text(regular_font, "Press \"R\" to reset progress", 360 , 700)
    cookie_name_text = Text(regular_font, str(name), 360, 480)
    top_hat_text = Text(multiplier_font, "Top Hat: $1M", 80, 595)

    last_click_time = 0
    last_autoclick_time = time.time()

    ### END OF VARIABLES AND TEXT SETUP ###

    def draw_cookie(screen, size):
        """
        This function creates the main cookie that the user clicks
        :param screen: The window that it is created on
        :param size: An integer - The size that the cookie is scaled pff of when it is clicked
        :return: The cookie rect, in order to change its size
        """

        cookie = pygame.draw.circle(screen, (206, 154, 114), (360, 360), 80 + size)
        chip1 = pygame.draw.circle(screen, (20, 15, 14), (400, 340), 15 + (size - 5))
        chip2 = pygame.draw.circle(screen, (20, 15, 14), (320, 370), 11 + (size - 5))
        chip3 = pygame.draw.circle(screen, (20, 15, 14), (380, 400), 19 + (size - 5))
        chip4 = pygame.draw.circle(screen, (20, 15, 14), (330, 320), 13 + (size - 5))
        return cookie

    def draw_multiplier_button(screen):
        """
        This function creates the multiplier button that the user can click
        :param screen: The window that it is created on
        :return: The main button rect
        """

        # button_background = pygame.draw.rect(screen, (10, 10, 10), (575, 15, 130, 90))
        multi_button = pygame.draw.rect(screen, (230, 230, 230), (20, 155, 120, 80))
        return multi_button

    def draw_autoclick_button(screen):
        """
        This function creates the autoclicker button that the user can click
        :param screen: The window that it is created on
        :return: The main button rect
        """

        # button_background = pygame.draw.rect(screen, (10, 10, 10), (575, 150, 130, 90))
        auto_button = pygame.draw.rect(screen, (230, 230, 230), (580, 155, 120, 80))
        return auto_button

    def draw_autoclick_speed_button(screen):
        """
        This function creates the auto click speed button that the user can click
        :param screen: The window that it is created on
        :return: The main button rect
        """
        # button_background = pygame.draw.rect(screen, (10, 10, 10), (575, 250, 130, 90))
        auto_speed_button = pygame.draw.rect(screen, (230, 230, 230), (580, 255, 120, 80))
        return auto_speed_button

    def draw_tophat_button(screen):
        """
        This function creates the top hat button that the user can click
        :param screen: The window that it is created on
        :return: The main button rect
        """

        # button_background = pygame.draw.rect(screen, (10, 10, 10), (575, 15, 130, 90))
        top_hat_button = pygame.draw.rect(screen, (230, 230, 230), (20, 555, 120, 80))
        return top_hat_button

    def draw_tophat(screen):
        """
        This function creates the top hat accessory and puts it on the cookie
        :param screen: The window that it is created on
        :return: Nothing
        """

        bottom = pygame.draw.rect(screen, (15, 15, 15), (272, 280, 180, 30))
        middle = pygame.draw.rect(screen, (220, 10, 10), (290, 260, 140, 20))
        top = pygame.draw.rect(screen, (15, 15, 15), (290, 160, 140, 100))

    # While the window is running, keep the screen drawn and updated, along with tracking time
    while running:

        screen.fill((255, 255, 255))

        ### SHAPE CREATORS ###

        the_cookie = draw_cookie(screen, size)
        colliding_cookie = the_cookie.collidepoint(pygame.mouse.get_pos())

        the_multiplier_button = draw_multiplier_button(screen)
        colliding_multi_button = the_multiplier_button.collidepoint(pygame.mouse.get_pos())

        the_autoclick_button = draw_autoclick_button(screen)
        colliding_auto_button = the_autoclick_button.collidepoint(pygame.mouse.get_pos())

        the_autoclick_speed_button = draw_autoclick_speed_button(screen)
        colliding_auto_speed_button = the_autoclick_speed_button.collidepoint(pygame.mouse.get_pos())

        the_tophat_button = draw_tophat_button(screen)
        colliding_tophat_button = the_tophat_button.collidepoint(pygame.mouse.get_pos())

        if tophat_bought:
            draw_tophat(screen)

        ### END OF SHAPE CREATORS ###

        # User Input Events
        for event in pygame.event.get():

            # If the user quits, set the variable "running" to false in order to close the window
            if event.type == pygame.QUIT:
                running = False

            # If the user clicks the cookie, make it change size to show it got clicked and add to the score along with update it
            if event.type == pygame.MOUSEBUTTONDOWN and colliding_cookie:
                score += multiplier
                size = 10
                last_click_time = time.time()
                score_text = Text(score_font, "Clicks: " + str(int(score)), WIDTH // 2, 50)

            # If the user clicks the multiplier button, and they have enough clicks, change and update the multiplier amount and price along with getting rid of the clicks that they spent
            if event.type == pygame.MOUSEBUTTONDOWN and colliding_multi_button and (score >= multiplier_price):
                score -= multiplier_price
                multiplier *= 2
                multiplier_price *= 3
                if auto_click_bought:
                    auto_click_amount = int((0.5 * multiplier) * autoclick + 1)

                multiplier_text = Text(multiplier_font,"Multiplier " + str(multiplier * 2) + "x: $" + str(multiplier_price), 80, 195)
                score_text = Text(score_font, "Clicks: " + str(int(score)), WIDTH // 2, 50)

            # If the user clicks the auto clicker button, and they have enough clicks, change and update the autoclicker
            # amount and price along with getting rid of the clicks that they spent
            if event.type == pygame.MOUSEBUTTONDOWN and colliding_auto_button and (score >= autoclick_price):
                score -= autoclick_price
                auto_click_bought = True
                autoclick += 1
                auto_click_amount = int((0.5 * multiplier) * autoclick + 1)

                autoclick_price *= 2
                autoclick_text = Text(autoclick_font, "Autoclick " + str(autoclick + 1) + ": $" + str(autoclick_price), 640 , 195)
                # If the speed has not been maxed, update it again
                if auto_click_speed_amount >= 0.1125:
                    autoclick_speed_text = Text(autoclick_font, "Speed " + str(autoclick_speed + 1) + ": $" + str(autoclick_speed_price), 640, 295)
                score_text = Text(score_font, "Clicks: " + str(int(score)), WIDTH // 2, 50)

            # If the user clicks the auto click speed button, and they have enough clicks, and they have
            # bought the auto click button, change and update the auto click speed amount and price along with
            # getting rid of the clicks that they spent
            if autoclick > 0:
                if event.type == pygame.MOUSEBUTTONDOWN and (score >= autoclick_speed_price) and colliding_auto_speed_button:
                    score -= autoclick_speed_price
                    autoclick_speed += 1
                    # If the speed has not been maxed, keep increasing it and updating it
                    if auto_click_speed_amount >= 0.1125:
                        auto_click_speed_amount /= 2
                        autoclick_speed_price *= 4
                        autoclick_speed_text = Text(autoclick_font, "Speed " + str(autoclick_speed + 1) + ": $" + str(autoclick_speed_price), 640, 295)

                    else:
                        autoclick_speed_text = Text(autoclick_font, "MAX", 640, 295)

                    score_text = Text(score_font, "Clicks: " + str(int(score)), WIDTH // 2, 50)

            # If the user clicks the top hat button with enough clicks, give the cookie a top hat and multiply
            # the multiplier by 10
            if event.type == pygame.MOUSEBUTTONDOWN and colliding_tophat_button and (score >= tophat_price) and not tophat_bought:
                score -= tophat_price
                multiplier *= 10
                print("Buying the top hat increased your aura! Multiplier increased by 10x!!!")
                tophat_bought = True
                top_hat_text = Text(multiplier_font, "Purchased", 80, 595)
                multiplier_text = Text(multiplier_font,"Multiplier " + str(multiplier * 10) + "x: $" + str(multiplier_price), 80, 195)
                score_text = Text(score_font, "Clicks: " + str(int(score)), WIDTH // 2, 50)

            # If the user clicks "R" to restart, set everything back to its default
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    autoclick = 0
                    autoclick_amount = 0
                    autoclick_price = 1000
                    tophat_bought = False
                    auto_click_bought = False
                    score = 0
                    multiplier = 1
                    multiplier_price = 50
                    autoclick_speed = 0
                    auto_click_speed_amount = 0.9
                    autoclick_speed_price = 2500
                    autoclick_text = Text(autoclick_font, "Autoclick " + str(autoclick + 1) + ": $" + str(autoclick_price), 640 , 195)
                    top_hat_text = Text(multiplier_font, "Top Hat: $1M", 80, 595)
                    autoclick_speed_text = Text(autoclick_font, "Need: Autoclick", 640 , 295)
                    multiplier_text = Text(multiplier_font, "Multiplier " + str(multiplier * 2) + "x: $" + str(multiplier_price), 80 , 195)
                    score_text = Text(score_font, "Clicks: " + str(int(score)), WIDTH // 2, 50)


        ### TEXT UPDATERS ###

        rendered_score, score_rect = score_text.update_text()
        rendered_multiplier, multiplier_rect = multiplier_text.update_text()
        rendered_autoclick, autoclick_rect = autoclick_text.update_text()
        rendered_autoclick_speed, autoclick_speed_rect = autoclick_speed_text.update_text()
        rendered_reset, reset_rect = reset_text.update_text()
        rendered_cookie_name, cookie_name_rect = cookie_name_text.update_text()
        rendered_tophat, tophat_rect = top_hat_text.update_text()

        screen.blit(rendered_score, score_rect)
        screen.blit(rendered_multiplier, multiplier_rect)
        screen.blit(rendered_autoclick, autoclick_rect)
        screen.blit(rendered_autoclick_speed, autoclick_speed_rect)
        screen.blit(rendered_reset, reset_rect)
        screen.blit(rendered_cookie_name, cookie_name_rect)
        screen.blit(rendered_tophat, tophat_rect)

        ### END OF TEXT UPDATERS ###

        # If the user had clicked the cookie, and it has been sized to 10 for 0.05 seconds, set it back to normal
        if size == 10 and time.time() - last_click_time > 0.05:
            size = 5

        current_time = time.time()
        # If the autoclicker has been purchased at least once, start the autoclick and have it update by its value every second
        if autoclick > 0 and current_time - last_autoclick_time >= (1 * auto_click_speed_amount):
            score += auto_click_amount
            score_text = Text(score_font, "Clicks: " + str(score), WIDTH // 2, 50)
            last_autoclick_time = time.time()

        pygame.display.flip()
main()