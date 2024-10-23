import os
from collections import deque

import pygame


def invoke(elementq: deque) -> tuple[int, int]:
    quas = 0
    wex = 0

    for element in elementq:
        if element == "q":
            quas += 1
        elif element == "w":
            wex += 1

    return quas, wex


def main():
    pygame.init()
    length = 1280
    width = 720
    screen = pygame.display.set_mode((length, width))
    pygame.display.set_caption("Invoker Trainee")
    clock = pygame.time.Clock()
    running = True
    dt = 0

    quas = pygame.image.load(os.path.join("assets", "quas.png"))
    wex = pygame.image.load(os.path.join("assets", "wex.png"))
    exort = pygame.image.load(os.path.join("assets", "exort.png"))

    elementq = deque(maxlen=3)
    spellq = deque(maxlen=2)
    spell_tensor = {
        0: {
            0: pygame.image.load(os.path.join("assets", "sun_strike.png")),
            1: pygame.image.load(os.path.join("assets", "chaos_meteor.png")),
            2: pygame.image.load(os.path.join("assets", "alacrity.png")),
            3: pygame.image.load(os.path.join("assets", "EMP.png")),
        },
        1: {
            0: pygame.image.load(os.path.join("assets", "forge_spirit.png")),
            1: pygame.image.load(os.path.join("assets", "deafening_blast.png")),
            2: pygame.image.load(os.path.join("assets", "tornado.png")),
        },
        2: {
            0: pygame.image.load(os.path.join("assets", "ice_wall.png")),
            1: pygame.image.load(os.path.join("assets", "ghost_walk.png")),
        },
        3: {0: pygame.image.load(os.path.join("assets", "cold_snap.png"))},
    }

    font = pygame.font.Font("freesansbold.ttf", 32)
    spell_slot0 = font.render("D", True, (255, 255, 255))
    slot0_rect = spell_slot0.get_rect()
    slot0_rect.center = (length / 2 - 64, width / 2 - 64 - 32)
    spell_slot1 = font.render("F", True, (255, 255, 255))
    slot1_rect = spell_slot1.get_rect()
    slot1_rect.center = (length / 2 + 64, width / 2 - 64 - 32)

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
                        spell = invoke(elementq)

                        if len(spellq) == 0 or spellq[-1] != spell:
                            spellq.append(spell)

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

        i = -1
        for j, k in reversed(spellq):
            position = (length / 2 + i * 128, width / 2 - 64)
            i += 1

            spell_image = spell_tensor[j][k]
            screen.blit(spell_image, position)

        screen.blit(spell_slot0, slot0_rect)
        screen.blit(spell_slot1, slot1_rect)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

    pygame.quit()


if __name__ == "__main__":
    main()
