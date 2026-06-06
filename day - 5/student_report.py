{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "59e410d9-7673-43d4-a44d-df9eecbd3463",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Yash | Roll No: 1 | Avg: 87.67 | Grade: B | School: ABC School\n",
      "Rahul | Roll No: 2 | Avg: 72.33 | Grade: C | School: ABC School\n",
      "Aman | Roll No: 3 | Avg: 55.00 | Grade: D | School: ABC School\n"
     ]
    }
   ],
   "source": [
    "# Student Report System using OOP\n",
    "\n",
    "class Student:\n",
    "    school_name = \"ABC School\"\n",
    "\n",
    "    def __init__(self, name, roll_no, marks):\n",
    "        self.name = name\n",
    "        self.roll_no = roll_no\n",
    "        self.marks = marks\n",
    "\n",
    "    def average(self):\n",
    "        return sum(self.marks) / len(self.marks)\n",
    "\n",
    "    def grade(self):\n",
    "        avg = self.average()\n",
    "\n",
    "        if avg >= 90:\n",
    "            return \"A\"\n",
    "        elif avg >= 75:\n",
    "            return \"B\"\n",
    "        elif avg >= 60:\n",
    "            return \"C\"\n",
    "        elif avg >= 40:\n",
    "            return \"D\"\n",
    "        else:\n",
    "            return \"F\"\n",
    "\n",
    "    def __str__(self):\n",
    "        return f\"{self.name} | Roll No: {self.roll_no} | Avg: {self.average():.2f} | Grade: {self.grade()} | School: {Student.school_name}\"\n",
    "\n",
    "\n",
    "s1 = Student(\"Yash\", 1, [85, 90, 88])\n",
    "s2 = Student(\"Rahul\", 2, [70, 75, 72])\n",
    "s3 = Student(\"Aman\", 3, [50, 60, 55])\n",
    "\n",
    "print(s1)\n",
    "print(s2)\n",
    "print(s3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5462f1e7-a860-46fd-bfc2-5261a0fbf214",
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
