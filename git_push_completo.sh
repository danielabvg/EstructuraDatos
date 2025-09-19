#!/bin/bash

# Ir al directorio del repo correcto
cd /Users/dani/Documents/CursoEstructuraDatos || exit

# Agregar todos los cambios
git add .

# Crear commit con fecha y hora actual
git commit -m "update: $(date '+%Y-%m-%d %H:%M:%S')"

# Hacer push a la rama actual
git push

