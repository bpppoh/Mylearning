def calculate_stats (*num) : 
    """ฟังก์ชั่นคำนวณค่าต่าง ๆ จากเลขที่ถูกนำเข้าเป็น argument โดยใส่ไปกี่ argument ก็ได้

    Args:
        *num (int/float): ตัวเลขจำนวนเท่าใดก็ได้ที่ต้องการคำนวณ
    
    Returns:
        dict: ประกอบด้วยค่า sum (ผลรวมของ argument ทั้งหมด) , average (ค่าเฉลี่ยของ argument ทั้งหมด) , max (ค่าสูงสุดจาก argument ทั้งหมดที่นำเข้าไป) , min (ค่าต่ำที่สุดที่ถูกนำเข้าไปเป็น argument)
    """
    dict = {}
    dict['sum'] = 0
    dict['average'] = 0
    dict['max'] = 0
    dict['min'] = 0
    for i in num :
        dict['sum'] += i
        if dict['max'] < i :
            dict['max'] = i
        if dict['min'] > i :
            dict['min'] = i
    if len(num)!=0 : 
        dict['average'] = dict['sum'] / len(num) 
    return dict
    
print(calculate_stats(10,20,30,40,50))
print(calculate_stats(5,5))
print(calculate_stats())