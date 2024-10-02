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

v1, v2, v3 = sympy.symbols('v_1 v_2 v_3')
t = sympy.symbols('t')

tanMat = sympy.Matrix([[1,v1*t, -v2*t], [-v1*t, 1, v3*t], [v2*t,-v3*t, 1]])

finalTan = R.transpose() * tanMat * R
# finaltan = sympy.simplify(finalTan)

with open("momMapTest.tex", "w") as output_file:
  output_file.write(r"""\documentclass{article}
\usepackage[margin = 0cm,landscape, a1paper]{geometry}
\usepackage{amsmath}
\usepackage{amssymb}
\begin{document}
\begin{equation*}""")
  output_file.write(sympy.latex(tanMat))
  output_file.write(r"""\end{equation*}
                    \begin{equation*}""")
  output_file.write(sympy.latex(finalTan))
  output_file.write(r"""\end{equation*}
                    \end{document}""")


subprocess.run(["pdflatex", "momMapTest.tex"]) 
