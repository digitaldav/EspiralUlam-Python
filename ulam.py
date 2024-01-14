
import numpy as np
import pandas as pd
import dataframe_image


def _ColorPrimo(v):
    color = 'white'
    if(_Primos(v)!=''):
        color = 'red'
    else:
        color = 'white'
    
    return 'background-color: %s' %color


def _Primos(v):
    
    c=0
    d=1
    while d<=v:
        if(v%d==0):
            c+=1
        d+=1
        if c>2:
            break;
    
    if(c==2):
        return v
    else:
        return ''



def _SelectorMatrizEspiralUlam(m):
    
    if len(m)%2==0:
        _MatrizEspiralUlamPar(m)  
    else:
        _MatrizEspiralUlam(m)    

def _MatrizEspiralUlam(m):
    
    v=len(m)*len(m)
    izq = 0
    der = len(m)-1
    arr = 0
    abj = der
    

    while izq<=der and arr<=abj:
        for r in range (der, izq-1,-1):
            m[abj][r] = v
            v-=1
        abj-=1
            
        for r in range(abj, arr-1,-1):
                m[r][izq] = v
                v-=1
        izq+=1
        
        if(arr <= abj):
            for r in range(izq, der+1):
                m[arr][r] = v
                v-=1
            arr+=1
            
        if(izq <= der):
            for r in range(arr, abj+1):
                m[r][der] = v
                v-=1
            der-=1    

def _MatrizEspiralUlamPar(m):
    
    v=len(m)*len(m)
    izq = 0
    der = len(m)-1
    print(der)
    arr = 0
    abj = der
    
    
    while izq <= der and arr<=abj:
        for r in range (izq, der+1):
            m[arr][r] = v
            v-=1
        arr+=1
        
        for r in range(arr, abj+1):
            m[r][der] = v
            v-=1
        der-=1
        
        if(arr <= abj):
            for r in range(der, izq-1, -1):
                m[abj][r] = v
                v-=1
            abj-=1
            
        if(izq <= der):
            for r in range(abj, arr-1, -1):
                m[r][izq] = v
                v-=1
            izq+=1 


def _PintarMatrizNumpy(m):
    print(np.array(m))

def _PintarMatrizPandas(m):
    df = pd.DataFrame(np.array(m))
    print(df)
    
def _GenerarImagen(a, nombreFichero):
    df = pd.DataFrame(np.array(a))
    df = df.style.hide(axis="columns").hide(axis="index").applymap(_ColorPrimo)
    dataframe_image.export(df,nombreFichero+'.png', max_cols=-1,max_rows=-1)


def _InicializarMatrizDescendente(n):
    
    m=[]
    v=n*n
    
    for r in range(0,n):
        a =[]
        for c in range(0,n):
            a.append(v)
            v-=1
        m.append(a)
    return m 

def _InicializarMatriz(n):
    v=0
    return [[0 for c in range(n)] for r in range(n)]   
            

def _SucesionFib(n):
    v=[]
    v.append(0)
    v.append(1)
    t = n-2
    for i in range(0,t):
        v.append(v[i]+v[i+1])
    return v


def _MatrizEspiralUlamFib(m, d):
    
    v=len(d)-1
    izq = 0
    der = len(m)-1
    arr = 0
    abj = der
    

    while izq<=der and arr<=abj:
        for r in range (der, izq-1,-1):
            m[abj][r] = d[v]
            v-=1
        abj-=1
            
        for r in range(abj, arr-1,-1):
                m[r][izq] = d[v]
                v-=1
        izq+=1
        
        if(arr <= abj):
            for r in range(izq, der+1):
                m[arr][r] = d[v]
                v-=1
            arr+=1
            
        if(izq <= der):
            for r in range(arr, abj+1):
                m[r][der] = d[v]
                v-=1
            der-=1    
            
            
def _SucesionPad(n):
    v=[]
    v.append(1)
    v.append(1)
    v.append(1)
    t = n-3
    for i in range(0,t):
        print(i,v[i+1],v[i])
        v.append(v[i+1]+v[i])
    return v