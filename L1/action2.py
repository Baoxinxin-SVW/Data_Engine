import numpy as np
    ScoreType = np.dtype({'names':['name','Chinese','Math','English'],'formats':['U32','i','i','i']})
    Score = np.array([('张飞',68,65,30),
                     ('关羽',95,76,98),
                     ('刘备',98,86,88),
                      ('典韦',90,88,77),
                     ('许褚',80,90,90)],dtype = ScoreType)
   
    print('语文平均成绩：%s,最小成绩：%s,最大成绩:%s,方差:%.2f,标准差:%.2f'%(Score['Chinese'].mean(),Score['Chinese'].min(),Score['Chinese'].max(),Score['Chinese'].var(),Score['Chinese'].std()))
    print('数学平均成绩：%s,最小成绩：%s,最大成绩:%s,方差:%.2f,标准差:%.2f'%(Score['Math'].mean(),Score['Math'].min(),Score['Math'].max(),Score['Math'].var(),Score['Math'].std()))
    print('英语平均成绩：%s,最小成绩：%s,最大成绩:%s,方差:%.2f,标准差:%.2f'%(Score['English'].mean(),Score['English'].min(),Score['English'].max(),Score['English'].var(),Score['English'].std()))
    ScoreSum = -(Score['Chinese']+Score['Math']+Score['English'])
    y = ScoreSum.argsort()
 
    print('分数由高到低为：')
    for i in y:
       print (Score[i][0],Score[i][1]+Score[i][2]+Score[i][3],end = ",")

