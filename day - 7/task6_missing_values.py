{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "21c4fbfd-7176-453d-a5c1-adcfa12add3d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Missing Values:\n",
      "Name     1\n",
      "Marks    1\n",
      "dtype: int64\n",
      "\n",
      "Using dropna():\n",
      "   Name  Marks\n",
      "0  Yash   85.0\n",
      "\n",
      "Using fillna():\n",
      "      Name  Marks\n",
      "0     Yash   85.0\n",
      "1     Amit   88.0\n",
      "2  Unknown   91.0\n"
     ]
    }
   ],
   "source": [
    "# task6_missing_values.py\n",
    "\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "\n",
    "data = {\n",
    "    \"Name\": [\"Yash\", \"Amit\", np.nan],\n",
    "    \"Marks\": [85, np.nan, 91]\n",
    "}\n",
    "\n",
    "df = pd.DataFrame(data)\n",
    "\n",
    "print(\"Missing Values:\")\n",
    "print(df.isnull().sum())\n",
    "\n",
    "print(\"\\nUsing dropna():\")\n",
    "print(df.dropna())\n",
    "\n",
    "print(\"\\nUsing fillna():\")\n",
    "filled = df.fillna({\n",
    "    \"Name\": \"Unknown\",\n",
    "    \"Marks\": df[\"Marks\"].mean()\n",
    "})\n",
    "\n",
    "print(filled)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8a964900-940a-4312-946f-cd09b7171ee9",
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
