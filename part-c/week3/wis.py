def create_path(filepath):
    path = []
    file = open(filepath, "r")
    lines = file.readlines()

    size = int(lines[0])

    i = 1
    for line in lines[1:]:
        vertex = int(line.split()[0])
        path.append(vertex)

        i = + 1

    return size, path


def compute_max_weights(size, path):
    A = []

    for l in range(size+1):
        A.append([])

    A[0] = 0
    A[1] = path[0]

    for i in (range(2, size + 1)):
        A[i] = max(A[i-1], A[i-2] + path[i-1])

    return A


def reconstruce_wis(wis, path):
    import pdb
    pdb.set_trace()
    S = []
    i = len(path)

    while i >= 2:
        if wis[i-1] >= wis[i-2] + path[i-1]:
            i -= 1
        else:
            S.append(i)
            i -= 2

    if i == 1:
        S.append(1)

    return S


def get_answers(S):
    vertices = [1, 2, 3, 4, 17, 117, 517, 997]
    answer = ""

    for vertex in vertices:
        if vertex in S:
            answer = answer + "1"
        else:
            answer = answer + "0"

    return answer


def main():
    size, path = create_path("path.txt")

    max_weights = compute_max_weights(size, path)

    set_weight = reconstruce_wis(max_weights, path)

    print(get_answers(set_weight))


if __name__ == "__main__":
    main()
