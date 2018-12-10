import random #Allows me to randomly match the two lists
import threading #Allows bot to periodically print a new string

L = ["Sunshine she's here,", "I think about you day and night,", "When you're with me,", "But you heard it, darling,", "Fighting against all odds", "Whether skies are gray or blue", "Or stay up on the phone late at night when you're alone,", "I'll give the shelter,"]
M = ["you can take a break", "it's only right", "baby the skies'll be blue", "you look perfect tonight", "I know we'll be alright this time", "any place on earth will do", "looking out the window gazing up at stars", "like you've done for me"]
"""
Songs: Happy by Pharrell Williams, Happy Together by The Turtles, Perfect by Ed Sheeran, My Happiness by Connie Francis, If You Wonder by Jeff Bernat, Shelter by Porter Robinson and Madeon
"""

def mix_match(L, M):
    """
    This function will randomly match a string from list L with a string from list M

    L: A list of the first half of a lyric
    M: A list of the second half of a lyric
    """
    print(random.choice(L) + " " + random.choice(M))

class mix_match_timer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.__finish = threading.Event()
        self.__interval = 972.0
        """
        I chose this number because an average of 16.2 million adults in the Unites States have depression
        I converted that number to seconds, then I divided it by 1 million
        https://www.verywellmind.com/depression-statistics-everyone-should-know-4159056
        """

    def setInterval(self, interval):
        self.__interval = __interval

    def shutdown(self):
        self.__finished.set()

    def run(self):
        while l:
            if self.__finished.isSet():
                return self.task()

    def task(self):
        pass
