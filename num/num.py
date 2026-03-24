num = input("ingrese un numero:")
try:
    num = int(num)
except ValueError:
    num = None

def num_int(num):
    return isinstance(num, int) and num > 0
def num_par_o_impar(num):
    if num is None:
        print("el numero no es un numero")
    else:
        if num is not None and num_int(num):
            if num % 2 == 0:
                print("el numero es par")
            else:
                print("el numero es impar")
        else:        
            print("el numero no es natural")
num_par_o_impar(num)