{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "63a7e24f-a780-46c8-bcec-6e3e7a79a141",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "8\n",
      "5.0\n",
      "8\n",
      "1\n"
     ]
    }
   ],
   "source": [
    "# Calculator with Type Hints\n",
    "\n",
    "from typing import Optional\n",
    "\n",
    "def add(a: float, b: float) -> float:\n",
    "    \"\"\"Returns addition\"\"\"\n",
    "    return a + b\n",
    "\n",
    "def subtract(a: float, b: float) -> float:\n",
    "    \"\"\"Returns subtraction\"\"\"\n",
    "    return a - b\n",
    "\n",
    "def multiply(a: float, b: float) -> float:\n",
    "    \"\"\"Returns multiplication\"\"\"\n",
    "    return a * b\n",
    "\n",
    "def divide(a: float, b: float) -> Optional[float]:\n",
    "    \"\"\"Returns division result\"\"\"\n",
    "    if b == 0:\n",
    "        return None\n",
    "    return a / b\n",
    "\n",
    "def power(base: float, exp: float) -> float:\n",
    "    \"\"\"Returns power value\"\"\"\n",
    "    return base ** exp\n",
    "\n",
    "def modulo(a: int, b: int) -> int:\n",
    "    \"\"\"Returns modulo\"\"\"\n",
    "    if b == 0:\n",
    "        return 0\n",
    "    return a % b\n",
    "\n",
    "print(add(5, 3))\n",
    "print(divide(10, 2))\n",
    "print(power(2, 3))\n",
    "print(modulo(10, 3))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3d8b8c3b-8d41-46af-94b2-bdc0fd1c437b",
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
