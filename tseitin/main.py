# -*- coding: utf-8 -*-

# Transformación de una formula en forma clausal
# Input: cadena de la formula en notacion inorder
# Output: lista de listas de literales

# Importando la libreria FNC
import FNC as fn
letrasProposicionalesA = ['p', 'q', 'r', 's', 't']
# # Formula a la cual encontrar su forma clausal
formula = "-p"
# formula = "(pYq)"
# formula = "(pOq)"
#formula = "(p>q)"

# Aplicando el algoritmo de Tseitin a formula
# Se obtiene una cada que representa la formula en FNC
fFNC = fn.Tseitin(formula, letrasProposicionalesA)
#recibe una formula en su forma normal y el conjunto de letras que pueden pertenecer a esas formulas anteriores
#sale la formula con nuevas variables y ya hecha la transmormacion de de Tseitin
# Se obtiene la forma clausal como lista de listas de literales
fClaus = fn.formaClausal(fFNC)
#recibe un formula cualquiera pero principalmente recibe ya hecha la de tseitin para pasarla a forma  clausal

# Imprime el resultado en consola
print(fClaus)

#para la linea 11 primero se hace el tseitin y luego este resultado se pasa por fclaus para volverlo en forma clausal