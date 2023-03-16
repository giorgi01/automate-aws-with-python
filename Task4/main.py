import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument('input', type=str)
args = parser.parse_args()
text = args.input

floats = []
odds = []
evens = []

for match in re.findall(r'\d+\.\d+', text):
    floats.append(float(match))

for match in re.findall(r'\d*[13579]\d*', text):
    odds.append(int(match))

for match in re.findall(r'\d*[02468]\d*', text):
    evens.append(int(match))

print(f"Floats: {floats}")
print(f"Odds: {odds}")
print(f"Evens: {evens}")
