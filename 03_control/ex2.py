# 반복문

# while문
# 1 ~ 10까지 반복 출력
i = 0
while i < 10:
    i += 1
    print(i)
    # if i == 5:
    #     break
else:
    print("End")

# target값 찾아내기
nums = [1, 3, 5, 7, 9]
target = 2
i = 0
# found = False

while i < len(nums):
    if nums[i] == target:
        print(f"찾았다! {i}번째다!")
        # found = True
        break
    i += 1
else:
    print("못 찾아부러쓰...")

# if not found:
#   print(f"{target} not found")

# 1 ~ 10까지의 합
# sum = 55
i = 1
tot = 0

while i <= 10:
    tot += i
    i += 1

print(f"sum = {tot}")

i = 0
tot = 0

while i <= 10:
    if i % 2 == 1:
        continue
    tot += i
    i += 1

print(f"sum = {tot}")

