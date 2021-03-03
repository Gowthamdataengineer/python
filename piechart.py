import matplotlib.pyplot as plt
import numpy as np

y=np.array([35,25,20,10])
datas=["Mobile","TV","Dress","Doll"]
mexplode=[0.2,0.1,0.3,0.6]

plt.pie(y, labels=datas,explode=mexplode , shadow=True)
plt.show()
