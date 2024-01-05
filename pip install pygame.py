import pygame
import sys

# 初始化Pygame
pygame.init()

# 定義顏色和一些常量
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

# 創建遊戲窗口
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Simple Game')

# 定義角色的屬性
player_size = 50
player_x, player_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT - player_size * 2
player_speed = 5

# 主遊戲迴圈
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    # 控制角色移動
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # 確保角色在窗口內移動
    if player_x <= 0:
        player_x = 0
    elif player_x >= SCREEN_WIDTH - player_size:
        player_x = SCREEN_WIDTH - player_size
    if player_y <= 0:
        player_y = 0
    elif player_y >= SCREEN_HEIGHT - player_size:
        player_y = SCREEN_HEIGHT - player_size

    # 填充背景色
    screen.fill(WHITE)

    # 繪製角色
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_size, player_size))

    # 更新畫面
    pygame.display.flip()

pygame.quit()
sys.exit()
