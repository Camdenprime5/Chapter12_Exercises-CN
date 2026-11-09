For the Chapter 12 exercises, I worked with text analysis and text generation using Python. These exercises focused on processing text from *The Strange Case of Dr. Jekyll and Mr. Hyde*, counting groups of words, creating successor maps, and generating new text using a Markov-style system.

Exercise 1 focused on the `setdefault()` dictionary method. I learned that `setdefault()` can simplify code when a dictionary key needs to contain a list of values. Instead of first checking whether a key exists, the program can create an empty list when necessary and immediately append a value to it.

Exercise 2 counts trigrams, which are groups of three consecutive words. The program cleans the book text, moves through the words using a three-word sliding window, and stores each trigram in a dictionary along with how many times it appears. My program found `"said the lawyer"` as the most common trigram with a frequency of 20.

Exercise 3 uses trigrams to create a successor map. The first two words are stored as a tuple and used as a dictionary key, while the third word is added to a list of possible successors. Repeated words are kept because a word that occurs more often should have a greater chance of being randomly selected. My program created 16,569 bigram keys from the book.

Exercise 4 uses the successor map to generate new text. It randomly chooses a starting bigram, selects one of its possible successor words, and then moves the bigram forward using the newest word. My version generates 50 words, stores them in a list, and formats the completed result into readable lines.

After completing the exercises, I compared my solutions with the instructor’s GitHub solutions. Both versions use the same main Chapter 12 concepts, including dictionaries, tuples, sliding windows, `get()`, `setdefault()`, and random selection. The instructor’s solutions are useful because they stay close to the textbook and show the concepts step-by-step.

There were also some differences between the solutions. In Exercise 2, my version removes the Project Gutenberg header and footer before analyzing the book. This prevents the Gutenberg license text from affecting the trigram results and gives `"said the lawyer"` as the most common trigram. My version also uses `max(counter, key=counter.get)` to find the largest count directly instead of using several different approaches.

For Exercise 3, my version reuses the same `read_words()` function from Exercise 2. I think this improves consistency because the same punctuation, capitalization, and em-dash cleaning rules are used throughout the project. The instructor’s solution demonstrates the same successor-map idea but handles some of the text processing separately.

For Exercise 4, my version separates generating the words from formatting the output. It stores all 50 generated words first and then joins and formats them afterward. I think this makes the program easier to follow and also makes sure that the final partial line is displayed.

Overall, I think the instructor’s solutions are better for demonstrating the individual textbook concepts step-by-step, while my versions are better for reuse, consistency, and handling a few edge cases. Both could still be improved by adding more tests and allowing things like the filename and number of generated words to be entered by the user instead of being hard-coded.

One challenge I had was getting Python to locate the book file because the programs expected it to be inside a folder named `files`. After fixing the project structure and file path, Exercises 2, 3, and 4 all ran successfully in PyCharm.

I used AI assistance to help explain some of the Chapter 12 concepts, practice identifying which pieces of code were needed, debug the file-path issue, and compare my solutions with the instructor’s versions. I reviewed and tested the programs myself in PyCharm.