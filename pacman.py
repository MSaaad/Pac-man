
import pygame
from game import Game

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 576

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption("PACMAN")
    done = False
    clock = pygame.time.Clock()
    game = Game()
    # ==== Main game loop ==== # 
    while not done:
        # ===== keystrokes, mouse clicks ===== #
        done = game.process_events()
        # === game logic ==== #
        game.run_logic()
        game.display_frame(screen)
        clock.tick(45)
    pygame.quit()

if __name__ == '__main__':
    main()
