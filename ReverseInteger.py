#Reverse Integer
def solution(x):
  string = str(x)

  #notation "[a:b:c]" means "count in increments of c starting at a inclusive, up to b exclusive"
  if string[0] == '-':
    return int('-'+string[:0:-1])
  else:
    return int(string[::-1])

print(solution(-123))
print(solution(2.5))
  