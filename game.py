# Here, we import the Pygame and math libraries and initialize the Pygame module.
import pygame
import math


pygame.init()

# We set the dimensions of the display window to 800x600 pixels and set the caption of the window to "Draw a Perfect Circle by Nurasyl Nurtaza".
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Draw a Perfect Cirlce by Nurasyl Nurtaza")

# We define some colors in RGB format that we will use to draw on the screen.
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 170, 51)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# We define some variables that we will use to draw circles.
radus = 13
Draw = False
mode = BLACK

# We define the fonts that we will use to display text on the screen.
font = pygame.font.SysFont("Verdana", 50)
fonttxt = pygame.font.SysFont("Verdana", 20)
font_col = (0, 0, 0)
# We define some texts that we will display on the screen.
percenttxt = font.render(str(""), True, BLUE)
closetxt = fonttxt.render("Too close to the dot!", True, RED)
statustxt = fonttxt.render("0", True, RED)


start = 0
startpos = 0, 0
flag = True

time_up_count = 1
time_up_ticks = 0

# We define some helper functions that we will use in the program.
def reversedline(x1, y1, x2, y2, x3, y3):
    if x2 - x1 == 0:
        return x3 == x1 and y3 == -y1
    slope = (y2 - y1) / (x2 - x1)
    y_intercept = y1 - slope * x1
    return y3 == -slope * x3 - y_intercept


def isline(x0, y0, x1, y1, x, y):
    k = (y1-y0)/(x1-x0)
    b = y0 - k*x0
    new_y = k*x + b
    new_x =0
    temp_y =1

def delta(start, end):
    start_x = start[0]-400
    start_y = start[1]-300
    end_x = end[0]-400
    end_y  = end[1]-300
    a = math.sqrt(start_x**2 + start_y**2)
    b = math.sqrt(end_x**2 + end_y**2)
    return abs(a-b)

def rad(start):
    a = math.sqrt((start[0] - 400) ** 2 + (start[1] - 300) ** 2)
    return a

el_set = {(1, 1)}

percent = 0
elements = []

sum = 0

best_score = 0
best_mode = (0, 0, 0)

stpos = 0
status_close = 0
status_wrongside = 0
status_default = 0
status_newscore = 0
status_timeUp = 0

start = 0
startpos = 0, 0

negative_percent = 0

start_countdown =1


while True:
    if start_countdown:
        start_ticks = 0
        start_ticks = pygame.time.get_ticks()
        start_countdown = 0
        tick_pos = pygame.mouse.get_pos()

    if time_up_count:
        time_up_ticks = 0
        time_up_ticks = pygame.time.get_ticks()
        time_up_count = 0

    timeUp_seconds = (pygame.time.get_ticks() - time_up_ticks)/1000
    seconds = (pygame.time.get_ticks() - start_ticks)/1000


    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if start:
            start = 0
            startpos = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONDOWN:
            elements = []
            start, Draw = 1, 1
            flag = False
            negative_percent = 0
            status_wrongside = 0
            status_default = 0
            status_timeUp = 0
            timeUp_seconds = 0
            status_newscore = 0
            time_up_count=1

            pos = pygame.mouse.get_pos()
            if(rad(startpos)<=100):
                stpos = 1
            element = {"type": "circle", "mode": mode, "radus": radus, "pos": pos}
            elements.append(element)


        elif event.type == pygame.MOUSEBUTTONUP:

            if(percent>best_score and not status_timeUp):
                status_newscore = 1
                best_score = percent
                best_mode = font_col
            elif not (status_timeUp or status_wrongside or stpos):
                status_default = 1

            radus = 8
            percent = 0
            el_set = {(1, 1)}
            Draw = False

        elif event.type == pygame.MOUSEMOTION and Draw:
            if timeUp_seconds>9:
                status_timeUp = 1
                Draw = 0
            if seconds>0.008:
                seconds = 0
                start_countdown = 1
                if(tick_pos==pos):
                    if(radus<12):
                        radus+=1
                else:
                    if(radus>2):
                        radus-=1

            pos = pygame.mouse.get_pos()
            if (rad(pos) <= 10):
                stpos = 1
                status_default = 0
            if (delta(startpos, pos) < 25):
                circle_mode = GREEN
            elif (delta(startpos, pos) > 25 and delta(startpos, pos) < 35):
                circle_mode = YELLOW
            else:
                circle_mode = (255, 0, 0)


            lenn = len(el_set) // 2

            if(len(el_set)>13):
                for i in el_set:
                    sum+=delta(i, startpos)
                temp = (sum/(lenn+1))
                sum = 0
                percent = (1-temp/rad(startpos)*0.7)
                if(percent>0.7):
                    font_col = (int(255-(((percent-0.7)/0.3)*255)), int(((percent-0.7)/0.3)*255), 0)
                else:
                    font_col = (255, 0, 0)
                if(isline(400, 300,startpos[0], startpos[1],pos[0], pos[1])==1):
                    status_default=1
                    Draw=0
                if (reversedline(400, 300, startpos[0], startpos[1], pos[0], pos[1]) == 1):
                    status_default = 1
                    Draw = 0

                if(percent<0):
                    negative_percent = 1
                    status_wrongside = 1
                    Draw = 0

                if negative_percent:
                    percenttxt = font.render('XX:xx%', True, font_col)
                else:
                    percenttxt = font.render(str(round(percent * 100, 2)) + '%', True, font_col)


            prev_pos = elements[-1]["pos"]  
            distance = max(abs(pos[0] - prev_pos[0]), abs(
                pos[1] - prev_pos[1]))  
            for i in range(distance):
                x = int(prev_pos[0] + (pos[0] - prev_pos[0]) * float(i) / distance)
                y = int(prev_pos[1] + (pos[1] - prev_pos[1]) * float(i) / distance)
                element = {"type": "circle", "mode": circle_mode, "radus": radus, "pos": (x, y)}
                elements.append(element)
                el_set.add((x,y))
    k = (startpos[0] - 400) / (startpos[1] - 300)
    b = startpos[1] - startpos[0]
    screen.fill(BLACK)
    screen.blit(percenttxt, (320, 250))
    pygame.draw.circle(screen, (255, 255, 255), (400, 300), 6, width=0)
    if status_timeUp and not status_wrongside and not status_default:
        statustxt = fonttxt.render("Too slow", True, GREEN)
        screen.blit(statustxt, (300, 340))
    if status_newscore and not status_wrongside and not status_default and not status_close:
        statustxt = fonttxt.render("New best score", True, BLUE)
        screen.blit(statustxt, (350, 240))
    if status_wrongside:
        statustxt = fonttxt.render("Wrong side!", True, YELLOW)
        screen.blit(statustxt, (350, 140))
        Draw = 0
    if status_default and not status_wrongside and not stpos:
        statustxt = fonttxt.render("Best: ", True, WHITE)
        bst_2 = fonttxt.render(str(round(best_score * 100, 2)) + '%', True, best_mode)
        screen.blit(statustxt, (340, 340))
        screen.blit(bst_2, (410, 340))
    if status_close and not Draw and not status_wrongside and not stpos:
        screen.blit(closetxt, (300, 340))
    else:
        status_close = 0
    if stpos and not status_wrongside and not status_default:
        screen.blit(closetxt, (300, 340))
        Draw = 0
        stpos = 0
        status_close = 1


    for element in elements:
        if element["type"] == "circle":
            pygame.draw.circle(screen, element["mode"], element["pos"], element["radus"])

    pygame.display.update()
