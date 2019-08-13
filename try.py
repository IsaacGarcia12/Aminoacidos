#!/usr/bin/python3

with open(cadena) as f:
    data = f.read()
    print([data[i:i+3] for i in range(0, len(data), 3)]) 
f.close()