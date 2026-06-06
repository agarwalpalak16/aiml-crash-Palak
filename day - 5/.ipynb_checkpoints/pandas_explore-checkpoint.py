{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "b8506a43-ae54-435f-be0d-24669ef910ae",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  name    city  math_score  science_score  english_score\n",
      "0    A  Jaipur          90             85             88\n",
      "1    B   Delhi          80             70             75\n",
      "2    C  Jaipur          76             80             82\n",
      "3    D  Mumbai          88             90             85\n",
      "4    E   Delhi          67             72             70\n",
      "math_score       82.5\n",
      "science_score    80.6\n",
      "english_score    80.6\n",
      "dtype: float64\n",
      "name                  F\n",
      "city             Mumbai\n",
      "math_score           95\n",
      "science_score        89\n",
      "english_score        92\n",
      "total               276\n",
      "Name: 5, dtype: object\n",
      "city\n",
      "Jaipur    3\n",
      "Delhi     3\n",
      "Mumbai    2\n",
      "Pune      2\n",
      "Name: count, dtype: int64\n",
      "  name    city  math_score  science_score  english_score  total\n",
      "0    A  Jaipur          90             85             88    263\n",
      "1    B   Delhi          80             70             75    225\n",
      "2    C  Jaipur          76             80             82    238\n",
      "3    D  Mumbai          88             90             85    263\n",
      "5    F  Mumbai          95             89             92    276\n",
      "6    G    Pune          78             76             74    228\n",
      "7    H    Pune          85             84             80    249\n",
      "8    I  Jaipur          92             91             89    272\n",
      "  name    city  math_score  science_score  english_score  total\n",
      "5    F  Mumbai          95             89             92    276\n",
      "8    I  Jaipur          92             91             89    272\n",
      "0    A  Jaipur          90             85             88    263\n"
     ]
    }
   ],
   "source": [
    "# Pandas Data Exploration\n",
    "\n",
    "import pandas as pd\n",
    "\n",
    "data = {\n",
    "    \"name\": [\"A\",\"B\",\"C\",\"D\",\"E\",\"F\",\"G\",\"H\",\"I\",\"J\"],\n",
    "    \"city\": [\"Jaipur\",\"Delhi\",\"Jaipur\",\"Mumbai\",\"Delhi\",\"Mumbai\",\"Pune\",\"Pune\",\"Jaipur\",\"Delhi\"],\n",
    "    \"math_score\": [90,80,76,88,67,95,78,85,92,74],\n",
    "    \"science_score\": [85,70,80,90,72,89,76,84,91,69],\n",
    "    \"english_score\": [88,75,82,85,70,92,74,80,89,71]\n",
    "}\n",
    "\n",
    "df = pd.DataFrame(data)\n",
    "\n",
    "print(df.head())\n",
    "\n",
    "print(df[[\"math_score\",\"science_score\",\"english_score\"]].mean())\n",
    "\n",
    "df[\"total\"] = df[\"math_score\"] + df[\"science_score\"] + df[\"english_score\"]\n",
    "\n",
    "print(df.loc[df[\"total\"].idxmax()])\n",
    "\n",
    "print(df[\"city\"].value_counts())\n",
    "\n",
    "print(df[df[\"math_score\"] > 75])\n",
    "\n",
    "print(df.nlargest(3, \"total\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b6370032-3dc9-41c4-b4ee-4a4548e58703",
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
