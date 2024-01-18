from heapq import heappop, heappush


def maximum_cpu_load(jobs):
    jobs.sort()
    active_jobs = []  # a heap ds
    curr_load = 0
    max_load = 0
    count = 0
    for job in jobs:
        count += 1
        [start_time, end_time, load] = job
        while active_jobs and active_jobs[0][0] < start_time:
            job_to_remove = active_jobs[0]
            curr_load -= job_to_remove[1]
            heappop(active_jobs)

        heappush(active_jobs, (end_time, load, count))
        curr_load += load
        max_load = max(max_load, curr_load)

    return max_load


print(maximum_cpu_load([[1,4,2], [2,4,1], [3,6,5]]))
