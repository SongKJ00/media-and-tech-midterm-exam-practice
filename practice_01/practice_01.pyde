# Draw 3 circles on your canvas. When you move the mouse on any circls, change the color of that circle.

circleDiam = 100 # 원들의 공통 지름

# 첫번째 원 x, y
circle1 = [100, 300]

# 두번째 원 x, y
circle2 = [300, 300]

# 세번째 원 x, y
circle3 = [500, 300]

# 마우스가 원 밖에 있을 때는 원 색깔이 originalColor이고,
# 원 안에 있을 때는 newColor임.
originalColor = 0xFFFF0000 # red  
newColor = 0xFF00FF00 # green 

def setup():
    size(800, 600)
    
# 마우스가 원 안에 있는 경우, True 반환
def isMouseInCircle(circleX, circleY):
    return dist(mouseX, mouseY, circleX, circleY) <= circleDiam
    
def draw():
    circles = [circle1, circle2, circle3]
    
    for x, y in circles:
        # 마우스가 원 안에 있을 때, fill(newColor)로 새로운 색깔로 셋팅 후 ellipse로 원 그
        if isMouseInCircle(x, y):
            fill(newColor)
        else:
            fill(originalColor)
        ellipse(x, y, circleDiam, circleDiam)
    
