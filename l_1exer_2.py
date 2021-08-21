# Задание №2
times = int(input("Введите время в секундах"))
m_hrs = times // 60
mts = (times // 60) % 60
hrs = m_hrs // 60
print(f"{hrs:02}:{mts:02}:{times % 60:02}")
