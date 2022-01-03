import pygame
import random
###########################################################################
# 기본 초기화 (반드시 해야 하는 것들)
pygame.init() #초기화 

#화면 크기 설정
screen_width = 480 #가로 크기
screen_height = 640 #세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))


#화면 타이틀 설정
pygame.display.set_caption("똥 피하기") # 게임 이름

# FPS
clock = pygame.time.Clock()
###########################################################################

# 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 속도, 폰트 등)
# 배경 만들기
background = pygame.image.load('C:/Users/지윤/PycharmProjects/pythonProject/python-practice/pygame_basic/background.png')

# 캐릭터 불러오기
character = pygame.image.load('C:/Users/지윤/PycharmProjects/pythonProject/python-practice/pygame_basic/character.png')
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2) 
character_y_pos = screen_height - character_height

# 이동할 좌표
to_x = 0

# 이동 속도
character_speed = 10


# 적 캐릭터
enemy = pygame.image.load('C:/Users/지윤/PycharmProjects/pythonProject/python-practice/pygame_basic/enemy.png')
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = random.randint(0, screen_width - enemy_width)
enemy_y_pos = 0
enemy_speed = 10

# 폰트 정의
game_font = pygame.font.Font(None, 40)

# 총 시간
total_time = 0

# 시작 시간 정보
start_ticks = pygame.time.get_ticks()


# 이벤트 루프
running = True 
while running:
    dt = clock.tick(30)  # 게임 화면의 초당 프레임 수를 설정

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():  
        if event.type == pygame.QUIT: 
            running = False  
    if event.type == pygame.KEYDOWN:  #키가 눌러졌는지 확인
        if event.key == pygame.K_LEFT:  #캐릭터 왼쪽으로
            to_x -= character_speed  
        elif event.key == pygame.K_RIGHT:  # 캐릭터 오른쪽으로
            to_x += character_speed

    if event.type == pygame.KEYUP: #방향키를 떼면 멈춤
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            to_x = 0
        elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            to_y = 0

    # 3. 게임 캐릭터 위치 정의
    character_x_pos += to_x

    # 가로 경계값 처리
    if character_x_pos <= 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    enemy_y_pos += enemy_speed

    if enemy_y_pos > screen_height:
        enemy_y_pos = 0
        enemy_x_pos = random.randint(0, screen_width - enemy_width)

    # 4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌했어요.")
        running = False


    # 5. 화면에 그리기
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    elapsed_time = pygame.time.get_ticks() / 1000

    timer = game_font.render(str(int(total_time + elapsed_time)), True, (0, 0, 0))
    screen.blit(timer, (10, 10))

    pygame.display.update()  # 게임화면을 다시 그리기! 


# pygame 종료
pygame.quit()