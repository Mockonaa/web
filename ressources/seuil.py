def seuil(u):
  n=0
  while u > 2000:
    n += 1
    u=u*0.95+80*0.95
  return n

seuil(3000)
