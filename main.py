import pygame
from random import *
# import pymunk
pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
class level_1():
    def background(self, screen):
        bg = pygame.image.load("Images/Backgrounds/background_1.jpg")
        bg = pygame.transform.scale(bg, (1200, 800))
        screen.blit(bg, (0, 0))

class level_2():
    def background(self, screen):
        bg = pygame.image.load("Images/Backgrounds/background_2.png")
        bg = pygame.transform.scale(bg, (1200, 800))
        screen.blit(bg, (0, 0))

class level_3():
    def background(self, screen):
        bg = pygame.image.load("Images/Backgrounds/background_3.jpg")
        bg = pygame.transform.scale(bg, (1200, 800))
        screen.blit(bg, (0, 0))

class Player():
    global sound_on

    def __init__(self, player_x, player_y):
        self.player_x = player_x
        self.player_y = player_y
        self.width = 45
        self.height = 68
        self.player_anim_count = 0
        self.player_jump_anim_count = 0
        self.add_count = 0
        self.player_run_anim_count = 0
        self.player_speed = 9
        self.is_jump = False
        self.jump_count = 6
        self.jump_sound_count = True
        self.check_sound = False

    def display_player(self, screen):
        walk_left = [pygame.image.load("images/Spritesheet walk left/tile000.png").convert_alpha(),
                     pygame.image.load("images/Spritesheet walk left/tile001.png").convert_alpha(),
                     pygame.image.load("images/Spritesheet walk left/tile002.png").convert_alpha(),
                     pygame.image.load("images/Spritesheet walk left/tile003.png").convert_alpha(),
                     pygame.image.load("images/Spritesheet walk left/tile004.png").convert_alpha(),
                     pygame.image.load("images/Spritesheet walk left/tile005.png").convert_alpha(),
                     pygame.image.load("images/Spritesheet walk left/tile006.png").convert_alpha()]
        walk_right = [pygame.image.load("images/Spritesheet walk right/tile000.png").convert_alpha(),
                      pygame.image.load("images/Spritesheet walk right/tile001.png").convert_alpha(),
                      pygame.image.load("images/Spritesheet walk right/tile002.png").convert_alpha(),
                      pygame.image.load("images/Spritesheet walk right/tile003.png").convert_alpha(),
                      pygame.image.load("images/Spritesheet walk right/tile004.png").convert_alpha(),
                      pygame.image.load("images/Spritesheet walk right/tile005.png").convert_alpha(),
                      pygame.image.load("images/Spritesheet walk right/tile006.png").convert_alpha()]
        jump_right = [pygame.image.load("images/jump/tile000.png").convert_alpha(),
                      pygame.image.load("images/jump/tile001.png").convert_alpha(),
                      pygame.image.load("images/jump/tile002.png").convert_alpha(),
                      pygame.image.load("images/jump/tile003.png").convert_alpha(),
                      pygame.image.load("images/jump/tile004.png").convert_alpha(),
                      pygame.image.load("images/jump/tile005.png").convert_alpha(),
                      pygame.image.load("images/jump/tile006.png").convert_alpha(),
                      pygame.image.load("images/jump/tile007.png").convert_alpha(),
                      pygame.image.load("images/jump/tile008.png").convert_alpha(),
                      pygame.image.load("images/jump/tile009.png").convert_alpha(),
                      pygame.image.load("images/jump/tile010.png").convert_alpha()]
        jump_left = [pygame.image.load("images/jump2/tile010.png").convert_alpha(),
                     pygame.image.load("images/jump2/tile009.png").convert_alpha(),
                     pygame.image.load("images/jump2/tile008.png").convert_alpha(),
                     pygame.image.load("images/jump2/tile007.png").convert_alpha(),
                     pygame.image.load("images/jump2/tile006.png").convert_alpha(),
                     pygame.image.load("images/jump2/tile005.png").convert_alpha(),
                     pygame.image.load("images/jump2/tile004.png").convert_alpha(),
                     pygame.image.load("images/jump2/tile003.png").convert_alpha(),
                     pygame.image.load("images/jump2/tile002.png").convert_alpha(),
                     pygame.image.load("images/jump2/tile001.png").convert_alpha(),
                     pygame.image.load("images/jump2/tile000.png").convert_alpha()]
        run_right = [pygame.image.load("images/run right/tile000.png").convert_alpha(),
                     pygame.image.load("images/run right/tile001.png").convert_alpha(),
                     pygame.image.load("images/run right/tile002.png").convert_alpha(),
                     pygame.image.load("images/run right/tile003.png").convert_alpha(),
                     pygame.image.load("images/run right/tile004.png").convert_alpha(),
                     pygame.image.load("images/run right/tile005.png").convert_alpha(),
                     pygame.image.load("images/run right/tile006.png").convert_alpha(),
                     pygame.image.load("images/run right/tile007.png").convert_alpha()]
        run_left = [pygame.image.load("images/run left/tile007.png").convert_alpha(),
                    pygame.image.load("images/run left/tile006.png").convert_alpha(),
                    pygame.image.load("images/run left/tile005.png").convert_alpha(),
                    pygame.image.load("images/run left/tile004.png").convert_alpha(),
                    pygame.image.load("images/run left/tile003.png").convert_alpha(),
                    pygame.image.load("images/run left/tile002.png").convert_alpha(),
                    pygame.image.load("images/run left/tile001.png").convert_alpha(),
                    pygame.image.load("images/run left/tile000.png").convert_alpha()]
        keys = pygame.key.get_pressed()
        if self.is_jump == True:
            if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and keys[pygame.K_LCTRL] and self.player_x < 1110:
                if wind:
                    self.player_speed = 9
                else:
                    self.player_speed = 14
                self.player_x += self.player_speed
                walk_sound.stop()
                if self.jump_sound_count == True:
                    if sound_on == True:
                        jump_sound.play()
                    self.jump_sound_count = False
                self.check_sound = False
                screen.blit(jump_right[self.player_jump_anim_count], (self.player_x, self.player_y))
            elif (keys[pygame.K_LEFT] or keys[pygame.K_a]) and keys[pygame.K_LCTRL] and self.player_x > -40:
                if wind:
                    self.player_speed = 19
                else:
                    self.player_speed = 14
                self.player_x -= self.player_speed
                walk_sound.stop()
                if self.jump_sound_count == True:
                    if sound_on == True:
                        jump_sound.play()
                    self.jump_sound_count = False
                self.check_sound = False
                screen.blit(jump_left[self.player_jump_anim_count], (self.player_x, self.player_y))
            elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and self.player_x < 1110:
                if wind:
                    self.player_speed = 5
                else:
                    self.player_speed = 9
                self.player_x += self.player_speed
                walk_sound.stop()
                if self.jump_sound_count == True:
                    if sound_on == True:
                        jump_sound.play()
                    self.jump_sound_count = False
                self.check_sound = False
                screen.blit(jump_right[self.player_jump_anim_count], (self.player_x, self.player_y))
            elif (keys[pygame.K_LEFT] or keys[pygame.K_a]) and self.player_x > -40:
                if wind:
                    self.player_speed = 14
                else:
                    self.player_speed = 9
                self.player_x -= self.player_speed
                walk_sound.stop()
                if self.jump_sound_count == True:
                    if sound_on == True:
                        jump_sound.play()
                    self.jump_sound_count = False
                self.check_sound = False
                screen.blit(jump_left[self.player_jump_anim_count], (self.player_x, self.player_y))
            else:
                if self.jump_sound_count == True:
                    if sound_on == True:
                        jump_sound.play()
                    self.jump_sound_count = False
                if wind and self.player_x > -40:
                    self.player_x -= 2
                else:
                    pass
                screen.blit(pygame.image.load("images/Standing/tile004.png").convert_alpha(),
                            (self.player_x, self.player_y))
        else:
            if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and keys[pygame.K_LCTRL] and self.player_x > -40:
                if wind:
                    self.player_speed = 19
                else:
                    self.player_speed = 14
                self.player_x -= self.player_speed
                if self.check_sound == False:
                    if sound_on == True:
                        walk_sound.play(-1)
                    self.check_sound = True
                screen.blit(run_left[self.player_run_anim_count], (self.player_x, self.player_y))
            elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and keys[pygame.K_LCTRL] and self.player_x < 1110:
                if wind:
                    self.player_speed = 9
                else:
                    self.player_speed = 14
                self.player_x += self.player_speed
                if self.check_sound == False:
                    if sound_on == True:
                        walk_sound.play(-1)
                    self.check_sound = True
                screen.blit(run_right[self.player_run_anim_count], (self.player_x, self.player_y))
            elif (keys[pygame.K_LEFT] or keys[pygame.K_a]) and self.player_x > -40:
                if wind:
                    self.player_speed = 14
                else:
                    self.player_speed = 9
                self.player_x -= self.player_speed
                if self.check_sound == False:
                    if sound_on == True:
                        walk_sound.play(-1)
                    self.check_sound = True
                screen.blit(walk_left[self.player_anim_count], (self.player_x, self.player_y))
            elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and self.player_x < 1110:
                if wind:
                    self.player_speed = 5
                else:
                    self.player_speed = 9
                self.player_x += self.player_speed
                if self.check_sound == False:
                    if sound_on == True:
                        walk_sound.play(-1)
                    self.check_sound = True
                screen.blit(walk_right[self.player_anim_count], (self.player_x, self.player_y))
            else:
                walk_sound.stop()
                self.check_sound = False
                if wind and self.player_x > -40:
                    self.player_x -= 2
                else:
                    pass
                screen.blit(pygame.image.load("images/Standing/tile004.png").convert_alpha(),
                            (self.player_x, self.player_y))
            self.jump_sound_count = True
        if not self.is_jump:
            if keys[pygame.K_SPACE] or keys[pygame.K_UP] or keys[pygame.K_w]:
                self.is_jump = True
        else:
            if self.jump_count >= -6:
                if self.jump_count > 0:
                    self.player_y -= (self.jump_count ** 2) / 1.2
                else:
                    self.player_y += (self.jump_count ** 2) / 1.2
                self.jump_count -= 1
            else:
                self.is_jump = False
                self.jump_count = 6
        if self.player_anim_count == 6:
            self.player_anim_count = 0
        else:
            self.player_anim_count += 1
        if self.player_run_anim_count == 7:
            self.player_run_anim_count = 0
        else:
            self.player_run_anim_count += 1
        if self.is_jump == True:
            if self.add_count == 100:
                self.player_jump_anim_count += 1
                self.add_count = 0
            else:
                self.add_count += 100
        else:
            self.player_jump_anim_count = 0


