import random
import sys

print("Hello!")

p1burst = int(sys.argv[1])
p1successvalue = int(sys.argv[2])
p2burst = int(sys.argv[3])
p2successvalue = int(sys.argv[4])

p1successCount = 0
p2successCount = 0
neitherplayersuccesscount = 0

for i in range(0, 100000):
    print("trial # " + str(i))
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

    # Determine which player won f2f
    # Crits
    if (p1crit and p2crit):
        neitherplayersuccesscount += 1
        continue
    if (p1crit and not p2crit):
        p1successCount += 1
        continue
    if (p2crit and not p1crit):
        p2successCount += 1
        continue

    #one or both players have 0 successful rolls
    if (p1successes == [] and p2successes == []):
        neitherplayersuccesscount += 1
        continue
    if(p1successes == [] and not p2successes == []):
        p2successCount += 1
        continue
    if(p2successes == [] and not p1successes == []):
        p1successCount += 1
        continue
    # Equal max success bounces
    if max(p1successes) == max(p2successes):
        neitherplayersuccesscount += 1
        continue
    # Player with highest success wins
    if max(p1successes) > max(p2successes):
        p1successCount += 1
        continue
    if max(p2successes) > max(p1successes):
        p2successCount += 1
        continue

print("Player one wins " + str(p1successCount))
print("Player two wins " + str(p2successCount))
print("Neither player wins " + str(neitherplayersuccesscount))
