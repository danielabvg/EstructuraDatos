### Guía práctica: Flujo básico de Git en un proyecto de Estructura de Datos

#Este documento describe paso a paso el proceso de creación de una rama,
#agregar cambios, hacer commits y subirlos a GitHub.

#Comandos ejecutados en la terminal:

# 1. Verificar el estado actual del repositorio
# --------------------------------------------
# Muestra en qué rama estás y si hay cambios pendientes por guardar.
# Comando:
# git status
print("git status -> muestra el estado actual del repositorio")


# 2. Ver las ramas existentes en el repositorio
# ---------------------------------------------
# Lista todas las ramas locales y marca con * la rama actual.
# Comando:
# git branch
print("git branch -> muestra las ramas locales y resalta en cuál estás trabajando")


# 3. Crear y cambiarse a una nueva rama
# -------------------------------------
# Se crea una rama para trabajar de manera independiente (en este caso: unidad1).
# Comando:
# git checkout -b development/unidad1
print("git checkout -b development/unidad1 -> crea y mueve a la nueva rama 'development/unidad1'")


# 4. Agregar los cambios al área de preparación (staging area)
# ------------------------------------------------------------
# Se añaden los archivos modificados o creados.
# Comando:
# git add .
print("git add . -> agrega todos los cambios al área de preparación")


# 5. Crear un commit con un mensaje descriptivo
# ---------------------------------------------
# Guarda los cambios en la historia de Git con un mensaje.
# Comando:
# git commit -m "Ejemplo de arreglos"
print('git commit -m "Ejemplo de arreglos" -> crea un commit con el mensaje')


# 6. Subir los cambios al repositorio remoto
# ------------------------------------------
# Se suben los cambios de la nueva rama al repositorio en GitHub.
# Comando:
# git push -u origin development/unidad1
print("git push -u origin development/unidad1 -> sube la nueva rama al remoto y la vincula")


# 7. Crear un Pull Request (PR)
# ------------------------------
# Una vez subida la rama, GitHub sugiere crear un Pull Request para fusionar los cambios
# en la rama principal (main).
# Enlace sugerido:
# https://github.com/danielabvg/EstructuraDatos/pull/new/development/unidad1
print("Ir a GitHub y crear un Pull Request desde la rama 'development/unidad1' hacia 'main'")

#ejemplo
