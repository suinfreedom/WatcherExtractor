import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Watcher:
        DIRECTORY_TO_WATCH =  "Test"

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
                    print("Error")

            self.observer.join()

class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            print( "Received %s." % event.src_path)


if __name__ == '__main__':
    w = Watcher()
    w.run()