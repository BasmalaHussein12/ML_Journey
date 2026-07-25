# Linear Algebra Notes

**Book:** Mathematics for Machine Learning

---

# Session 01

**Date:** July 26, 2026

## Topics Covered

- What is Linear Algebra?
- Vectors
- Systems of Linear Equations
- Matrices
- Matrix Addition
- Matrix Multiplication
- Identity Matrix
- Matrix Inverse
- Matrix Transpose
- Scalar Multiplication
- Matrix Form of Linear Systems (Ax = b)

---

# 1. What is Linear Algebra?

Linear Algebra is the branch of mathematics that studies vectors, matrices, and the mathematical rules used to manipulate them.

Instead of solving one equation at a time, Linear Algebra provides tools to solve many equations simultaneously.

It is one of the mathematical foundations of Machine Learning.

---

# 2. What is a Vector?

A vector is an object that can

- be added to another vector
- be multiplied by a scalar

Examples of vectors include

- Geometric vectors
- Polynomials
- Audio signals
- Elements of Rⁿ

The most common representation in Machine Learning is a vector of numbers.

Example

x = [1, 2, 3]ᵀ

---

## Why Are Vectors Important?

Vectors allow us to represent almost any kind of data.

Examples

- Image
- Audio
- Student information
- House information
- Text embeddings

---

# 3. Systems of Linear Equations

Example

x₁ + x₂ + x₃ = 3

x₁ − x₂ + 2x₃ = 2

x₂ + x₃ = 2

The objective is to find values of x₁, x₂ and x₃ that satisfy all equations simultaneously.

---

## Possible Outcomes

A system of linear equations has

- No solution
- One unique solution
- Infinitely many solutions

---

## Geometric Interpretation

Two variables

→ Every equation represents a line.

Possible intersections

- One point
- No intersection
- Same line

Three variables

→ Every equation represents a plane.

Possible intersections

- Point
- Line
- Plane
- No common intersection

---

# 4. Matrices

A matrix is a rectangular arrangement of numbers.

Example

|1 2 3|
|4 5 6|

Rows = horizontal

Columns = vertical

Matrix size is always

Rows × Columns

Example

2 × 3 matrix

---

## Matrix Element Notation

aᵢⱼ

First index → Row

Second index → Column

Example

a₂₃

means

Row 2

Column 3

---

# 5. Matrix Addition

Matrices are added element by element.

Example

A

|1 2|

|3 4|

-

B

|5 6|

|7 8|

=

|6 8|

|10 12|

Matrices must have the same dimensions.

---

# 6. Matrix Multiplication

Matrix multiplication is NOT element-wise multiplication.

To calculate one element of the product

- Take one row from the first matrix
- Take one column from the second matrix
- Multiply corresponding elements
- Sum the products

---

## Dimension Rule

If

A is m × n

B is n × k

Then

AB exists

and its size is

m × k

The inner dimensions must match.

---

## Important

Generally

AB ≠ BA

Matrix multiplication is NOT commutative.

---

# 7. Identity Matrix

The identity matrix behaves like the number 1.

Example

I₂

|1 0|

|0 1|

Property

AI = IA = A

---

# 8. Matrix Inverse

The inverse of a matrix undoes the original matrix.

If

AA⁻¹ = I

then

A⁻¹ is called the inverse of A.

Not every matrix has an inverse.

If the determinant is zero, the matrix is not invertible.

---

# 9. Matrix Transpose

The transpose swaps rows and columns.

Example

|1 2 3|

|4 5 6|

↓

|1 4|

|2 5|

|3 6|

Notation

Aᵀ

---

## Symmetric Matrix

A matrix is symmetric if

A = Aᵀ

Example

|1 2|

|2 3|

---

# 10. Scalar Multiplication

A scalar is a single number.

Multiplying a matrix by a scalar multiplies every element by that number.

Example

3

×

|1 2|

|3 4|

=

|3 6|

|9 12|

---

# 11. Compact Representation of Linear Systems

Instead of writing many equations

we write

Ax = b

where

A → coefficient matrix

x → unknown vector

b → output vector

This notation is used throughout Machine Learning.

---

# Machine Learning Connections

Linear Algebra appears in

- Linear Regression
- Logistic Regression
- Principal Component Analysis (PCA)
- Neural Networks
- Computer Vision
- Natural Language Processing
- Recommender Systems

Almost every ML algorithm represents data as vectors and matrices.

---

# Research Notes

A researcher rarely asks

"How do I solve this equation?"

Instead, they ask

- What does this matrix represent?
- What do the rows represent?
- What do the columns represent?
- What are the unknown variables?
- Why is this mathematical model useful?

Thinking in this way develops mathematical intuition for research.

---

# Key Takeaways

- Vectors represent data.
- Matrices organize vectors.
- Matrix multiplication combines information across rows and columns.
- The identity matrix behaves like 1.
- The inverse undoes a matrix.
- The transpose swaps rows and columns.
- Most Machine Learning algorithms are built on Ax = b.
