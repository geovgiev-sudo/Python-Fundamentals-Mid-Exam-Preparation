songs = input().split()
commands = int(input())

for i in range(commands):
    command = input().split(" * ")
    action = command[0]

    if action == "Add Song":
        song = command[1]
        if song not in songs:
            songs.append(song)
            print(f"{song} successfully added")

    elif action == "Delete Song":
        songs_to_delete = int(command[1])
        if len(songs) < songs_to_delete:
            continue
        deleted_songs = songs[:songs_to_delete]
        del songs[:songs_to_delete]
        print(f"{', '.join(deleted_songs)} deleted")

    elif action == "Shuffle Songs":
        song_index_1 = int(command[1])
        song_index_2 = int(command[2])
        if 0 <= song_index_1 < len(songs) and 0 <= song_index_2 < len(songs):
            songs[song_index_1], songs[song_index_2] = songs[song_index_2], songs[song_index_1]
            print(f"{songs[song_index_1]} is swapped with {songs[song_index_2]}")

    elif action == "Insert":
        song = command[1]
        song_index = int(command[2])
        if 0 <= song_index < len(songs):
            if song in songs:
                print(f"Song is already in the playlist")
            else:
                songs.insert(song_index, song)
                print(f"{songs[song_index]} successfully inserted")
        else:
            print(f"Index out of range")

    elif action == "Sort":
        songs.sort(reverse=True)

    elif action == "Play":
        print(f"Songs to Play:")
        for song in songs:
            print(song)