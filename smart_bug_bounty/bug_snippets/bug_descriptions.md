# Bug Descriptions

Five buggy snippets in three languages (Python, JavaScript, Java). Each file contains a short demo so the wrong behavior can be seen by running it.

## bug1.py
- **Language**: Python
- **Intended Behavior**: `last_n_items(items, n)` returns the last `n` items of a list (`[1, 2, 3, 4, 5]` with `n = 2` gives `[4, 5]`; `n = 0` gives `[]`; `n` larger than the list returns the whole list).
- **Current Issue**: The slice has an extra item because of an off-by-one error, so `[1, 2, 3, 4, 5]` with `n = 2` returns `[3, 4, 5]`.

## bug2.js
- **Language**: JavaScript
- **Intended Behavior**: `loadUsers(ids, fetchUser)` loads all users and returns them as an array in the same order as `ids`.
- **Current Issue**: `forEach` does not wait for the `async` callbacks, so the function returns before any user is loaded and the result is an empty array `[]`.

## bug3.java
- **Language**: Java
- **Intended Behavior**: `isAdmin(role)` returns `true` when the role text is exactly `"admin"`, and `false` otherwise.
- **Current Issue**: The code compares strings with `==`, which compares object references. It works for a string literal but returns `false` for `new String("admin")` (for example, a value read from user input).

## bug4.py
- **Language**: Python
- **Intended Behavior**: `add_tag(tag, tags)` adds a tag to the given list; when no list is given, each call starts with a new empty list.
- **Current Issue**: The default argument `tags=[]` is created once and shared between calls, so the second call returns `['python', 'testing']` instead of `['testing']`.

## bug5.py
- **Language**: Python
- **Intended Behavior**: `find_user(conn, username)` returns the row of the user with exactly that username, or `None` if it does not exist.
- **Current Issue**: The SQL query is built with string formatting, so it is vulnerable to SQL injection. The input `x' OR '1'='1` returns the first user (`alice`, an admin) instead of `None`.
