{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "fe5b4cce-ee8d-4fad-adaa-602dfd166eb7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Yash is learning Python\n"
     ]
    }
   ],
   "source": [
    "# task3_class.py\n",
    "\n",
    "class Learner:\n",
    "    def __init__(self, name, course):\n",
    "        self.name = name\n",
    "        self.course = course\n",
    "\n",
    "    def get_details(self):\n",
    "        return f\"{self.name} is learning {self.course}\"\n",
    "\n",
    "student = Learner(\"Yash\", \"Python\")\n",
    "\n",
    "print(student.get_details())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2cef2115-0143-4d62-8716-0f4c3df66d2e",
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
