# Draw 10 balls, choose their starting x positions randomly, and move them up and down in different speed. Use list data type to keep each ball's positin.

ballDiam = 50
balls = []

def setup():
    size(800, 600)
    for i in range(10):
        # 각 공마다의 x, y, dirY(y 변화값) 저장
        # x값은 랜덤해야 하므로, random 함수 사용.
        # dirY는 각 공마다 이동 속도를 다르게 하기 위해 다른 값으로 할당함.
        balls.append([random(750), 50, i+5])
    
def draw():
    background(200)
    fill(0xFFFF0000)
    
    for ball in balls:
        # 공 그리기
        x = ball[0]
        y = ball[1]
        dirY = ball[2]
        ellipse(x, y, ballDiam, ballDiam)
        
        # 새로운 y, dirY 선언
        newY = y + dirY
        newDirY = dirY
        
        # 상단 혹은 하단 벽에 부딪히는 경우, y 진행방향 변경
        if newY >= height:
            newDirY *= -1
        if newY <= 0:
            newDirY *= -1
        
        # 해당 공에 업데이트한 값 저장
        ball[1] = newY
        ball[2] = newDirY
        
    
