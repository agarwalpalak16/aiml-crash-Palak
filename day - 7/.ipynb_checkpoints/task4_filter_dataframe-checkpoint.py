{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "c6a26d42-1402-4299-8325-886a15bbcaf3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   Name  Marks\n",
      "0  Yash     85\n",
      "2  Riya     91\n",
      "\n",
      "Filter Applied:\n",
      "Showing students with marks greater than 75.\n"
     ]
    }
   ],
   "source": [
    "# task4_filter_dataframe.py\n",
    "\n",
    "import pandas as pd\n",
    "\n",
    "data = {\n",
    "    \"Name\": [\"Yash\", \"Amit\", \"Riya\", \"Karan\"],\n",
    "    \"Age\": [21, 20, 22, 21],\n",
    "    \"Marks\": [85, 72, 91, 65]\n",
    "}\n",
    "\n",
    "df = pd.DataFrame(data)\n",
    "\n",
    "filtered = df[[\"Name\", \"Marks\"]]\n",
    "\n",
    "result = filtered[df[\"Marks\"] > 75]\n",
    "\n",
    "print(result)\n",
    "\n",
    "print(\"\\nFilter Applied:\")\n",
    "print(\"Showing students with marks greater than 75.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e87f58bb-2a6b-4395-b4a4-8b2f1580bff5",
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
