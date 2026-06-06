{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "e4816490-10ed-46bc-9301-7a0106709712",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Using loc:\n",
      "Name     Amit\n",
      "Marks      72\n",
      "Name: 1, dtype: object\n",
      "\n",
      "Using iloc:\n",
      "Name     Amit\n",
      "Marks      72\n",
      "Name: 1, dtype: object\n",
      "\n",
      "Difference:\n",
      "loc uses labels, iloc uses index positions.\n"
     ]
    }
   ],
   "source": [
    "# task5_loc_iloc.py\n",
    "\n",
    "import pandas as pd\n",
    "\n",
    "data = {\n",
    "    \"Name\": [\"Yash\", \"Amit\", \"Riya\"],\n",
    "    \"Marks\": [85, 72, 91]\n",
    "}\n",
    "\n",
    "df = pd.DataFrame(data)\n",
    "\n",
    "print(\"Using loc:\")\n",
    "print(df.loc[1, [\"Name\", \"Marks\"]])\n",
    "\n",
    "print(\"\\nUsing iloc:\")\n",
    "print(df.iloc[1, [0, 1]])\n",
    "\n",
    "print(\"\\nDifference:\")\n",
    "print(\"loc uses labels, iloc uses index positions.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2238b0f4-b7f9-4a89-bade-96a68b8a80a9",
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
