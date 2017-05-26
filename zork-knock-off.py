from sys import exit

#your character can pick up items through out the 'game' they will get stored in the inventory list
inventory = []

#this is the very first thing 
def start():
	
	print "There is a door to your right and left."
	print "Which one do you take?"
	room = 'start'
	next = raw_input("> ")
	
# here are the first 2 options 
# the left door leading to the chasm/pit room
# the right door leads to the room with a chest in the middle

	if next == "left":
		pit_room_start()
	elif next == "right":
		chest_room_start()
# as always if you dont follow the storyline you will die.
	else:
		dead("You stumble around the room until you starve.")

#you end up in this loop if you enter the left door to the chasm room
def pit_room_start():
	room = 'pit start'
	print "\nYou open the door and enter the room. "
	print "There is a large dark chasm that cuts across the middle of the room."
	print "The chasm is about 8 feet across and you cannot see the bottom."
	print "You see a door on the otherside of the chasm.\n"
	
	if 'bridge' in inventory:
		print "Use magic bridge to cross?"
	else:
		print "do you attempt to jump across or turn back?"  
	next = raw_input('> ')
	
	if 'jump'in next:
		dead('plummeting down the infinite chasm')
	elif 'back' in next:
		print "you go back to the door you came through"
		room = 'start'
		start()
	elif 'bridge' in inventory and 'yes' in next or 'bridge' in next:
		print "You place your magic bridge down and walk over the chasm"
		pit_room_end()
	elif 'bridge' not in inventory and 'yes' in next or 'bridge' in next:	
		print "You dont have a bridge you cant do that."
	else:
		print dead('putsing around not solving the puzzle')
	
def pit_room_end():
	print "You stand at the edge of the chasm with the door in front of you."
	print "do you go back across the bridge or open the door?"
	next2 = raw_input('> ')
	if 'back' in next2:
		print " you walk back across the magic bridge






def dead(why):
	print "You have died %r you are dumb!" % why
	exit(0)
	
	
print "You awake from a deep slumber in an unfamilar dark room."	
start()