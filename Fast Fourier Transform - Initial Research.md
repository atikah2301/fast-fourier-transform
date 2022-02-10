# Fast Fourier Transform - Initial Research

[Video Link](https://www.youtube.com/watch?v=h7apO7q16V0)

## Introduction:

FFT has many applications in modern technology (e.g. GPS, wireless, signal processing)

The graph visualisation of FFT is an FFT circuit

A lot of prerequisite knowledge required:

- Discrete Fourier Transform
- Time-domain to Frequency-domain conversions etc.

## Polynomial Multiplication:

Two polynomials, $A(x)$ and $B(x)$, and we want to find $C(x)=A(x)\cdot B(x)$

### How can we find an efficient algorithm for this?

- Naively, we can apply the distributive property of multiplication of algebraic terms, i.e. multiply terms systematically, collect like-terms, and repeat.
- However this would not be very efficient. The representation of the polynomial we use will effect the efficiency of the algorithm. 
- So, we should explore other representations which may be more efficient.

### Representations of polynomials

- **Coefficient representation**:
    - Arrange the coefficients of the polynomial in some data structure, such as an array, matrix etc.
    
    - E.g. $A(x)=2+3x+x^2+3x^4$ could be `A = [2,3,1,0,3]`. 
    - We go in the reverse order of how a polynomial is naturally written since this allows our array's i-th index to match the i-th degree coefficient. So, we know that `C[4]` refers to $kx^4$
    
    - Multiplying 2 polynomials of degree $d$ using the distributive property has a run time of $O(d^2)$ since we are multiplying $d+1$ terms in the first polynomial by $d+1$ terms in the second, giving $O(d^2+2d+1)=O(d^2)$
    - Can we do better?
    
- **Value representation**:

    - Any $d+1$ points of a degree $d$ polynomial is sufficient to unique represent the polynomial. E.g. 3 points are enough to define a quadratic, 4 points define a cubic etc.
    - ***Proof***: 
        - $d+1$ points evaluated by the degree $d$ polynomial $P(x)$ gives us a system of $d+1$ equations, which we can represent as a matrix-vector product, $P=XC$.
        - $P$ is the $(d+1)\times1$ vector of values that $P(x)$ is evaluated to at each point
        - $X$ is $(d+1)\times (d+1)$ matrix where 
            - row $i\in \{0,..,d\}$ is for the the $i$-th point 
            - column $j\in \{0,..,d\}$ is the $x$ coordinate of the $j$-th point to the power of $j$ 
        - $C$ is the $(d+1)\times1$ vector of coefficients of $P(x)$
        - If each of the points chosen are unique, then $X$ will always be an invertible matrix. This is because the determinant of $X$ will be non-zero. ***(Proof required)***
        - Therefore, there is a unique solution, $C$, to the matrix equation, and thus a unique polynomial that is described by the points.
    - Using this representation for multiplication, say polynomial $A(x)$ and $B(x)$ both have degree $d$. Then, their product $C(x)$ must have degree $d^2$, so it can be described by $d^2+1$ unique points.
    - We can simply choose any $d^2+1$ values of $x$, evaluate $A(x_i)$ and $B(x_i)$ at these values, and multiply them together to get $A(x_i)\cdot B(x_i)= C(x_i)$. Then, we have $d^2+1$ points in the form $\{(x_0,C(x_0)),...,(x_{d^2}, C(x_{d^2}))\}$, which represents our polynomial product. 
    - The complexity of this algorithm is only $O(d)$, therefore it is more efficient than distributive multiplication.

### Problems converting between coefficients and values

- The faster algorithm takes value representation as input, and gives value representation as output.
- We want the input to be coefficient rep, and the output to be coefficient rep, since these are more common, useable, and straightforward in representing polynomials.
- One way to go from **coefficients to values** is to evaluate the polynomial at $d+1$ different $x$ values (either chosen at random, or chosen as $\{0,1,..,d\}$ etc.). However, since we need to evaluate at each of the $d+1$ terms in the polynomial, the whole process is $O(d^2)$, which would defeat the point of using the more efficient $O(n)$ algorithm.
- One way to go from **values to coefficients** is to solve a system of linear equations. This also has an algorithmic complexity, at best, of $O(n^2)$, and at worst, $O(n^3)$. 
- Clearly we need more efficient conversion methods. This is where the FFT comes into play.

### Choosing $x$ values for faster conversion

- Converting from coefficient representation to value representation could be made much faster if we could somehow use fewer than $d+1$ unique $x$ values to find all our points. Let $n=d+1$ be the number of points in the value representation of a polynomial.
- This is possible if we choose our $x$ values to exploit the symmetries that exist in polynomials. 
    - All single-term polynomials of even degree (i.e. $x^2,\,x^4,..$) are even functions, with symmetry $P(-x)=P(x)$
    - All single-term polynomials of odd degree (i.e. $x^3,\,x^5,..$) are odd functions, with symmetry $P(-x)=-P(x)$
    - So for these polynomials, we only need at least half as many $x$ values to be able to represent a polynomial. We simply use the symmetry to evaluate $P(-x)$ virtually instantly.
- Generalising this, we can try splitting up any polynomial into its even degree and odd degree terms, then factorise $x$ from the odd degree terms to get an expression with only even degree terms, e.g. 
    - $P(x)=3x^5+2x^4+x^3+7x^2+4x+8$
    - $P(x)=(2x^4+7x^2+8)+(3x^5+x^3+4x)$
    - $P(x)=(2x^4+7x^2+8)+x(3x^4+x^2+4)$
- A polynomial with all even degree terms can be considered as polynomial with terms of half the degree, which take squared input. This can be demonstrated by writing the even degree term polynomials using $w=x^2$, e.g.
    - $P(x)=(2w^2+7w+8)+x(3w^2+w+4)$
    - $P(x)=P_{even}(w)+xP_{odd}(w)$
    - $P(x)=P_{even}(x^2)+xP_{odd}(x^2)$
- So, we can say any degree $d$ polynomial that we want to evaluate at $n=d+1$ points can be split into 2 $n/2$ degree polynomial, if $n$ is even, or an split into an $n/2$ degree polynomial and a polynomial with degree $n/2-1$ at most.
- Now using the symmetry of even and odd polynomials, and where $x_i$ is one of the $n$ different $x$ values we have chosen, we can say that:
    - If $P(x_i)=P_{even}(x_i^2)+x_iP_{odd}(x_i^2)$
    - Then $P(-x_i)=P_{even}(x_i^2)-x_iP_{odd}(x_i^2)$
- For example, if $P(x)=3x^5+2x^3+x^2-6$, then $P_{even}(w)=w-6$ and $P_{odd}(w)=3w^2+2$ where $w=x^2$ 
- Evaluating $P(x)$ at $x=2$ require us to evaluate $P_{even}(2^2)=-2$ and $P_{odd}(2^2)=56$. Then we just calculate that $P(2)=-2+2(56)=110$ and $P(-2)=-2-2(56)=-114$
    - Note: we got $P(-x_i)$ "for free", i.e. at complexity $O(1)$, since we only needed 2 arithmetic operations in addition to the ones we did anyway to get $P(x_i)$ to calculate it. These 2 operations are independent of the size of the polynomial or the degree, hence constant time. 
- More generally, we can keep splitting up a polynomial of any degree and keep reducing the required number of computations by half..... **How does the complexity get reduced to $O(nlogn)$?** Something to do with the halving brings about $log_2(n)$ but not sure how...

- **What exactly is the recursive step?**
- Since we need to choose our $x$ values such that $x_i^2=-x_j^2$ in order for us to continue taking advantage of the symmetry of polynomials at each recursive step.
- A systematic way for us to choose such values is by finding the $n$th roots of unity for $n\geq d+1$, ideally where $2^k|n$ for some $k\in \N$. 

### Complex numbers revision

The set of complex numbers, $\C$, encompasses all possible numbers, but is distinguished from the set of real numbers, $\R$, for including numbers with an "imaginary component", which is some multiple of the imaginary unit, $i$.

$i$ is defined as $\sqrt{-1}$. So, its integer powers have the property such that $i^k\equiv i^{k\,mod\,4}$, so they cycle between 1, $i$, $-1$, and $-i$.



Complex numbers can be represented in 3 forms:

- Polar - $r(cos(\theta)+isin(\theta))$
    - Represents both the argument, $\theta$, and the magnitude, $r$ 
    - Can instantly convert to exponential form
    - Evaluate the expression to convert to rectangular form
- Exponential - $re^{i\theta}$
    - Represents both the argument, $\theta$, and the magnitude, $r$ 
    - Can instantly convert to polar form
    - Convert to polar form then evaluate to convert to rectangular form
- Rectangular - $a+bi$
    - Represents the vertical and horizontal coordinates on the Euclidian complex plane
    - Use $tan(\frac{a}{b})$ to get the argument
    - Use Pythagoras' to get the magnitude

$n$th roots of unity are all the complex numbers given on the complex plane when taking the argument to be $\frac{2\pi}{n}$.



### Evaluation Algorithm

### Interpolation Algorithm