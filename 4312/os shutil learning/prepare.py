import os

# สร้างโฟลเดอร์จำลอง
os.makedirs('messy_data', exist_ok=True)

# สร้างไฟล์จำลอง (รูปภาพและข้อความ)
sample_files = ['dog_01.jpg', 'dog_01.txt', 'cat_01.jpg', 'cat_01.txt', 
                'bird_01.png', 'bird_01.txt', 'readme.md']

for f in sample_files:
    with open(os.path.join('messy_data', f), 'w') as file:
        file.write('dummy data')

print("เตรียม messy_data เรียบร้อยแล้ว!")