import os
from collections import deque

import pygame


def main():
    pygame.init()
    length = 1280
    width = 720
    screen = pygame.display.set_mode((length, width))
    clock = pygame.time.Clock()
    running = True
    dt = 0

    quas = pygame.image.load(os.path.join("assets", "quas.png"))
    wex = pygame.image.load(os.path.join("assets", "wex.png"))
    exort = pygame.image.load(os.path.join("assets", "exort.png"))

    elementq = deque(maxlen=3)
    spellq = deque(maxlen=2)
    spell_tensor = {
        0: {0: {"sun_strike"}, 1: {"chaos_meteor"}, 2: {"alacrity"}, 3: {"EMP"}},
        1: {0: {"forge_spirit"}, 1: {"deafening_blast"}, 2: {"tornado"}},
        2: {0: {"ice_wall"}, 1: {"ghost_walk"}},
        3: {0: {"cold_snap"}},
    }

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    elementq.append("q")
                elif event.key == pygame.K_w:
                    elementq.append("w")
                elif event.key == pygame.K_e:
                    elementq.append("e")
                elif event.key == pygame.K_r:
                    if len(elementq) == 3:
                        pass

        screen.fill("black")

        i = -1
        for element in elementq:
            position = (length / 2 + i * 128 - 64, 0)
            i += 1

            if element == "q":
                screen.blit(quas, position)
            elif element == "w":
                screen.blit(wex, position)
            else:
                screen.blit(exort, position)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

    pygame.quit()


if __name__ == "__main__":
    main()
