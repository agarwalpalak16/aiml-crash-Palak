{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "f3a80e05-872f-4396-8589-428117c0beb1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Masked Values:\n",
      "[30 40 50]\n",
      "\n",
      "Broadcasting Result:\n",
      "[15 25 35 45 55]\n",
      "\n",
      "Cosine Similarity Pair 1:\n",
      "0.9746318461970762\n",
      "\n",
      "Cosine Similarity Pair 2:\n",
      "0.0\n"
     ]
    }
   ],
   "source": [
    "# task9_numpy_advanced.py\n",
    "\n",
    "import numpy as np\n",
    "\n",
    "arr = np.array([10, 20, 30, 40, 50])\n",
    "\n",
    "mask = arr > 25\n",
    "print(\"Masked Values:\")\n",
    "print(arr[mask])\n",
    "\n",
    "broadcasted = arr + 5\n",
    "print(\"\\nBroadcasting Result:\")\n",
    "print(broadcasted)\n",
    "\n",
    "def cosine_similarity(v1, v2):\n",
    "    dot_product = np.dot(v1, v2)\n",
    "\n",
    "    norm_v1 = np.linalg.norm(v1)\n",
    "    norm_v2 = np.linalg.norm(v2)\n",
    "\n",
    "    return dot_product / (norm_v1 * norm_v2)\n",
    "\n",
    "vector1 = np.array([1, 2, 3])\n",
    "vector2 = np.array([4, 5, 6])\n",
    "\n",
    "vector3 = np.array([1, 0, 0])\n",
    "vector4 = np.array([0, 1, 0])\n",
    "\n",
    "print(\"\\nCosine Similarity Pair 1:\")\n",
    "print(cosine_similarity(vector1, vector2))\n",
    "\n",
    "print(\"\\nCosine Similarity Pair 2:\")\n",
    "print(cosine_similarity(vector3, vector4))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "94e68496-5aec-45fe-8f5d-46e57cfde1b1",
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
