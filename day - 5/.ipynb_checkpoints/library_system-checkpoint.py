{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "ec942ca1-fd97-42f9-85de-b785e73d46cf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Python by John (2020) - 300 pages\n",
      "AI Basics by Sam (2021) - 250 pages\n",
      "ML Guide by Alex (2022) - 5MB\n",
      "Data Science by David (2023) - 8MB\n"
     ]
    }
   ],
   "source": [
    "# Library Management using Inheritance\n",
    "\n",
    "class LibraryItem:\n",
    "    def __init__(self, title, author, year):\n",
    "        self.title = title\n",
    "        self.author = author\n",
    "        self.year = year\n",
    "\n",
    "    def describe(self):\n",
    "        return f\"{self.title} by {self.author} ({self.year})\"\n",
    "\n",
    "\n",
    "class Book(LibraryItem):\n",
    "    def __init__(self, title, author, year, pages):\n",
    "        super().__init__(title, author, year)\n",
    "        self.pages = pages\n",
    "\n",
    "    def describe(self):\n",
    "        return f\"{super().describe()} - {self.pages} pages\"\n",
    "\n",
    "\n",
    "class EBook(LibraryItem):\n",
    "    def __init__(self, title, author, year, file_size_mb):\n",
    "        super().__init__(title, author, year)\n",
    "        self.file_size_mb = file_size_mb\n",
    "\n",
    "    def describe(self):\n",
    "        return f\"{super().describe()} - {self.file_size_mb}MB\"\n",
    "\n",
    "\n",
    "items = [\n",
    "    Book(\"Python\", \"John\", 2020, 300),\n",
    "    Book(\"AI Basics\", \"Sam\", 2021, 250),\n",
    "    EBook(\"ML Guide\", \"Alex\", 2022, 5),\n",
    "    EBook(\"Data Science\", \"David\", 2023, 8)\n",
    "]\n",
    "\n",
    "for item in items:\n",
    "    print(item.describe())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8025139e-62fe-42ae-ac01-539d885dc25a",
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
