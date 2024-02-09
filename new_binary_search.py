#ทำเป็นกลุ่มกว้างๆ
import pyglet
import random

# Create a window สร้างหน้าต่างในการแสดงผล
window = pyglet.window.Window(width=800, height=200, caption='Binary Search Visualization')
batch = pyglet.graphics.Batch()

# สร้างตัวเลขที่มีการสุ่มและเรียงลำดับ รวมถึงจะต้องมีเลข 42 รวมอยู่ด้วย
numbers = sorted(random.sample(range(1, 100), 19) + [42])

# ตัวแปรที่ควบคุมการเคลื่อนไหวและการค้นหา
left, right = 0, len(numbers) - 1
mid = (left + right) // 2
found = False
search_complete = False

#ตัวที่ต่างจาก linear เป็นตัวที่จะย่อยกลุ่มลงไปเรื่อยๆจนหาเจอ
def binary_search():
    global left, right, mid, found, search_complete
    if left <= right and not found:
        mid = (left + right) // 2
        if numbers[mid] == 42:
            found = True
        elif numbers[mid] < 42:
            left = mid + 1
        else:
            right = mid - 1
    else:
        search_complete = True

# กำหนดเวลาให้ทำการค้นหาทุก ๆ 0.5 วินาที 
pyglet.clock.schedule_interval(lambda dt: binary_search(), 0.5)

@window.event
def on_draw():
    window.clear()
    for i, number in enumerate(numbers):
        # กำหนดตำแหน่งและขนาดกล่องแต่ละอันว่าต้องมีขนาดเท่ากัน
        x = i * 40 + 10
        y = window.height // 2
        width = 30
        height = 30

        # วาดกล่อง
        if left <= i <= right and not search_complete:
            color = (255, 0, 154)  # สีชมพูแทนการค้นหาในปัจจุบัน
        elif i == mid and not search_complete:
            color = (17, 0, 255)  # สีน้ำเงินแทนองค์ประกอบตรงกลาง
        elif found and i == mid:
            color = (0, 203, 14)  # สีเขียวแทนตอนเจอเลข 42 ที่ต้องการหา
        else:
            color = (98, 108, 99)  # สีเทาแทนกล่องที่ยังไล่ไม่ถึงหรือไม่ได้ทำงานอยู่ในตอนนั้น
        
        pyglet.shapes.Rectangle(x, y, width, height, color=color, batch=batch).draw()
        # วาดตัวเลขภายในกล่อง
        label = pyglet.text.Label(str(number), x=x+width//2, y=y+height//2, anchor_x='center', anchor_y='center', batch=batch)
        label.draw()

pyglet.app.run()