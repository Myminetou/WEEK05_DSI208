#เปรียบเทียบระหว่างสองวิธี
import pyglet
import random

# Create a window สร้างหน้าต่าง, มีการปรับขนาดหากต้องรองรับหน้าต่างเพื่อให้เลย์เอาต์ใหญ่ขึ้น
window = pyglet.window.Window(width=1000, height=800, caption='Search Algorithms Comparison')
batch = pyglet.graphics.Batch()

def reset_searches():
    global numbers, linear_index, linear_found, binary_left, binary_right, binary_mid, binary_found
    #  สร้างตัวเลขที่มีการสุ่มและเรียงลำดับ รวมถึงจะต้องมีเลข 42 รวมอยู่ด้วยแล้วจัดเรียงเพื่อทำ binary search
    numbers = random.sample(range(1, 100), 31) + [42]
    random.shuffle(numbers)  # สับเปลี่ยนสำหรับ linear search
    numbers.sort()  # เรียงลำดับเพื่อทำการค้นหาแบบ binary search

    # Reset ตัวแปรค้นหา
    linear_index = 0
    linear_found = False
    binary_left, binary_right = 0, len(numbers) - 1
    binary_mid = (binary_left + binary_right) // 2
    binary_found = False

reset_searches()  # เริ่มต้นการค้นหา

def update_searches(dt):
    global linear_index, linear_found, binary_left, binary_right, binary_mid, binary_found

    # Update linear search
    if not linear_found and linear_index < len(numbers):
        if numbers[linear_index] == 42:
            linear_found = True
        linear_index += 1

    # Update binary search
    if not binary_found and binary_left <= binary_right:
        binary_mid = (binary_left + binary_right) // 2
        if numbers[binary_mid] == 42:
            binary_found = True
        elif numbers[binary_mid] < 42:
            binary_left = binary_mid + 1
        else:
            binary_right = binary_mid - 1

@window.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.R:
        reset_searches()

pyglet.clock.schedule_interval(update_searches, 0.5)

@window.event
def on_draw():
    window.clear()
    margin = 5  # ระยะขอบระหว่างกล่อง
    box_size = (window.width - margin * (len(numbers) + 1)) // len(numbers)  # สั่งให้คำนวณกล่องตามความกว้างและระยะขอบของหน้าต่าง
    for i, number in enumerate(numbers):
        x = i * (box_size + margin) + margin  # คำนวณตำแหน่ง x พร้อมระยะขอบ
        # Linear search boxes (อยู่ครึ่งบน)
        y_linear = window.height * 3/4 - box_size / 2
        color_linear = (0, 203, 14) if linear_found and i == linear_index - 1 else (247, 0, 255) if i == linear_index else (98, 108, 99)
        pyglet.shapes.Rectangle(x, y_linear, box_size, box_size, color=color_linear, batch=batch).draw()

        # Binary search boxes (อยู่ครึ่งล่าง)
        y_binary = window.height / 4 - box_size / 2
        color_binary = (0, 203, 14) if binary_found and i == binary_mid else (247, 0, 255) if binary_left <= i <= binary_right else (98, 108, 99)
        pyglet.shapes.Rectangle(x, y_binary, box_size, box_size, color=color_binary, batch=batch).draw()

        # วาดตัวเลขในแต่ละช่องไว้ค้นหาและปรับขนาดตัวอักษรให้อ่านง่ายขึ้น
        label = pyglet.text.Label(str(number), x=x + box_size/2, y=y_linear + box_size/2, anchor_x='center', anchor_y='center', color=(255, 255, 255, 255), batch=batch)
        label.draw()
        label = pyglet.text.Label(str(number), x=x + box_size/2, y=y_binary + box_size/2, anchor_x='center', anchor_y='center', color=(255, 255, 255, 255), batch=batch)
        label.draw()

pyglet.app.run()