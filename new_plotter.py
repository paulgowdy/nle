import matplotlib.pyplot as plt
import pandas as pd

runs = [
#'2021-08-05/09-53-24',
'2021-08-08/17-38-17',
'2021-08-09/17-54-30',
]

colors = ['navy','darkred','green','navy','navy','red','aqua','cyan','red','red','darkred']


prefix = "//wsl$/Ubuntu-20.04/home/paulgamble/neurips-2021-the-nethack-challenge/nethack_baselines/torchbeast/outputs/"
#prefix = "//wsl$/Ubuntu-20.04/home/paulgamble/hackbot_transformer/nethack_baselines/torchbeast/outputs/"
suffix = "/logs.csv"

roll_window = 100

plt.figure()
ax = plt.gca()

for r, c in zip(runs, colors):
    log_fn = prefix + r + suffix

    df = pd.read_csv(log_fn)

    df['rolling_score'] = df['mean_episode_return'].rolling(roll_window).mean()
    #df['score_std_low'] = df['rolling_score'] - df['mean_episode_return'].rolling(roll_window).std()
    #df['score_std_high'] = df['rolling_score'] + df['mean_episode_return'].rolling(roll_window).std()

    #ax.fill_between(df['step'], df['score_std_low'], df['score_std_high'], color=c, alpha=0.3)
    df.plot(x='step',y='rolling_score',ax=ax, color=c)


labels = [x.split('/')[-1] for x in runs]
plt.legend(labels)
plt.title("Mean Episode Score")
#plt.ylim(-200,0)

plt.figure()
ax = plt.gca()

for r, c in zip(runs, colors):
    log_fn = prefix + r + suffix

    df = pd.read_csv(log_fn)
    df['rolling_score'] = df['mean_episode_step'].rolling(roll_window).mean()
    #df['rolling_score'] = df['mean_episode_return'].rolling(roll_window).mean()
    #df['rolling_score'].plot(x='step')
    #df['mean_episode_return'].plot()
    df.plot(x='step',y='rolling_score',ax=ax, color=c)
plt.legend(runs)
#plt.ylim(-200,0)
plt.title("Mean Episode Steps")

plt.show()
