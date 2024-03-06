def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left, right = merge_sort(array[:mid]), merge_sort(array[mid:])
    return merge(left, right, array.copy())


def merge(left, right, merged):
    left_cursor, right_cursor = 0, 0

    while left_cursor < len(left) and right_cursor < len(right):
        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor + right_cursor] = left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1

    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]

    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    return merged


def is_anagram(first_string, second_string):
    if not first_string or not second_string:
        if first_string:
            first_sorted = list(first_string.lower())
            first_merge_sorted = merge_sort(first_sorted)
            return ("".join(first_merge_sorted), "", False)
        elif second_string:
            second_sorted = list(second_string.lower())
            second_merge_sorted = merge_sort(second_sorted)
            return ("", "".join(second_merge_sorted), False)
        else:
            return ("", "", False)

    first_sorted = list(first_string.lower())
    second_sorted = list(second_string.lower())

    first_merge_sorted = merge_sort(first_sorted)
    second_merge_sorted = merge_sort(second_sorted)

    return (
        "".join(first_merge_sorted),
        "".join(second_merge_sorted),
        "".join(first_merge_sorted) == "".join(second_merge_sorted),
    )
