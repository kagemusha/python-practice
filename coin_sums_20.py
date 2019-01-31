# 20 10 5 2 1
# want combos to make 200
import numpy_practice as np

obj = 20
solutions = [(1,0,0,0,0), (0,2,0,0,0)]
val_matrix = np.array([10,5,2,1])


def val(l, m, n, o):
  return np.array([l,m,n,o]).dot(val_matrix)

def log_sol(k,l,m,n):
  sol = (0,k,l,m,n)
  solutions.append(sol)
  print(sol)

for j in range(0, 2): #j: 10
  v = val(j,0,0,0)
  if v == obj:
    log_sol(j,0,0,0)
    break
  else:
    for k in range(0, 5):  #k: 5
      v = val(j,k,0,0)
      if v == obj:
        log_sol(j,k,0,0)
        break
      elif v > obj:
        break
      else:
        for l in range(0, 10):
          v = val(j,k,l,0)
          if v == obj:
            log_sol(j,k,l,0)
            break
          elif v > obj:
            break
          else:
            log_sol(j,k,l,obj-v)

print(len(solutions))



