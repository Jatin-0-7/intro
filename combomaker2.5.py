from faker import Faker

fake = Faker(['en_US', 'es_ES', ])

print("""\33[32m
  COMBO MAKER Y REMOVEDOR DE REPETIDOS
            AUTOMATICAMENTE
""")

print("""
  OPCIONES:
  1) Nombres: Nombres + Números (Remueve los repetidos)
  Los números se generan automáticamente
  Ejemplo:
  antonio123:antonio123
  Antonio1234:Antonio123
  ANTONIO123:ANTONIO1234

  0) SALIR
""")

menu = input("Ingrese una opción: ")

if menu == "1":
    print("\t\t (.txt) No escriba")
    filename = input("\nIngrese el nombre de su Combo: ")
    num_lines = 100000  # Cambié el valor de 20,000 a 100,000
    specific_num1 = input("Ingrese el número específico que desea usar: ")
    specific_num2 = input("Ingrese el número específico que desea usar para la contraseña: ")

    combos = set()
    with open(f"/storage/emulated/0/combo/{filename}.txt", "a+", encoding="utf-8") as f:
        count = 0
        while len(combos) < num_lines and count < 100000:
            first_name = fake.first_name()
            last_name = fake.last_name()

            num1 = specific_num1
            num2 = specific_num2

            alln = f"{first_name}{num1}:{first_name}{num2}"
            allf = f"{last_name}{num1}:{last_name}{num2}"

            print(alln)
            print(allf)

            combos.add(alln)
            combos.add(allf)
            combos.add(alln.lower())
            combos.add(allf.lower())
            combos.add(alln.upper())
            combos.add(allf.upper())

            count += 1

        for combo in combos:
            if len(combo) <= 100000:
                f.write(combo + "\n")

    print("\nCombo generado con éxito. ¡Happy cracking!")
