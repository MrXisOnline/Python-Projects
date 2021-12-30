
def rose_valley(player_name):
	print("So %s, You're in rose valley and you're hungry and thristy also." %player_name)
	print("In east there are a bee nest and the west there is a river")
	f2 = input("[e -> east][w -> west] <:>")
	if f2 == "e":
		beehive(player_name)
	elif f2 == "w":
		rivershore(player_name)


def rivershore(player_name):
	print("You have taken the right option %s" %player_name)
	print("At rivershore you drinked water and also eaten some fishes.")
	print("After you travelled across river and you find a village where you happily living.")

def beehive(player_name):
	print("You tried to take honey from beehive But you got injured and dead from thrist.")


def dead_sea(player_name):
	print("So %s, You're in the dead sea where is no one alive. So, you can easily travel the sea." %player_name)
	print("At Seashore there is village where you can live safely.")


def start_game():
	player_name = input("What's Your Name :")
	print("Hello %s, Welcome to Text Adventure Game..." %player_name)
	print("Hey %s, You're in a village with some villager and around the village there are lots of mobs.\nSo, you need to escape the village to somewhere else." %player_name)
	print("This night you escaped the village outside village there are 2 Ways.\nLeft and Right which way you go")
	f1 = input("[l -> left][r -> right] <:>")
	if f1 == "l":
		rose_valley(player_name)
	elif f1 == "r":
		dead_sea(player_name)

start_game()

