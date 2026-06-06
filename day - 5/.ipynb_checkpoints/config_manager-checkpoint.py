{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "a2d16e9a-bd07-401f-ac9b-fcb49ef4c0e9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'model': 'GPT', 'learning_rate': 0.001, 'epochs': 20}\n"
     ]
    }
   ],
   "source": [
    "# JSON Config Manager\n",
    "\n",
    "import json\n",
    "\n",
    "def save_config(data: dict, filename: str):\n",
    "    with open(filename, \"w\") as file:\n",
    "        json.dump(data, file, indent=4)\n",
    "\n",
    "def load_config(filename: str) -> dict:\n",
    "    with open(filename, \"r\") as file:\n",
    "        return json.load(file)\n",
    "\n",
    "def update_config(filename: str, key: str, value):\n",
    "    data = load_config(filename)\n",
    "    data[key] = value\n",
    "    save_config(data, filename)\n",
    "\n",
    "config = {\n",
    "    \"model\": \"GPT\",\n",
    "    \"learning_rate\": 0.001,\n",
    "    \"epochs\": 10\n",
    "}\n",
    "\n",
    "save_config(config, \"config.json\")\n",
    "\n",
    "update_config(\"config.json\", \"epochs\", 20)\n",
    "\n",
    "print(load_config(\"config.json\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3a66e906-50ed-4501-ab6f-418e2ae43e31",
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
