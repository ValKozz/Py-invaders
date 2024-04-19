import pygame
from config import *
from player import PlayerSprite
from alien import AlienSprite
from missile import Missile


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
        self.clock = pygame.time.Clock()
        self.run = True
        self.player_is_alive = True
        self.alien_moves = 0
        self.time_since_shot = pygame.time.Clock.get_time()

        # Init game
        pygame.init()
        # init sprites
        self.init_sprites()
        self.game_loop()

    def init_sprites(self):
        # Define group of sprites
        self.aliens_group = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group()
        self.missile_group = pygame.sprite.Group()

        self.init_player()
        self.init_aliens()

    def init_player(self):
        self.player = PlayerSprite()
        self.player_group.add(self.player)

    def init_aliens(self):
        x_proportion = int(SCREEN_W / 80)
        y_proportion = ALIEN_POS_Y
        for y in y_proportion:
            for x in range(x_proportion):
                if x != 0:
                    self.aliens_group.add(AlienSprite(x=x * 80, y=y))


    def move_alien_group(self):
        for alien in self.aliens_group:
            if alien.alive == False:
                alien.kill()

            if self.alien_moves < 2:
                alien.rect.move_ip(+10, 0)
            elif self.alien_moves == 2:
                alien.rect.move_ip(0, 10)
            elif self.alien_moves < 5 and self.alien_moves > 2:
                alien.rect.move_ip(-10, 0)
            else:
                alien.rect.move_ip(0, 10)

            if pygame.Rect.colliderect(self.player.rect, alien.rect):
                print(self.player.rect)
                self.show_gameover()

            for missile in self.missile_group:
                if pygame.Rect.colliderect(missile.rect, alien.rect):
                    alien.image = alien.explosion_image
                    missile.kill()
                    alien.alive = False

        self.alien_moves += 1 

        if self.alien_moves > 5:
            self.alien_moves = 0

    def move_player(self, key):
        if key[pygame.K_a]:
            self.player.rect.move_ip(-10, 0)
        elif key[pygame.K_d]:
            self.player.rect.move_ip(10, 0)
        elif key[pygame.K_s]:
            self.player.rect.move_ip(0, 10)
        elif key[pygame.K_w]:
            self.player.rect.move_ip(0, -10)
        elif key[pygame.K_SPACE]:
            self.shoot()

    def shoot(self):
        missile = Missile(x=self.player.rect.x + (self.player.image.get_width()/2), y=self.player.rect.y)
        self.missile_group.add(missile)
                
    def game_loop(self):
        alien_clock = 0
        while self.run and self.player_is_alive:
            target = self.clock.tick(TARGET_FPS)
            alien_clock += target

            if alien_clock > 60 * target:
                alien_clock = 0
                self.move_alien_group()

            self.screen.fill((0, 0, 0))
            self.player_group.update(target)
            self.player_group.draw(self.screen)

            self.aliens_group.update(target)
            self.aliens_group.draw(self.screen)
            

            if len(self.missile_group):
                self.missile_group.update(target)
                self.missile_group.draw(self.screen)

                for missile in self.missile_group:
                    missile.move_self()

            key = pygame.key.get_pressed()
            self.move_player(key)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

            pygame.display.update()

        pygame.quit()

    def show_gameover(self):
        self.player_is_alive = False
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render('GAME OVER', True, 'white', 'black')
        text_rect = text.get_rect()
        text_rect.center = (SCREEN_W//2, SCREEN_H//2)

        while self.run:
            self.screen.fill((0, 0, 0))
            self.screen.blit(text, text_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

            pygame.display.update()


if __name__ == "__main__":
    Game()