class Saw():
    global num
    def __init__(self, saw_x, saw_y, speed):
        self.saw_x = saw_x
        self.saw_y = saw_y
        if num == 1:
            self.image = pygame.image.load("Images/Objects/saw1.png")
        elif num == 2:
            self.image = pygame.image.load("Images/Objects/saw2.png")
        elif num == 3:
            im = choice(["Images/Objects/tile000.png", "Images/Objects/tile001.png", "Images/Objects/tile002.png",
                         "Images/Objects/tile003.png"])
            self.image = pygame.image.load(im)
        self.image = pygame.transform.scale(self.image, (75, 75))
        self.speed = speed

    def draw_saw(self, screen):
        screen.blit(self.image, (self.saw_x, self.saw_y))
        self.saw_x -= self.speed


def Saw_generator():
    global playing_count
    global playing
    global saw
    global i
    global arr
    global num
    global spawn_rate
    global player_hitbox
    if playing == False:
        pass
    else:
        if playing_count % spawn_rate == 0:
            x = choice([-50, 1300])
            if x == -50:
                speed = choice([-15, -20, 20, -25, -25, -30])
            else:
                speed = choice([15, 20, 20, 25, 25, 30])
            arr[i] = Saw(x, 650, speed)
            if i == 5:
                i = 0
            else:
                i += 1
        if arr[0] is not None:
            arr[0].draw_saw(screen)
            saw_hitbox = pygame.Rect(arr[0].saw_x, arr[0].saw_y, 50, 50)
            if player_hitbox.colliderect(saw_hitbox):
                lose_screen()
        if arr[1] is not None:
            arr[1].draw_saw(screen)
            saw_hitbox = pygame.Rect(arr[1].saw_x, arr[1].saw_y, 50, 50)
            if player_hitbox.colliderect(saw_hitbox):
                lose_screen()
        if arr[2] is not None:
            arr[2].draw_saw(screen)
            saw_hitbox = pygame.Rect(arr[2].saw_x, arr[2].saw_y, 50, 50)
            if player_hitbox.colliderect(saw_hitbox):
                lose_screen()
        if arr[3] is not None:
            arr[3].draw_saw(screen)
            saw_hitbox = pygame.Rect(arr[3].saw_x, arr[3].saw_y, 50, 50)
            if player_hitbox.colliderect(saw_hitbox):
                lose_screen()
        if arr[4] is not None:
            arr[4].draw_saw(screen)
            saw_hitbox = pygame.Rect(arr[4].saw_x, arr[4].saw_y, 50, 50)
            if player_hitbox.colliderect(saw_hitbox):
                lose_screen()
        if arr[5] is not None:
            arr[5].draw_saw(screen)
            saw_hitbox = pygame.Rect(arr[5].saw_x, arr[5].saw_y, 50, 50)
            if player_hitbox.colliderect(saw_hitbox):
                lose_screen()


