#!/usr/bin/python

from sys import argv
from time import sleep
import os

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


def all_c_files(directory):
    files = []
    for filename in os.listdir(directory):
        if filename.endswith(".c"): files.append(filename)
    return files



class RecompileHandler(FileSystemEventHandler):

    def __init__(self, executable, flags):
        self.executable = executable
        self.flags = flags

    def on_any_event(self, event):
        filepath = event.src_path
        if filepath.endswith(".h") or filepath.endswith(".c"):

            msg = "%s: CHANGE DETECTED - RECOMPILING FROM SOURCE" % os.path.basename(filepath)
            print "\n\n%s\n%s\n%s\n\n" % ("*" * len(msg), msg, "*" * len(msg))
            self.recompile_c_code()
    
    def recompile_c_code(self):
        pid = os.fork()
        if pid == 0:
            cmd = "gcc"
            args = [cmd] + self.flags + all_c_files(os.getcwd()) + ["-o", self.executable]
            os.execvp(cmd, args)
            os._exit(0)



if __name__ == "__main__":
    assert len(argv) >= 2, "Not Enough Parameters"
    executable, flags = argv[1], argv[2:]
    event_handler = RecompileHandler(executable, flags)
    observer = Observer()
    observer.schedule(event_handler, os.getcwd())
    observer.start()
    try:
        while True:
            sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

