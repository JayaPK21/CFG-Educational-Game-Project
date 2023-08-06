import pygame
import sys
import random

pygame.init()

SW, SH = 800, 800  # Screen width and height

BLOCK_SIZE = 50  # Size of each block in the game grid

FONT = pygame.font.Font(None, BLOCK_SIZE)  # Font for displaying numbers

screen = pygame.display.set_mode((800, 800))  # Create the game window
pygame.display.set_caption("Snake!")  # Set window title
clock = pygame.time.Clock()  # Create a clock object to control frame rate


class Snake:
    def __init__(self):
        self.x, self.y = BLOCK_SIZE, BLOCK_SIZE  # Initial position of the snake
        self.xdir = 1  # Initial movement direction (x-axis)
        self.ydir = 0  # Initial movement direction (y-axis)
        self.head = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)  # Snake's head rectangle
        self.body = [pygame.Rect(self.x - BLOCK_SIZE, self.y, BLOCK_SIZE, BLOCK_SIZE)]  # Snake's body segments
        self.dead = False  # Flag indicating whether the snake is dead (hit itself or boundaries)

    def update(self):
        global numbers
        for square in self.body:
            if self.head.x == square.x and self.head.y == square.y:
                self.dead = True  # Check if snake collided with itself
            if self.head.x not in range(0, SW) or self.head.y not in range(0, SH):
                self.dead = True  # Check if snake hit the game boundaries
        if self.dead:
            # Reset snake's position and attributes
            self.x, self.y = BLOCK_SIZE, BLOCK_SIZE
            self.head = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
            self.body = [pygame.Rect(self.x - BLOCK_SIZE, self.y, BLOCK_SIZE, BLOCK_SIZE)]
            self.xdir = 1
            self.ydir = 0
            self.dead = False
            numbers = [Number() for _ in range(8)]  # Generate 8 random numbers

        # Move the snake's body and head
        self.body.append(self.head)
        for i in range(len(self.body) - 1):
            self.body[i].x, self.body[i].y = self.body[i + 1].x, self.body[i + 1].y
        self.head.x += self.xdir * BLOCK_SIZE
        self.head.y += self.ydir * BLOCK_SIZE
        self.body.remove(self.head)


class Number:
    def __init__(self):
        self.value = self.generate_unique_number()
        self.color = self.generate_bright_color()
        self.x = int(random.randint(0, SW / BLOCK_SIZE - 1)) * BLOCK_SIZE
        self.y = int(random.randint(0, SH / BLOCK_SIZE - 1)) * BLOCK_SIZE
        self.rect = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)  # Number rectangle

    def generate_unique_number(self):
        possible_values = list(range(1, 21))
        for num in snake.body:
            if num.value in possible_values:
                possible_values.remove(num.value)
        return random.choice(possible_values)

    def generate_bright_color(self):
        while True:
            color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
            if sum(color) / 3 > 150:
                return color

    def update(self):
        text_color = (255, 255, 255)  # Default to white
        if sum(self.color) / 3 < 128:
            text_color = (0, 0, 0)  # Use black text on dark background

        number_text = FONT.render(str(self.value), True, text_color)
        text_rect = number_text.get_rect(center=self.rect.center)
        screen.blit(number_text, text_rect.topleft)


class Equation:
    def __init__(self):
        self.num1 = random.randint(1, 9)
        self.num2 = random.randint(1, 9)
        self.operator = random.choice(['+', '-'])
        if self.operator == '-':
            self.num1, self.num2 = max(self.num1, self.num2), min(self.num1, self.num2)  # Ensure positive result
        self.result = str(eval(str(self.num1) + self.operator + str(self.num2)))
        self.text = f"{self.num1} {self.operator} {self.num2}"

    def display(self):
        equation_text = FONT.render(self.text, True, "white")
        equation_rect = equation_text.get_rect(center=(SW / 2, SH / 20))
        screen.blit(equation_text, equation_rect.topleft)


class Button:
    def __init__(self, x, y, width, height, text, callback):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.callback = callback

    def draw(self, surface):
        pygame.draw.rect(surface, "gray", self.rect)  # Draw the button rectangle
        font = pygame.font.Font(None, 36)
        text = font.render(self.text, True, "black")
        text_rect = text.get_rect(center=self.rect.center)
        surface.blit(text, text_rect)  # Draw the button text

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)  # Check if the button is clicked


start_button = Button(SW / 4, SH / 4, SW / 2, SH / 8, "Start", lambda: start_game())
quit_button = Button(SW / 4, SH / 4 + SH / 4, SW / 2, SH / 8, "Quit", sys.exit)
buttons = [start_button, quit_button]
game_started = False


def start_game():
    global game_started
    game_started = True


def draw_buttons():
    for button in buttons:
        button.draw(screen)


def main():
    snake = Snake()
    equation = Equation()
    numbers = [Number() for _ in range(8)]  # Generate 8 random numbers

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if not game_started:
                    for button in buttons:
                        if button.is_clicked(event.pos):
                            button.callback()

            if game_started and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    snake.ydir = 1
                    snake.xdir = 0
                elif event.key == pygame.K_UP:
                    snake.ydir = -1
                    snake.xdir = 0
                elif event.key == pygame.K_RIGHT:
                    snake.ydir = 0
                    snake.xdir = 1
                elif event.key == pygame.K_LEFT:
                    snake.ydir = 0
                    snake.xdir = -1

        if game_started:
            snake.update()
            screen.fill("black")
            drawGrid()
            equation.display()

            for num in numbers:
                num.update()

            pygame.draw.rect(screen, "green", snake.head)
            for square in snake.body:
                pygame.draw.rect(screen, "green", square)

            for num in numbers:
                if snake.head.x == num.x and snake.head.y == num.y:
                    if str(num.value) == str(equation.result):
                        snake.body.append(pygame.Rect(square.x, square.y, BLOCK_SIZE, BLOCK_SIZE))
                        equation = Equation()  # Generate a new equation
                    numbers.remove(num)
                    numbers.append(Number())  # Generate a new number

            pygame.display.update()
            clock.tick(8)

        else:
            screen.fill("black")
            draw_buttons()

        pygame.display.flip()


def drawGrid():
    for x in range(0, SW, BLOCK_SIZE):
        for y in range(0, SH, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, "#3c3c3b", rect, 1)


if __name__ == "__main__":
    score = FONT.render("1", True, "white")
    score_rect = score.get_rect(center=(SW / 2, SH / 20))

    drawGrid()
    main()  # Start the main game loop
