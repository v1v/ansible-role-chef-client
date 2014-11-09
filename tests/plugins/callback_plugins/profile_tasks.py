import time


class CallbackModule(object):
    """
    A plugin for timing tasks
    """
    def __init__(self):
        # For storing timings
        self.stats = {}
        # For storing the name of the current task
        self.current = None

    def playbook_on_task_start(self, name, is_conditional):
        """
        Logs the start of each task
        """
        if self.current is not None:
            # Record the running time of the last executed task
            self.stats[self.current] = time.time() - self.stats[self.current]
        self.current = name
        # Record the start time of the current task
        self.stats[self.current] = time.time()

    def playbook_on_stats(self, stats):
        """
        Print the timings
        """
        if self.current is not None:
            # Record the timing of the very last task
            self.stats[self.current] = time.time() - self.stats[self.current]

        # Sort the tasks by their running time
        results = sorted(self.stats.items(), key=lambda value: value[1], reverse=True)

        # Just keep the top 10
        results = results[:10]

        # Print the timings
        for name, elapsed in results:
            print "{0:-<70}{1:->9}".format('{0} '.format(name), ' {0:.02f}s'.format(elapsed))
