from apscheduler.schedulers.blocking import BlockingScheduler
from monitor import monitor

sched = BlockingScheduler()

@sched.scheduled_job('interval', hour=1)
def timed_job():
    print('This job is run every hour.')
    monitor()

# sched.configure(options_from_ini_file)
sched.start()