# Draw 10 balls, choose their starting x positions randomly, and move them up and down in different speed. Use list data type to keep each ball's positin.

ballDiam = 50 # 공들의 공통 지름
balls = []

def setup():
    size(800, 600)
    
    # for문을 이용해, 공 10개의 x, y, dirY값을 balls에 저장함. 
    for i in range(10):
        # 각 공마다의 x, y, dirY(y 변화값) 저장
        # x값은 랜덤해야 하므로, random 함수 사용.
        # dirY는 각 공마다 이동 속도를 다르게 하기 위해 서로 다른 값으로 할당함.
        balls.append([random(750), 50, i+5])
    
def draw():
    background(200)
    fill(0xFFFF0000)
    
    for ball in balls:
        # 현재 x, y, dirY 값 꺼내기
        x = ball[0]
        y = ball[1]
        dirY = ball[2]
        
        # 공 그리기
        ellipse(x, y, ballDiam, ballDiam)
        
        # 다음에 그릴 원의 y값이 상단 혹은 하단 벽에 부딪히는 경우, y 진행방향 변경
        newDirY = dirY
        if y + dirY <= 0 or y + dirY >= height:
            newDirY *= -1
        newY = y + newDirY
            
        # 공의 y, dirY 값을 위에서 계산한 새로운 값으로 저장되도록 함.
        ball[1] = newY
        ball[2] = newDirY
