estatura1 = float(input("Informe a primeira estatura:"))
estatura2 = float(input("Informe a segunda estatura:"))
estatura3 = float(input("Informe a terceira estatura:"))
estaturas = [estatura1, estatura2, estatura3]
if estatura1 == estatura2 or estatura2 == estatura3 or estatura3 == estatura1:
    print("Há 2 pessoas com o mesmo tamanho")
else:
    print(f"A maior estatura é: {max(estaturas)}")