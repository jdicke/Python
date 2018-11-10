# Threading allows for running multiple things at once
# So its good for messaging...
# Sending
# Listening

import threading

class Messenger(threading.Thread):

    # Every time we create a thread calls run function
    def run(self):
        for _ in range(10):
            print(threading.currentThread().getName())

x = Messenger(name='Send out messages')
y = Messenger(name='Receive messages')
x.start()
y.start()