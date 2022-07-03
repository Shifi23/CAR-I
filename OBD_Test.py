# import necessary libraries
import math
import obd
import pygame
from pygame.locals import *
flags = FULLSCREEN | DOUBLEBUF
obd.logger.setLevel(obd.logging.DEBUG)
# define pi
pi = 3.141592653
# pygame settings
pygame.init()
pygame.mixer.init()
#icon = pygame.image.load('/home/pi/Documents/obd2.png')
# pygame.display.set_icon(icon)
connection = obd.Async(fast=True)
screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE | DOUBLEBUF, 16)
screen.set_alpha(None)
pygame.display.set_caption("OBD2 HUD")
screen_w = screen.get_width()
screen_h = screen.get_height()
coolant_text_x = screen_w * .25
coolant_text_y = screen_h * .09
voltage_text_x = screen_w * .725
voltage_text_y = screen_h * .09
load_text_x = screen_w * .25
load_text_y = screen_h * .49
throttle_text_x = screen_w * .725
throttle_text_y = screen_h * .49
headerFont = pygame.font.SysFont("Arial", 30)
digitFont = pygame.font.SysFont("Arial", 40)
# define colors
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
grey = (180, 180, 180)
#global variables
coolant = 20
voltage = 11.8
load = 0
throttle = 17
coolbit = 0
throttlebit = 0
# function definitions


def map(x, in_min, in_max, out_min, out_max):
    return int((x-in_min) * (out_max-out_min) / (in_max-in_min) + out_min)


def draw_hud():
    screen.fill(black)
    coolant_text = headerFont.render("COOLANT", True, white)
    voltage_text = headerFont.render("VOLTAGE", True, white)
    load_text = headerFont.render("LOAD", True, white)
    throttle_text = headerFont.render("THROT POS", True, white)
    coolant_text_loc = coolant_text.get_rect(
        center=(coolant_text_x, coolant_text_y))
    voltage_text_loc = voltage_text.get_rect(
        center=(voltage_text_x, voltage_text_y))
    load_text_loc = load_text.get_rect(center=(load_text_x, load_text_y))
    throttle_text_loc = throttle_text.get_rect(
        center=(throttle_text_x, throttle_text_y))
    screen.blit(coolant_text, coolant_text_loc)
    screen.blit(voltage_text, voltage_text_loc)
    screen.blit(load_text, load_text_loc)
    screen.blit(throttle_text, throttle_text_loc)


def get_coolant(c):
    global coolant
    if not c.is_null():
        coolant = int(c.value.magnitude)


def get_voltage(v):
    global voltage
    if not v.is_null():
        voltage = float(v.value.magnitude)


def get_load(l):
    global load
    if not l.is_null():
        load = int(l.value.magnitude)


def get_throttle(t):
    global throttle
    if not t.is_null():
        throttle = int(t.value.magnitude)


# OBD connections
connection.watch(obd.commands.COOLANT_TEMP, callback=get_coolant, force=False)
connection.watch(obd.commands.CONTROL_MODULE_VOLTAGE,
                 callback=get_voltage, force=False)
connection.watch(obd.commands.ENGINE_LOAD, callback=get_load, force=False)
connection.watch(obd.commands.THROTTLE_POS, callback=get_throttle, force=False)
connection.start()
# while running kill with esc key, then draw heads up display
running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                connection.stop()
                connection.close()
                running = False
            elif event.type == QUIT:
                connection.stop()
                connection.close()
                running = False

    draw_hud()
# render parameters for HUD numbers
    coolantDisplay = digitFont.render(str(coolant), 3, white)
    voltageDisplay = digitFont.render(str(round(voltage, 1)), 3, white)
    loadDisplay = digitFont.render(str(load), 3, white)
    throttleDisplay = digitFont.render(str(throttle), 3, white)
# if statements that determine color and sounds
    if throttle <= 40:
        throttleColor = green
    if throttle > 40 and throttle < 60:
        throttleColor = yellow
    if throttle >= 60:
        throttleColor = red
    if coolant < 54:
        coolantColor = blue
    if coolant >= 54 and coolant <= 90:
        coolantColor = green
    if coolant > 90:
        coolantColor = red
    if voltage > 12 and voltage < 13:
        voltageColor = yellow
    if voltage <= 12:
        voltageColor = red
    if voltage >= 13:
        voltageColor = green
    if load >= 80:
        loadColor = red
    if load < 80 and load > 50:
        loadColor = yellow
    if load <= 50:
        loadColor = green
    if throttle >= 80 and throttlebit == 0:
        throttlebit = 1
    if coolant > 90 and coolbit == 0:
        coolbit = 1
    if coolant == 54 and coolbit == 0:
        coolbit = 1
    if coolant < 85 and coolbit == 1 and coolant > 60:
        coolbit = 0
    if throttle < 78 and throttlebit == 1:
        throttlebit = 0
