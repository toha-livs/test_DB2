def change_it_in_int(r):
    g = (r[0], int(r[1]), int(r[2]), int(r[3]))
    return g


def change_it_in_str(r):
    g = (r[0], str(r[1]), str(r[2]), str(r[3]))
    return g


def solve(List):
    changed_list = []
    for i in List:
        changed_list.append(change_it_in_int(i))
    List.clear()
    changed_list = sorted(changed_list, key=lambda x: (x[0], -x[1], -x[2], -x[3]))
    for i in changed_list:
        List.append(change_it_in_str(i))
    return List


if __name__ == '__main__':
    List = [
            ("Tom", "19", "167", "54"),
            ("Jony", "24", "180", "69"),
            ("Json", "21", "185", "75"),
            ("John", "27", "190", "87"),
            ("Jony", "24", "191", "98"),
            ]
    print(solve(List))