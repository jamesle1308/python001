import random

def random_2_consecutive_combination_on_laptop(keyboard):
  """Bốc 2 ký tự cách nhau 1 ký tự giữa từ bàn phím laptop keyboard, nhưng các ký tự không nằm cùng một hàng, và kết quả được viết liền nhau."""
  for row in keyboard:
    for i in range(len(row)):
      for j in range(i + 1, len(row)):
        if row[i] != row[j]:
          yield row[i] + row[j]

# Tạo bàn phím laptop
keyboard = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]

# Tạo một list trống để lưu trữ các tổ hợp ký tự
combinations = []

# Bốc 1000 tổ hợp 2 ký tự cách nhau 1 ký tự giữa
for combination in random_2_consecutive_combination_on_laptop(keyboard):
  # Thêm tổ hợp ký tự vào list
  combinations.append(combination)
  print(combinations, end=",")
# In ra 10 tổ hợp đầu tiên
# for combination in combinations[:10]:
#   # In ra các tổ hợp ký tự liên tiếp
#   print(combination, end=", ")
