{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "1d0597b7-c7b3-44c2-ae56-ee3910567a4b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Name   : Yash Dadhich\n",
      "Role   : Student\n",
      "Skills : PYTHON, PANDAS, NUMPY\n"
     ]
    }
   ],
   "source": [
    "import json\n",
    "\n",
    "with open(\"data.json\", \"r\") as file:\n",
    "    data = json.load(file)\n",
    "\n",
    "skills = [skill.upper() for skill in data[\"skills\"]]\n",
    "\n",
    "print(f\"Name   : {data['name']}\")\n",
    "print(f\"Role   : {data['role']}\")\n",
    "print(f\"Skills : {', '.join(skills)}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6cd2729a-fb10-4193-bbee-021adad7e536",
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
