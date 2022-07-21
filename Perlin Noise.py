import pygame
import math
import random

Width = Height = 500

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def dotProduct(v1: Vector, v2: Vector):
    return v1.x * v2.x + v1.y * v2.y

def Lerp(t, a, b):
	return a + t * (b-a)

def Fade(t):
	return ((6*t - 15)*t + 10)*t*t*t

def GetConstantVector(v):
	h = v % 4
	
	if h == 0:
		return Vector(1, 1);
	elif h == 1:
		return Vector(-1, 1);
	elif h == 2:
		return Vector(-1, -1);
	else:
		return Vector(1, -1);

def Shuffle(tab: list):
    for x in reversed(range(len(tab))):
        index = round(random.random()*(x-1))
        temp = tab[x]
        tab[x] = tab[index]
        tab[index] = temp

P = []
for x in range(256):
	P.append(x)

Shuffle(P)

for x in range(256):
	P.append(P[x])


def noise(x, y):
    X = math.floor(x) & 255
    Y = math.floor(y) & 255

    xf = x - math.floor(x)
    yf = y - math.floor(y)

    topLeftVector = Vector(xf, yf-1)
    topRightVector = Vector(xf-1, yf-1)
    bottomLeftVector = Vector(xf, yf)
    bottomRightVector = Vector(xf-1, yf)

    valueTopLeft = P[P[X]+Y+1]
    valueTopRight = P[P[X+1]+Y+1]
    valueBottomLeft = P[P[X]+Y]
    valueBottomRight = P[P[X+1]+Y]

    dotTopLeft = dotProduct(topLeftVector, GetConstantVector(valueTopLeft))
    dotTopRight = dotProduct(topRightVector, GetConstantVector(valueTopRight))
    dotBottomLeft = dotProduct(bottomLeftVector, GetConstantVector(valueBottomLeft))
    dotBottomRight = dotProduct(bottomRightVector, GetConstantVector(valueBottomRight))

    u = Fade(xf)
    v = Fade(yf)
	
    return Lerp(u, Lerp(v, dotBottomLeft, dotTopLeft), Lerp(v, dotBottomRight, dotTopRight))



def draw(screen, pixelArray):     
    for y in range(Height):
        for x in range(Width):

            n = noise(x*0.01, y*0.01)
            n += 1
            n /= 2
		
            c = round(255*n)
            pixelArray[y][x] = pygame.Color(c, c, c)

            '''n = 0
            a = 1
            f = 0.005
            for o in range(10):
                v = a*noise(x*f, y*f)
                n += v

                a *= 0.5
                f *= 2.0


            n += 1.0
            n *= 0.5
            rgb = round(255*n)
            
            if rgb > 255: rgb = 255
            if rgb < 0: rgb = 0

            if n < 0.5:
                try:
                    pixelArray[x][y] = pygame.Color(0, 0, rgb)
                except: 
                    print(rgb)
            elif n < 0.9:
                pixelArray[x][y] = pygame.Color(0, rgb, round(rgb*0.5))
            else:
                #pixelArray[x][y] = pygame.Color(rgb, rgb, rgb)
                pixelArray[x][y] = pygame.Color(0, rgb, round(rgb*0.5))
                pass'''
                
    pygame.display.update()

def main():
    clock = pygame.time.Clock()


    pygame.init()
    screen = pygame.display.set_mode((Width, Height))
    pygame.display.set_caption("Improved Perlin Noise")

    pixelArray = pygame.PixelArray(screen)
    
    draw(screen, pixelArray)

    run = True

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        
     
     
if __name__=="__main__": main()