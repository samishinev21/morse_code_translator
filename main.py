import pygame
import sys
import pygame_gui
from morse_code import from_english_to_morse


pygame.init()

WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Morse Code Translator v0.1")

CLOCK = pygame.time.Clock()
UI_MANAGER = pygame_gui.UIManager((WIDTH, HEIGHT))

TEXT_INPUT = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((100, 275), (600, 50)), manager=UI_MANAGER, object_id="#main_text_entry")

def main():
    while True:
        ui_refresh_rate = CLOCK.tick(60)/1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "#main_text_entry":
                show_morse(event.text)

            UI_MANAGER.process_events(event)

        UI_MANAGER.update(ui_refresh_rate)
            
        SCREEN.fill("white")

        UI_MANAGER.draw_ui(SCREEN)

        pygame.display.update()

def show_morse(text):
    morse = from_english_to_morse(text)
    morse = " ".join(morse)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        SCREEN.fill("white")
        morse_code_text = pygame.font.SysFont("bahnschrift", 30).render(f"{morse}", True, "black")
        morse_code_text_rect = morse_code_text.get_rect(center = (WIDTH/2, HEIGHT/2))
        SCREEN.blit(morse_code_text, morse_code_text_rect)

        CLOCK.tick(20)

        pygame.display.update()

main()