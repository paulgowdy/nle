import glob
import matplotlib.pyplot as plt
import pickle

prefix = "//wsl$/Ubuntu-20.04/home/paulgamble/neurips-2021-the-nethack-challenge/nethack_baselines/torchbeast/saved_episodes/actor_"
suffix = ".p"


for i in range(100):
    fn = prefix + "0_ep_" + str(i) + suffix

    with open(fn, 'rb') as f:
        z = pickle.load(f)

    print(len(z))
    print(len(set(z)))
    #print(set(z))
