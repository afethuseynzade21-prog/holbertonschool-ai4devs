def add_tag(tag, tags=None):
    """Add a tag to a list of tags and return the list.

    If no list is given, a new empty list must be used for each call.
    """
    if tags is None:  # fix: create a new list on every call instead of sharing one default list
        tags = []
    tags.append(tag)
    return tags


if __name__ == "__main__":
    post1_tags = add_tag("python")
    post2_tags = add_tag("testing")

    print(post1_tags)  # expected: ['python']
    print(post2_tags)  # expected: ['testing']

    existing = ["news"]
    print(add_tag("sport", existing))  # expected: ['news', 'sport']
