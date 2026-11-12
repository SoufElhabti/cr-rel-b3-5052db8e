import pickle, os
def load(b): return pickle.loads(b)
def sh(x): os.system("echo " + x)