class Disco_ball():
    def __init__(self, ball_x, ball_y):
        self.ball_x = ball_x
        self.ball_y = ball_y

    def draw_disco(self, screen):
        screen.blit(pygame.transform.scale(pygame.image.load("Images/Objects/disco.png"), (200, 200)),
                    (self.ball_x, self.ball_y))
        self.ball_y += 20


def Disco_ball_generator():
    global playing_count
    global playing
    global arr_disco
    global j
    global disco
    global player_hitbox
    if playing == False:
        pass
    else:
        #player_hitbox = pygame.Rect(player2.player_x + 45, player2.player_y + 57, 40, 70)
        if playing_count % 50 == 0:
            x = randint(0, 1200)
            disco = Disco_ball(x, -100)
        if disco is not None:
            disco.draw_disco(screen)
            ball_hitbox = pygame.Rect(disco.ball_x + 60, disco.ball_y + 50, 82, 82)
            if player_hitbox.colliderect(ball_hitbox):
                lose_screen()


class Button:
    global sound_on
    def __init__(self, x, y, width, height, text, image_path, hover_image_path=None, sound_path=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.transform.scale(pygame.image.load(image_path), (width, height))
        self.hover_image = self.image
        if hover_image_path:
            self.hover_image = pygame.transform.scale(pygame.image.load(hover_image_path), (width, height))
        self.text = text
        if sound_path and sound_on:
            self.sound = pygame.mixer.Sound(sound_path)
        else:
            self.sound = pygame.mixer.Sound("Sounds/silence-sound-effect.mp3")
        self.button_hitbox = self.image.get_rect(topleft=(x, y))
        self.mouse_hover = False

    def draw_button(self, screen):
        current_image = self.hover_image if self.mouse_hover else self.image
        screen.blit(current_image, self.button_hitbox.topleft)
        text = pygame.font.Font(None, 36)
        text_surface = text.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.button_hitbox.center)
        screen.blit(text_surface, text_rect)

    def mouse_check(self, mouse_pos):
        self.mouse_hover = self.button_hitbox.collidepoint(mouse_pos)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.mouse_hover:
            if self.sound:
                self.sound.play()
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, button=self))


