"""
Посчитать количество строчных (маленьких) и прописных (больших) букв в
введенной строке. Учитывать только английские буквы.Посчитать количество
строчных (маленьких) и прописных (больших) букв в введенной строке.
Учитывать только английские буквы.
"""

a = str(input("Введите строку:\n"))
lowercase = 0
capital = 0
for symbol in a:
    if "a" <= symbol <= "z":
        lowercase += 1
print("Строчных: ", lowercase)
for symbol in a:
    if "A" <= symbol <= "Z":
        capital += 1
print("Заглавных: ", capital)