# draw heads up display (coolant, voltage, load, throttle)
    pygame.draw.arc(
        screen, white, [screen_w * .1+65, screen_h * .35-100, 220, 220], pi/4, pi, 5)
    pygame.draw.arc(
        screen, white, [screen_w * .6+50, screen_h * .35-100, 220, 220], pi/4, pi, 5)
    pygame.draw.arc(
        screen, white, [screen_w * .1+65, screen_h * .75-100, 220, 220], pi/4, pi, 5)
    pygame.draw.arc(
        screen, white, [screen_w * .6+50, screen_h * .75-100, 220, 220], pi/4, pi, 5)

    pygame.draw.line(screen, grey, [screen_w * .1+165, screen_h * .35], [screen_w * .1 + 150-25+40 + 102*math.cos(math.radians(
        map(coolant, 20, 110, 180, 45))), screen_h * .35 - 102*math.sin(math.radians(map(coolant, 20, 110, 180, 45)))], 10)
    pygame.draw.line(screen, grey, [screen_w * .6+150, screen_h * .35], [screen_w * .6 + 200-100+50 + 102*math.cos(math.radians(
        map(voltage, 11.8, 14.5, 180, 45))), screen_h * .35 - 102*math.sin(math.radians(map(voltage, 11.8, 14.5, 180, 45)))], 10)
    pygame.draw.line(screen, grey, [screen_w * .1+165, screen_h * .75], [screen_w * .1 + 150-25+40 + 102*math.cos(
        math.radians(map(load, 0, 100, 180, 45))), screen_h * .75 - 102*math.sin(math.radians(map(load, 0, 100, 180, 45)))], 10)
    pygame.draw.line(screen, grey, [screen_w * .6+150, screen_h * .75], [screen_w * .6 + 200-100+50 + 102*math.cos(math.radians(
        map(throttle, 17, 80, 180, 45))), screen_h * .75 - 102*math.sin(math.radians(map(throttle, 17, 81, 180, 45)))], 10)

    pygame.draw.line(screen, coolantColor, [screen_w * .1+165, screen_h * .35], [screen_w * .1 + 150-25+40 + 100*math.cos(
        math.radians(map(coolant, 20, 110, 180, 45))), screen_h * .35 - 100*math.sin(math.radians(map(coolant, 20, 110, 180, 45)))], 5)
    pygame.draw.line(screen, voltageColor, [screen_w * .6+150, screen_h * .35], [screen_w * .6 + 200-100+50 + 100*math.cos(
        math.radians(map(voltage, 11.8, 14.5, 180, 45))), screen_h * .35 - 100*math.sin(math.radians(map(voltage, 11.8, 14.5, 180, 45)))], 5)
    pygame.draw.line(screen, loadColor, [screen_w * .1+165, screen_h * .75], [screen_w * .1 + 150-25+40 + 100*math.cos(
        math.radians(map(load, 0, 100, 180, 45))), screen_h * .75 - 100*math.sin(math.radians(map(load, 0, 100, 180, 45)))], 5)
    pygame.draw.line(screen, throttleColor, [screen_w * .6+150, screen_h * .75], [screen_w * .6 + 200-100+50 + 100*math.cos(
        math.radians(map(throttle, 17, 80, 180, 45))), screen_h * .75 - 100*math.sin(math.radians(map(throttle, 17, 81, 180, 45)))], 5)

    screen.blit(coolantDisplay, (screen_w * .175-30-25, screen_h * .2-30))
    screen.blit(voltageDisplay, (screen_w * .7-30-85, screen_h * .2-30))
    screen.blit(loadDisplay, (screen_w * .175-30-25, screen_h * .6-30))
    screen.blit(throttleDisplay, (screen_w * .715-30-75, screen_h * .6-30))

    pygame.draw.circle(screen, grey, [screen_w-555, screen_h-310], 15, 0)
    pygame.draw.circle(screen, grey, [screen_w-170, screen_h-310], 15, 0)
    pygame.draw.circle(screen, grey, [screen_w-555, screen_h-120], 15, 0)
    pygame.draw.circle(screen, grey, [screen_w-170, screen_h-120], 15, 0)
# update screen
    pygame.display.update()
    pygame.display.flip()
