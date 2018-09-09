# -*- coding: utf-8 -*-
#   File Name：     12pygame
#   Description :
#   Author :       zongyanzhang
#   date：          2018/8/26

import pygame, sys
import pygame.locals

# 初始化所有的游戏模块
pygame.init()

# 构建游戏窗口
#pygame.display.init()
# screen Surface类型的对象
screen = pygame.display.set_mode((800, 600))
rect = screen.get_rect()
print(rect.top, rect.bottom, rect.left, rect.right, rect.midtop, rect.center)

pygame.display.set_caption("这是我的第一个游戏")


# 加载一个图片
plane = pygame.image.load("./img.png")
planerect = plane.get_rect()
planerect.midbottom = rect.midbottom

# 设置帧率fps
clock = pygame.time.Clock()

n = 0

while True:
    # 设置颜色
    screen.fill((255, 255, 255))

    # 获取游戏事件
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            sys.exit() # 终止进程

    n += 1
    if n % 10 == 0:
        planerect.top -= 5

    # 显示图片对象
    screen.blit(plane, planerect)

    clock.tick(60)
    pygame.display.update()