def displ1():
    global playing
    global playing_count
    global num
    global spawn_rate
    global player_hitbox
    global level_count
    running = True
    num = 1
    spawn_rate = 25
    atm = pygame.transform.scale(pygame.image.load("Images/Objects/atm.png").convert_alpha(), (70, 70))
    atm_hitbox = pygame.Rect(554, 607, 45, 70)
    while running:
        lvl1.background(screen)
        screen.blit(atm, (541, 607))
        player1.display_player(screen)
        player_hitbox = pygame.Rect(player1.player_x + 45, player1.player_y + 57, 40, 70)
        if player_hitbox.colliderect(atm_hitbox) and playing_count == 0:
            pygame.mixer.music.pause()
            if sound_on:
                start_sound.play()
            screen.blit(pygame.image.load("images/Standing/tile004.png").convert_alpha(),
                        (player1.player_x, player1.player_y))
            pygame.display.flip()
            pygame.time.wait(5000)
            start_sound.stop()
            playing = True
            if music_count == 0:
                pygame.mixer.music.load("Sounds/KRS-One_-_Sound_of_da_Police.mp3")
                pygame.mixer.music.set_volume(0.2)
                pygame.mixer.music.play(-1)
        if playing_count == 100 and playing == True:
            playing = False
            playing_count = 1
            level_count += 1
            win_screen()
        elif playing_count < 1000 and playing == True:
            playing_count += 1
        Saw_generator()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    pause_menu()
        pygame.display.flip()
        clock.tick(20)


def displ2():
    global playing
    global playing_count
    global num
    global spawn_rate
    global player_hitbox
    global level_count
    running = True
    num = 2
    spawn_rate = 20
    atm = pygame.transform.scale(pygame.image.load("Images/Objects/atm.png").convert_alpha(), (70, 70))
    atm_hitbox = pygame.Rect(554, 607, 45, 70)
    while running:
        lvl2.background(screen)
        screen.blit(atm, (541, 607))
        player2.display_player(screen)
        player_hitbox = pygame.Rect(player2.player_x + 45, player2.player_y + 57, 40, 70)
        if player_hitbox.colliderect(atm_hitbox) and playing_count == 0:
            pygame.mixer.music.pause()
            if sound_on:
                start_sound.play()
            screen.blit(pygame.image.load("images/Standing/tile004.png").convert_alpha(),
                        (player2.player_x, player2.player_y))
            pygame.display.flip()
            pygame.time.wait(5000)
            start_sound.stop()
            playing = True
            if music_count == 0:
                pygame.mixer.music.load("Sounds/Kordhell - Murder In My Mind.mp3")
                pygame.mixer.music.set_volume(0.2)
                pygame.mixer.music.play(-1)
        if playing_count == 1000 and playing == True:
            playing = False
            playing_count = 1
            level_count+=1
            win_screen()
        elif playing_count < 1000 and playing == True:
            playing_count += 1
        Saw_generator()
        Disco_ball_generator()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    pause_menu()
        pygame.display.flip()
        clock.tick(120)


def displ3():
    global wind
    global playing
    global playing_count
    global num
    global spawn_rate
    global player_hitbox
    running = True
    num = 3
    spawn_rate = 20
    atm = pygame.transform.scale(pygame.image.load("Images/Objects/atm.png").convert_alpha(), (70, 70))
    atm_hitbox = pygame.Rect(554, 607, 45, 70)
    while running:
        lvl3.background(screen)
        screen.blit(atm, (541, 607))
        player3.display_player(screen)
        player_hitbox = pygame.Rect(player3.player_x + 45, player3.player_y + 57, 40, 70)
        if player_hitbox.colliderect(atm_hitbox) and playing_count == 0:
            wind = True
            pygame.mixer.music.pause()
            if sound_on:
                start_sound.play()
            screen.blit(pygame.image.load("images/Standing/tile004.png").convert_alpha(),
                        (player3.player_x, player3.player_y))
            pygame.display.flip()
            pygame.time.wait(5000)
            start_sound.stop()
            playing = True
            if music_count == 0:
                pygame.mixer.music.load("Sounds/wind.mp3")
                pygame.mixer.music.set_volume(1)
                pygame.mixer.music.play(-1)
        if playing_count == 1000 and playing == True:
            playing = False
            playing_count = 1
            wind=False
            win_screen()
        elif playing_count < 1000 and playing == True:
            playing_count += 1
        Saw_generator()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    wind=False
                    pause_menu()
        pygame.display.flip()
        clock.tick(20)
