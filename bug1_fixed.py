def last_n_items(items, n):
    """Return the last n items of a list.

    Examples:
        last_n_items([1, 2, 3, 4, 5], 2) -> [4, 5]
        last_n_items([1, 2, 3], 5)       -> [1, 2, 3]
        last_n_items([1, 2, 3], 0)       -> []
    """
    if n <= 0:
        return []
    return items[-n:]  # fix: removed the extra "- 1"; negative start also handles n > len(items)


if __name__ == "__main__":
    print(last_n_items([1, 2, 3, 4, 5], 2))  # expected [4, 5]
    print(last_n_items([1, 2, 3], 5))        # expected [1, 2, 3]
    print(last_n_items([1, 2, 3], 0))        # expected []
