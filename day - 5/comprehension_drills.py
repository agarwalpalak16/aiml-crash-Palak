{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "43180205-ae98-48a5-a11e-69ee01715a0f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[3, 6, 9, 12, 15, 18]\n",
      "['Apple', 'Elephant', 'Banana']\n",
      "[32.0, 68.0, 86.0, 104.0]\n",
      "[1, 2, 3, 4, 5, 6, 7, 8]\n",
      "{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}\n",
      "{0, 2, 4, 6, 8}\n"
     ]
    }
   ],
   "source": [
    "# List Comprehension Practice\n",
    "\n",
    "numbers = list(range(1, 21))\n",
    "\n",
    "div_by_3 = [x for x in numbers if x % 3 == 0]\n",
    "print(div_by_3)\n",
    "\n",
    "words = [\"apple\", \"cat\", \"elephant\", \"dog\", \"banana\"]\n",
    "long_words = [word.title() for word in words if len(word) > 4]\n",
    "print(long_words)\n",
    "\n",
    "celsius = [0, 20, 30, 40]\n",
    "fahrenheit = [(temp * 9/5) + 32 for temp in celsius]\n",
    "print(fahrenheit)\n",
    "\n",
    "nested = [[1,2],[3,4],[5,6],[7,8]]\n",
    "flat = [num for sublist in nested for num in sublist]\n",
    "print(flat)\n",
    "\n",
    "# Dict comprehension\n",
    "squares = {x: x*x for x in range(5)}\n",
    "print(squares)\n",
    "\n",
    "# Set comprehension\n",
    "even_set = {x for x in range(10) if x % 2 == 0}\n",
    "print(even_set)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5f017fc7-1858-49c4-ab67-7ca7bdd02478",
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
