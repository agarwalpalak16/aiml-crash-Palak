{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "9f4d1eb1-bd66-4ae7-8d58-50d67c8cca6d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "102500\n"
     ]
    }
   ],
   "source": [
    "# Inventory Management System\n",
    "\n",
    "import csv\n",
    "\n",
    "class Product:\n",
    "    def __init__(self, name, price, quantity):\n",
    "        self.name = name\n",
    "        self.price = price\n",
    "        self.quantity = quantity\n",
    "\n",
    "\n",
    "class Inventory:\n",
    "    def __init__(self):\n",
    "        self.products = []\n",
    "\n",
    "    def add_product(self, product):\n",
    "        self.products.append(product)\n",
    "\n",
    "    def total_value(self):\n",
    "        return sum(p.price * p.quantity for p in self.products)\n",
    "\n",
    "    def find_product(self, name):\n",
    "        for product in self.products:\n",
    "            if product.name.lower() == name.lower():\n",
    "                return product\n",
    "        return None\n",
    "\n",
    "    def save_to_csv(self, filename):\n",
    "        with open(filename, \"w\", newline=\"\") as file:\n",
    "            writer = csv.writer(file)\n",
    "\n",
    "            writer.writerow([\"name\", \"price\", \"quantity\"])\n",
    "\n",
    "            for p in self.products:\n",
    "                writer.writerow([p.name, p.price, p.quantity])\n",
    "\n",
    "    def load_from_csv(self, filename):\n",
    "        with open(filename, \"r\") as file:\n",
    "            reader = csv.DictReader(file)\n",
    "\n",
    "            for row in reader:\n",
    "                self.add_product(\n",
    "                    Product(\n",
    "                        row[\"name\"],\n",
    "                        float(row[\"price\"]),\n",
    "                        int(row[\"quantity\"])\n",
    "                    )\n",
    "                )\n",
    "\n",
    "inventory = Inventory()\n",
    "\n",
    "inventory.add_product(Product(\"Laptop\", 50000, 2))\n",
    "inventory.add_product(Product(\"Mouse\", 500, 5))\n",
    "\n",
    "print(inventory.total_value())\n",
    "\n",
    "inventory.save_to_csv(\"inventory.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6af3dbe1-1638-40be-b5cc-5c23f63a83fb",
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
