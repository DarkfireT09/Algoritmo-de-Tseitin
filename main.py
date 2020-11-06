# -*- coding: utf-8 -*-

# Transformación de una formula en forma clausal
# Input: cadena de la formula en notacion inorder
# Output: lista de listas de literales

# Importando la libreria FNC
import FNC as fn
letrasProposicionalesA = ['p', 'q', 'r', 's', 't']
# # Formula a la cual encontrar su forma clausal
#formula = "(((pY-q)Y-r)O((-pYq)Y-r))"
formula = "-(-p>(rO-q))"
#formula = "((p>-q)>r)"
#formula = "(((-pOq)O(p>-q))>-((q>(rY(sO-t)))>-p))"
#formula = "(((p>(rY(sO-t)))>-q)>-((-pOq)O(p>-q)))"
#formula = "(((-pOq)O(p>-q))>-((p>(rY(sO-t)))>-q))"
#formula = "((p>(rY(sO-t)))>-q)"

# Aplicando el algoritmo de Tseitin a formula
# Se obtiene una cada que representa la formula en FNC
fFNC = fn.Tseitin(formula, letrasProposicionalesA)

# Se obtiene la forma clausal como lista de listas de literales
fClaus = fn.formaClausal(fFNC)

# Imprime el resultado en consola
print(fClaus)
