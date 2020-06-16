{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 115,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "语文平均成绩：86.2,最小成绩：68,最大成绩:98,方差:120.16,标准差:10.96\n",
      "数学平均成绩：81.0,最小成绩：65,最大成绩:90,方差:87.20,标准差:9.34\n",
      "英语平均成绩：76.6,最小成绩：30,最大成绩:98,方差:587.84,标准差:24.25\n",
      "分数由高到低为：\n",
      "刘备 272,关羽 269,许褚 260,典韦 255,张飞 163,"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "ScoreType = np.dtype({'names':['name','Chinese','Math','English'],'formats':['U32','i','i','i']})\n",
    "\n",
    "Score = np.array([('张飞',68,65,30),\n",
    "                  ('关羽',95,76,98),\n",
    "                  ('刘备',98,86,88),\n",
    "                  ('典韦',90,88,77),\n",
    "                  ('许褚',80,90,90)],dtype = ScoreType)\n",
    "\n",
    "print('语文平均成绩：%s,最小成绩：%s,最大成绩:%s,方差:%.2f,标准差:%.2f'\n",
    "      %(Score['Chinese'].mean(),Score['Chinese'].min(),Score['Chinese'].max(),Score['Chinese'].var(),Score['Chinese'].std()))\n",
    "print('数学平均成绩：%s,最小成绩：%s,最大成绩:%s,方差:%.2f,标准差:%.2f'\n",
    "     %(Score['Math'].mean(),Score['Math'].min(),Score['Math'].max(),Score['Math'].var(),Score['Math'].std()))\n",
    "print('英语平均成绩：%s,最小成绩：%s,最大成绩:%s,方差:%.2f,标准差:%.2f'\n",
    "     %(Score['English'].mean(),Score['English'].min(),Score['English'].max(),Score['English'].var(),Score['English'].std()))\n",
    "\n",
    "ScoreSum = -(Score['Chinese']+Score['Math']+Score['English'])\n",
    "y = ScoreSum.argsort()\n",
    "\n",
    "print('分数由高到低为：')\n",
    "for i in y:\n",
    "    print (Score[i][0],Score[i][1]+Score[i][2]+Score[i][3],end = \",\")\n",
    "    #print ('总分数由高到低为：%s,%i'%(Score[i][0],Score[i][1]+Score[i][2]+Score[i][3]))\n"
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
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
