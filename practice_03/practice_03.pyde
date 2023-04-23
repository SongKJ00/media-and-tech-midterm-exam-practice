# Draw 2 balls in different colors, move them in different directions.

ballDiam = 50 # 공들의 공통 지름

# 첫번째 공 x, y
ball1X = 10
ball1Y = 10

# 두번째 공 x, y
ball2X = 600
ball2Y = 300

# 첫번째 공의 x, y 변화값
ball1DirX = 10
ball1DirY = 0

# 두번째 공의 x, y 변화값
ball2DirX = -10
ball2DirY = -10


def setup():
    size(800, 600)
    
    # 공이 너무 빠르게 사라지므로, draw 함수가 천천히 호출되도록 frameRate 조절
    # 초당 draw 함수가 4번 불
    frameRate(4)  

def draw():
    global ball1X, ball1Y, ball2X, ball2Y
    
    background(200)
    fill(0xFFFF0000) # red

    # 공 그리기
    ellipse(ball1X, ball1Y, ballDiam, ballDiam)
    ellipse(ball2X, ball2Y, ballDiam, ballDiam)
    
    # 공 x, y 위치값 업데이트
    ball1X += ball1DirX
    ball1Y += ball1DirY
    
    ball2X += ball2DirX
    ball2Y += ball2DirY
