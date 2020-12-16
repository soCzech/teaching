# OS
# ----------------
import os

print(os.path.exists("slozka/text1.txt"))
print(os.listdir("slozka"))

soubor1 = os.listdir("slozka")[0]

# soubor1 = "slozka/" + soubor1
print(os.path.join("C:", "users", "slozka", soubor1))


# SHUTIL
# ----------------
import shutil
shutil.copy("slozka/text1.txt", "slozka/text1-kopie.txt")


# SYS
# ----------------
import sys
print(sys.argv)

if len(sys.argv) == 1:
    print("Zadejte argument")
    exit(1)

if not os.path.exists(sys.argv[1]):
    print("Zadejte existujici soubor")
    exit(1)

# lepsi pro argumenty...
import argparse


# RANDOM
# ----------------
import random

print(random.randint(0,10), random.random())
if random.random() < 0.3:
    pass


# DATETIME
# ----------------
from datetime import datetime

print(datetime.now())
print(datetime.strftime(datetime.now(), "%Y %m %d"))
