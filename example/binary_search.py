

def binary_search(sorted_list: list,
                  value: int):
    if len(sorted_list) == 0:
        return -1
    i = 0
    j = len(sorted_list) - 1
    while i <= j:
        mid = (i + j) // 2
        if sorted_list[mid] == value:
            return mid
        elif value < sorted_list[mid]:
            j = mid - 1
        else:
            i = mid + 1
    return j


if __name__ == '__main__':
    l = []
    assert binary_search([], 1) == -1
