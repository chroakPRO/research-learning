import pygame
import random
from blob import Blob


STARTING_BLUE_BLOBS = 10
STARTING_RED_BLOBS = 3

WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blod World")
clock = pygame.time.Clock()

class BlueBlob(Blob):
    
    def __init__(self, color, x_boundary, y_boundary):
        super().__init__(color, x_boundary, y_boundary)
        self.color = BLUE

    def super_move(self):
        self.x += random.randrange(-5, 5)
        self.y += random.randrange(-5, 5)
        


def draw_enviroment(blob_list):
    game_display.fill(WHITE)
    
    for blobs_dict in blob_list:    
        for blob_id in blobs_dict:
            blob = blobs_dict[blob_id]
            pygame.draw.circle(game_display, blob.color, [blob.x, blob.y], blob.size)
            #blob.move()
            blob.super_move()
            blob.check_bounds()
            
    pygame.display.update()



def main():
    red_blobs = dict(enumerate([BlueBlob(RED, WIDTH, HEIGHT) for i in range(STARTING_RED_BLOBS)])) 
    blue_blobs = dict(enumerate([BlueBlob(BLUE, WIDTH, HEIGHT) for i in range(STARTING_BLUE_BLOBS)])) 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        draw_enviroment([blue_blobs, red_blobs])
        clock.tick(60)
    


if __name__ == "__main__":
    main()
