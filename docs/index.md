# Cifra de César

A ideia desse projeto é representar uma biblioteca capaz de executar a cifra de César (ROT13)

## Exemplos de uso

### Encriptação

```python
from cifra_cesar import encripta

encripta('Eduardo')   # rqhneqb
```

### Decriptação

```python
from cifra_cesar import decripta

decripta('rqhneqb')   # eduardo
```

### Rotações diferentes de 13
```python
from cifra_cesar import decripta, encripta

encripta('Eduardo')   # sriofrc
decripta('sriofrc', 14)   # eduardo
```