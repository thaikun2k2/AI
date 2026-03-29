# 🧠 Python OOP (Lập Trình Hướng Đối Tượng) - Hướng Dẫn Đầy Đủ

## 📌 Tổng quan
Lập trình hướng đối tượng (OOP) là phương pháp tổ chức code bằng **class (lớp)** và **object (đối tượng)**.

Mỗi object gồm:
- **Thuộc tính (attributes)** → dữ liệu
- **Phương thức (methods)** → hành vi

---

## 🚀 Mục lục
- Class & Object
- Constructor
- Encapsulation
- Inheritance
- Polymorphism
- Abstraction
- Advanced (Nâng cao)
- Best Practices
- Project Ideas

---

## 🧱 1. Class & Object
```python
class Person:
    def __init__(self, name):
        self.name = name  # attribute: lưu tên của object

# tạo object (instance)
p = Person("Thai")

# truy cập attribute
print(p.name)  # output: Thai
```

👉 Giải thích:
- `class` = bản thiết kế
- `object` = đối tượng thực tế được tạo từ class
- `self` = đại diện cho chính object đó

---

## ⚙️ 2. Constructor (`__init__`)
```python
class Student:
    def __init__(self, name, age):
        self.name = name   # gán giá trị cho attribute name
        self.age = age     # gán giá trị cho attribute age

s = Student("Thai", 22)
```

👉 Giải thích:
- `__init__` chạy tự động khi tạo object
- Dùng để khởi tạo dữ liệu ban đầu

---

## 🔐 3. Encapsulation (Đóng gói)
```python
class BankAccount:
    def __init__(self):
        self.__balance = 0  # private attribute (không truy cập trực tiếp)

    def deposit(self, amount):
        self.__balance += amount  # cập nhật số dư

    def get_balance(self):
        return self.__balance  # truy cập thông qua method

acc = BankAccount()
acc.deposit(100)
print(acc.get_balance())  # 100
```

👉 Giải thích:
- `__balance` = private (bị ẩn)
- Không cho truy cập trực tiếp → tăng bảo mật

---

## 🧬 4. Inheritance (Kế thừa)
```python
class Animal:
    def speak(self):
        print("Some sound")  # method chung

class Dog(Animal):
    def bark(self):
        print("Woof")  # method riêng của Dog

# sử dụng
d = Dog()
d.speak()  # kế thừa từ Animal
```

👉 Giải thích:
- `Dog` kế thừa `Animal`
- Tái sử dụng code

---

## 🔄 5. Polymorphism (Đa hình)
```python
class Cat:
    def speak(self):
        print("Meow")

class Dog:
    def speak(self):
        print("Woof")

animals = [Cat(), Dog()]

for animal in animals:
    animal.speak()  # cùng method nhưng hành vi khác nhau
```

👉 Giải thích:
- Cùng tên method (`speak`)
- Nhưng mỗi class có hành vi riêng

---

## 🎭 6. Abstraction (Trừu tượng)
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # không có logic cụ thể

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side  # implement method
```

👉 Giải thích:
- Class cha chỉ định nghĩa "khung"
- Class con phải implement

---

## ⚙️ 7. Advanced (Nâng cao)

### 🔹 Magic Methods
```python
class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Person: {self.name}"  # hiển thị khi print

p = Person("Thai")
print(p)  # gọi __str__
```

---

### 🔹 Class Method vs Static Method
```python
class Example:
    count = 0

    def __init__(self):
        Example.count += 1  # tăng biến class

    @classmethod
    def get_count(cls):
        return cls.count  # truy cập biến class

    @staticmethod
    def greet():
        print("Hello")  # không dùng self hoặc cls
```

---

### 🔹 Property (Getter/Setter)
```python
class Student:
    def __init__(self):
        self._score = 0  # protected

    @property
    def score(self):
        return self._score  # getter

    @score.setter
    def score(self, value):
        if value >= 0:
            self._score = value  # setter có kiểm tra
```

---

### 🔹 Composition (HAS-A)
```python
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()  # Car có Engine

    def start_car(self):
        self.engine.start()
```

👉 Giải thích:
- Car "có" Engine
- Linh hoạt hơn kế thừa

---

## 🧠 Best Practices

- Ưu tiên **composition hơn inheritance**
- Mỗi class chỉ nên làm 1 nhiệm vụ
- Đặt tên rõ ràng
- Tránh over-engineering

---

## 🛠️ Project Ideas

### Beginner
- Quản lý sinh viên
- To-do app

### Intermediate
- Hệ thống ngân hàng
- Quản lý thư viện

### Advanced
- Game (nhân vật, skill)
- IoT device manager

---

## ⭐ Kết luận

OOP giúp bạn viết code:
- Dễ bảo trì
- Dễ mở rộng
- Chuẩn chuyên nghiệp

> "Viết code không chỉ để chạy, mà còn để người khác hiểu và mở rộng."

