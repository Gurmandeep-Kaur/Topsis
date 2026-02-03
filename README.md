# Topsis
This repository contains the complete implementation of TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)

---

## 1. What is TOPSIS?

TOPSIS stands for **Technique for Order Preference by Similarity to Ideal Solution**.  
It is a multi-criteria decision-making method used to rank alternatives when multiple criteria are involved.

The basic idea of TOPSIS is:
- The best alternative should be closest to the ideal best solution
- The best alternative should be farthest from the ideal worst solution

Each alternative is evaluated based on several criteria, and each criterion can either be:
- Beneficial (higher value is better), or
- Non-beneficial (lower value is better)

---

## Steps Involved in TOPSIS

1. Construct the decision matrix from the input data
2. Normalize the decision matrix
3. Multiply each column by its corresponding weight
4. Determine the ideal best and ideal worst values
5. Calculate the distance of each alternative from the ideal best and ideal worst
6. Compute the TOPSIS score
7. Rank the alternatives based on the TOPSIS score

The alternative with the highest TOPSIS score is ranked first.

---

## 2. Topsis Package

The complete package can be accessed at https://pypi.org/project/Topsis-Gurmandeep-102303764/

---

## 3. Topsis Web Service

The folder Topsis-Web-Service contains a web-based interface built using Flask. The web layer does not reimplement TOPSIS logic.
All computations and validations are handled by the existing package. Actual email credentials are not included in the repository.

---

## Author

Gurmandeep Kaur

---
