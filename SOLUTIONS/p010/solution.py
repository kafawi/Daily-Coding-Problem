from threading import Lock, Thread
from time import sleep

class Scheduler: 
    lock_ = Lock() 
    tasks_ = set()

    def schedule(self, f :callable, n :int):
        th = Task(f, n, self)
        self.add_task_(th)
        th.start()


    def add_task_(self, th: Thread):
        with self.lock_:
            self.tasks_.add(th)

    def remove_task_(self, th :Thread):
        with self.lock_:
            self.tasks_.remove(th)

    def wait_for_all(self):
        tasks = []
        with self.lock_:
            tasks = [x for x in self.tasks_]
        for task in tasks:
            task.join()

class Task(Thread):
        
        def __init__(self, fn :callable, delay_ms :int, scheduler: Scheduler):
            Thread.__init__(self)
            self.fn_ = fn
            self.delay_ms_ = delay_ms
            self.scheduler_ = scheduler


        def run(self):
            sleep(self.delay_ms_ / 1000)
            self.fn_()
            self.scheduler_.remove_task_(self)


if __name__=="__main__":
    scheduler = Scheduler()
    scheduler.schedule(lambda : print("10 sec"), 10000)
    scheduler.schedule(lambda : print("9 sec"), 9000)
    scheduler.schedule(lambda : print("8 sec"), 8000)

    scheduler.wait_for_all()