def win_screen():
    running=True
    global saw
    global disco
    global arr
    global playing_count
    global playing
    global num
    global wind
    global player1
    global player2
    global player3
    if music_count == 0:
        pygame.mixer.music.load("Sounds/48bb90af8e1e401.mp3")
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)
    back_button = Button(0, 0, 270, 100, "Back to Map", "Images/Buttons/button_menu.png",
                         "Images/Buttons/button_menu_hovered.png", "Sounds/button_click_sound.wav")
    while running:
        if num==1:
            screen.blit(pygame.transform.scale(pygame.image.load("Images/Objects/money.png"), (70, 70)),(player1.player_x+30, player1.player_y-40))
        if num==2:
            screen.blit(pygame.transform.scale(pygame.image.load("Images/Objects/money.png"), (70, 70)),(player2.player_x+30, player2.player_y-40))
        if num==3:
            screen.blit(pygame.transform.scale(pygame.image.load("Images/Objects/money.png"), (70, 70)),(player3.player_x+30, player3.player_y-40))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exit()
            if event.type == pygame.USEREVENT and event.button == back_button:
                if num == 1:
                    player1 = Player(100, 550)
                    saw = None
                    arr = [None, None, None, None, None, None]
                    playing = False
                    playing_count = 0
                elif num == 2:
                    player2 = Player(100, 550)
                    saw = None
                    disco = None
                    arr = [None, None, None, None, None, None]
                    playing = False
                    playing_count = 0
                elif num == 3:
                    player3 = Player(100, 550)
                    saw = None
                    arr = [None, None, None, None, None, None]
                    playing = False
                    playing_count = 0
                    wind = False
                levels()
            back_button.handle_event(event)
        back_button.mouse_check(pygame.mouse.get_pos())
        back_button.draw_button(screen)
        pygame.display.flip()
        clock.tick(20)
def lose_screen():
    running=True
    global saw
    global disco
    global arr
    global playing_count
    global playing
    global num
    global wind
    global player1
    global player2
    global player3
    back_button = Button(0, 0, 270, 100, "Back to Map", "Images/Buttons/button_menu.png",
                         "Images/Buttons/button_menu_hovered.png", "Sounds/button_click_sound.wav")
    restart_button = Button(0, 90, 270, 100, "Restart", "Images/Buttons/button_menu.png",
                         "Images/Buttons/button_menu_hovered.png", "Sounds/button_click_sound.wav")
    if music_count==0:
        pygame.mixer.music.load("Sounds/48bb90af8e1e401.mp3")
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exit()
            if event.type == pygame.USEREVENT and event.button == back_button:
                if num == 1:
                    player1 = Player(100, 550)
                    saw = None
                    arr = [None, None, None, None, None, None]
                    playing = False
                    playing_count = 0
                elif num == 2:
                    player2 = Player(100, 550)
                    saw = None
                    disco = None
                    arr = [None, None, None, None, None, None]
                    playing = False
                    playing_count = 0
                elif num == 3:
                    player3 = Player(100, 550)
                    saw = None
                    arr = [None, None, None, None, None, None]
                    playing = False
                    playing_count = 0
                    wind = False
                levels()
            if event.type == pygame.USEREVENT and event.button == restart_button:
                running = False
                if num == 1:
                    player1 = Player(100, 550)
                    saw = None
                    arr = [None, None, None, None, None, None]
                    playing = False
                    playing_count = 0
                    displ1()
                elif num == 2:
                    player2 = Player(100, 550)
                    saw = None
                    disco = None
                    arr = [None, None, None, None, None, None]
                    playing = False
                    playing_count = 0
                    displ2()
                elif num == 3:
                    player3 = Player(100, 550)
                    saw = None
                    arr = [None, None, None, None, None, None]
                    playing = False
                    wind = False
                    playing_count = 0
                    displ3()
            for button in [back_button, restart_button]:
                button.handle_event(event)
        for button in [back_button, restart_button]:
            button.mouse_check(pygame.mouse.get_pos())
            button.draw_button(screen)
        pygame.display.flip()
        clock.tick(20)
