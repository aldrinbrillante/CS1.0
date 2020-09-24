'''
Let's practice access values from dicitionaries.

Values be anything  -- from integers to lists!
'''

# Below is a dicitonary that is strong different playlists for different occassions.

playlist = {
  'gym'  : ['Eye of the Tiger', 'POWER', 'Level Up'],
  'study': ['White Noise', 'ChilledCow', 'Space Ambient'],
  'bbq'  : ['Before I Let Go', 'Summertime', 'Outstanding']
}


# Using the playlist dictionary, access the 'gym' playlist.
gym_songs = playlist["gym"]

# Using a for loop, print the each songs from the 'gym' playlist
for i in gym_songs:
    print(i)