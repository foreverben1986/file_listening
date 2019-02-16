import pyinotify
import sys

if len(sys.argv) >= 2:
    path = sys.argv[1]
else:
    raise Exception("pleas assign the folder argument for listening")

multi_event = pyinotify.IN_CREATE
wm = pyinotify.WatchManager()


class MyEventHandler(pyinotify.ProcessEvent):
    def process_IN_CREATE(self, event):
        print('OPEN', event.pathname)
        print(event)


handler = MyEventHandler()
notifier = pyinotify.Notifier(wm, handler)

print(path)
wm.add_watch(path, multi_event)
notifier.loop()
