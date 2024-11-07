import pygame
import sys
import random
import time

pygame.init()

class GameObject:
    def __init__(self, color, position):
        self.color = color
        self.position = position

    def draw(self, game_window):
        pygame.draw.rect(game_window, self.color, pygame.Rect(self.position[0], self.position[1], 10, 10))

class Snake(GameObject):
    def __init__(self, position):
        super().__init__(pygame.Color(0, 255, 0), position)
        self.body = [list(position), [position[0] - 10, position[1]], [position[0] - 20, position[1]]]
        self.direction = 'RIGHT'
        self.change_to = self.direction

    def change_direction(self, direction):
        
        if direction == 'UP' and self.direction != 'DOWN':
            self.change_to = 'UP'
        if direction == 'DOWN' and self.direction != 'UP':
            self.change_to = 'DOWN'
        if direction == 'LEFT' and self.direction != 'RIGHT':
            self.change_to = 'LEFT'
        if direction == 'RIGHT' and self.direction != 'LEFT':
            self.change_to = 'RIGHT'

    def move(self):
        # Mengubah arah sesuai input terbaru
        self.direction = self.change_to
        if self.direction == 'UP':
            self.position[1] -= 10
        if self.direction == 'DOWN':
            self.position[1] += 10
        if self.direction == 'LEFT':
            self.position[0] -= 10
        if self.direction == 'RIGHT':
            self.position[0] += 10
        self.body.insert(0, list(self.position))

    def shrink(self):
        self.body.pop()

    def draw(self, surface):
        for pos in self.body:
            pygame.draw.rect(surface, self.color, pygame.Rect(pos[0], pos[1], 10, 10))

    def check_collision(self, frame_size_x, frame_size_y):
        if (self.position[0] < 0 or self.position[0] >= frame_size_x or
            self.position[1] < 0 or self.position[1] >= frame_size_y):
            return True
        for block in self.body[1:]:
            if self.position == block:
                return True
        return False

class Apple(GameObject):
    def __init__(self, frame_size_x, frame_size_y, color):
        position = [random.randrange(1, (frame_size_x // 10)) * 10,
                    random.randrange(1, (frame_size_y // 10)) * 10]
        super().__init__(color, position)

    def respawn(self, frame_size_x, frame_size_y):
        self.position = [random.randrange(1, (frame_size_x // 10)) * 10,
                         random.randrange(1, (frame_size_y // 10)) * 10]


class Game:
    def __init__(self):
        self.frame_size_x = 720
        self.frame_size_y = 480
        self.game_window = pygame.display.set_mode((self.frame_size_x, self.frame_size_y))
        pygame.display.set_caption('Snake Game')
        self.fps_controller = pygame.time.Clock()
        self.snake = Snake([100, 50])
        self.apple_red = Apple(self.frame_size_x, self.frame_size_y, pygame.Color(255, 0, 0))
        self.apple_blue = Apple(self.frame_size_x, self.frame_size_y, pygame.Color(0, 0, 255))
        self.score = 0

    def show_score(self):
        # Menampilkan skor di layar
        score_font = pygame.font.SysFont('Arial', 20)
        score_surface = score_font.render('Score : ' + str(self.score), True, pygame.Color(0, 0, 0))
        score_rect = score_surface.get_rect()
        score_rect.midtop = (72, 15)
        self.game_window.blit(score_surface, score_rect)

    def game_over(self):
        # Menampilkan layar game over
        my_font = pygame.font.SysFont('Arial', 90)
        game_over_surface = my_font.render('YOU DIED', True, pygame.Color(255, 0, 0))
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (self.frame_size_x / 2, self.frame_size_y / 4)
        self.game_window.fill(pygame.Color(0, 0, 0))
        self.game_window.blit(game_over_surface, game_over_rect)
        pygame.display.flip()
        time.sleep(3)
        pygame.quit()
        sys.exit()

    def run(self):
        # Loop utama permainan
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.snake.change_direction('UP')
                    elif event.key == pygame.K_DOWN:
                        self.snake.change_direction('DOWN')
                    elif event.key == pygame.K_LEFT:
                        self.snake.change_direction('LEFT')
                    elif event.key == pygame.K_RIGHT:
                        self.snake.change_direction('RIGHT')
                    elif event.key == pygame.K_ESCAPE:
                        pygame.event.post(pygame.event.Event(pygame.QUIT))

            # Menggerakkan ular
            self.snake.move()

            # Cek jika ular makan apel merah
            if self.snake.position == self.apple_red.position:
                self.score += 1
                self.apple_red.respawn(self.frame_size_x, self.frame_size_y)
                # Tidak memangkas ekor ular agar ular bertambah panjang
            # Cek jika ular makan apel biru
            elif self.snake.position == self.apple_blue.position:
                self.score += 2
                self.apple_blue.respawn(self.frame_size_x, self.frame_size_y)
                # Tidak memangkas ekor ular agar ular bertambah panjang
            else:
                # Panggil shrink hanya jika tidak makan apel
                self.snake.shrink()

            # Menggambar elemen permainan
            self.game_window.fill(pygame.Color(255, 255, 255))
            self.snake.draw(self.game_window)
            self.apple_red.draw(self.game_window)
            self.apple_blue.draw(self.game_window)
            self.show_score()

            # Cek tabrakan
            if self.snake.check_collision(self.frame_size_x, self.frame_size_y):
                self.game_over()

            pygame.display.update()
            self.fps_controller.tick(10)

# Menjalankan game
if __name__ == "__main__":
    game = Game()
    game.run()
