import sys
from random import choice


class SimpleMarkovGenerator(object):

    def read_files(self, filenames):
        """Given a list of files, create a corpus, and make chains from it."""

        input_text = ''
        for file_name in filenames:
            input_text += (open(file_name).read() + " ")
        # save chains dictionary to our instance
        self.chains = self.make_chains(input_text)

        # WHY?
        # my_generator = SimpleMarkovGenerator()
        # my_generator.read_files(filenames)
        # my_generator.chains --> returns chains made from .make_chains


    def make_chains(self, corpus):
        """Takes input text as string; stores chains."""

        chains = {}

        words = corpus.split()

        for i in range(len(words) - 2):
            key = (words[i], words[i + 1])
            value = words[i + 2]

            if key not in chains:
                chains[key] = []

            chains[key].append(value)

        return chains # needed


    def make_text(self):
        """Takes dictionary of markov chains; returns random text."""

        key = choice(self.chains.keys())
        words = [key[0], key[1]]
        while key in self.chains:
            # Keep looping until we have a key that isn't in the chains
            # (which would mean it was the end of our original text)
            #
            # Note that for long texts (like a full book), this might mean
            # it would run for a very long time.

            word = choice(self.chains[key])
            words.append(word)
            key = (key[1], word)

        return " ".join(words)



if __name__ == "__main__":

    # we should get list of filenames from sys.argv
    filenames = sys.argv[1:]
    # we should make an instance of the class
    mark = SimpleMarkovGenerator()
    # we should call the read_files method with the list of filenames
    mark.read_files(filenames)
    # we should call the make_text method 5x
    for i in range(5):
        print "time {}".format(i+1)
        print mark.make_text()
