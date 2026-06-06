{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "7e2e057e-e642-4715-aead-407c16f742be",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Array 1: [10 20 30 40 50]\n",
      "Shape: (5,)\n",
      "Dtype: int64\n",
      "Dimensions: 1\n",
      "\n",
      "Array 2: [ 1  2  3  4  5  6  7  8  9 10]\n",
      "Shape: (10,)\n",
      "Dtype: int64\n",
      "Dimensions: 1\n",
      "\n",
      "Negative Index:\n",
      "50\n",
      "\n",
      "Slice:\n",
      "[3 4 5 6 7]\n"
     ]
    }
   ],
   "source": [
    "# task8_numpy_basics.py\n",
    "\n",
    "import numpy as np\n",
    "\n",
    "arr1 = np.array([10, 20, 30, 40, 50])\n",
    "\n",
    "arr2 = np.arange(1, 11)\n",
    "\n",
    "print(\"Array 1:\", arr1)\n",
    "print(\"Shape:\", arr1.shape)\n",
    "print(\"Dtype:\", arr1.dtype)\n",
    "print(\"Dimensions:\", arr1.ndim)\n",
    "\n",
    "print(\"\\nArray 2:\", arr2)\n",
    "print(\"Shape:\", arr2.shape)\n",
    "print(\"Dtype:\", arr2.dtype)\n",
    "print(\"Dimensions:\", arr2.ndim)\n",
    "\n",
    "print(\"\\nNegative Index:\")\n",
    "print(arr1[-1])\n",
    "\n",
    "print(\"\\nSlice:\")\n",
    "print(arr2[2:7])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b2e89673-458c-4143-b921-0b9aded5d734",
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
