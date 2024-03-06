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


# print(is_anagram("amor", "roma"))  # saída: ('amor', 'amor', True)
# print(is_anagram("pedra", "perda"))  # saída: ('adepr', 'adepr', True)
# print(is_anagram("pato", "tapo"))  # saída: ('aopt', 'aopt', True)
# print(is_anagram("Amor", "Roma"))  # saída: ('amor', 'amor', True)
# print(is_anagram("coxinha", "empada"))  # saída: ('achinox', 'aademp', False)
