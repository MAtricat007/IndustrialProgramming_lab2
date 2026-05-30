import pygame as pg
from player import Player
from platforms import Platform
from level_test import Level
from ghost import Ghost
from mele_attack import Mele_attack
from healthbar import Healthbar_red
from healthbar import Healthbar_green
import sys
import time
import random as r

room_prCH = [
    ["|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|"],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    ["|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|"],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    ["=", " ", "=", " ", "=", " ", "=", " ", "=", " ", "=", " ", "=", " ", "=", " ", "=", " ", "=", " "],
    ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    ["=", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "=", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ["=", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "=", " "],
    ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    ['=', ' ', '=', ' ', '=', ' ', '=', ' ', '=', ' ', '=', ' ', '=', ' ', '=', ' ', '=', ' ', '=', ' '],
    ["|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|"],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    ["|", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', "|"],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
]

room_prCV = [
    ["=", " ", "=", " ", "=", " ", "=", " ", " ", " ", "_", "_", "=", " ", "=", " ", "=", " ", "=", " "],
    [" ", " ", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", "|", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", "_", "_", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", ' ', ' ', ' ', ' ', ' ', ' ', "|", ' ', ' ', ' ', ' ', "|", ' ', ' ', ' ', ' ', ' ', ' ', " "],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [" ", ' ', ' ', ' ', ' ', ' ', ' ', "|", ' ', ' ', ' ', ' ', "|", ' ', ' ', ' ', ' ', ' ', ' ', " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", '_', '_', " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", "|", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", ' ', ' ', " ", " ", " ", " ", " ", " ", " ", " "],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', "|", ' ', ' ', ' ', ' ', "|", ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [" ", " ", " ", " ", " ", " ", " ", " ", '_', '_', " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', "|", ' ', ' ', ' ', ' ', "|", ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", ' ', ' ', " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", ' ', ' ', ' ', ' ', ' ', ' ', "|", ' ', ' ', ' ', ' ', "|", ' ', ' ', ' ', ' ', ' ', ' ', " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", '_', '_', " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", "|", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", ' ', ' ', " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", ' ', ' ', ' ', ' ', ' ', ' ', "|", ' ', ' ', ' ', ' ', "|", ' ', ' ', ' ', ' ', ' ', ' ', " "],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '_', '_', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['=', ' ', '=', ' ', '=', ' ', '=', ' ', ' ', ' ', ' ', ' ', '=', ' ', '=', ' ', '=', ' ', '=', ' ']
]

pg.init()

dis_height = 900
dis_width = 900
dis = pg.display.set_mode((dis_width, dis_height))

Red = 255
Green = 255
Blue = 255

xs = dis_width / 2
ys = dis_height / 2
left = right = down = up = False

floor = Level()
floor_level = 1
rand_min = 4
rand_max = 7
yc = floor.ys
xc = floor.xs
print(yc, xc)
print(floor.ye, floor.xe)
platforms_actual = []
enemy_actual = []
enemy_count = 0
attack_direction = ""
attack = None
mele_attack_existance = False
timer = 0
exit_left, exit_top, exit_right, exit_bottom = False, False, False, False

lvl_map = [[[] for _ in range(len(floor.lvl[0]))]for _ in range(len(floor.lvl))]
enemy_map = [[[] for _ in range(len(floor.lvl[0]))]for _ in range(len(floor.lvl))]

if floor.lvl[yc][xc - 1] != "_":
    exit_left = True
if floor.lvl[yc][xc + 1] != "_":
    exit_right = True
if floor.lvl[yc - 1][xc] != "|":
    exit_top = True
if floor.lvl[yc + 1][xc] != "|":
    exit_bottom = True
floor.generate_room(exit_left, exit_top, exit_right, exit_bottom)
exit_left, exit_top, exit_right, exit_bottom = False, False, False, False

for y in range(len(floor.room)):
    for x in range(len(floor.room[y])):
        if floor.room[y][x] == "=":
            platforms_actual.append(Platform((x + 1) * 45, (y + 0.5) * 45,r.choice(["floor1.png", "floor2.png", "floor3.png"])))
        if floor.room[y][x] == "|":
            platforms_actual.append(Platform((x + 0.5) * 45, (y + 1) * 45, r.choice(["wall1.png", "wall2.png", "wall3.png"])))
        if floor.room[y][x] == "_":
            platforms_actual.append(Platform((x + 0.55) * 45, (y + 0.2) * 45, "cracked_platform1.png"))
floor.regenerate_room()

"""for yr in range(len(floor.lvl)):
    for xr in range(len(floor.lvl[yr])):
        if floor.lvl[yr][xr] != ' ' and floor.lvl[yr][xr] != "_" and floor.lvl[yr][xr] != "|" ''' and floor.lvl[yr][xr] != "e"''' :
            if floor.lvl[yc][xc - 1] != "_":
                exit_left = True
            if floor.lvl[yc][xc + 1] != "_":
                exit_right = True
            if floor.lvl[yc - 1][xc] != "|":
                exit_top = True
            if floor.lvl[yc + 1][xc] != "|":
                exit_bottom = True
            floor.generate_room(exit_left, exit_top, exit_right, exit_bottom)
        elif floor.lvl[yr][xr] == "_":
            floor.room = room_prCH
        elif floor.lvl[yr][xr] == "|":
            exit_left = exit_right = True
            floor.room = room_prCV

        for y in range(len(floor.room)):
            for x in range(len(floor.room[y])):
                if floor.room[y][x] == "=":
                    lvl_map[yr][xr].append(Platform((x + 1) * 45, (y + 0.5) * 45,r.choice(["floor1.png", "floor2.png", "floor3.png"])))
                if floor.room[y][x] == "|":
                    lvl_map[yr][xr].append(Platform((x + 0.5) * 45, (y + 1) * 45, r.choice(["wall1.png", "wall2.png", "wall3.png"])))
                if floor.room[y][x] == "_":
                    lvl_map[yr][xr].append(Platform((x + 0.5) * 45, y * 45, "cracked_platform1.png"))"""


"""if floor.lvl[yc][xc-1] != "_":
    exit_left = True
if floor.lvl[yc][xc+1] != "_":
    exit_right = True
if floor.lvl[yc-1][xc] != "|":
    exit_top = True
if floor.lvl[yc+1][xc] != "|":
    exit_bottom = True
floor.generate_room(exit_left, exit_top, exit_right, exit_bottom)

for y in range(len(floor.room)):
    for x in range(len(floor.room[y])):
        if floor.room[y][x] == "=":
            platforms_actual.append(Platform((x+1) * 45, (y + 0.5) * 45, r.choice(["floor1.png", "floor2.png", "floor3.png"])))
        if floor.room[y][x] == "|":
            platforms_actual.append(Platform((x + 0.5) * 45, (y + 1) * 45, r.choice(["wall1.png", "wall2.png", "wall3.png"])))
        if floor.room[y][x] == "_":
            platforms_actual.append(Platform((x + 0.5) * 45, y * 45, "cracked_platform1.png"))"""

entities = pg.sprite.Group()
pl1 = Player(xs, ys)
healthbar_red = Healthbar_red(pl1)
healthbar_green = Healthbar_green(pl1)
"""ghost1 = Ghost(800, 100)"""
entities.add(pl1, platforms_actual, enemy_actual, healthbar_red, healthbar_green)

game_over = False
clock = pg.time.Clock()

font_gameover = pg.font.SysFont("arial", 100)
font_highscore = pg.font.SysFont("arial", 60)

pg.display.update()
pg.display.set_caption("Dungeons 2D")
while not game_over:
    for event in pg.event.get():        #управление персонажем
        if event.type == pg.QUIT:
            print("Вы завершаете игру досрочно. Прогресс будет утерян без возможности восстановления")
            game_over = True
            sys.exit()

        up = False
        down = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_a or event.key == pg.K_LEFT:
                left = True
                attack_direction = "left"
            if event.key == pg.K_w or event.key == pg.K_UP or event.key == pg.K_SPACE:
                up = True
                """font45 = pg.font.SysFont("arial", 0)
                font20 = pg.font.SysFont("arial", 0)"""

            if event.key == pg.K_s or event.key == pg.K_DOWN:
                down = True
            if event.key == pg.K_d or event.key == pg.K_RIGHT:
                right = True
                attack_direction = "right"

        if event.type == pg.KEYUP:
            if event.key == pg.K_a:
                left = False
            if event.key == pg.K_d:
                right = False

        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1 and not mele_attack_existance:
                timer = time.time()
                attack = Mele_attack(pl1, attack_direction)
                mele_attack_existance = True
                entities.add(attack)
            elif event.button == 3:
                pass
        
        pl1.update(left, right, up, platforms_actual, enemy_actual, floor_level)
        entities.remove(healthbar_red, healthbar_green)
        healthbar_red = Healthbar_red(pl1)
        if pl1.health > 0:
            healthbar_green = Healthbar_green(pl1)
        entities.add(healthbar_red, healthbar_green)
        if mele_attack_existance:
            attack.update(pl1)
        print(pl1.health)
        for enemy in enemy_actual:
            enemy.update(pl1, enemy_actual, attack)
            if enemy.health <= 0:
                enemy_count -= 1
                entities.remove(enemy_actual)
                enemy_actual.remove(enemy)
                entities.add(enemy_actual)

    if pl1.health <= 0:
        entities.empty()
        dis.blit(font_gameover.render("Неудача", False, (255, 10, 10)), (280, 350))
        dis.blit(font_highscore.render(f"Вы погибли на этаже {floor_level}", False, (255, 10, 10)), (150, 550))


    if time.time() - timer >= 0.25:
        entities.remove(attack)
        attack = None
        mele_attack_existance = False


    """text_start = font45.render("Pixel Dungeon", False, (120, 155, 119))
    text_toStart = font20.render("Press SPACE to start", False, (0, 0, 0))"""
    """dis.blit(text_start, (0, ys))
    dis.blit(text_toStart, (0, ys+50))"""


    """
    создание новых и сохранение старых чанков V1
    """
    if pl1.rect.x < 0 and pl1.x_speed < 0:
        lvl_map[yc][xc] = platforms_actual
        enemy_map[yc][xc] = enemy_actual
        entities.remove(platforms_actual, enemy_actual)
        platforms_actual = []
        enemy_actual = []
        xc -= 1
        if lvl_map[yc][xc] == []:
            if floor.lvl[yc][xc] == "_":
                room_actual = room_prCH
            elif floor.lvl[yc][xc] == "1" or floor.lvl[yc][xc] == "2" or floor.lvl[yc][xc] == "3" or floor.lvl[yc][xc] == "4" or floor.lvl[yc][xc] == "5" or floor.lvl[yc][xc] == "e":
                if floor.lvl[yc][xc - 1] != "_":
                    exit_left = True
                if floor.lvl[yc][xc + 1] != "_":
                    exit_right = True
                if floor.lvl[yc - 1][xc] != "|":
                    exit_top = True
                if floor.lvl[yc + 1][xc] != "|":
                    exit_bottom = True
                floor.generate_room(exit_left, exit_top, exit_right, exit_bottom)
                room_actual = floor.room
                exit_left, exit_top, exit_right, exit_bottom = False, False, False, False
                """enemy_actual = Ghost.summon(floor_level, rand_min, rand_max)"""
            if floor.lvl[yc][xc] != "_" and floor.lvl[yc][xc] != "e":
                count = r.randint(rand_min, rand_max)
                enemy_actual = [Ghost(r.randint(100, 800), r.randint(100, 800), floor_level) for _ in range(count)]
                enemy_count += count
            for y in range(len(room_actual)):
                for x in range(len(room_actual[y])):
                    if room_actual[y][x] == "=":
                        platforms_actual.append(Platform((x + 1) * 45, (y + 0.5) * 45,r.choice(["floor1.png", "floor2.png", "floor3.png"])))
                    if room_actual[y][x] == "|":
                        platforms_actual.append(Platform((x + 0.5) * 45, (y + 1) * 45, r.choice(["wall1.png", "wall2.png", "wall3.png"])))
                    if room_actual[y][x] == "_":
                        platforms_actual.append(Platform((x + 0.5) * 45, y * 45, "cracked_platform1.png"))
        elif lvl_map[yc][xc] != []:
            platforms_actual = lvl_map[yc][xc]
            enemy_actual = enemy_map[yc][xc]

        entities.add(platforms_actual, enemy_actual)
        pl1.rect.x = 880
        pl1.rect.y -= 10
        floor.regenerate_room()

    elif pl1.rect.left > dis_width and pl1.x_speed > 0:
        lvl_map[yc][xc] = platforms_actual
        enemy_map[yc][xc] = enemy_actual
        entities.remove(platforms_actual, enemy_actual)
        platforms_actual = []
        enemy_actual = []
        xc += 1
        if lvl_map[yc][xc] == []:
            if floor.lvl[yc][xc] == "_":
                room_actual = room_prCH
            elif floor.lvl[yc][xc] == "1" or floor.lvl[yc][xc] == "2" or floor.lvl[yc][xc] == "3" or floor.lvl[yc][xc] == "4" or floor.lvl[yc][xc] == "5" or floor.lvl[yc][xc] == "e":
                if floor.lvl[yc][xc - 1] != "_":
                    exit_left = True
                if floor.lvl[yc][xc + 1] != "_":
                    exit_right = True
                if floor.lvl[yc - 1][xc] != "|":
                    exit_top = True
                if floor.lvl[yc + 1][xc] != "|":
                    exit_bottom = True
                floor.generate_room(exit_left, exit_top, exit_right, exit_bottom)
                room_actual = floor.room
                exit_left, exit_top, exit_right, exit_bottom = False, False, False, False
                """enemy_actual = Ghost.summon(floor_level, rand_min, rand_max)"""
            if floor.lvl[yc][xc] != "_" and floor.lvl[yc][xc] != "e":
                count = r.randint(rand_min, rand_max)
                enemy_actual = [Ghost(r.randint(100, 800), r.randint(100, 800), floor_level) for _ in range(count)]
                enemy_count += count
            for y in range(len(room_actual)):
                for x in range(len(room_actual[y])):
                    if room_actual[y][x] == "=":
                        platforms_actual.append(Platform((x + 1) * 45, (y + 0.5) * 45,r.choice(["floor1.png", "floor2.png", "floor3.png"])))
                    if room_actual[y][x] == "|":
                        platforms_actual.append(Platform((x + 0.5) * 45, (y + 1) * 45, r.choice(["wall1.png", "wall2.png", "wall3.png"])))
                    if room_actual[y][x] == "_":platforms_actual.append(Platform((x + 0.5) * 45, y * 45, "cracked_platform1.png"))
        elif lvl_map[yc][xc] != []:
            platforms_actual = lvl_map[yc][xc]
            enemy_actual = enemy_map[yc][xc]

        entities.add(platforms_actual, enemy_actual)
        pl1.rect.x = 20
        pl1.rect.y -= 10
        floor.regenerate_room()

    elif pl1.rect.bottom < 0 and pl1.y_speed < 0:
        lvl_map[yc][xc] = platforms_actual
        enemy_map[yc][xc] = enemy_actual
        entities.remove(platforms_actual, enemy_actual)
        platforms_actual = []
        enemy_actual = []
        yc -= 1
        if lvl_map[yc][xc] == []:
            if floor.lvl[yc][xc] == "|":
                room_actual = room_prCV
            elif floor.lvl[yc][xc] == "1" or floor.lvl[yc][xc] == "2" or floor.lvl[yc][xc] == "3" or floor.lvl[yc][xc] == "4" or floor.lvl[yc][xc] == "5" or floor.lvl[yc][xc] == "e":
                if floor.lvl[yc][xc - 1] != "_":
                    exit_left = True
                if floor.lvl[yc][xc + 1] != "_":
                    exit_right = True
                if floor.lvl[yc - 1][xc] != "|":
                    exit_top = True
                if floor.lvl[yc + 1][xc] != "|":
                    exit_bottom = True
                floor.generate_room(exit_left, exit_top, exit_right, exit_bottom)
                room_actual = floor.room
                exit_left, exit_top, exit_right, exit_bottom = False, False, False, False
                """enemy_actual = Ghost.summon(floor_level, rand_min, rand_max)"""
            if floor.lvl[yc][xc] != "|" and floor.lvl[yc][xc] != "e":
                count = r.randint(rand_min, rand_max)
                enemy_actual = [Ghost(r.randint(100, 800), r.randint(100, 800), floor_level) for _ in range(count)]
                enemy_count += count
            for y in range(len(room_actual)):
                for x in range(len(room_actual[y])):
                    if room_actual[y][x] == "=":
                        platforms_actual.append(Platform((x + 1) * 45, (y + 0.5) * 45,r.choice(["floor1.png", "floor2.png", "floor3.png"])))
                    if room_actual[y][x] == "|":
                        platforms_actual.append(Platform((x + 0.5) * 45, (y + 1) * 45, r.choice(["wall1.png", "wall2.png", "wall3.png"])))
                    if room_actual[y][x] == "_":
                        platforms_actual.append(Platform((x + 0.5) * 45, y * 45, "cracked_platform1.png"))
        elif lvl_map[yc][xc] != []:
            platforms_actual = lvl_map[yc][xc]
            enemy_actual = enemy_map[yc][xc]

        entities.add(platforms_actual, enemy_actual)
        pl1.rect.x = 480
        pl1.rect.y = 775
        floor.regenerate_room()

    elif pl1.rect.y > dis_height:
        lvl_map[yc][xc] = platforms_actual
        enemy_map[yc][xc] = enemy_actual
        entities.remove(platforms_actual, enemy_actual)
        platforms_actual = []
        enemy_actual = []
        yc += 1
        if lvl_map[yc][xc] == []:
            if floor.lvl[yc][xc] == "|":
                room_actual = room_prCV
            elif floor.lvl[yc][xc] == "1" or floor.lvl[yc][xc] == "2" or floor.lvl[yc][xc] == "3" or floor.lvl[yc][
                xc] == "4" or floor.lvl[yc][xc] == "5" or floor.lvl[yc][xc] == "e":
                if floor.lvl[yc][xc - 1] != "_":
                    exit_left = True
                if floor.lvl[yc][xc + 1] != "_":
                    exit_right = True
                if floor.lvl[yc - 1][xc] != "|":
                    exit_top = True
                if floor.lvl[yc + 1][xc] != "|":
                    exit_bottom = True
                floor.generate_room(exit_left, exit_top, exit_right, exit_bottom)
                room_actual = floor.room
                exit_left, exit_top, exit_right, exit_bottom = False, False, False, False
                """enemy_actual = Ghost.summon(floor_level, rand_min, rand_max)"""
            if floor.lvl[yc][xc] != "|" and floor.lvl[yc][xc] != "e":
                count = r.randint(rand_min, rand_max)
                enemy_actual = [Ghost(r.randint(100, 800), r.randint(100, 800), floor_level) for _ in range(count)]
                enemy_count += count
            for y in range(len(room_actual)):
                for x in range(len(room_actual[y])):
                    if room_actual[y][x] == "=":
                        platforms_actual.append(Platform((x + 1) * 45, (y + 0.5) * 45,
                                                         r.choice(["floor1.png", "floor2.png", "floor3.png"])))
                    if room_actual[y][x] == "|":
                        platforms_actual.append(
                            Platform((x + 0.5) * 45, (y + 1) * 45, r.choice(["wall1.png", "wall2.png", "wall3.png"])))
                    if room_actual[y][x] == "_":
                        platforms_actual.append(Platform((x + 0.5) * 45, y * 45, "cracked_platform1.png"))
        elif lvl_map[yc][xc] != []:
            platforms_actual = lvl_map[yc][xc]
            enemy_actual = enemy_map[yc][xc]

        entities.add(platforms_actual, enemy_actual)
        pl1.rect.x = 450
        pl1.rect.y = 90
        floor.regenerate_room()

    if pl1.health > 0:
        dis.blit(pg.image.load("bg_full_dark.png"), (0, 0))

    if xc == floor.xe and yc == floor.ye and enemy_count == 0:
        if pl1.health < 500:
            pl1.health *= 1.4
            if pl1.health > 500:
                pl1.health -= pl1.health % 500
        round(pl1.health)
        pl1.rect.x = 450
        pl1.rect.y = 450
        floor_level += 1
        """timer = time.time()
        bool_timer = True
        while bool_timer == True:
            if time.time() - timer == 3:
                bool_timer = False"""
        entities.remove(platforms_actual)
        platforms_actual = []
        floor.__init__()
        yc = floor.ys
        xc = floor.xs
        print(yc, xc)
        print(floor.ye, floor.xe)
        lvl_map = [[[] for _ in range(len(floor.lvl[0]))] for _ in range(len(floor.lvl))]

        if floor.lvl[yc][xc - 1] != "_":
            exit_left = True
        if floor.lvl[yc][xc + 1] != "_":
            exit_right = True
        if floor.lvl[yc - 1][xc] != "|":
            exit_top = True
        if floor.lvl[yc + 1][xc] != "|":
            exit_bottom = True
        floor.generate_room(exit_left, exit_top, exit_right, exit_bottom)
        exit_left, exit_top, exit_right, exit_bottom = False, False, False, False

        for y in range(len(floor.room)):
            for x in range(len(floor.room[y])):
                if floor.room[y][x] == "=":
                    platforms_actual.append(Platform((x + 1) * 45, (y + 0.5) * 45, r.choice(["floor1.png", "floor2.png", "floor3.png"])))
                if floor.room[y][x] == "|":
                    platforms_actual.append(Platform((x + 0.5) * 45, (y + 1) * 45, r.choice(["wall1.png", "wall2.png", "wall3.png"])))
                if floor.room[y][x] == "_":
                    platforms_actual.append(Platform((x + 0.55) * 45, (y + 0.2) * 45, "cracked_platform1.png"))
        floor.regenerate_room()
        entities.add(platforms_actual)


    """
    создание и сапись чанков карты V2
    """

    """if pl1.rect.left < 0 and pl1.x_speed < 0:
        pass
    elif pl1.rect.right > dis_width and pl1.x_speed > 0:
        pass
    elif pl1.rect.bottom < 0 and pl1.y_speed < 0:
        pass
    elif pl1.rect.top > dis_height and pl1.y_speed > 0:
        pass

    if xc == floor.xe and yc == floor.ye:
        pass"""


    entities.draw(dis)
    pg.display.update()
    clock.tick(60)


pg.quit()
quit()