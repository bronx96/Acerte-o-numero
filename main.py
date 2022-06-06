from random import randint
valor = randint(0,100)
while True:
  palpite = int(input("diga seu palpite de um a 100\n"))
  if palpite - 30 > valor:
    print("seu palpite foi muito alto")
  elif palpite + 30 < valor:
    print("seu palpite foi muito baixo")
  elif palpite > valor:
    print("seu valor foi um pouco mais alto que o correto")
  elif palpite < valor:
    print("seu valor foi um pouco mais baixo que o correto")
  else:
    break
print("parabens, você acertou")
