class Song(object):

	def __init__(self,lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print(line)

happy_bday = Song(["Happy birthday to you",
				   "I don't want to get sued",
				   "So I'll stop right there."])

bulls_on_parade = Song(["They rally around the family",
						"With pockets full of shells"])

white_riot = Song(["Black man gotta lot a problems",
				   "But they don't mind throwin a brick",
				   "White people go to school",
				   "Where they teach you how ta be thick"])

lyrics = Song(["Black man gotta lot a problems",
				"But they don't mind throwin a brick",
				"White people go to school",
				"Where they teach you how ta be thick"])

wight_riot = lyrics

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

white_riot.sing_me_a_song()

wight_riot.sing_me_a_song()

