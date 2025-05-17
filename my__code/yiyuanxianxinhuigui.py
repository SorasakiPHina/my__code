
import numpy as np
import matplotlib.pyplot as plt

true_w=2
true_b=1
data_lens=100
np.random.seed(123)

def get_data():     #生成数据
    data_x=np.random.randint(-1,8,size=data_lens)
    data_x=data_x.astype(np.float32)
    data_true_y=[true_w*x+true_b for x in data_x]
    data_y=[y+np.random.randn() for y in data_true_y]

    return data_x,data_y,data_true_y

def draw_data(x,y):         #画图
    plt.scatter(x,y)
    plt.xlabel("x")
    plt.ylabel("y")

def draw_hypeplane(w,b,X,label):
    Y=[w*x +b for x in X]
    plt.plot(X,Y,label=label)

def predict(w,b,x):     #计算Y值并返回
    return w*x+b

def train(x,y,lr=0.01):     #训练
    w,b=0.0,0.0
    n=len(x)
    R_thetas=[]
    R_thetas.append(np.mean([np.square(predict(w,b,x[i])-y[i]) for i in range(n)]))

    for i in range(20):
        w=w-lr*2*np.mean([(predict(w,b,x[j])-y[j])*x[j] for j in range(n)])
        b=b-lr*2*np.mean([(predict(w,b,x[j])-y[j]) for j in range(n)])
        R_thetas.append(np.mean([np.square(predict(w,b,x[i])-y[i]) for i in range(n)]))

    return w,b,R_thetas

x,y=get_data()[:2]
w,b,R_thetas=train(x,y)
print("w:",w,";b:",b)
print("R_thetas:",R_thetas)
draw_data(x,y)
draw_hypeplane(true_w,true_b,x,label="true")
plt.legend()
plt.show()