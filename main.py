n, m = map(int, input().split())
ls = []
for i in range(n):
  ls.append(int(input()))
result = 0
while m > 0:
  cnt = [999999] * n
  for i in range(n):
    if m // ls[i] >= 1:
      cnt[i] = m // ls[i]
  mins = min(cnt)
  m = m - mins * ls[cnt.index(mins)]
  result += mins

print(result)
