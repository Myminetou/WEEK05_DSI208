#ไล่ไปทีละตัวจนกว่าจะหาเจอ
import pyglet
import random

# Create a window สร้างหน้าต่างในการแสดงผล
window = pyglet.window.Window(width=800, height=200, caption='Linear Search Visualization')
batch = pyglet.graphics.Batch()

# สร้างตัวเลขที่มีการสุ่มและเรียงลำดับ รวมถึงจะต้องมีเลข 42 รวมอยู่ด้วย
numbers = random.sample(range(1, 100), 19) + [42]
random.shuffle(numbers)

# ตัวแปรที่ควบคุมการเคลื่อนไหวและการค้นหา
current_index = 0
found_index = -1
search_complete = False

#ตัวที่ต่างจาก binary เป็นตัวที่จะไล่เลขไปเรื่อยๆจนกว่าจะเจอตัวที่ค้นหา
def linear_search():
    global current_index, found_index, search_complete
    if current_index < len(numbers):
        if numbers[current_index] == 42:
            found_index = current_index
            search_complete = True
        current_index += 1
    else:
        search_complete = True

# กำหนดเวลาให้ทำการค้นหาทุก ๆ 0.5 วินาที 
pyglet.clock.schedule_interval(lambda dt: linear_search(), 0.5)

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
        if i == current_index and not search_complete:
            color = (255, 0, 154)  # สีแดงแทนช่องปัจจุบันที่กำลังทำงานอยู่ตรงนั้น
        elif i == found_index:
            color = (0, 203, 14)  # สีเขียวแทนตอนเจอเลข 42
        else:
            color = (98, 108, 99)  # สีเทาแทนกล่องที่ยังไล่ไม่ถึงหรือไม่ได้ทำงานอยู่ในตอนนั้น
        
        pyglet.shapes.Rectangle(x, y, width, height, color=color, batch=batch).draw()
        # วาดตัวเลขภายในกล่อง
        label = pyglet.text.Label(str(number), x=x+width//2, y=y+height//2, anchor_x='center', anchor_y='center', batch=batch)
        label.draw()

pyglet.app.run()