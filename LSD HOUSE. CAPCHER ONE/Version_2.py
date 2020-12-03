import pygame
from random import choice

# Функция градиента
'''def gradientRect(window, left_colour, right_colour, target_rect):
    """ Draw a horizontal-gradient filled rectangle covering <target_rect> """
    colour_rect = pygame.Surface((2, 2))  # tiny! 2x2 bitmap
    pygame.draw.line(colour_rect, left_colour, (0, 0), (0, 1))  # left colour line
    pygame.draw.line(colour_rect, right_colour, (1, 0), (1, 1))  # right colour line
    colour_rect = pygame.transform.smoothscale(colour_rect, (target_rect.width, target_rect.height))  # stretch!
    window.blit(colour_rect, target_rect)  # paint it'''


class Main:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('LSD/Sweet house')
        self.size = self.width, self.height = 800, 800
        self.screen = pygame.display.set_mode(self.size)
        self.fps = 7
        self.clock = pygame.time.Clock()

    def lsd_corridor(self):
        self.screen.fill((0, 0, 0))

        font = pygame.font.Font("BAUHS93.TTF", 50)
        text = font.render("Welcome to the LSD house!", True,
                           (choice(range(255)), choice(range(255)), choice(range(255))))
        text_x = self.width // 2 - text.get_width() // 2
        text_y = self.height // 2 - text.get_height() // 2
        text_w = text.get_width()
        text_h = text.get_height()
        self.screen.blit(text, (text_x, text_y - 50))
        pygame.draw.rect(self.screen, (choice(range(255)), choice(range(255)), choice(range(255))),
                         (text_x - 10, text_y - 60, text_w + 20, text_h + 20), 1)

    def lsd_room_1(self):
        self.screen.fill((0, 0, 0))
        font = pygame.font.Font("BAUHS93.TTF", 48)
        text = font.render("Loading LSD room 1, please wait...", True,
                           (choice(range(255)), choice(range(255)), choice(range(255))))
        text_x = self.width // 2 - text.get_width() // 2
        text_y = self.height // 2 - text.get_height() // 2
        text_w = text.get_width()
        text_h = text.get_height()
        self.screen.blit(text, (text_x, text_y - 50))
        pygame.draw.rect(self.screen, (choice(range(255)), choice(range(255)), choice(range(255))),
                         (text_x - 10, text_y - 60, text_w + 20, text_h + 20), 1)

    def lsd_room_2(self):
        self.screen.fill((0, 0, 0))
        font = pygame.font.Font("BAUHS93.TTF", 48)
        text = font.render("Loading LSD room 2, please wait...", True,
                           (choice(range(255)), choice(range(255)), choice(range(255))))
        text_x = self.width // 2 - text.get_width() // 2
        text_y = self.height // 2 - text.get_height() // 2
        text_w = text.get_width()
        text_h = text.get_height()
        self.screen.blit(text, (text_x, text_y - 50))
        pygame.draw.rect(self.screen, (choice(range(255)), choice(range(255)), choice(range(255))),
                         (text_x - 10, text_y - 60, text_w + 20, text_h + 20), 1)

    def lsd_room_3(self):
        self.screen.fill((0, 0, 0))
        font = pygame.font.Font("BAUHS93.TTF", 48)
        text = font.render("Loading LSD room 3, please wait...", True,
                           (choice(range(255)), choice(range(255)), choice(range(255))))
        text_x = self.width // 2 - text.get_width() // 2
        text_y = self.height // 2 - text.get_height() // 2
        text_w = text.get_width()
        text_h = text.get_height()
        self.screen.blit(text, (text_x, text_y - 50))
        pygame.draw.rect(self.screen, (choice(range(255)), choice(range(255)), choice(range(255))),
                         (text_x - 10, text_y - 60, text_w + 20, text_h + 20), 1)

    def main(self):
        active = True
        while active:
            self.lsd_corridor()
            self.clock.tick(self.fps)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    active = False
                elif event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_1:
                        lsd_1_active = True
                        while lsd_1_active:
                            for event_2 in pygame.event.get():
                                if event_2.type == pygame.QUIT:
                                    lsd_1_active = False
                            self.lsd_room_1()
                            self.clock.tick(self.fps)
                            pygame.display.flip()

                    elif event.key == pygame.K_2:
                        lsd_2_active = True
                        while lsd_2_active:
                            for event_2 in pygame.event.get():
                                if event_2.type == pygame.QUIT:
                                    lsd_2_active = False
                            self.lsd_room_2()
                            self.clock.tick(self.fps)
                            pygame.display.flip()

                    elif event.key == pygame.K_3:
                        lsd_3_active = True
                        while lsd_3_active:
                            for event_2 in pygame.event.get():
                                if event_2.type == pygame.QUIT:
                                    lsd_3_active = False
                            self.lsd_room_3()
                            self.clock.tick(self.fps)
                            pygame.display.flip()
        pygame.quit()


if __name__ == '__main__':
    Main().main()
