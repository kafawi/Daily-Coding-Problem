This Problem is too vage.

Do we have to implement it for a concurrent enviroment with threads and processes. 

But the barebone should look like this
```
struct scheduler:
    schedule(f: function, n: int):
        wait(n)
        call(f)  
```
This can also be just the function.

If we want to make it parallel, we can start for every schedule call a Thread, that waits for n milliseconds and calls the function.
```
struct scheduler:
    tasks = List[Threads]

    schedule(f :function, n :int):
        th: Thread = new Thread(){
          wait(n)
          call(f)
          tasks.remove(this)
        }
        tasks.add(th)
        launch(th)


    wait_for_all():
        for task in task:
          task.join()
```

If we want to go more crazy, we can say, that the scheduler has an launcher thread, that launces threads, that are just calling the function at the right time.
This is achieved, because the launcher sleeps till the very next Task is scheduled, but if someone will add a new task, the laucher interruted and has to recheck his task queue.
This task queue is an priority queue, maybe implemented as a simple heap. Also, the taskthread (worker) can be launchedout of an preallocated pool, to improve speed.
-> if we do so, we have a producer - consumer pattern. But this aproache is to advanced for an interview. 

A more simple one, can be, that the scheduler thread is executing the functions. that will take some complexity away. and it is easy to append more complexity. 

lets do the simple one like in the last listing.

we have to make the `tasks list` thread safe. To make this critic area short, letzt use instead a hash set-> that provides near constant manipulation. 

[code](solution.py)



### Atferthouht
As I saw the api for threads, i stumbled apon the `concurrent.futures` and especially `ThreadPoolExecutor`, which provides a flexible way to implement such a scheduler, retrive the returntime pass arguments and so forth. 
This is for future use very good to know, that python has such advanced api. Many other languages has such api also provided. Dont be smart, so I ask more question to get the real propose for this problem. 