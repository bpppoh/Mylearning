from abc import ABC,abstractmethod

class Vehicle(ABC) :
    def __init__(self,license_plate,brand,base_rate_per_day) :
        self.license_plate = license_plate
        self.brand = brand
        self.base_rate_per_day = base_rate_per_day
        self._is_rented = False
    
    def rent_vehicle(self) :
        if self._is_rented :
            print(f"ไม่สามารถดำเนินการได้ ทะเบียน {self.license_plate} ถูกเช่าอยู่")
        else :
            self._is_rented = True
            print(f"ดำเนินการเรียบร้อย ทะเบียน {self.license_plate} ถูกเช่าแล้ว")
            
    def return_vehicle(self) : 
        if self._is_rented :
            self._is_rented = False
            print(f"ดำเนินการเรียบร้อย ทะเบียน {self.license_plate} ถูกส่งคืน")
        else :
            print(f"ไม่สามารถดำเนินการได้ ทะเบียน {self.license_plate} ไม่ได้ถูกเช่า")
        
    def get_status(self) :
        if self._is_rented :
            status = "ถูกเช่า"
        else :
            status = "ว่าง"
        print(f"สถานะปัจจุบัน: {status}")

    @abstractmethod
    def calculate_rental_fee(self,days) :
        pass

    @abstractmethod
    def display_details(self) :
        pass
    
class Car(Vehicle) :
    def __init__(self,license_plate,brand,base_rate_per_day,seat_capacity) :
        self.license_plate = license_plate
        self.brand = brand
        self.base_rate_per_day = base_rate_per_day
        self._is_rented = False
        self.seat_capacity = seat_capacity
    
    def calculate_rental_fee(self,days) :
        if self.seat_capacity > 5 :
            base = self.base_rate_per_day * days
            extra = base * 15.0 / 100
            price = base + extra
            print(f"คำนวณ {base:.2f}(ราคาพื้นฐาน) + {extra:.2f}(ที่นั่ง > 5) = {price:.2f} บาท")
        else :
            price = self.base_rate_per_day * days
            print(f"คำนวณ (รถขนาดมาตรฐาน): {price:.2f} บาท")
        return price
            
    def display_details(self) :
        print(f"ทะเบียน: {self.license_plate}, ยี่ห้อ: {self.brand}, ที่นั่ง: {self.seat_capacity}")
        
car1_large = Car("กข 1234","Toyota",1500,7)
car2_small = Car("บบ 5678","Honda",1000,4)

print("--แสดงข้อมูลรถในระบบ--")
car1_large.display_details()
car1_large.get_status()
car2_small.display_details()
car2_small.get_status()

print("--การเช่ารถ--")
car1_large.rent_vehicle()
car1_large.rent_vehicle()
car1_large.get_status()

print("--คำนวณค่าเช่า--")
print("คำนวณค่าเช่า กข 1234")
fee1 = car1_large.calculate_rental_fee(3)
print("คำนวณค่าเช่า บบ 5678")
fee2 = car2_small.calculate_rental_fee(3)

print(f"ค่าธรรมเนียมรวม: {fee1+fee2:.2f}")
            