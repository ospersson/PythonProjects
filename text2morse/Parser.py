import winsound
from time import sleep


class TextToMorseParser:
    _standard_duration = 150  # Set Duration To 300 ms == 0.3 second
    _standard_freq = 1000  # Set Frequency To 900 Hertz

    #@duration.setter
    def duration(self, duration):
        self._standard_duration = duration

    @property
    def frquency(self, frequency):
        self._standard_freq = frequency

    def play_dot(self):
        winsound.Beep(self._standard_freq, self._standard_duration)
        self.sleep_one_unit()

    def play_dash(self):
        winsound.Beep(self._standard_freq, self._standard_duration * 3)
        self.sleep_one_unit()

    """The space between parts of the same letter is one unit."""
    def sleep_one_unit(self):
        sleep(self._standard_duration / 1000)

    """The space between letters is three units"""
    def sleep_three_unit(self):
        sleep((self._standard_duration * 3) / 1000)

    def parse_word(cls, word):
        for char in word.upper():
            if char.isdigit():
                self = cls
                self.parse_integer(char)
                continue

            if char == "A":
                cls.play_dot()
                cls.play_dash()
            elif char == "B":
                cls.play_dash()
                cls.play_dot()
                cls.play_dot()
                cls.play_dot()
            elif char == "C":
                cls.play_dash()
                cls.play_dot()
                cls.play_dash()
                cls.play_dot()
            elif char == "D":
                cls.play_dash()
                cls.play_dot()
                cls.play_dot()
            elif char == "E":
                cls.play_dot()
            elif char == "F":
                cls.play_dot()
                cls.play_dot()
                cls.play_dash()
                cls.play_dot()
            elif char == "G":
                cls.play_dash()
                cls.play_dash()
                cls.play_dot()
            elif char == "H":
                cls.play_dot()
                cls.play_dot()
                cls.play_dot()
                cls.play_dot()
            elif char == "I":
                cls.play_dot()
                cls.play_dot()
            elif char == "J":
                cls.play_dot()
                cls.play_dash()
                cls.play_dash()
                cls.play_dash()
            elif char == "K":
                cls.play_dash()
                cls.play_dot()
                cls.play_dash()
            elif char == "L":
                cls.play_dot()
                cls.play_dash()
                cls.play_dot()
                cls.play_dot()
            elif char == "M":
                cls.play_dash()
                cls.play_dash()
            elif char == "N":
                cls.play_dash()
                cls.play_dot()
            elif char == "O":
                cls.play_dash()
                cls.play_dash()
                cls.play_dash()
            elif char == "P":
                cls.play_dot()
                cls.play_dash()
                cls.play_dash()
                cls.play_dot()
            elif char == "Q":
                cls.play_dash()
                cls.play_dash()
                cls.play_dot()
                cls.play_dash()
            elif char == "R":
                cls.play_dot()
                cls.play_dash()
                cls.play_dot()
            elif char == "S":
                cls.play_dot()
                cls.play_dot()
                cls.play_dot()
            elif char == "T":
                cls.play_dash()
            elif char == "U":
                cls.play_dot()
                cls.play_dot()
                cls.play_dash()
            elif char == "V":
                cls.play_dot()
                cls.play_dot()
                cls.play_dot()
                cls.play_dash()
            elif char == "W":
                cls.play_dot()
                cls.play_dash()
                cls.play_dash()
            elif char == "X":
                cls.play_dash()
                cls.play_dot()
                cls.play_dot()
                cls.play_dash()
            elif char == "Y":
                cls.play_dash()
                cls.play_dot()
                cls.play_dash()
                cls.play_dash()
            elif char == "Z":
                cls.play_dash()
                cls.play_dash()
                cls.play_dot()
                cls.play_dot()
            elif char == "Å":
                cls.play_dot()
                cls.play_dash()
                cls.play_dash()
                cls.play_dot()
                cls.play_dash()
            elif char == "Ä":
                cls.play_dot()
                cls.play_dash()
                cls.play_dot()
                cls.play_dash()
            elif char == "Ö":
                cls.play_dash()
                cls.play_dash()
                cls.play_dash()
                cls.play_dot()
            else:
                print('Char not found')

            """Pause after each char."""
            cls.sleep_three_unit()

    def parse_integer(self, char):
        if char == "0":
            self.play_dash()
            self.play_dash()
            self.play_dash()
            self.play_dash()
            self.play_dash()
        elif char == "1":
            self.play_dot()
            self.play_dash()
            self.play_dash()
            self.play_dash()
            self.play_dash()
        elif char == "2":
            self.play_dot()
            self.play_dot()
            self.play_dash()
            self.play_dash()
            self.play_dash()
        elif char == "3":
            self.play_dot()
            self.play_dot()
            self.play_dot()
            self.play_dash()
            self.play_dash()
        elif char == "4":
            self.play_dot()
            self.play_dot()
            self.play_dot()
            self.play_dot()
            self.play_dash()
        elif char == "5":
            self.play_dot()
            self.play_dot()
            self.play_dot()
            self.play_dot()
            self.play_dot()
        elif char == "6":
            self.play_dash()
            self.play_dot()
            self.play_dot()
            self.play_dot()
            self.play_dot()
        elif char == "7":
            self.play_dash()
            self.play_dash()
            self.play_dot()
            self.play_dot()
            self.play_dot()
        elif char == "8":
            self.play_dash()
            self.play_dash()
            self.play_dash()
            self.play_dot()
            self.play_dot()
        elif char == "9":
            self.play_dash()
            self.play_dash()
            self.play_dash()
            self.play_dash()
            self.play_dot()
        else:
            print('Integer not found')

        """Pause after each char."""
        self.sleep_three_unit()
