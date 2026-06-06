{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "1874f4ba-c3a7-433c-b51c-608c1a957bdd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Describe Output:\n",
      "           Marks\n",
      "count   5.000000\n",
      "mean   84.000000\n",
      "std     9.617692\n",
      "min    70.000000\n",
      "25%    80.000000\n",
      "50%    85.000000\n",
      "75%    90.000000\n",
      "max    95.000000\n",
      "\n",
      "Value Counts:\n",
      "Department\n",
      "AI    3\n",
      "CS    2\n",
      "Name: count, dtype: int64\n",
      "\n",
      "Observation:\n",
      "Average marks are above 80.\n",
      "AI department has the highest number of students.\n"
     ]
    }
   ],
   "source": [
    "# task7_insights.py\n",
    "\n",
    "import pandas as pd\n",
    "\n",
    "data = {\n",
    "    \"Department\": [\"AI\", \"AI\", \"CS\", \"CS\", \"AI\"],\n",
    "    \"Marks\": [80, 90, 70, 85, 95]\n",
    "}\n",
    "\n",
    "df = pd.DataFrame(data)\n",
    "\n",
    "print(\"Describe Output:\")\n",
    "print(df.describe())\n",
    "\n",
    "print(\"\\nValue Counts:\")\n",
    "print(df[\"Department\"].value_counts())\n",
    "\n",
    "print(\"\\nObservation:\")\n",
    "print(\"Average marks are above 80.\")\n",
    "print(\"AI department has the highest number of students.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "28a00835-ed27-4c1d-8df6-11ce74add79d",
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
