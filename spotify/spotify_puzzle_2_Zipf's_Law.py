#!usr/bin/ python

# Program for finding the best song based on
# Zipf's Law

import sys
from operator import itemgetter

number_of_songs = None
number_to_output = None
first_song_plays = None
song_list = []
data = []

for song in sys.stdin:
	if not number_of_songs:
		conditions = song.split()
		number_of_songs = conditions[0]
		number_to_output = int(conditions[1])
	else:
		song_list.append(song.split())

first_song_plays = int(song_list[0][0])

def evaluate(song_list):
	song_info=[]
	for i, song in enumerate(song_list):
	 	data={}
		data['order_on_album'] = i+1
	 	data['song_name'] = song[1]
	 	data['song_qi'] = int(song[0]) / (first_song_plays/(i+1))
		song_info.append(data) 
	song_info = sorted(song_info, key=itemgetter('order_on_album'))
	song_info = sorted(song_info, key=itemgetter('song_qi'), reverse=True)
	return song_info

for song in evaluate(song_list)[:number_to_output]:
	print song['song_name']


