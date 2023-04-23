# Divide the canvas into 4 sections. When you move the mouse on one of the sections, change the color of that.

sections = []

# 마우스가 섹션 안에 있으면, 해당 섹션 색상은 blue, 없으면 red
originalColor = 0xFFFF0000 # red
newColor = 0xFF0000FF # blue

def setup():
    size(800, 600)
    # 각 섹션별 x, y, width, height를 sections에 추가
    sections.append([0, 0, width/2, height/2]) # upper left section
    sections.append([width/2, 0, width/2, height/2]) # upper right section
    sections.append([0, height/2, width/2, height/2]) # lower left section
    sections.append([width/2, height/2, width/2, height/2]) # lower right section 

# 마우스가 해당 섹션 안에 있으면 True 반환
def isMouseInSection(x, y, w, h):
    return x <= mouseX and mouseX <= x + w and y <= mouseY and mouseY <= y + h
    
def draw():
    for x, y, w, h in sections:
        if isMouseInSection(x, y, w, h):
            fill(newColor)
        else:
            fill(originalColor)
        rect(x, y, w, h)
    
