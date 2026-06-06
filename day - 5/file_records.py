{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "1d2166de-2d10-4d83-a2de-1ef9f17fb5c5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "results.csv created successfully\n"
     ]
    }
   ],
   "source": [
    "# CSV File Handling\n",
    "\n",
    "import csv\n",
    "\n",
    "students = [\n",
    "    [\"Yash\", 90, 85, 88],\n",
    "    [\"Rahul\", 70, 75, 72],\n",
    "    [\"Aman\", 60, 65, 68]\n",
    "]\n",
    "\n",
    "with open(\"students.csv\", \"w\", newline=\"\") as file:\n",
    "    writer = csv.writer(file)\n",
    "    writer.writerow([\"name\", \"math\", \"science\", \"english\"])\n",
    "    writer.writerows(students)\n",
    "\n",
    "results = []\n",
    "\n",
    "with open(\"students.csv\", \"r\") as file:\n",
    "    reader = csv.DictReader(file)\n",
    "\n",
    "    for row in reader:\n",
    "        avg = (\n",
    "            int(row[\"math\"]) +\n",
    "            int(row[\"science\"]) +\n",
    "            int(row[\"english\"])\n",
    "        ) / 3\n",
    "\n",
    "        grade = \"A\" if avg >= 80 else \"B\"\n",
    "\n",
    "        results.append({\n",
    "            \"name\": row[\"name\"],\n",
    "            \"average\": avg,\n",
    "            \"grade\": grade\n",
    "        })\n",
    "\n",
    "with open(\"results.csv\", \"w\", newline=\"\") as file:\n",
    "    fieldnames = [\"name\", \"average\", \"grade\"]\n",
    "\n",
    "    writer = csv.DictWriter(file, fieldnames=fieldnames)\n",
    "    writer.writeheader()\n",
    "    writer.writerows(results)\n",
    "\n",
    "print(\"results.csv created successfully\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "15b3dfbe-6394-4f0c-aeff-4197aacb0346",
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
