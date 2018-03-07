""" Problem 1: Print the 95% t-based confidence intervals for the expected reward and the
        probability of loss. You can use 1,000 simulated games to calculate these confidence
        intervals.
    Problem 2: How do you interpret the confidence intervals you reported in Problem 1?"""

import HW6_P1P2 as SourceCode
import scr.StatisticalClasses as Statistics

ALPHA = 0.05

myGame = SourceCode.SetOfGames(prob_head=0.5, n_games=1000)
myGameStats_reward = Statistics.SummaryStat('Games reward', myGame.get_reward_list())
myGameStats_loss = Statistics.SummaryStat('Probability of loss', myGame.get_probability_loss())


# Problem 1, Problem 2
print('95% CI for expected reward: ',myGameStats_reward.get_t_CI(ALPHA))
print('For many repeated iterations of the game, 95% of the intervals obtained from each iteration '
      'will capture the true expected reward of the game')

print('95% CI for probability of loss: ',myGameStats_loss.get_t_CI(ALPHA))
print('For many repeated iterations of the game, 95% of the intervals obtained from each iteration'
      'will capture the true probability of loss for this game')