def pause_menu():
    global sound_on
    global music_count
    global sound_count
    global player1
    global player2
    global player3
    global saw
    global disco
    global arr
    global playing_count
    global playing
    global num
    global wind
    running = True
    back_to_level_button = Button(350, 100, 360, 126, "Continue", "Images/Buttons/button_menu.png",
                                  "Images/Buttons/button_menu_hovered.png", "Sounds/button_click_sound.wav")
    back_to_map_button = Button(430, 228, 360, 126, "Back to the map",
                                "Images/Buttons/button_menu.png", "Images/Buttons/button_menu_hovered.png",
                                "Sounds/button_click_sound.wav")
    restart_button = Button(350, 356, 360, 126, "Restart", "Images/Buttons/button_menu.png",
                            "Images/Buttons/button_menu_hovered.png", "Sounds/button_click_sound.wav")
    audio_off_button = Button(430, 484, 360, 126, "Audio", "Images/Buttons/button_menu.png",
                              "Images/Buttons/button_menu_hovered.png", "Sounds/button_click_sound.wav")
    sound_off_button = Button(350, 610, 360, 126, "Sound", "Images/Buttons/button_menu.png",
                              "Images/Buttons/button_menu_hovered.png", "Sounds/button_click_sound.wav")
    sound_on_image = pygame.image.load("Images/Buttons/button_audio_on.png")
    sound_on_image = pygame.transform.scale(sound_on_image, (60, 60))
    sound_off_image = pygame.image.load("Images/Buttons/button_audio_off.png")
    sound_off_image = pygame.transform.scale(sound_off_image, (60, 60))
    if music_count == 0:
        screen.blit(sound_on_image, (800, 520))
    else:
        screen.blit(sound_off_image, (800, 520))
    if sound_on:
        screen.blit(sound_on_image, (720, 645))
    else:
        screen.blit(sound_off_image, (720, 645))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exit()
            if event.type == pygame.USEREVENT and event.button == restart_button:
                running = False
                if num == 1:
                    player1 = Player(100, 550)
                    saw = None
                    arr = [None, None, None, None, None, None]
                    playing = False
                    playing_count = 0
                    pygame.mixer.music.load("Sounds/48bb90af8e1e401.mp3")
                    pygame.mixer.music.set_volume(0.2)
                    if music_count == 0:
                        pygame.mixer.music.play(-1)
                    displ1()
                elif num == 2:
                    player2 = Player(100, 550)
                    saw = None
                    disco = None
                    arr = [None, None, None, None, None, None]
                    playing = False
                    playing_count = 0
                    pygame.mixer.music.load("Sounds/48bb90af8e1e401.mp3")
                    pygame.mixer.music.set_volume(0.2)
                    if music_count == 0:
                        pygame.mixer.music.play(-1)
                    displ2()
                elif num == 3:
                    player3 = Player(100, 550)
                    saw = None
                    arr = [None, None, None, None, None, None]
                    playing = False
                    wind=False
                    playing_count = 0
                    pygame.mixer.music.load("Sounds/48bb90af8e1e401.mp3")
                    pygame.mixer.music.set_volume(0.2)
                    if music_count == 0:
                        pygame.mixer.music.play(-1)
                    displ3()
            if event.type == pygame.USEREVENT and event.button == back_to_level_button:
                running = False
                if num == 1:
                    displ1()
                elif num == 2:
                    displ2()
                elif num == 3:
                    displ3()
            if event.type == pygame.USEREVENT and event.button == back_to_map_button:
                running = False
                if num == 1:
                    player1 = Player(100, 550)
                    saw = None
                    arr = [None, None, None, None, None, None]
                    playing = False
                    playing_count = 0
                    pygame.mixer.music.load("Sounds/48bb90af8e1e401.mp3")
                    pygame.mixer.music.set_volume(0.2)
                    if music_count == 0:
                        pygame.mixer.music.play(-1)
                elif num == 2:
                    player2 = Player(100, 550)
                    saw = None
                    disco = None
                    arr = [None, None, None, None, None, None]
                    playing = False
                    playing_count = 0
                    pygame.mixer.music.load("Sounds/48bb90af8e1e401.mp3")
                    pygame.mixer.music.set_volume(0.2)
                    if music_count == 0:
                        pygame.mixer.music.play(-1)
                elif num == 3:
                    player3 = Player(100, 550)
                    saw = None
                    arr = [None, None, None, None, None, None]
                    playing = False
                    playing_count = 0
                    wind=False
                    pygame.mixer.music.load("Sounds/48bb90af8e1e401.mp3")
                    pygame.mixer.music.set_volume(0.2)
                    if music_count == 0:
                        pygame.mixer.music.play(-1)
                levels()
            if event.type == pygame.USEREVENT and event.button == audio_off_button:
                if music_count == 1:
                    pygame.mixer.music.unpause()
                    screen.blit(sound_on_image, (800, 520))
                    music_count = 0
                else:
                    pygame.mixer.music.pause()
                    screen.blit(sound_off_image, (800, 520))
                    music_count = 1
            if event.type == pygame.USEREVENT and event.button == sound_off_button:
                if sound_count == 1:
                    sound_on = True
                    screen.blit(sound_on_image, (720, 645))
                    sound_count = 0
                else:
                    sound_on = False
                    screen.blit(sound_off_image, (720, 645))
                    sound_count = 1
            for button in [back_to_level_button, back_to_map_button, restart_button, audio_off_button,
                           sound_off_button]:
                button.handle_event(event)
        for button in [back_to_level_button, back_to_map_button, restart_button, audio_off_button, sound_off_button]:
            button.mouse_check(pygame.mouse.get_pos())
            button.draw_button(screen)
        pygame.display.flip()
        clock.tick(20)


