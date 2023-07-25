from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import threading

class Watcher:
    DIRECTORY_TO_WATCH = "images/known"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print ("Error")

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # DO Some Operation
            print (event.src_path)

        elif event.event_type == 'modified':
            # Do Some Operation
            print (event.src_path)



w = Watcher()
wrun= threading.Thread(target=w.run)
wrun.start()
