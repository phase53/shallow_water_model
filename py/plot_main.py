#----ライブラリインストール---------------------------------------------
import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.colors import ListedColormap,LinearSegmentedColormap
import matplotlib as mpl
#----ファイルパス設定---------------------------------------------------
DATPAS='../dat/'
PNGPAS='../png/'
#----パラメタ設定-------------------------------------------------------
JM=512
IM=1024
DAY=100                                                  #図示したい日付
ALLDAY=100                                               #計算日数
WDAY=str(DAY).zfill(4)
BYTESIZE=8
#----描画構成-----------------------------------------------------------
LON=np.arange(start=0,stop=2,step=2/IM)
LAT=np.fromfile(DATPAS+'LAT.dat',dtype='>f8')
LAT=np.sin(LAT)
LAT, LON=np.meshgrid(LAT, LON)
G=np.zeros((JM,IM))
TMP=np.zeros((JM,IM//2))
cmap=np.loadtxt('colormap.txt', dtype=float)
cmap=cmap/65535.0
BIRe=LinearSegmentedColormap.from_list(colors=cmap,name='BIRe')
mpl.colormaps.register(BIRe)
#----描画---------------------------------------------------------------
"""
print('DAY '+str(DAY)+' is printed...') 
G=np.fromfile(f"{DATPAS}ZETA_G{WDAY}.dat",dtype='>f8').reshape(JM,IM)
plt.figure(figsize=(6, 6))
c=plt.contourf(LON,LAT,np.transpose(G[:,:]),\
np.linspace(-10,10,101),cmap='BIRe')
plt.colorbar(c)
plt.title(f'DAY{WDAY}')
plt.xlabel(r'$\lambda (\times\pi)$')
plt.ylabel(r'$\mu$')
plt.rcParams['axes.xmargin']=0.
plt.rcParams['axes.ymargin']=0.
plt.axis('equal')
plt.savefig(f"{PNGPAS}ZETA{WDAY}.png")
plt.close()  

print('DAY '+str(DAY)+' is printed...') 
G=np.fromfile(f"{DATPAS}DIV_G{WDAY}.dat",dtype='>f8').reshape(JM,IM)
plt.figure(figsize=(6, 6))
c=plt.contourf(LON,LAT,np.transpose(G[:,:]),\
np.linspace(-2,2,101),cmap='BIRe')
plt.colorbar(c)
plt.title(f'DAY{WDAY}')
plt.xlabel(r'$\lambda (\times\pi)$')
plt.ylabel(r'$\mu$')
plt.rcParams['axes.xmargin']=0.
plt.rcParams['axes.ymargin']=0.
plt.axis('equal')
plt.savefig(f"{PNGPAS}DIV{WDAY}.png")
plt.close()  

print('DAY '+str(DAY)+' is printed...') 
G=np.fromfile(f"{DATPAS}DEPTH_G{WDAY}.dat",dtype='>f8').reshape(JM,IM)
plt.figure(figsize=(6, 6))
c=plt.contourf(LON,LAT,np.transpose(G[:,:]),\
np.linspace(0,2,101),cmap='BIRe')
plt.colorbar(c)
plt.title(f'DAY{WDAY}')
plt.xlabel(r'$\lambda (\times\pi)$')
plt.ylabel(r'$\mu$')
plt.rcParams['axes.xmargin']=0.
plt.rcParams['axes.ymargin']=0.
plt.axis('equal')
plt.savefig(f"{PNGPAS}DEPTH{WDAY}.pdf")
plt.close()  

"""
#ここから全出力用
DAY=0
for i in range(0,ALLDAY+1,1):
  WDAY=str(DAY).zfill(4)
  print('DAY '+str(DAY)+' is printed...') 
  G=np.fromfile(f"{DATPAS}ZETA_G{WDAY}.dat",dtype='>f8').reshape(JM,IM)
  plt.figure(figsize=(6, 6))
  c=plt.contourf(LON,LAT,np.transpose(G[:,:]),\
  np.linspace(-10,10,101),cmap='BIRe')
  plt.colorbar(c)
  plt.title(f'DAY{WDAY}')
  plt.xlabel(r'$\lambda (\times\pi)$')
  plt.ylabel(r'$\mu$')
  plt.rcParams['axes.xmargin']=0.
  plt.rcParams['axes.ymargin']=0.
  plt.axis('equal')
  plt.savefig(f"{PNGPAS}ZETA{WDAY}.png")
  plt.close()  

  print('DAY '+str(DAY)+' is printed...') 
  G=np.fromfile(f"{DATPAS}DIV_G{WDAY}.dat",dtype='>f8').reshape(JM,IM)
  plt.figure(figsize=(6, 6))
  c=plt.contourf(LON,LAT,np.transpose(G[:,:]),\
  np.linspace(-2,2,101),cmap='BIRe')
  plt.colorbar(c)
  plt.title(f'DAY{WDAY}')
  plt.xlabel(r'$\lambda (\times\pi)$')
  plt.ylabel(r'$\mu$')
  plt.rcParams['axes.xmargin']=0.
  plt.rcParams['axes.ymargin']=0.
  plt.axis('equal')
  plt.savefig(f"{PNGPAS}DIV{WDAY}.png")
  plt.close()  

  print('DAY '+str(DAY)+' is printed...') 
  G=np.fromfile(f"{DATPAS}DEPTH_G{WDAY}.dat",dtype='>f8').reshape(JM,IM)
  plt.figure(figsize=(6, 6))
  c=plt.contourf(LON,LAT,np.transpose(G[:,:]),\
  np.linspace(-0,2,101),cmap='BIRe')
  plt.colorbar(c)
  plt.title(f'DAY{WDAY}')
  plt.xlabel(r'$\lambda (\times\pi)$')
  plt.ylabel(r'$\mu$')
  plt.rcParams['axes.xmargin']=0.
  plt.rcParams['axes.ymargin']=0.
  plt.axis('equal')
  plt.savefig(f"{PNGPAS}DEPTH{WDAY}.png")
  plt.close()  
  DAY=DAY+1
