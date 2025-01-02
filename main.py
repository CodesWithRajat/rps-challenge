from RPS_game import play, quincy, mrugesh, kris, abbey
from RPS import player

print("Testing against Quincy:")
play(player, quincy, 1000, verbose=True)

print("\nTesting against Mrugesh:")
play(player, mrugesh, 1000, verbose=True)

print("\nTesting against Kris:")
play(player, kris, 1000, verbose=True)

print("\nTesting against Abbey:")
play(player, abbey, 1000, verbose=True)
