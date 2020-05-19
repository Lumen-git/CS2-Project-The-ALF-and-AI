import lyricsgenius
import os
import time

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def menu():
    clear()
    print(""" _______        ___            _______
|   _   |      |   |          |       |
|  |_|  |      |   |          |    ___|
|       |      |   |          |   |___
|       | ___  |   |___  ___  |    ___| ___
|   _   ||   | |       ||   | |   |    |   |
|__| |__||___| |_______Automatic Lyric Finder""")
    global currentArtist
    print("The current artist is {}".format(currentArtist))
    userChoice = 0
    print("1) Change Artist")
    print("2) Find Song")
    print("3) Band Mode")
    print("4) Batch Mode")
    print("5) Fuzzy Search")
    print("s) Settings")
    userChoice = input(">>")
    if userChoice == "1":
        changeArtist()
    if userChoice == "2":
        findSong()
    if userChoice == "3":
        bandMode()
    if userChoice == "4":
        batchMode()
    if userChoice == "5":
        fuzzySearch()
    if userChoice.lower() == "s":
        settings()
    else:
        clear()
        menu()

def changeArtist():
    global currentArtist
    global artist
    clear()
    artistSearch = input("Enter the artist's name: ")
    artist = genius.search_artist(artistSearch, max_songs=3, sort="popularity")
    print("{} Found!".format(artist.name))
    input("\n\nPress enter to return to the menu")
    currentArtist = artist.name
    menu()

def findSong():
    clear()
    global artist
    songSearch = input("Enter song name: ")
    song = genius.search_song(songSearch, artist.name)
    print(song.lyrics)
    print("Save lyrics? (y/n)")
    userSave = input(">>")
    if userSave.lower() == "y":
        try:
            writeFile = open("input.txt","a")
            writeFile.write(song.lyrics)
            writeFile.write("\n\n\n")
            writeFile.close()
        except:
            print("Song unable to be saved...")
    userSave = 0
    input("\n\nPress enter to return to the menu")
    menu()

def bandMode():
    global currentArtist
    global artist
    global bandCount
    clear()
    print("Search set to {} songs".format(bandCount))
    artistSearch = input("Enter the artist's name: ")
    artist = genius.search_artist(artistSearch, max_songs=bandCount, sort="popularity")
    print("Are you sure? (y/n)")
    userSure = input(">>")
    if userSure.lower() == "n":
        menu()
    writeFile = open("input.txt","a")
    for songSearch in artist.songs:
        try:
            print(songSearch.lyrics)
            writeFile.write(songSearch.lyrics)
            writeFile.write("\n\n\n")
        except:
            print("Skipped Song")
    writeFile.close()
    input("\n\nPress enter to return to the menu")
    menu()

def fuzzySearch():
    clear()
    global artist
    songSearch = input("Enter song name: ")
    song = genius.search_song(songSearch)
    print(song.lyrics)
    print("Save lyrics? (y/n)")
    userSave = input(">>")
    if userSave.lower() == "y":
        try:
            writeFile = open("input.txt","a")
            writeFile.write(song.lyrics)
            writeFile.write("\n\n\n")
            writeFile.close()
        except:
            print("Song unable to be saved...")
    userSave = 0
    input("\n\nPress enter to return to the menu")
    menu()

def batchMode():
    global InputFile
    global bandCount
    clear()
    print("Searching for {} songs from all bands in {}".format(bandCount, InputFile))
    writeFile = open("input.txt","a")
    try:
        bandFile = open(InputFile, "r")
    except:
        print("File not found!")
        time.sleep(2)
        menu()
    bands = bandFile.readlines()
    for band in bands:
        artist = genius.search_artist(band, max_songs=bandCount, sort="popularity")
        for songSearch in artist.songs:
            try:
                print(songSearch.lyrics)
                writeFile.write(songSearch.lyrics)
                writeFile.write("\n\n\n")
            except:
                print("Skipped Song")
    print("All bands searched!")
    input()
    menu()


def settings():
    global purist
    global InputFile
    global bandCount
    clear()
    print("1) Toggle Purist Mode (skips remixes and live editions): {}".format(purist))
    print("2) Set 'Batch Mode' Input File: {}".format(InputFile))
    print("3) Set 'Band Mode' Save Amount: {}".format(bandCount))
    print("m) Return to menu")
    userSettings = input(">> ")
    if userSettings == "1":
        if purist == False:
            purist = True
            genius.excluded_terms = ["(Remix)", "(Live)", "Remix", "Live at"]
            print("Purist mode is now on")
            input()
            settings()
        if purist == True:
            purist = False
            genius.excluded_terms = []
            print("Purist mode is now off")
            input()
            settings()
    if userSettings == "2":
        InputFile = input("Enter new file name: ")
        print("Set as {}".format(InputFile))
        input()
        settings()
    if userSettings == "3":
        bandSet = input("Enter value for Band Mode: ")
        try:
            bandSet = int(bandSet)
        except:
            print("Invalid value!")
            input()
            settings()
        bandCount = bandSet
        print("Value set at {}".format(bandCount))
        input()
        settings()
    if userSettings.lower() == "m":
        menu()
    userSettings = ""
    settings()



genius = lyricsgenius.Genius("Bgo6HkwLu0Gf1T3C38XF4wtCDj7zTFQ_uMCU3BezOZiRJYA-v-TUtqqK_t4hbulU")
genius.skip_non_songs = True
bandCount = 5
purist = False
InputFile = "bands.txt"
currentArtist = "None"

menu()
