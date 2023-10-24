import time


class Clock:
    """
    The class clock represent a time such as: hh/mm/ss
    It takes one parameter:
    - time: a tuple that represent a duration

    Correct examples:
    - (72:30:00) -> 72 hours and 30 minutes
    - (23:72:119) -> 24 hours, 13 minutes and 59 seconds
    Note: the class will automatically make the conversion seconds into minutes and minutes into hours

    Incorrect examples:
    - (72:30)
    - (72)
    Note: you must indicate every numbers
    """

    def __init__(self, time: tuple) -> None:
        if len(time) != 3:
            raise ValueError("Clock missing arguments, you must specify the hours, time and seconds")
        
        self.hour = time[0]
        self.minute = time[1]
        self.second = time[2]

    
    def start(self):
        start = time.gmtime()
        print(start.tm_hour)