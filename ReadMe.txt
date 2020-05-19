FOR GITHUB: This is a project I did in 2020 for my computer scince 2 course (Python). I wrote a script to gather lyrics from Genius and train an AI to generate more. The AI used is the char-rnn. I'm uploading it to Gihub to save, show off, and to offer the ALF tool to anyone who wants to use it.





Here's a document to explain what everything in this folder is and what it does, as well as some other explanations.

<<<Files>>>

char-rnn-master:
A character level AI as described by Andrej Karpathy in the paper "The Unreasonable Effectiveness of Recurrent Neural Networks" (https://karpathy.github.io/2015/05/21/rnn-effectiveness/). This neural network was use to generate new text from the lyric text I trained it on. Requires Torch and Lua to run. Contains a few sample RNNs genreated. (NOT IN GITHUB FILES)

AutomaticLyricFinder:
The main part of my project. Using the Genius Lyrics API (https://genius.com/) I made a program to find lyrics in bulk and save them to one file. Lyrics can be found by artist and song (find song), top x (x = a configurable number of songs) songs from a band (band mode), top x songs from all bands in a text file (batch mode), and by song title alone (fuzzy search). "Change artist" sets the artist/band for the find song mode. Settings allows the user to set the batch (x) value, set the name of the input text file, and enable purist mode (remove live version and remixes from the search)


<<<Epoch samples>>>

1 epoch = 1 cycle through the full training data

� = A character that has an unknown encoding, either due to Python or merging Windows and Linux.

Epoch .19:
This is a sample from the .19th epoch of the AI. Mostly random letters and incomprehensible english. The AI does seem to already have an idea of the organization the lyrics take. Paragraphs are well made and several [Verse] and [Chorus] markers are made. Sentences begin in capital letters.

Epoch .94:
Many more words are appearing. The * used to censor the lyrics are now appearing in groups. The first pair of () is used correctly.

Epoch 4.91:
Parentheses are used more sparingly, although correctly. Contractions are mostly complete. Sentences are starting to make sense, although most have very little comprehensible meaning. A valid question is formed: "Do it take me?". A refrain is used.

Epoch 9.81:
Sentences are starting to have meaning. Typos are scarce. The first assignment of a vocalist is made: [Chorus: Jack Met]. The artist mentioned is real and not a made up string of characters (Jack Met: youngest member of AJR). The AI seems to be pairing " and ) together. A hook is used.


<<<AI training process>>>

A file roughly 3.5 mb was made by the lyrics of the top 200 (or all if less than 200) songs by several artists. The file was manually censored due to the Genius API gathering artist not intended (all bands were used due to their relative safety for a school project, a few unwanted ones slipped through). The AI was trained in a Ubuntu virtual machine until system failure. Epoch 9.81 was the highest reached until the system crashed, either due to lack of virtual hard drive space or virtual memory. Samples of 2000 characters were taken from several epochs. 


<<<Errors>>>

The virtual machine used limited training power and eventually crashed.
The Genius API returns the first artist by keyword, not the top result causing searches like “Queen” to return Beyonce (due to keywords like queen b, the queen, queen beyonce). This quark caused unwanted artists to be used.


<<<Possible future uses>>>

The AI could be trained longer and with more power to generate better lyrics.

Songs from 1 artist or genre could be used to generate songs in the style of a particular artist or genre.

Rather than lyrics, the AI could be trained on movie scripts, books, or other text media.



 
 
