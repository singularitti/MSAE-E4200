# HW 3

1. 

   1. If we choose 

   $$
   \begin{align}\label{eq:xaxb}
     x_A &= \frac{ 1 }{ \sqrt{2} } (x_a - x_b), \\
     x_B &= \frac{ 1 }{ \sqrt{2} } (x_a + x_b),
   \end{align}
   $$
   i.e., $x_A$ to be even mode and $x_B$ to be odd mode, we will get
   $$
   \begin{align}
     x_A &= - \frac{ x_0 }{ \sqrt{2} } \cos \sqrt{\frac{3\gamma}{m}} t, \\
     x_B &= \frac{ 3 x_0 }{ \sqrt{2} } \cos \sqrt{\frac{\gamma}{m}} t, \\
     p_A &= \frac{ x_0 }{ \sqrt{2} } \sqrt{3 \gamma m} \sin \sqrt{\frac{3\gamma}{m}} t, \\
     p_B &= - \frac{ 3 x_0 }{ \sqrt{2} } \sqrt{\gamma m} \cos \sqrt{\frac{\gamma}{m}} t.
   \end{align}
   $$
   Thus
   $$
   \begin{align}
     \frac{ x_A^2 }{ \frac{ x_0^2 }{ 2 } } + \frac{ p_A^2 }{ \frac{ 3 \gamma m x_0^2 }{ 2 } } &= 1, \\
     \frac{ x_B^2 }{ \frac{ 9 x_0^2 }{ 2 } } + \frac{ p_B^2 }{ \frac{ 9 x_0^2 \gamma m }{ 2 } } &= 1.
   \end{align}
   $$
   The intercepts on x-axis:
   $$
   \begin{align}
     x_A &= \pm \frac{ x_0 }{ \sqrt{2} }, \\
     x_B &= \pm \frac{ 3 x_0 }{ \sqrt{2} },
   \end{align}
   $$
   and the intercepts on p-axis:
   $$
   \begin{align}
     p_A &= \pm \sqrt{\frac{ 3 \gamma m }{ 2 }} x_0, \\
     p_B &= \pm 3 \sqrt{\frac{ \gamma m }{ 2 }} x_0.
   \end{align}
   $$
   No figure: $-1$, label intercepts incorrectly: $-0.5$, wrong answer: $-1.25$.

   2. This question is a bit tricky. Two ways of answering: Integerate
   $$
   Z_1 = \frac{ 1 }{ h^2 } \int dp_a e^{-\beta \frac{ p_a^2 }{ 2m }} \int dp_b e^{-\beta \frac{ p_b^2 }{ 2m }} \int dx_a \int dx_b e^{-\beta \frac{ 1 }{ 2 } \gamma \Big( x_a^2 + x_b^2 + (x_b - x_a)^2 \Big)} = \frac{ 4 \pi^2 m }{ \sqrt{3} h^2 \gamma \beta^2 },
   $$
   **no points is taken off if you write only $1$ $h$**; or integrate
   $$
   Z_2 = \frac{ 1 }{ h^2 } \int dp_a e^{-\beta \frac{ p_a^2 }{ 2m }} \int dp_b e^{-\beta \frac{ p_b^2 }{ 2m }} \int dx_A e^{-\beta \frac{ 3 }{ 2 } \gamma x_A^2} \int dx_B e^{-\beta \frac{ 1 }{ 2 } \gamma x_B^2}.
   $$

   Now the tricky part comes: We want to make sure that $Z_1 = Z_2$, this is not naturally true since you change the integration variable from $x_a$, $x_b$ to $x_A$, $x_B$ now.

   First, let's say we are still integrating the same region. For $x_a$, $x_b$, we integrate over the whole $\mathbb{R}^2$ plane; $x_A$ and $x_B$ are just a linear combination of $x_a$ and $x_b$, so we are still integrating over the $\mathbb{R}^2$ plane.

   Next, when we are changing variables for a double integral, we need to time a Jacobian of the transformation, just like [this page](http://tutorial.math.lamar.edu/Classes/CalcIII/ChangeOfVariables.aspx) shows. In the above case, the Jacobian $J$ will satisfy 
   $$
   dx_a dx_b = \det(J) dx_A dx_B = \det \bigg\{\frac{ 1 }{ \sqrt{2} } \begin{bmatrix}
     1 & -1\\
     1 & 1
   \end{bmatrix} \bigg\} \, dx_A dx_B = dx_A dx_B,
   $$
   so we are sure that $Z_1 = Z_2$ now. So
   $$
   Z_2 = \frac{ 4 \pi^2 m }{ h^2 \beta^2 \gamma \sqrt{3} }.
   $$

   If a different combination other than $\eqref{eq:xaxb}$ is used and not divided by the determinant of $J$, **$0.5$ points will be taken off**. For example, if
   $$
   \begin{align}
     x_A &= \frac{ 1 }{ 2 }(x_a - x_b), \\
     x_B &= \frac{ 1 }{ 2 }(x_a + x_b),
   \end{align}
   $$
   then $Z_1 = \frac{ 1 }{ 2 } Z_2$, and if

   $$
   \begin{align}
     x_A &= x_a - x_b, \\
     x_B &= x_a + x_b,
   \end{align}
   $$

   then $Z_1 = 2 Z_2$. If you use $p_A$ and $p_B$ in the integration, then they will be $Z_1 = \frac{ 1 }{ 4 } Z_2$ and $Z_1 = 4  Z_2$. 

   $E = -\frac{ \partial \ln Z }{ \partial \beta }$ is not affected by $Z$, so no matter what basis you choose, $E$ is always $\frac{ 2 }{ \beta }$.

2. Because the potential is analytical, which means its second-order derivatives are continuous, we know that
   $$
   \frac{ \partial^2 V }{ \partial x_i \partial x_j } = \frac{ \partial^2 V }{ \partial x_j \partial x_i },
   $$
   so the force constant matrix is symmetric. Let us assume it to be
   $$
   \hat{\mathrm{ V }} = \begin{pmatrix}
     a & b & c \\
     d & e & f \\
     g & h & i
   \end{pmatrix}.
   $$
   Directly starts from
   $$
   \gamma \begin{pmatrix}
     2 & -1 & 0 \\
     -1 & 2 & -1 \\
     0 & -1 & 2
   \end{pmatrix}
   $$
   **will be taken $1$ point off**, since the question asks (irreducible derivatives are) “dictated by the mirror and symmetric nature of stiffness matrix”.

   1. We start in the naive basis with a general Taylor series and then enforce symmetry. Apply mirror
      $$
      \hat{\sigma} = \begin{pmatrix}
        0 & 0 & -1 \\
        0 & -1 & 0 \\
        -1 & 0 & 0
      \end{pmatrix}
      $$
      to $\hat{\mathrm{ V }}$: $\hat{\sigma} \hat{\mathrm{ V }} \hat{\sigma}^\mathrm{ T } = \hat{\mathrm{ V }}$or $\hat{\sigma} \hat{\mathrm{ V }} = \hat{\mathrm{ V }} \hat{\sigma}$ since $\hat{\sigma} \hat{\sigma}^\mathrm{ T } = 1$. We find there are only $4$ irreducible derivatives:
      $$
      \hat{\mathrm{ V }} = \begin{pmatrix}
        a & b & c \\
        b & d & b \\
        c & b & a
      \end{pmatrix}.
      $$

   2. Gram-Schmidt is a little bit overkill here. We know $\sigma$ only has $2$ eigenvalues. This can be seen from
        $$
        \begin{align}
          \hat{\sigma}^2 = \hat{\sigma} \hat{\sigma}^\mathrm{ T } &= 1, \\
          \hat{\sigma} | \phi \rangle &= \lambda | \phi \rangle, \\
        \hat{\sigma} (\hat{\sigma} | \phi \rangle) &= \lambda \hat{\sigma} | \phi \rangle = \lambda^2 | \phi \rangle = 1 | \phi \rangle, \\
          \lambda^2 = 1 \Rightarrow \lambda& = \pm 1.
        \end{align}
        $$
        For eigenvectors with eigenvalues $-1$, we call them “odd”, otherwise we call them “even”. Thus for matrix has dimension larger than $2$, we must have degeneracies. Now we know $-1$ corresponds to $2$ eigenvectors, one is $\frac{ 1 }{ \sqrt{10} } [1, 3, 1]$, we can find the other by
        $$
        \hat{\sigma} | \phi \rangle = \hat{\sigma} [a, b, c]^\mathrm{ T } = [-c, -b, -a]^\mathrm{ T } = - [a, b, c]^\mathrm{ T },
        $$
        so $c = a$, and $\frac{ 1 }{ \sqrt{10} } [1, 3, 1] \cdot [a, b, c]^\mathrm{ T } = 0$, we get
        $$
        2 a + 3b = 0,
        $$
        so we get $| \phi \rangle = \frac{ 1 }{ \sqrt{22} } [3, -2, 3]^\mathrm{ T }$.

        Of course, you can find other eigenvectors as long as they are “odd”, or $2$ eigenvectors that are a linear combination of $\frac{ 1 }{ \sqrt{10} } [1, 3, 1]$ and $\frac{ 1 }{ \sqrt{22} } [3, -2, 3]^\mathrm{ T }$.

   3. Almost everybody does this question correctly so I am not going to explain here. But please you match “odd” and “even” labels correctly with the vectors.

   4. 

        1. Almost everybody does this question correctly.

        2. Starts from
             $$
             \hat{\mathrm{ V }} = \begin{pmatrix}
               a & b \\
               c & d
             \end{pmatrix},
             $$
             or apply symmetric condition:
             $$
             \hat{\mathrm{ V }} = \begin{pmatrix}
               a & b\\
               b & a
             \end{pmatrix}.
             $$
             They apply $\hat{\mathrm{ V }} = \hat{\mathrm{ T }}^\dagger \hat{\mathrm{ V }} \hat{\mathrm{ T }}$ condition, where $\mathrm{ T }$ is $\mathrm{ T }_1$ (since $\mathrm{ T }_2$ is just identity operator).

             They apply acoustic sum rule, we find $a + b = 0$.

             So

             $$
             \hat{\mathrm{ V }} = a \begin{pmatrix}
               1 & -1\\
               -1 & 1
             \end{pmatrix}.
             $$

        3. The eigenvalues of $\hat{\mathrm{ V }}$ are just $0$ and $2 a$. The eigenvalues of the dynamical matrix are the same of the eigenvalues of the stiffness matrix.


​       






