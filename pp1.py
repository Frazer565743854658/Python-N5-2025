# input
homeHT = int(input("Enter the half time score for the home team: "))
awayHT = int(input("Enter the half time score for the away team: "))
print()
homeFT = int(input("Enter the full time score for the home team: "))
awayFT = int(input("Enter the full time score for the away team: "))
# process
noGoalsScored = (homeFT + awayFT) - (homeHT + awayHT)
# output
print()
print("The number of goals scored after the half time break was: "+str(noGoalsScored))