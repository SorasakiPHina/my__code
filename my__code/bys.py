import random

#统计训练集中true与false的数量
def cout(train):   
    true=0
    for i in train:
        if(i[1]):
            true+=1
    false=len(train)-true
    return true,false

#统计某个特征值出现的次数
def couts(ex,s):    
    num=0
    for i in ex:
        for j in i[0]:
            if(j==s):
                num+=1
    return num

#统计某个特征值出现时，结果是true，false的数量
def yes_or_no(ex,s):
    num=0
    nyes=0
    nno=0
    for i in ex:
        for j in i[0]:
            if(j==s):
                num+=1
                if(i[1]):
                    nyes+=1
    nno=num-nyes
    return nyes,nno

#通过测试集计算的先验概率进行分类
def bys(train,test):
    print("*"*100)
    zd={}   #用于统计每个特征向量的特征值数量

    #统计训练集中true与false的数量
    y,n=cout(train)
    print("True:",y,"False:",n)
    for i in train:
        for j in range(len(i[0])):
            zd[j]=[]
    for i in train:
        ii=i[0]
        for j in range(len(ii)):
            if ii[j] not in zd[j]:
                zd[j].append(ii[j])
    
    #概率平滑方法
    pyes=(y+1)/(y+n+2)
    pno=(n+1)/(y+n+2)
    
    #计算概率
    for i in range(len(test)):
        dui,cuo=yes_or_no(train,test[i])
        #print(s[i],"Yes:",(dui+1)/(y+len(zd[i])),(dui+1),(y+len(zd[i])))
        pyes*=(dui+1)/(y+len(zd[i]))
        #print("No:",(cuo+1)/(n+len(zd[i])),(cuo+1),(n+len(zd[i])))
        pno*=(cuo+1)/(n+len(zd[i]))

    #输出结果
    print("-----"*10)
    print(test)
    print("pyes:",pyes)
    print("pno:",pno)
    print("结果是：")
    if(pyes>pno):
        print("Pyes>Pno,Vnb=YES!!!")
    else:
        print("Pyes<Pno,Vnb=NO!!!")
    
#打乱数据后按要求返回训练集与测试集
def dataout(ex):
    random.shuffle(ex)
    train=ex[:10]
    test=ex[:9:-1]
    new_test=[]
    for i in test:
        new_test.append(i[0])
    print("测试集：")
    for k in test:
        print(k)
    return train,new_test

if __name__=="__main__":
#样例
    examples=[
        [["Sunny","Hot","High","Weak"],False],  
        [["Sunny","Hot","High","Strong"],False],
        [["Overcast","Hot","High","Weak"],True],
        [["Rain","Mild","High","Weak"],True],
        [["Rain","Cool","Normol","Weak"],True],
        [["Rain","Cool","Normol","Strong"],False],
        [["Overcast","Cool","Normol","Strong"],True],
        [["Sunny","Mild","High","Weak"],False],
        [["Sunny","Cool","Normol","Weak"],True],
        [["Rain","Mild","Normol","Weak"],True],
        [["Sunny","Mild","Normol","Strong"],True],
        [["Overcast","Mild","High","Strong"],True],
        [["Overcast","Hot","Normol","Weak"],True],
        [["Rain","Mild","High","Strong"],False]
    ]

#处理数据
    train,test=dataout(examples)

#进行测试
    for i in test:
        bys(train,i)
