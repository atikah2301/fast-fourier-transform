# Fast Fourier Transform - Initial Research

## Links and References

[Long Video Link](https://www.youtube.com/watch?v=h7apO7q16V0)

[Exponential Form with C++ code](https://www.youtube.com/watch?v=htCj9exbGo0)

[MIT Divide & Conquer, FFT](https://www.youtube.com/watch?v=iTMn0Kt18tg)

[MIT "Design and Analysis of Algorithms" Course page](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-046j-design-and-analysis-of-algorithms-spring-2015/)

Erik Demaine, Srini Devadas, and Nancy Lynch. *6.046J Design and Analysis of Algorithms.* Spring 2015. Massachusetts Institute of Technology: MIT OpenCourseWare, [https://ocw.mit.edu](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-046j-design-and-analysis-of-algorithms-spring-2015). License: [Creative Commons BY-NC-SA](https://creativecommons.org/licenses/by-nc-sa/4.0/).

## Checklist

- [x] Define FFT and DFT
- [x] Understand Coefficient vs Value representation
    - [ ] Proof that n distinct points uniquely determine a polynomial of degree n-1
        - [ ] Matrix / linear algebraic proof using Vandermonde matrix
        - [ ] Uniqueness & Existence proof by Prof CLG
- [x] Understanding time complexity of FFT and naive algorithms
- [ ] Understanding properties of complex numbers
    - [x] Representations of complex numbers
        - [x] Polar
        - [x] Trigonometric
        - [x] Exponential
    - [ ] Roots of unity
- [ ] Best way of selecting x_k terms for value rep
- [x] Understanding the recursion by splitting polynomials into even and odd numbered coefficients
- [x] Divide & Conquer approach
- [ ] Inverse of FFT
- [x] FFT, Multiply, IFFT
- [ ] At what value of n does FFT method become faster than naive multiplication?
- [ ] Give an example of the recursion
- [ ] Give an example of running the FFT
- [ ] Give an example of running the IFFT



## Introduction

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
    - We go in the reverse order of how a polynomial is naturally written since this allows our array's i-th index to match the i-th degree coefficient. So, we know that `C[4]` refers to $kx^4$
    - Multiplying 2 polynomials of degree $d$ using the distributive property has a run time of $O(d^2)$ since we are multiplying $d+1$ terms in the first polynomial by $d+1$ terms in the second, giving $O(d^2+2d+1)=O(d^2)$
    - Can we do better?
    
- **Value representation**:

    **Theorem** - **polynomial interpolation**: 

    - Let $F$ be any field.
    
    - Let $n > 0$ be an integer, and let $a_0, ...,a_n$ be any $n+1$ distinct elements of $F$.
    
    - Let $b_0,…,b_n$ be any elements of $F$, not necessarily distinct.  
    
    - Then, there is one and only one polynomial $f(x)$ over $F$ of degree at most $n$ such that $f(a_i)=b_i$ for $0 \le i \le n$.
    
    - I.e. any polynomial degree $n$ defined over a field (rational, real, or complex numbers) can be uniquely represented by a set of least $n+1$ points. 
    
    - ***Proof***:
    
        - **Existence** -  To prove the existence of such a polynomial, there must exist $c_0,..,c_n$ such that $f(x)=\sum_{i=0}^{n}c_ix^i$. By evaluating $f(x)$ at each $a_0,..,a_n$ value, we get a system of equations, each of the form $f(a_i)=\sum_{i=0}^{n}c_ia_i^i=b_i$. Since there are $n+1$ equations and $n+1$ terms in each equation, 
    
            
    
        - Consider the Newton Interpolation Polynomial, $f(x)=\sum_{i=0}^n c_i \prod_{j\ne i}(x-a_j)$, equivalently, $f(x)=c_0+c_1(x-a_0)+c_2(x-a_0)(x-a_1)+...+c_n(x-a_0)..(x-a_{n-1})$
    
        - The coefficients can be easily found using quotients of differences. We can start by observing that $f(a_0)=c_0=b_0$. So $f(a_1)=b_0+c_1(a_1-a_0)=b_1$, the rest of the terms in $f(x)$ become $0$ because of $(a_1-a_1)=0$ is a factor in each of them.  By rearranging, we can get that $c_1=\frac{b_1-b_0}{a_1-a_0}$. 
    
            - This forms the start of a recursive relationship, where:
    
        - It is easy to see how to find the unique values for $d_0,\ldots,d_n$ for which $f(x)$ has the required property.  (Supply detail.)  
    
        - **Uniqueness** - It suffices to prove that if $f(a_i)=0$ for all $i$, where $f(x)$ has degree at most $n$, then $f$ is the zero polynomial.
    
            So suppose that $f(x)$ has this vanishing property, and that $f(x)$ has degree $m\le n$.  If $m=0$ then $f(x)$ is constant, and this constant must be zero, as required
    
            So suppose that $m>0$, and let $f(x)=(x-a_n)g(x)+c$ where $g(x)$ has degree $m-1<n$.  Clearly $c=0$, and $g(a_i)=0$ for $0\le i\le n-1$.  By induction on $n$ it follows that $g$ is the zero polynomial, as required. 
    
            Q.E.D.
    
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

- Converting from coefficient representation to value representation could be made much faster if we could somehow use fewer than $d+1$ unique $x$ values to find all our points. Let $n \geq d+1$ be the number of points in the value representation of a polynomial.
- This is possible if we choose our $x$ values to exploit the symmetries that exist in polynomials. 
    - All single-term polynomials of even degree (i.e. $x^2,\,x^4,..$) are even functions, with symmetry $P(-x)=P(x)$
    - All single-term polynomials of odd degree (i.e. $x^3,\,x^5,..$) are odd functions, with symmetry $P(-x)=-P(x)$
    - So for these polynomials, we only need at least half as many $x$ values to be able to represent a polynomial. We simply use the symmetry to evaluate $P(-x)$ in $O(1)$ time.
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

Note that taking a root of unity to some power, $k$, is equivalent to multiplying its argument by $k$, which effectively moves the point along the unit circle on the complex plane. So, $(e^{i\theta})^k=e^{ik\theta}$. So if you square a root of unity, and it had argument $\theta=\frac{\pi}{4}$, which is a one-eighth turn, it becomes $\theta = \frac{\pi}{2}$ which is a quarter turn.

Due to the periodicity of roots of unity, since they quite literally go around in a circle.



### Evaluation Algorithm

- Going from coefficient rep to value rep is essentially evaluating P(x) with degree n at n+1 points.
- So we call Coefficient => Value FFT the "evaluation algorithm"
- Consider evaluating P(x), a degree 7 polynomial, at 8 points, x = {1,2,3,4,5,6,7,8}. 
- Using Horner's rule, we can evaluate a polynomial at 1 value of x to get y in O(n), so doing this for all n+1 points would mean getting the value rep in O(n^2) time
- However, if we chose x = (-1, 1, -2, 2, -3, 3, -4, 4), then for odd or even functions, which have symmetry, we can perform half as many evaluations, and simply get the remaining evaluations either for free (if even symmetry) or at the low-cost of just multiplying by -1 (if odd symmetry)
- Let's extend this to general polynomials

Divide and conquer:

- Split a polynomial into odd and even numbered coefficients, and create two new polynomials of degree n/2
- 

### Interpolation Algorithm







### Radix-2 FFT Algorithm

- Two  types DIT and DIF (decimation in time and frequency)
- Both are divide and conquer algorithms
- Choose the polynomial length N such that it can be factored as r_1, r_2, .. 2_m
- And if all the radixes are the same, then N=r^m 
- The most practical choice of r=2, hence radix-2, so, N=2^m
- N-point DFT can be broken into 2 DFTs of length N/2, etc.
- To do this, we need a few properties of polynomials
    - Symmetry of roots of unity: $\omega_N^{k+\frac{n}{2}}=-\omega_N^k$
    - Periodicity: $\omega_N^{k+N}=\omega_N^{k}$
    - $\omega_N^2 = \omega_{N/2}$

- Let x(n) be a polynomial of degree N and 





# MIT Lecture Notes

## Polynomial Operations & Time Complexity

Evaluation:

Naive method:

- Multiply coefficients by x^k and add them - constant time
- Carry out the exponentiation - quadratic time, since exponentiation is at most n multiplications carried out for n different terms
- So, naive evaluation is O(n^2)

Horner's rule:

- Factor out x from the first n-1 terms, then from the first n-2 terms, etc. 
- This is ultimately 1st coefficient * x + 2nd coefficient, all times by x, and add the 3rd coefficient, all times by x and add the 4th etc.
- So you only do 2 constant time operations for each of the n terms
- So that's O(n), which is highly efficient  

Why do we care about polynomial multiplication? It is similar to a widely used operation on vectors - convolution.

You can smooth waveform functions through multiplication with another function, or do a transformation of a vector my multiplying with a matrix.

Since coefficient rep is O(n) for for evaluation and addition but O(n^2) for multiplication, and value rep is O(n) for addition and multiplication but O(n^2) for evaluation (?), neither is perfect.

DFT is the transformation from coefficient rep to value rep, but FFT is the fast algorithm for doing so.

Vandermonde matrix formula represents the multiplication of samples for evaluation as an nxn matrix of all x^k evaluated as all samples of x, multiplied by a column vector of coefficients, to get a column vector of y values. This is multiplication using value rep in O(n^2)

To get back to coefficient rep from Vandermonde, we could use Gaussian elimination to get the inverse of the square matrix and multiply it by the column vector on the right hand side, but this is O(n^3). Finding the inverse the "normal" way (through computing the determinant etc) is O(n^2). This is bad, because we lose the benefit of having an O(n) time multiplication method via value rep if it costs O(n) or more to convert first.

### Divide and Conquer

1. Divide

Divide the coefficient rep of the polynomial into odd and even numbered coefficients, so {a0, a2, a4,..} and {a1, a3, a5...} which are themselves polynomials with x^0, x^1, x^2, terms etc.

Time complexity - iterating over the coefficients and performing the basic operation of storing them in new vectors has complexity O(n)

2. Conquer 

Recursively compute A_even(w) and A_odd(w) for al w which are each of the x values squared.

3. Combine 

$A(x) = A_{even}(x^2) + xA_{odd}(x^2)$

Time complexity - If we know each term, then this is constant time since its just 3 basic operations.



EXAMPLE:

- Start with a polynomial of degree n-1 with n terms. Let n be a power of 2. In this case, n=8
- $A(x) = (5,6,2,4,7,3,1,8)$ 
- Split into $A_e(w)=(6,4,3,8)$ and $A_o(w)=(5,2,7,1)$
- Split further into $A_{ee}=(4,8)$, $A_{eo}=(6,3)$ and $A_{oe}=(2,1)$, $A_{oe}=(5,7)$
- $A(x)=(0,6,0,4,0,3,0,8) + (5,0,2,0,7,0,1)$

Although the problem is being broken up into smaller parts, the combined sum of these parts is the same as what we originally had, which isn't really an improvement. We know this because there are $\log_2(n)$ recursions, which leave us with $2^{\log_2(n)}$ coefficients to  work with in the final recursive step, which is just $n$. If we consider how the splitting of the polynomial takes $n$ basic operations at most, then this whole process is still $O(n^2)$

If we can find a way to make the recursion reduce the computations needed, then divide and conquer would be worth pursuing. 

We can take inspiration from merge sort, which is a recursive algorithm whose time complexity is expressed as $T(n)=2T(\frac{n}{2})+O(n)$ which evaluates to $O(n\log(n))$. This comes from the fact there are $log_2(n)$ recursive steps since we are halving the data set at each step, and it takes $n$ steps to deal with each recursion

If we choose our initial values of $x$ carefully before we begin computations, we will be able to reuse some computations and only do half as much. 

One way of doing this is by using roots of unity.

### Overview

Let A and B be vectors for polynomials in coefficient rep. We can compute the polynomials in value rep by running the FFT on each of them, giving A* and B*.

Then, the dot product of these two vectors (the sum of the element-wise products) is C*, the value rep of the product of the two polynomials.

To convert C* to C, its coefficient rep, we need an inverse for the FFT. 

### Inverse FFT

Consider the Vandermonde matrix formula, X.A=Y. Y is the value rep, A is the coefficient rep. So, A=Y.X^-1

But what is the inverse of the Vandermonde matrix, X?

Claim = X^-1 = Conjugate(X)/n

The complex conjugate is just the reciprocal of the exponential form of a complex number, i.e. the negative of the argument.

Proof of claim:

Consider p= X * Conjugate(X) = nI i.e. n times identity matrix



EXAMPLE : Using recursive splitting of polynomials to evaluate at positive-negative pairs of x_k values

$P(x)=x^3+x^2-x-1$
