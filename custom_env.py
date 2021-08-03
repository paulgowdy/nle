import gym
import pickle
import numpy as np

SAVE_PREFIX = '/home/paulgamble/neurips-2021-the-nethack-challenge/nethack_baselines/torchbeast/saved_episodes/'

class CustomNLEWrapper(gym.Wrapper):
    def __init__(self, env, env_id):
        super().__init__(env)
        self.env = env
        self.env_id = env_id

        #self.env.observation_space

        self.episode_record = []
        self.episode_count = 0

        #print("PG action space") 113 actions
        #print(self.env.action_space)

        self.prev_fog = np.array([False])
        #self.prev_level = 1

    def step(self, action):
        next_state, reward, done, info = self.env.step(action)

        #if self.env_id == 0:
        #print(next_state['blstats'])
        #print(action)
        #self.episode_record.append([int(x) for x in next_state['blstats']])

        self.fog = np.where(next_state['glyphs'] == 2359, np.ones(next_state['glyphs'].shape), np.zeros(next_state['glyphs'].shape))
        #dungeon_level = int(next_state['blstats'][-1])
        #exp_level = int(next_state['blstats'][-7])
        #exp_points = int(next_state['blstats'][-6])

        if self.prev_fog.any():
            z = np.sum(self.prev_fog - self.fog)
            # just max against zero and skip the level checking stuff
            # only rewarded for decreasing fog, never punished for new fog
            z = max(0, z)
            reward += z/50.

            #print("PG explore reward: ", z)

            #if self.prev_level == self.level:
            #    reward += z/20.

        #if exp_level < 3 and dungeon_level > 1:
        #    print("delved too quickly and too deep!")
        #    reward = -100
        #    done = True

        self.prev_fog = self.fog
        #self.prev_level = self.level

        '''
        self.episode_record.append(int(action))

        if done:
            # save
            #with open(SAVE_PREFIX + 'actor_' + str(self.env_id) + '_ep_' + str(self.episode_count) + '.p', 'wb') as f:
            #    pickle.dump(self.episode_record, f)
            # reset record
            self.episode_record = []
            self.episode_count += 1
        '''
        next_state['inv_oclasses'][0] = action
        #print(self.env_id, next_state['inv_oclasses'][:3])
        #print(next_state['inv_oclasses'].shape)
        #print(next_state["message"])
        #print(next_state['prev_action'])
        #print('info', info)
        #info['prev_action'] = action
        return next_state, reward, done, info
