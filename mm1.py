import numpy as np 

def P0(lam, mu):
    return 1.0 - lam/mu

def Pn(n, lam, mu):
    return (1.0 - (lam/mu)) * (lam / mu) ** n

def L(lam, mu):
    return lam / (mu - lam)

def Lq(lam, mu):
    return lam ** 2 / (mu * (mu - lam))

def W(lam, mu):
    return 1.0 / (mu - lam)

def Wq(lam, mu):
    return lam / (mu * (mu - lam))

def Pw(lam, mu):
    return lam / mu

def rho(lam, mu):
    return lam / mu