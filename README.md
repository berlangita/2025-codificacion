# 2025-codificiacion

## 1 - Codificación ASCII

---

Imprime por pantalla una lista de todos los carácteres ASCII

extracto:

```sh
...
97  - a
98  - b
99  - c
100 - d
...
```

te serán necesarios:

- [string.ljust()](https://www.w3schools.com/python/ref_string_ljust.asp)
- [ord()](https://www.w3schools.com/python/ref_func_ord.asp)
- [chr()](https://www.w3schools.com/python/ref_func_chr.asp)

## 2 Cuadricula ASCII

---

# Cuadricula

Vamos a crear una cuadricula.

La cuadricula leerá el tamaño del terminal y dibujará un recuadro basado en el mismo

```python
import os

# Print the size of terminal

dimensiones = {
    "col": os.get_terminal_size().columns,
    "lines": os.get_terminal_size().lines,
}

print(dimensiones)
```

## Ejemplo de visualización

```sh
Contador Izq: 0                                             Contador Der:0
╔═════════════════════════════════════════════════════════════════════════╗
║*************************************************************************║
║*************************************************************************║
║*************************************************************************║
║*************************************************************************║
║*************************************************************************║
║*************************************************************************║
║*************************************************************************║
║*************************************************************************║
║*************************************************************************║
║*************************************************************************║
║*************************************************************************║
║*************************************************************************║
║*************************************************************************║
╚═════════════════════════════════════════════════════════════════════════╝
Registro 1:
Registro 2:
Registro 3:
```
