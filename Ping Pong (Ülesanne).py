import pygame

# Initsialiseerime Pygame
pygame.init()

# Ekraani seaded
WIDTH, HEIGHT = 640, 480
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PyGame Pallimäng")

# Värvid
BACKGROUND_COLOR = (200, 200, 255)

# Laeme pildiressursid
ball_image = pygame.image.load("images/pingpong/ball-1.png")
pad_image = pygame.image.load("images/pingpong/pad.png")

# Palli seaded
ball_rect = ball_image.get_rect()
ball_rect.topleft = (WIDTH // 2, HEIGHT // 2)
ball_speed = [4, 4]

# Aluse seaded (liigub automaatselt)
pad_rect = pad_image.get_rect()
pad_rect.topleft = (WIDTH // 2 - 60, HEIGHT // 1.5)
pad_speed = 5  # Aluse kiirus
pad_direction = 1  # Algne suund paremale

# Küsi kasutajalt maksimaalne skoor
max_score = int(input("Sisesta punktisumma, mille saavutamisel mäng lõpeb: "))

# Punktiskoor
score = 0
font = pygame.font.Font(None, 36)

# Mängu olek
running = True
game_over = False

# Mängutsükkel
while running:
    SCREEN.fill(BACKGROUND_COLOR)

    # Sündmuste kontrollimine
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Kui mäng on läbi, kuvame teate ja ootame hetke
    if game_over:
        game_over_text = font.render(f"Mäng läbi! Lõplik skoor: {score}", True, (255, 0, 0))
        SCREEN.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2))
        pygame.display.flip()
        pygame.time.delay(3000)
        running = False
        continue

    # Alus liigub automaatselt edasi-tagasi
    pad_rect.x += pad_speed * pad_direction
    if pad_rect.left <= 0 or pad_rect.right >= WIDTH:
        pad_direction *= -1  # Vahetab suunda, kui jõuab seina

    # Palli liikumine
    ball_rect.x += ball_speed[0]
    ball_rect.y += ball_speed[1]

    # Pall põrkub ekraani servadest
    if ball_rect.left <= 0 or ball_rect.right >= WIDTH:
        ball_speed[0] = -ball_speed[0]
    if ball_rect.top <= 0:
        ball_speed[1] = -ball_speed[1]

    # Kokkupõrke tuvastamine alusega
    if ball_rect.colliderect(pad_rect) and ball_speed[1] > 0:
        ball_speed[1] = -ball_speed[1]  # Muudame suunda
        score += 1  # Lisame punkti

    # Kui pall läheb alumisest servast välja
    if ball_rect.bottom >= HEIGHT:
        score -= 1
        ball_rect.topleft = (WIDTH // 2, HEIGHT // 2)  # Lähtestame palli

    # Kontrollime, kas mängija on saavutanud maksimaalse punktisumma
    if score >= max_score:
        game_over = True

    # Joonista elemendid
    SCREEN.blit(ball_image, ball_rect)
    SCREEN.blit(pad_image, pad_rect)

    # Kuvame skoori ekraanile
    score_text = font.render(f"Skoor: {score}", True, (0, 0, 0))
    SCREEN.blit(score_text, (10, 10))

    pygame.display.flip()
    pygame.time.delay(16)

pygame.quit()