# Abstract Algebra - Revision & Further Study



## Group Theory

**Definition**: Group

A group is a set $G$ with a binary operation, denoted as "$\cdot$",  such that if $a,b\in G$ then $a\cdot b \in G$, and such that the following axioms hold:

1. The binary operation is associative
2. There exists an identity element in $G$
3. Every element of $G$ has an inverse in $G$

**Definition**: Order of a Group

The order of a group $G$ is the number of elements in $G$, denoted as $|G|$.

**Theorem**: Lagrange's Theorem

If $H$ and $G$ are both groups, and $H\le G$, then $|H|$ divides $|G|$. 

Note: This places a useful restriction on what the order of a subgroup can be. The theorem only applies to finite groups.

**Definition**: Coset

Let $G$ be an abelian group, let $H$ be a subgroup of $G$. A coset of $G$ is the set of all $g\cdot h$ for some $g\in G$ and for all $h\in H$. In other words, a coset is set of all values obtained from combining each element of a subgroup by an element chosen from the group containing the subgroup. 

Note: For a non-abelian group, we distinguish between left and right cosets depending on the order of $h$ and $g$ in the operation

**Definition**: Normal Subgroups

A normal subgroup, $N$, is a subgroup of group $G$ such that:

1. Elements of $N$ can be partitioned into cosets of $G$ 
2. These cosets form a group.
3. $g\cdot N\cdot g^{-1}=N\,\,\forall \,g\in G$ ([Proof](https://youtu.be/vYKdh5oQ4Zw?t=327))

**Definition**: Quotient Group (or Factor Group)

A quotient group, $G/N$, of group $G$ and its normal subgroup $N$, is a group of cosets based on $G$ and $N$ which can partition $G$. 

**Example**: Integers $\mod n$ in the language of group theory

Let $G$ be the group of integers, $\Z$, under addition. Let $H$ be the subgroup $G$ with elements $n\Z$ for any $n\in \N$. $n\Z$ would be the congruence class for $0\, \mod\, n$. Consider the cosets of $G$ formed by adding elements of $G$ from $1$ to $n-1$  to each element of $n\Z$. The union of these disjoint cosets gives us all the elements of $G$.

Since these cosets form a group (adding any of the $n$ cosets gets you one of the $n$ cosets), we call $H$ a normal subgroup of $G$, while the group of cosets is a quotient group, $\Z/n\Z$.

Consider $n=5$ for a more concrete example. The subgroup has elements $5\Z=\{..,-5,0,5,10,..\}$. Consider this and 4 other cosets of $G$ forming their own set, $\Z/5\Z=\{0+5\Z, ..,4+5\Z\}=\{[0]_5,.,[4]_5\}$, i.e.  the congruence classes $\mod\, 5$. This set is a group under addition, called a quotient group. This implies that $5\Z$ forms a normal subgroup of the group of integers $\Z$.

Note that the quotient group is NOT a subgroup of $G$ since the cosets are not themselves elements of $G$, they  are sets of some elements of $G$. 



## Ring Theory

**Definition**: Ring

A set $R$ on which the binary operations of addition and multiplication are defined, under the following axioms:

- (A0) - If $a,b\in R$, then $a + b \in R$ i.e. addition is closed
- (A1) - If $a,b,c\in R$, then $a+(b+c)=(a+b)+c$ i.e. addition is associative.
- (A2) - If $a,b\in R$, then $a+b=b+a$ i.e. addition is commutative.
- (A3) - There exists $0 \in R$, such that $0+a=a$ and $0+a=a$ $\forall a\in R$ i.e. additive identity.
- (A4) - If $a\in R$, $\exists -a\in R$ such that $a+(-a)=(-a)+a=0$ i.e. additive inverses for all elements.
- (D1) - If $a,b\in R$, then $a\cdot (b+c)=a\cdot b+a\cdot c$ and $a$ i.e. operations are distributive from the left.
- (D2) - If $a,b\in R$, then $(a+b)\cdot c=a\cdot c+b\cdot c$ and $a$ i.e. operations are distributive from the right.
- (M0) - If $a,b\in R$, then $a\cdot b \in R$ i.e. multiplication is closed.
- (M1) - If $a,b\in R$, then $a\cdot (b\cdot c)=(a\cdot b)\cdot c$ i.e. multiplication is associative.

Note: Subtraction is defined trivially through addition operations and additive inverses.

Further types of rings may satisfy these further axioms:

- (M2) - If $a,b\in R$, then $a\cdot b=b\cdot a$ i.e. multiplication is commutative.
- (M3) - There exists $1 \in R$, such that $1\cdot a=a\cdot 1$  $\forall a\in R$ i.e. multiplicative identity.
    - (M3.1) - $1\ne 0$ unless the ring is the trivial ring
- (M4) - If $a\in R\setminus\{0\}$, $\exists\, a^-\in R$ such that $a\cdot a^-=a^-\cdot a=1$ i.e. multiplicative inverses for all elements.
- (M5) - If $a,b\in R$ and $a\cdot b=0$ then $a=0$ or $b=0$ or both. i.e. no zero divisors.
    - This is the defining property of integral domains
    - It is a vital for solving polynomials by factorising e.g. When we solve $x^2-4=0$, we factorise the left side into $(x+2)(x-2)=0$ and then assume that either of the factors must be zero in order for the right side to be 0. 
    - This property may not hold under modular arithmetic, e.g. $3\cdot 4 \equiv0 \mod 12$, hence the term "zero divisors", because here 3 and 4 can "divide" 0 to get something that isn't 0.

Such rings are:

- Commutative ring - (M2)
- Ring with 1 - (M3)
- Commutative ring with 1 - (M2), (M3)
- Division ring - (M3), (M4), (M5) - has multiplicative identity and inverses
- Integral domain - (M2), (M3), (M5) - commutative ring with 1 and without zero divisors
- Field - (M2), (M3), (M4), (M5) - has multiplicative identity and inverses, and is commutative

Note: Some sources will assume rings have identity. For clarity, assume they don't unless specified.

**Example**: Integers $\mod\, p$, denoted $\Z/p\Z=\{0,1,..,p-1\}$ where $p$ is prime is a field.

This is because $a\in \Z/p\Z$ can only have a multiplicative inverse when $a$ and $p$ are coprime. When $p$ is prime, every nonzero element of $\Z/p\Z$ is coprime to p. 

In being a field, it is also an integral domain, a division ring, and a commutative ring with 1, since these are all special cases of a field (sub rings?).

**Definition**: Ideal & Quotient Ring

An ideal is some subset of elements of a ring for which its cosets can partition elements of the ring and form a new ring, the quotient ring.

To identify whether a subset of a ring is an ideal, its elements must:

- From a subgroup of the ring
- Be closed under multiplication with elements from the ring not in the subset

Every ring had the trivial ring and itself as ideals.

Remark: Ideals are related to rings in a similar way that normal subgroups are related to groups. However, ideals are NOT subrings of a ring since they do not contain a multiplicative identity.

Note: For the sake of simplicity, consider only two-sided ideals (since the goal of this study is to look at polynomials, which are typically commutative rings)

**Example**: Consider the ring of integers, $\Z$. For any integer $n$, an ideal of $\Z$ would be $n\Z$. Let $n=2$. Any two even numbers added or multiplied together in any order give an even number (so, this is a subgroup closed under addition and multiplication). Multiplying an even integer by any other integer in $\Z$ gives a

**Example**: Consider the ring $\Z[x]$, polynomials with integer coefficients, and the set, $I=x\cdot\Z[x]$, i.e. all polynomials with its constant term as 0. Is $I$ an ideal?

- First, check if $I$ is a subgroup of the ring:
    - Associative and commutative properties are inherited from the ring
    - It has an additive identity since we know $0\in I$
    - It must be closed under addition since adding any two polynomials in $I$ could never give us a polynomial with a non-zero constant term, since $0+0=0$
    - Multiplying any such polynomial by $-1$ would give a constant term $0\cdot -1 = 0$ so additive inverses are also in $I$
    - So, $I$ is a subgroup
- Now, we need to show that for all $f(x)\in \Z[x]$ and $j(x)\in J$, their two-sided product is in $J$.
    - Since the ring is commutative under addition, $f(x)\cdot j(x) = j(x) \cdot f(x)$ 
    - Consider $j(x) = x\cdot  k(x)$, so, $f(x) \cdot j(x) = x \cdot f(x) \cdot k(x)$  (distributive property), and since we know the ring is closed under multiplication, that means $f(x)\cdot k(x)$ is in the ring, and multiplying it by $x$ would make it an element of $I$ by its definition.

Therefore, it is an ideal.

**Definition**: Principal Ideal

The principal ideal of $R$, a commutative ring with 1, generated by $a\in R$ is $(a)=\{ar|r\in R\}=Ra$ 

**Theorem**: $(a)=R \iff a\in R$ is a unit (an element with a multiplicative inverse)

**Proof**: First proving from left to right: since $R$ is a ring with 1, $(a)$ must have 1, so $ar=1$ for some $r\in R$, which by definition makes $r$ the multiplicative inverse of $a$, so $a$ is a unit.

Now proving from right to left: since $a$ is a unit, that means there is some $r \in R$ for which $ar=1$, meaning $1\in (a)$. This means any element of $R$, say $b\in R$, would be in $(a)$ since $b=b\cdot 1 \in (a)$ due to the absorption property of ideals.

**Example**: The ideal $(2)$ for the ring $\Z_{15}$ i.e. integers mod 15, is $\{0,2,4,..,14,1,3,..13\}$. 2 is the unit since $2\cdot 8 \equiv 1 \mod 15$.

**Definition**: Principal Ideal Domain

A ring for which every ideal of the ring is a principal ideal.

**Example**: The ring of integers is a PID. Every ideal of the ring has the form $n\Z$. If we take smallest positive element of this ideal, it would be $n$. $(n)$ would be principle ideal generated by $n$, which is itself $n\Z$. So every ideal of the integers is a principle ideal, so the ring is a principal ideal domain.



**Definition**: Irreducible

An element $p$ of an integral domain $D$ is irreducible if when $p=ab$, either $a$ or $b$ is a unit of $D$ (analogous to being prime, and the uniqueness of prime factorisations i.e. Fundamental Theorem of Arithmetic).

**Definition**: Unique Factorisation Domain

An integral domain $D$ is a UFD if:

- Every non-zero non-unit of $D$ can be written as the product of irreducible elements of $D$
- For any $a\in D$ with factorisations $a=p_1 \cdot ... p_r =q_1 \cdot ... q_s$$r=s$, we have that:
    -  $r=s$ (so, the number of factors in each factorisation is the same), and
    - There ex



**Definition**: Euclidian Domain

Any integral domain with a Euclidian function that maps all elements to a natural number is a Euclidian domain.

**Theorem**: Every Euclidian domain is a principal ideal domain 



**Definition**: Characteristic

The characteristic of a ring $R$, denoted $char(R)$, is $n$ where $\sum^n1=0$, i.e. the smallest number of summands of $1$ (the ring's multiplicative identity) needed to get $0$ (the ring's additive identity).

If the sum never reaches $0$, then $char(R)=0$.  

**Theorem**: Characteristic of a Field

The characteristic of any field is either 0 or a prime number (Proof or explanation required...)





## Checklist  

- [x] Commutative Fields. (e.g. rational numbers, real numbers, complex numbers, $\Z/p\Z$ (integers mod prime),
- [x] Commutative Rings with Identity (e.g. integers, the ring F[x] of polynomials with coefficients in a field 
- [x] Fields and integral domains
- [x] Ideals and Quotient rings
- [x] Principal ideal
- [ ] Prime Ideal
- [ ] Maximal Ideal.
- [ ] Euclidean domain.
- [x] Principal Ideal domain.
- [x] Unique factorisation domain.
- [x] Divisor of zero.