def setting_menu():
    global sound_on
    global music_count
    global sound_count
    running = True
    bg = pygame.image.load("Images/Backgrounds/menu_background.png")
    bg = pygame.transform.scale(bg, (1200, 800))
    screen.blit(bg, (0, 0))
    back_button = Button(0, 0, 270, 100, "Back", "Images/Buttons/button_menu.png",
                         "Images/Buttons/button_menu_hovered.png", "Sounds/button_click_sound.wav")
    audio_off_button = Button(320, 330, 360, 126, "Audio",
                              "Images/Buttons/button_menu.png", "Images/Buttons/button_menu_hovered.png",
                              "Sounds/button_click_sound.wav")
    sound_off_button = Button(320, 450, 360, 126, "Sound", "Images/Buttons/button_menu.png",
                              "Images/Buttons/button_menu_hovered.png", "Sounds/button_click_sound.wav")
    sound_on_image = pygame.image.load("Images/Buttons/button_audio_on.png")
    sound_on_image = pygame.transform.scale(sound_on_image, (60, 60))
    sound_off_image = pygame.image.load("Images/Buttons/button_audio_off.png")
    sound_off_image = pygame.transform.scale(sound_off_image, (60, 60))
    if music_count == 0:
        screen.blit(sound_on_image, (700, 360))
    else:
        screen.blit(sound_off_image, (700, 360))
    if sound_on:
        screen.blit(sound_on_image, (700, 480))
    else:
        screen.blit(sound_off_image, (700, 480))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    main_menu()
            if event.type == pygame.USEREVENT and event.button == back_button:
                running = False
                main_menu()
            if event.type == pygame.USEREVENT and event.button == audio_off_button:
                if music_count == 1:
                    pygame.mixer.music.unpause()
                    screen.blit(sound_on_image, (700, 360))
                    music_count = 0
                else:
                    pygame.mixer.music.pause()
                    screen.blit(sound_off_image, (700, 360))
                    music_count = 1
            if event.type == pygame.USEREVENT and event.button == sound_off_button:
                if sound_count == 1:
                    sound_on = True
                    screen.blit(sound_on_image, (700, 480))
                    sound_count = 0
                else:
                    sound_on = False
                    screen.blit(sound_off_image, (700, 480))
                    sound_count = 1
            for button in [back_button, audio_off_button, sound_off_button]:
                button.handle_event(event)
        for button in [back_button, audio_off_button, sound_off_button]:
            button.mouse_check(pygame.mouse.get_pos())
            button.draw_button(screen)
        pygame.display.flip()
        clock.tick(20)


def levels():
    global playing_count
    global level_count
    running = True
    bg = pygame.image.load("Images/Backgrounds/menu_background.png")
    bg = pygame.transform.scale(bg, (1200, 800))
    screen.blit(bg, (0, 0))
    back_button = Button(0, 0, 270, 100, "Back", "Images/Buttons/button_menu.png",
                         "Images/Buttons/button_menu_hovered.png", "Sounds/button_click_sound.wav")
    lvl1_button = Button(320, 480, 360, 126, "Level 1", "Images/Buttons/button_menu.png",
                         "Images/Buttons/button_menu_hovered.png", "Sounds/button_click_sound.wav")
    lvl2_button = Button(320, 335, 360, 126, "Level 2", "Images/Buttons/button_menu.png",
                         "Images/Buttons/button_menu_hovered.png", "Sounds/button_click_sound.wav")
    lvl3_button = Button(320, 200, 360, 126, "Level 3", "Images/Buttons/button_menu.png",
                         "Images/Buttons/button_menu_hovered.png", "Sounds/button_click_sound.wav")
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    main_menu()
            if event.type == pygame.USEREVENT and event.button == back_button:
                running = False
                main_menu()
            if event.type == pygame.USEREVENT and event.button == lvl1_button and level_count>0:
                playing_count = 0
                displ1()
            if event.type == pygame.USEREVENT and event.button == lvl2_button and level_count>1:
                playing_count = 0
                displ2()
            if event.type == pygame.USEREVENT and event.button == lvl3_button and level_count>2:
                playing_count = 0
                displ3()
            for button in [back_button, lvl1_button, lvl2_button, lvl3_button]:
                button.handle_event(event)
        for button in [back_button, lvl1_button, lvl2_button, lvl3_button]:
            button.mouse_check(pygame.mouse.get_pos())
            button.draw_button(screen)
        pygame.display.flip()
        clock.tick(20)

