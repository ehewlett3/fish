try:
	f = open("fish.dat") # read fishs
	fishes = f.readlines()
	f.close()
except IOError:
	fishes = []
i = 0 # strip newlines from fishs
for fish in fishes:
	if fish[len(fish)-1]=="\n":
		fishes[i] = fish[:len(fish)-1]
	fishes[i]=fishes[i].split('|')
	i+=1

# print all fish with scales
for fish in fishes:
	if fish[1]=="silver":
		print fish