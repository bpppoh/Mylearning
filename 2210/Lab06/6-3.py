def power_recursive(base,exponent) :
    """คำนวณค่าของการยกกำลัง โดยใช้การ Recursive

    Args:
        base (int): เลขฐานที่จะใช้ยกกำลัง
        exponent (int): เลขยกกำลัง ต้องเป็นค่าบวกขึ้นไป

    Returns:
        int: ผลจากการนำ base ไปยกกำลังกับ exponent
    """
    if exponent <= 0 :
        return 1
    elif exponent == 1 :
        return base
    elif exponent > 1 :
        return base * power_recursive(base,exponent-1)    
    
print(f"2^3 = {power_recursive(2, 3)}")
print(f"5^0 = {power_recursive(5, 0)}")
print(f"5^2 = {power_recursive(5, 2)}")