import sys, pygame
from random import randint




def main():
    pygame.init()
    pygame.font.init()
    run = True

    size = width,height = 600,600
    screensurf = pygame.display.set_mode(size)
    font = pygame.font.SysFont("Consolas",40)

    fps = pygame.time.Clock()

    board = [
        [1,5,9,13],
        [2,6,10,14],
        [3,7,11,15],
        [4,8,12,0]
    ]

    for i in range(100):
        x1,y1 = randint(0,3),randint(0,3)
        x2,y2 = randint(0,3),randint(0,3)
        temp = board[x1][x2]
        board[x1][x2] = board[x2][y2]
        board[x2][y2]= temp





    while run:
        fps.tick(60)
        pos = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

        screensurf.fill(pygame.Color(0, 0, 0))

        for x in range(4):
            for y in range(4):
                rect = pygame.Rect(150*x+10,150*y+10, 130, 135)
                if pos:
                    if rect.collidepoint(pos):


                        current_pice = board[x][y]
                        if current_pice > 0:
                            if x >= 0:
                                if board[x -1][y] == 0:
                                    board[x -1][y] = current_pice
                                    board[x][y] = 0

                                if x < 3:
                                    if board[x + 1][y] == 0:
                                        board[x + 1][y] = current_pice
                                        board[x][y] = 0
                                if y >= 0:
                                    if board[x][y -1] == 0:
                                        board[x][y -1] = current_pice
                                        board[x][y] = 0
                                if y < 3:
                                    if board[x][y +1] == 0:
                                        board[x][y +1] = current_pice
                                        board[x][y] = 0


                pygame.draw.rect(screensurf, pygame.Color(255,255,255), rect)
                piece = board[x][y]
                if piece:
                    fontsurf = font.render(str(piece),True,pygame.Color(255,0,0))
                    left, top = (rect.x + (rect.width / 2 - fontsurf.get_width()/2),
                                 rect.y + (rect.height / 2 - fontsurf.get_height() /2))
                    screensurf.blit(fontsurf,(left,top))



        pygame.display.flip()




if __name__ == "__main__":
    main()