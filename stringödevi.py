{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Ahmet-MeHmeT-HaKan\n"
     ]
    }
   ],
   "source": [
    "def TemizVeri(s1, s2, s3):\n",
    "    Birlesmis_deger = \"\"\n",
    "    for a in s1:\n",
    "        if not a.isdigit():\n",
    "            \n",
    "            Birlesmis_deger += a\n",
    "            \n",
    "    Birlesmis_deger += \"-\"\n",
    "\n",
    "    for a in s2:\n",
    "        if not a.isdigit():\n",
    "            \n",
    "            Birlesmis_deger += a\n",
    "            \n",
    "    Birlesmis_deger += \"-\"\n",
    "\n",
    "    for a in s3:\n",
    "        if not a.isdigit():\n",
    "             \n",
    "            Birlesmis_deger +=a\n",
    "\n",
    "    Birlesmis_deger=Birlesmis_deger.capitalize()\n
    "    return Birlesmis_deger\n",
    "\n",
    "print(TemizVeri(\"Ah5me4t\", \"M9eHm4eT\", \"Ha3K5a1n\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
