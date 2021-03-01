import string
import random


class Common_Utils:
    def random_generator(self, size = 8, chars = string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for self.i in range(size))