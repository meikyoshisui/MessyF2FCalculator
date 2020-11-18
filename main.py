#test comment
import random
import sys


p1burst = int(sys.argv[1])
p1successvalue = int(sys.argv[2])
p2burst = int(sys.argv[3])
p2successvalue = int(sys.argv[4])

p1successCount = 0
p2successCount = 0
neitherplayersuccesscount = 0

print("P1 rolls B" + str(p1burst) + " on " + str(p1successvalue))
print("P2 rolls B" + str(p1burst) + " on " + str(p1successvalue))

for i in range(0, 100000):
    p1rolls = []
    p2rolls = []
    p1successes = []
    p2successes = []
    p1crit = False
    p2crit = False

    # Roll Dice
    for j in range(0, p1burst):
        p1rolls.append(random.randint(1, 20))
    for j in range(0, p2burst):
        p2rolls.append(random.randint(1, 20))

    # Determine which dice are successes, and if there are crits
    for j in range(0, len(p1rolls)):
        if p1rolls[j] <= p1successvalue:
            p1successes.append(p1rolls[j])
        if p1rolls[j] == p1successvalue:
            p1crit = True
    for j in range(0, len(p2rolls)):
        if p2rolls[j] <= p2successvalue:
            p2successes.append(p2rolls[j])
        if p2rolls[j] == p2successvalue:
            p2crit = True

    print("Trial #" + str(i))
    print("P1 rolls " + str(p1rolls) + ", succeeding on " + str(p1successes))
    print("P2 rolls " + str(p2rolls) + ", succeeding on " + str(p2successes))


    # Determine which player won f2f
    # Crits
    if (p1crit and p2crit):
        neitherplayersuccesscount += 1
        print("Both players crit.")
        continue
    if (p1crit and not p2crit):
        p1successCount += 1
        print("P1 crit.")
        continue
    if (p2crit and not p1crit):
        p2successCount += 1
        print("P2 crit.")
        continue

    #one or both players have 0 successful rolls
    if (p1successes == [] and p2successes == []):
        neitherplayersuccesscount += 1
        print("Both players miss.")
        continue
    if(p1successes == [] and not p2successes == []):
        p2successCount += 1
        print("P2 wins, P1 has no successes.")
        continue
    if(p2successes == [] and not p1successes == []):
        p1successCount += 1
        print("P1 wins, P2 has no successes.")
        continue
    # Equal max success bounces
    if max(p1successes) == max(p2successes):
        neitherplayersuccesscount += 1
        print("The highest success of both players is equal. Neither player wins.")
        continue
    # Player with highest success wins
    if max(p1successes) > max(p2successes):
        p1successCount += 1
        print("P1's highest success is higher than P2's highest success. P1 wins")
        continue
    if max(p2successes) > max(p1successes):
        p2successCount += 1
        print("P2's highest success is higher than P1's highest success. P2 wins")
        continue

print("Player one wins " + str(p1successCount))
print("Player two wins " + str(p2successCount))
print("Neither player wins " + str(neitherplayersuccesscount))
