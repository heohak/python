"""Cha-ching!"""
amount = int(input("Enter a sum: "))
coins = 0

coins += amount // 50
amount %= 50
coins += amount // 20
amount %= 20
coins += amount // 10
amount %= 10
coins += amount // 5
amount %= 5
coins += amount // 1
amount %= 1
print(f"Amount of coins needed: {coins}")
