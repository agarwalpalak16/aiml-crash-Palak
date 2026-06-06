{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "a39b48c1-0636-485c-8211-17459e8634dd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Name    : Yash Dadhich\n",
      "Course  : AI & ML\n",
      "College : Arya College of Engineering & I.T.\n"
     ]
    }
   ],
   "source": [
    "# task1_profile_card.py\n",
    "\n",
    "from typing import Dict\n",
    "\n",
    "student = {\n",
    "    \"name\": \"Yash Dadhich\",\n",
    "    \"course\": \"AI & ML\",\n",
    "    \"college\": \"Arya College of Engineering & I.T.\"\n",
    "}\n",
    "\n",
    "def create_profile(profile: Dict[str, str]) -> str:\n",
    "    return (\n",
    "        f\"Name    : {profile['name']}\\n\"\n",
    "        f\"Course  : {profile['course']}\\n\"\n",
    "        f\"College : {profile['college']}\"\n",
    "    )\n",
    "\n",
    "print(create_profile(student))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c0559aa9-eeac-4b50-8886-4624d0763717",
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
