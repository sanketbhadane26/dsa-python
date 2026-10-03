def is_bad_version(version, first_bad):

    if version >= first_bad:
        return True

    return False


def first_bad_version(n, first_bad):

    left = 1
    right = n

    while left < right:

        mid = (left + right) // 2

        if is_bad_version(mid, first_bad):
            right = mid

        else:
            left = mid + 1

    return left


n = 7
first_bad = 4

result = first_bad_version(n, first_bad)

print(result)