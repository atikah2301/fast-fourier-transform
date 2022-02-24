# Abstract Algebra - Revision & Further Study

**Definition**: Ring

A set $R$ on which the binary operations of addition and multiplication are defined, under the following axioms:

1. If $a,b,c\in R$, then $a+(b+c)=(a+b)+c$ i.e. addition is associative.
2. There exists an identity for addition, $0$, such that $0+a=a$ and $0+a=a$ $\forall a\in R$.
3.  If $a\in R$, $\exists -a\in R$ such that $a+(-a)=0$ and $(-a)+a=0$ i.e. each element has an additive inverse.
4. If $a,b\in R$, then $a+b=b+a$ i.e. addition is commutative.
5. If $a,b\in R$, then $a\cdot (b\cdot c)=(a\cdot b)\cdot c$ i.e. multiplication is commutative.
6. If $a,b\in R$, then $a\cdot (b\cdot c)=a\cdot b+a\cdot c$ i.e. multiplication is distributive.

Note: Subtraction is defined for a ring conveniently through addition operations and additive inverses.

**Definition**: Commutative Ring

A ring $R(+,\cdot)$ is a commutative ring if its multiplication is commutative 

**Definition**: Ring with Identity

A ring $R(+,\cdot)$ is a ring with identity if:

1.  There exists some element $1\in R$ such that $1\cdot a = a$ and $a\cdot 1 =a$, $\forall a\in R$, i.e. there is an identity for multiplication, and
2. $1\neq0$

**Example**: Integers $mod\, n$, denoted $\Z/n\Z=\{0,1,..,n-1\}$, is a commutative ring with identity



**Definition**: Field

A set $F$ on which addition, subtraction, multiplication, and division is defined. 

In other words, a commutative ring with identity such that if $a\in F$ and $a\ne0$, then there exists $a^{-1}\in F$ where $a\cdot a^{-1}=1$ i.e. each nonzero element has a multiplicative inverse.

**Example**: Integers $mod\, p$, denoted $\Z/p\Z=\{0,1,..,p-1\}$ where $p$ is prime is a field.

This is because $a\in \Z/p\Z$ can only have a multiplicative inverse when $a$ and $p$ are coprime. When $p$ is prime, every nonzero element of $\Z/p\Z$ is coprime to p. 



**Definition**: Ideal

Remark: Ideals are to rings what normal subgroups are to groups 

**Definition**: Characteristic

The characteristic of a ring $R$, denoted $char(R)$, is $n$ where $\sum^n1=0$, i.e. the smallest number of summands of $1$ (the ring's multiplicative identity) needed to get $0$ (the ring's additive identity).

If the sum never reaches $0$, then $char(R)=0$.  

**Theorem**: Characteristic of a Field

The characteristic of any field is either 0 or a prime number (Proof or explanation required...)



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

**Example**: Integers $mod\,n$ in the language of group theory

Let $G$ be the group of integers, $\Z$, under addition. Let $H$ be the subgroup $G$ with elements $n\Z$ for any $n\in \N$. $n\Z$ would be the congruence class for $0\, mod\, n$. Consider the cosets of $G$ formed by adding elements of $G$ from $1$ to $n-1$  to each element of $n\Z$. The union of these disjoint cosets gives us all the elements of $G$.

Since these cosets form a group (adding any of the $n$ cosets gets you one of the $n$ cosets), we call $H$ a normal subgroup of $G$, while the group of cosets is a quotient group, $\Z/n\Z$.

Consider $n=5$ for a more concrete example. The subgroup has elements $5\Z=\{..,-5,0,5,10,..\}$. Consider this and 4 other cosets of $G$ forming their own set, $\Z/5\Z=\{0+5\Z, ..,4+5\Z\}=\{[0]_5,.,[4]_5\}$, i.e.  the congruence classes $mod\, 5$. This set is a group under addition, called a quotient group. This implies that $5\Z$ forms a normal subgroup of the group of integers $\Z$.

Note that the quotient group is NOT a subgroup of $G$ since the cosets are not themselves elements of $G$, they  are sets of some elements of $G$. 



- [ ] Commutative Fields. (e.g. rationals, reals, complex numbers, Z/pZ (integers mod prime),
    - [ ]  More generally, R/P, where R is a ring (see later), and P is a maximal ideal in R (see later.)
- [ ] Commutative Rings with Identity (e.g. integers, the ring F[x] of polynomials with coefficients in a field F)
    - [ ]  R/I, where I is any ideal in the ring R (see later).
- [ ]  Ideal.
- [ ]  Quotient ring.
    - [ ]  f R is a ring and I is an ideal in R, the ring R/I.
- [ ]  Principal ideal
- [ ]  Prime Ideal
- [ ]  Maximal Ideal.
- [ ]  Integral domain.
- [ ]  Euclidean domain.
- [ ]  Principal Ideal domain.
- [ ]  Unique factorisation domain.
- [ ]  Divisor of zero.