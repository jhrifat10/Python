from collections import deque
#Queue= First In, First Out
bank =deque(["Anis","karim","dorjoy"])
print(bank)
bank.popleft()
print(bank)

if not bank:
    print(bank)
    