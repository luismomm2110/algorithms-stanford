from functools import reduce


def populate_jobs(filepath):
    jobs = []

    file = open(filepath, "r")

    i = 1
    for line in file.readlines()[1:]:
        job = line.split()
        job = list(map(int, job))
        job.insert(0, i)

        i += 1

        jobs.append(job)

    return jobs


def order_by_diff(jobs):
    diff_jobs = list(map(lambda job: [job[1], job[2],
                                      int(job[1]) - int(job[2])], jobs))

    diff_jobs.sort(key=lambda x: (x[2], x[0]), reverse=True)

    weighted_dis = 0
    distance_so_far = 0

    for job in diff_jobs:
        distance_so_far += job[1]
        weighted_dis += job[1]*job[0]

    return weighted_dis


def order_by_ratio(jobs):
    diff_jobs = list(map(lambda job: [job[1], job[2],
                                      float(job[1])/float(job[2])], jobs))

    diff_jobs.sort(key=lambda x: (x[2], x[0]), reverse=True)

    weighted_dis1 = 0
    distance_so_far1 = 0

    for job in diff_jobs:
        distance_so_far1 += job[1]
        weighted_dis1 += job[1]*job[0]

    return weighted_dis1

    # 1 weight # length


def main():
    jobs = populate_jobs("jobs.txt")

    weighted_dis = order_by_diff(jobs)
    print(weighted_dis)

    weighted_dis2 = order_by_ratio(jobs)
    print(weighted_dis2)


if __name__ == "__main__":
    main()
