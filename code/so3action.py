import sympy
from sympy import cos, sin

import subprocess

a,b,c = sympy.symbols('a b c') # Euler angles
# sa, ca, sb, cb, sc, cc = sympy.symbols('s_a c_a s_b c_b s_c c_c')


sa = sin(a)
ca = cos(a)
sb = sin(b)
cb = cos(b)
sc = sin(c)
cc = cos(c)

A = sympy.Matrix([[1,0,0],[0,ca,sa],[0,-sa,ca]])
B = sympy.Matrix([[cb,0,-sb], [0,1,0], [sb,0,cb]])
C = sympy.Matrix([[cc,sc,0],[-sc,cc,0],[0,0,1]])

R = A*B*C

v1, v2, v3 = sympy.symbols('v1 v2 v3')
vMat = sympy.Matrix([[0,v3,-v2],[-v3,0,v1],[v2,-v1,0]])
vVec = sympy.Matrix([[v1],[v2],[v3]])

actMat = R * vMat * R.transpose()
actVec = R * vVec
actMat = sympy.simplify(actMat)
actVec = sympy.simplify(actVec)

with open("actionTest.tex", "w") as output_file:
  output_file.write(r"""\documentclass{article}
\usepackage[margin = 0cm,landscape, a2paper]{geometry}
\usepackage{amsmath}
\usepackage{amssymb}
\begin{document}
\begin{equation*}""")
  output_file.write(sympy.latex(A) + r'\qquad'+ sympy.latex(B)+ r'\qquad'+ sympy.latex(C))
  output_file.write(r"""\end{equation*}
                    
                    \begin{equation*}""")
  output_file.write(sympy.latex(vMat) + r'\qquad'+ sympy.latex(vVec))
  output_file.write(r"""\end{equation*}
                    
                    \begin{equation*}""")
  output_file.write(sympy.latex(actMat))
  output_file.write(r"""\end{equation*}
                    
                    \begin{equation*}""")
  output_file.write(sympy.latex(actVec))
  output_file.write(r"""\end{equation*}
                    \end{document}""")


subprocess.run(["pdflatex", "actionTest.tex"]) 
