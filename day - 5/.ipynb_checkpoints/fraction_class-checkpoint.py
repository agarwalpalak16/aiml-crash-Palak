{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "240883e1-fe56-45ca-9322-582db60e419e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1/1\n",
      "True\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "# Fraction Class using Dunder Methods\n",
    "\n",
    "import math\n",
    "\n",
    "class Fraction:\n",
    "    def __init__(self, numerator, denominator):\n",
    "        self.numerator = numerator\n",
    "        self.denominator = denominator\n",
    "\n",
    "    def simplify(self):\n",
    "        gcd = math.gcd(self.numerator, self.denominator)\n",
    "        return Fraction(\n",
    "            self.numerator // gcd,\n",
    "            self.denominator // gcd\n",
    "        )\n",
    "\n",
    "    def __str__(self):\n",
    "        return f\"{self.numerator}/{self.denominator}\"\n",
    "\n",
    "    def __add__(self, other):\n",
    "        num = (self.numerator * other.denominator) + (other.numerator * self.denominator)\n",
    "        den = self.denominator * other.denominator\n",
    "        return Fraction(num, den).simplify()\n",
    "\n",
    "    def __eq__(self, other):\n",
    "        return (\n",
    "            self.numerator * other.denominator ==\n",
    "            other.numerator * self.denominator\n",
    "        )\n",
    "\n",
    "    def __lt__(self, other):\n",
    "        return (\n",
    "            self.numerator * other.denominator <\n",
    "            other.numerator * self.denominator\n",
    "        )\n",
    "\n",
    "f1 = Fraction(1, 2)\n",
    "f2 = Fraction(2, 4)\n",
    "\n",
    "print(f1 + f2)\n",
    "print(f1 == f2)\n",
    "print(f1 < Fraction(3, 4))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5fdfbaba-0681-4ebe-bc6e-599857ec597b",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
