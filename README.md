# svglib

  
  

Handy library to manipulate SVG files in Python. Extension of the original svglib package from the Deepsvg paper.

  

**Currently under develpment.**

✅ fixed or newly implemented feature
⌛ to be checked
🚫 currently not supported 

|              | Line | Quadratic | Cubic | Rect | Circle | Ellipse |
|--------------|------|-----------|-------|------|--------|---------|
| shift        | ✅    | ⌛         | ⌛     | ⌛    | ⌛      | ⌛       |
| scale        | ✅    | ⌛         | ⌛     | ⌛    | ⌛      | ⌛       |
| bounding box | ✅    | 🚫         | 🚫     | 🚫    | 🚫      | 🚫       |

Quadratic Bezier are converted into Cubic Bezier according to the formula:

\[
\begin{aligned}
CP_0 &= QP_0 \\
CP_3 &= QP_2 \\
CP_1 &= QP_0 + \frac{2}{3} (QP_1 - QP_0) \\
CP_2 &= QP_2 + \frac{2}{3} (QP_1 - QP_2)
\end{aligned}
\]

## Usage

Tutorials can be found in the `examples` folder.

  
  ---

Credits: [original repository.](https://github.com/alexandre01/deepsvg/tree/master/deepsvg/svglib)