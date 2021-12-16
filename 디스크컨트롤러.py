from heapq import *


def solution(jobs):
    num_of_jobs = len(jobs)
    total_time, completion_time = 0, 0
    jobs.sort()
    ready_queue = []

    first_job = jobs.pop(0)
    completion_time = first_job[0] + first_job[1]
    total_time += first_job[1]

    def push_waited_jobs():
        while jobs and jobs[0][0] <= completion_time:
            job = jobs.pop(0)
            heappush(ready_queue, (job[1], job[0]))

    push_waited_jobs()
    while jobs or ready_queue:
        # dispatch
        if ready_queue:
            fjob = heappop(ready_queue)
            total_time += completion_time - fjob[1] + fjob[0]
            completion_time += fjob[0]
        else:
            fjob = jobs.pop(0)
            completion_time = fjob[1] + fjob[0]
            total_time += fjob[1]
        print(total_time)
        print(ready_queue)
        print(jobs)
        push_waited_jobs()

    return total_time // num_of_jobs


if __name__ == "__main__":
    print(solution( [[0, 5], [2, 10], [100000000000, 2]] 	))
    print(sorted([[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]))
