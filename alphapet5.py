import random

def random_consecutive_combination_on_laptop(keyboard):
  """Bốc 3 ký tự liên tiếp ngẫu nhiên từ bàn phím laptop keyboard."""
  for row in keyboard:
    for i in range(len(row) - 4):
      yield row[i:i + 5]

# Tạo bàn phím laptop
keyboard = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]

# Bốc 1000 tổ hợp 4 ký tự liên tiếp ngẫu nhiên
combinations = []
for combination in random_consecutive_combination_on_laptop(keyboard):
  combinations.append(combination)
  print(combinations)
# In ra 10 tổ hợp đầu tiên
# for combination in combinations[:10]:
#   print(combination)
