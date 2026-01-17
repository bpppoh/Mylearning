def final_price(price , tax_rate=0.07, **discount) : 
    """คำนวณยอดสทธิที่ลูกค้าต้องจ่ายหลังจากหักส่วนลด และคำนวณภาษีแล้ว

    Args:
        price (int/float): ราคาที่ลูกค้าต้องจ่าย ก่อนคำนวณส่วนลดและภาษี
        tax_rate (float, optional): อัตราภาษีมูลค่าเพิ่ม. Defaults to 0.07.
        **discount (dict) : ชื่อของส่วนลดและจำนวนส่วนลด ที่จะต้องนำไปคำนวณยอดสุทธิ

    Returns:
        float: ยอดสุทธืที่ลูกค้าต้องจ่าย เลขนัยสำคัญ 2 ตำแหน่ง
    """
    totalDiscount = 0
    for key,value in discount.items() :
        if "special_" in key :
            totalDiscount += value*2
        elif "expired_" in key :
            0
        else :
            totalDiscount += value
    result = price - totalDiscount
    if result < 0 : result = 0
    result *= (1 + tax_rate)
    return f"{result:,.2f}"
    
print(f"Case 1: {final_price(1000, discount_nov=100, expired_dec=500)}")
print(f"Case 2: {final_price(2000, special_vip=200)}")
print(f"Case 3: {final_price(3000, promo=100, special_year=200, expired_old=1000)}")
print(f"Case 4: {final_price(500, special_clearance=300)}")
print(f"Case 5: {final_price(2000, tax_rate=0, member=500)}")