def instructions_display():
    global sound_on
    global music_count
    global sound_count
    running = True
    bg = pygame.image.load("Images/Backgrounds/menu_background.png")
    bg = pygame.transform.scale(bg, (1200, 800))
    screen.blit(bg, (0, 0))
    back_button = Button(0, 0, 270, 100, "Back", "Images/Buttons/button_menu.png",
                         "Images/Buttons/button_menu_hovered.png", "Sounds/button_click_sound.wav")
    while running:
        f1 = pygame.font.Font(None, 36)
        text1 = f1.render("There's 3 levels and all of them are different. ", True, (255, 255, 255))
        text2 = f1.render('When you entered anu level, you have to move straight to ATM', True, (255, 255, 255))
        text3 = f1.render('Then the game starts. You need to jump over any obstacles and dont die', True, (255, 255, 255))
        text4 = f1.render('You, as a player, can move in any direction you want(WASD and arrows)', True,(255, 255, 255))
        text5 = f1.render('You can also jump on SPACE, W and arrow UP', True,(255, 255, 255))
        screen.blit(text1, (300, 100))
        screen.blit(text2, (300, 170))
        screen.blit(text3, (300, 240))
        screen.blit(text4, (300, 310))
        screen.blit(text5, (300, 380))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    main_menu()
            if event.type == pygame.USEREVENT and event.button == back_button:
                running = False
                main_menu()
            back_button.handle_event(event)
        back_button.mouse_check(pygame.mouse.get_pos())
        back_button.draw_button(screen)
        pygame.display.flip()
        clock.tick(20)

def main_menu():
    global sound_on
    running = True
    bg = pygame.image.load("Images/Backgrounds/menu_background.png")
    bg = pygame.transform.scale(bg, (1200, 800))
    screen.blit(bg, (0, 0))
    start_button = Button(320, 210, 360, 126, "Start", "Images/Buttons/button_menu.png",
                          "Images/Buttons/button_menu_hovered.png", "Sounds/button_click_sound.wav")
    settings_button = Button(320, 330, 360, 126, "Settings", "Images/Buttons/button_menu.png",
                             "Images/Buttons/button_menu_hovered.png", "Sounds/button_click_sound.wav")
    exit_button = Button(320, 450, 360, 126, "Exit", "Images/Buttons/button_menu.png",
                         "Images/Buttons/button_menu_hovered.png", "Sounds/button_click_sound.wav")
    instructions= Button(320, 570, 360, 126, "How to play?", "Images/Buttons/button_menu.png",
                         "Images/Buttons/button_menu_hovered.png", "Sounds/button_click_sound.wav")
    f1 = pygame.font.Font(None, 100)
    text1 = f1.render('Bank Robbery', True, (255, 255, 255))
    text2 = f1.render('GAME', True, (255, 255, 255))
    screen.blit(text1, (700, 100))
    screen.blit(text2, (700, 170))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exit()
            if event.type == pygame.USEREVENT and event.button == start_button:
                levels()
            if event.type == pygame.USEREVENT and event.button == settings_button:
                setting_menu()
            if event.type == pygame.USEREVENT and event.button == exit_button:
                running = False
                exit()
            if event.type == pygame.USEREVENT and event.button == instructions:
                instructions_display()
            for button in [start_button, settings_button, exit_button,instructions]:
                button.handle_event(event)
        for button in [start_button, settings_button, exit_button,instructions]:
            button.mouse_check(pygame.mouse.get_pos())
            button.draw_button(screen)
        pygame.display.flip()
        clock.tick(20)


# main code
pygame.display.set_caption("Bankomat game")
icon = pygame.image.load("images/icon.png")
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((1200, 800))
# sounds
pygame.mixer.music.load("Sounds/48bb90af8e1e401.mp3")
pygame.mixer.music.set_volume(0.2)
walk_sound = pygame.mixer.Sound("Sounds/playerwalking.mp3")
walk_sound.set_volume(1)
jump_sound = pygame.mixer.Sound("Sounds/pryjok-mario.mp3")
jump_sound.set_volume(0.5)
start_sound = pygame.mixer.Sound("Sounds/e7bf5bda5f8ba95.mp3")
pygame.mixer.music.play(-1)
sound_on = True
music_count = 0
sound_count = 0
# init
player1 = Player(100, 550)
player2 = Player(100, 550)
player3 = Player(100, 550)
lvl1 = level_1()
lvl2 = level_2()
lvl3 = level_3()
#counts
is_jump = False
jump_count = 6
playing = False
playing_count = 0
saw = None
disco = None
arr = [None, None, None, None, None, None]
i = 0
num = 0
spawn_rate = 0
wind = False
player_hitbox=None
level_count=3
main_menu()