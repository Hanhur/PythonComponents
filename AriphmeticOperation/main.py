import pygame as pg, sys, random

pg.init()
screen = pg.display.set_mode((800, 600))
pg.display.set_caption("Лети к курсору! (Теперь с логикой!)")

x, y = 400, 300
size = 30 # Зазмет шарика
color = (255, 0, 0) # Красный цвет. Зелёный - это (0, 255, 0).
font = pg.font.SysFont("Arial", 24)
shield = False

# and (и) - соединяет 2 утверждения, так что истиной (тrue) будет. только если оба ут верждения верны;
# or (или) - соединяет 2 утверждения, так что истиной (тrue) будет, если хотя бы одно из утверждений верно;
# not (не) - идет перед утверждением. отрицая его . Если утверждение было ложным, оно становится верным, и наоборот.

# Основные операторы сравнения:
# « > » - больше;
# « < » - меньше:
# « == » - равно;
# « != » - не равно;
# « >= » - больше или равно;
# « <= » - меньше или равно.
#
# Логические операторы and, or, not
# Иногда нам нужно проверить сразу несколько условий:

# and - «м» (оба условия должны быть True)
#   » (5 > 3) and (2 < 4) ➔ True
#   » (5 == 3) and (2 < 4) ➔ FaLse

# or - «нлм» (хотя бы одно условие True)
#   » (5 == 3) or (2 < 4) ➔ True (второе условие истинно)

# not - «не» (меняет True на FaLse и наоборот)
#   » 5 == 5 ➔ True
#   » not (5 == 5) ➔ FaLse

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            x, y = pg.mouse.get_pos()
            # Запрещаем выход за границы экрана
            x = max(size, min(x, 800 - size)) # Ограничиваем x от 0 до 800
            y = max(size, min(y, 600 - size)) # Ограничивам y от 0 до 600
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_s:
                shield = not shield

    keys = pg.key.get_pressed()
    # Давайте сделаем так, чтобы можно быпо менять цвет нашен кисти.
    if keys[pg.K_r]: # Если нажать кнопку R
        color = (255, 0, 0) # Меняем цвет на красный

    if keys[pg.K_g]: # Если нажать кнопку G
        color = (0, 255, 0) # Меняем цвет на зелёный

    if keys[pg.K_b]: # Если нажать кнопку B
        color = (0, 0, 255) # Меняем цвет на синий

    # Увеличение размера кисти
    if keys[pg.K_EQUALS] and size < 100: # И больше 100
        size += 1

    # Уменьшение размера кисти
    if keys[pg.K_MINUS] and size > 10: # Не дадим кружку стать меньше 10
        size -= 1

    # До6авляем радужный режим
    if keys[pg.K_c]:
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # Проверяем, коснулся ли круг границ
    touch_left = x - size <= 0 # Касается левой границы
    touch_right = x + size >= 800 # Касается правой граицы
    touch_top = y - size <= 0 # Касается верхией граицы
    touch_bottom = y + size >= 600 # Касается нижней границы

    if touch_left or touch_right or touch_top or touch_bottom:
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    if shield and (color == (255, 0, 0) or color == (0, 255, 0)):
        # Если щит включён и цвет круга красный или зелёный
        pg.draw.circle(screen, (0, 0, 255), (x, y), size + 10, 5)

    # Очищаем экран пробелом
    if keys[pg.K_SPACE]:
        screen.fill((255, 165, 0))

    pg.draw.rect(screen, (50, 50, 50), (0, 550, 800, 50))
    pg.draw.circle(screen, color, (50, 575), 15)
    pg.draw.circle(screen, (200, 200, 200), (50, 575), 15, 1)
    size_text = font.render(f"Размер: {size}", True, (255, 255, 255))
    screen.blit(size_text, (80, 560))

    pg.draw.circle(screen, color, (x, y), size)
    pg.display.flip()
    pg.time.delay(10)

pg.quit()