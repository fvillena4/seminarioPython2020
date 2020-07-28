import time
ok = True
while ok:
  localtime = time.localtime()
  result = time.strftime("%I:%M:%S %p", localtime)
  print(result, end="", flush=True)
  print("\r", end="", flush=True)
  time.sleep(1)
  print(" ")
  x = int(input("Ingrese 0 para finalizar: "))
  if x == 0:
    ok = False
    print(ok)
