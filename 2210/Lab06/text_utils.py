def count_words(text) :
    """นับจำนวนคำใน string ด้วยการ split (ใช้ช่องว่างในการแบ่ง)

    Args:
        text (string): ข้อความ

    Returns:
        int: จำนวนคำหลังจากถูกแบ่งแล้ว
    """
    words = text.split()
    return len(words)

def count_vowels(text) :
    """นับจำนวนสระจาก input text

    Args:
        text (string): คำที่จะนับจำนวนสระ

    Returns:
        int: จำนวนสระทีนับได้
    """
    vowels_count = 0
    for i in text.lower() :
        if i in ['a','e','i','o','u'] :
            vowels_count += 1
    return vowels_count

def clean_text(text) :
    """เคลียร์ space ด้านหน้าและหลังของ และปรับให้เป็นตัวเล็กทั้งหมด text(argument)

    Args:
        text (string): ข้อความนำเข้า

    Returns:
        string : ข้อความที่ไม่่มี
    """
    return text.strip().lower()

def highlight(text) :
    """เพิ่ม *** ไว้ที่ด้านหน้าและหลังของ text(argument)

    Args:
        text (string): ข้อความ

    Returns:
        string: ข้อความเดิมแต่มี *** อยู่ด้านหน้าและหลัง
    """
    return "*** "+text+" ***"