import sys
from random import choice


class SimpleMarkovGenerator(object):
    # no character limit on base class
    character_limit = None

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
        current_char = 0
        # Keep looping until we have a key that isn't in the chains
            # (which would mean it was the end of our original text)
            #
            # Note that for long texts (like a full book), this might mean
            # it would run for a very long time.
        while key in self.chains:
            # check character limit
            # note that order of if (cond1) AND (cond2) matters!                     
            word = choice(self.chains[key])
            # account for the " " in the join
            if self.character_limit is not None and (current_char + len(word)) >= self.character_limit and self.char_limit:
                break
            words.append(word)
            key = (key[1], word)
            
            formed_text = " ".join(words)
            # print formed_text
            current_char = len(formed_text)
        print len(formed_text)
        return formed_text


class TweetableMarkovGenerator(SimpleMarkovGenerator):
    character_limit = 140


    # some 140 char limit
    # def make_text(self):
        # return super(TweetableMarkovGenerator, self).make_text()       
        

if __name__ == "__main__":

    # we should get list of filenames from sys.argv
    filenames = sys.argv[1:]
    # # we should make an instance of the class
    mark = SimpleMarkovGenerator()
    # # we should call the read_files method with the list of filenames
    mark.read_files(filenames)
    print mark.make_text()
    # # we should call the make_text method 5x
    # for i in range(5):
    #     print "time {}".format(i+1)
    #     print mark.make_text()

    # make a tweetable my_generator
    birdie = TweetableMarkovGenerator()
    birdie.read_files(filenames)
    for i in range(5):
        # print "time {}".format(i+1)
        print birdie.make_text()
