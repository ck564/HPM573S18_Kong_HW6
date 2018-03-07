import HW6_P3 as SourceCode

PROB_HEADS = 0.5
N_GAMES = 10
N_SIM_SETS = 1000
ALPHA = 0.05

multiSets = SourceCode.MultipleSetofGames(
    id = range(N_SIM_SETS),
    prop_head= [PROB_HEADS]*N_SIM_SETS,
    n_games= [N_GAMES]*N_SIM_SETS,
)

multiSets.simulate()

print(multiSets.get_PI_ave_reward(ALPHA))

print('The expected reward of the casino owner in this case'
      'would be represented by a steady state simulation (reporting a '
      'confidence interval), while that of the gambler is best '
      'represented by a transient state simulation (reporting a prediction'
      'interval).')
