{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter a negative number -5\n",
      "enter a negative number 3\n",
      "enter a number 7\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.3 , 7.45\n"
     ]
    }
   ],
   "source": [
    "name = input(\"Enter your name\")\n",
    "a = float(input(\"enter a negative number\"))\n",
    "b = float(input(\"enter a number\"))\n",
    "c = float(input(\"enter a number\"))\n",
    "\n",
    "def f(x):\n",
    "    return (a*x*x)+(b*x)+c\n",
    "def f_p(x):\n",
    "    return(2*a*x)+b\n",
    "def f_pp(x):\n",
    "    return 2*a\n",
    "\n",
    "x = 0\n",
    "for i in range(0, 10):\n",
    "    x= x - (f_p(x)/f_pp(x))\n",
    "print(\"Coordinates of Maximum\", x, \",\" , f(x))"
   ]
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
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
