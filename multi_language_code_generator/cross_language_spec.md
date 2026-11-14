# Cross-Language Specification - Log Analyzer

## Algorithm

Parse web server access logs in the Apache Common Log Format and compute traffic statistics:

- Total requests
- Unique visitors
- Error requests and error rate
- Malformed lines

The same behavior must be reproduced exactly in every language (Python is the reference implementation).

### Processing rules

1. Read the input one line at a time. A trailing line terminator (`\n` or `\r\n`) is removed before parsing.
2. A line that is empty or contains only whitespace is **ignored** (it is not counted anywhere).
3. A line is **valid** if the whole line matches this pattern:

   ```
   ^(\S+) \S+ \S+ \[[^\]]+\] "[^"]*" (\d{3}) (\d+|-)$
   ```

   - Group 1: client IP (the visitor identifier)
   - Group 2: HTTP status code (exactly 3 digits)
   - The request field in quotes must not contain a double quote character.
   - The timestamp is not validated, only its brackets.
4. A non-blank line that does not match the pattern is **malformed**. It is counted in `malformed_lines` and skipped.
5. For every valid line:
   - `total_requests` increases by 1.
   - The IP is added to the set of visitors.
   - If the status code is `>= 400` (4xx and 5xx), `error_requests` increases by 1.
6. `unique_visitors` is the number of distinct IP strings among valid lines.
7. `error_rate` is `error_requests / total_requests * 100`, rounded **half up** to 2 decimals. It is `0.0` when `total_requests` is 0.
   To get identical results in every language, compute it with integers only:
   `hundredths = (2 * error_requests * 10000 + total_requests) // (2 * total_requests)` (integer division), then `error_rate = hundredths / 100`.

## Inputs

- A text file (or a list of strings) with one log entry per line, in Apache Common Log Format:

  ```
  IP ident user [timestamp] "METHOD path PROTOCOL" status bytes
  ```

  Example:

  ```
  192.168.1.1 - - [10/Oct/2023:13:55:36 +0000] "GET /index.html HTTP/1.1" 200 2326
  ```

  The `bytes` field is a number or `-`.

## Outputs

A JSON object with exactly these keys:

| Key | Type | Meaning |
|---|---|---|
| `total_requests` | integer | Number of valid lines |
| `unique_visitors` | integer | Number of distinct IPs among valid lines |
| `error_requests` | integer | Valid lines with status >= 400 |
| `error_rate` | number | Percentage of error requests, 2 decimals, `0.0` when there are no requests |
| `malformed_lines` | integer | Non-blank lines that do not match the pattern |

Numbers are compared by value (`20` and `20.0` are equal).

## Edge Cases

- Empty file (no lines): all values are 0 and `error_rate` is `0.0`.
- Blank or whitespace-only lines: ignored, not counted as malformed.
- Malformed entries (missing fields, non-numeric status, text that is not a log line): counted in `malformed_lines`, not in `total_requests`.
- The same IP appearing many times: counted once in `unique_visitors`.
- Status `399` is not an error and `400` is an error. Redirects (3xx) are not errors.
- `bytes` field equal to `-`: the line is valid.
- Lines ending with `\n` or `\r\n` are parsed the same as lines without a terminator.
- Rounding: half up, for example 1 error out of 3 requests gives `33.33` and 2 out of 3 gives `66.67`.

## Test Cases

In all cases below, `LINE(ip, status)` stands for this line:

```
<ip> - - [10/Oct/2023:13:55:36 +0000] "GET /index.html HTTP/1.1" <status> 2326
```

### TC1 - Empty input

- Input: no lines
- Expected: `{"total_requests": 0, "unique_visitors": 0, "error_requests": 0, "error_rate": 0.0, "malformed_lines": 0}`

### TC2 - Single valid request, bytes is `-`

- Input: `192.168.1.1 - - [10/Oct/2023:13:55:36 +0000] "GET /index.html HTTP/1.1" 200 -`
- Expected: `{"total_requests": 1, "unique_visitors": 1, "error_requests": 0, "error_rate": 0.0, "malformed_lines": 0}`

### TC3 - Mixed statuses and repeated visitors

- Input: `LINE(10.0.0.1, 200)`, `LINE(10.0.0.2, 404)`, `LINE(10.0.0.1, 500)`, `LINE(10.0.0.3, 301)`, `LINE(10.0.0.2, 200)`
- Expected: `{"total_requests": 5, "unique_visitors": 3, "error_requests": 2, "error_rate": 40.0, "malformed_lines": 0}`

### TC4 - Malformed and blank lines

- Input (5 lines):
  1. `LINE(10.0.0.1, 200)`
  2. `this is not a log line`
  3. an empty line
  4. `LINE(10.0.0.1, 503)`
  5. `10.0.0.9 - - [10/Oct/2023:13:55:36 +0000] "GET / HTTP/1.1"` (status and bytes are missing)
- Expected: `{"total_requests": 2, "unique_visitors": 1, "error_requests": 1, "error_rate": 50.0, "malformed_lines": 2}`

### TC5 - All requests are errors

- Input: `LINE(10.0.0.1, 400)`, `LINE(10.0.0.2, 404)`, `LINE(10.0.0.1, 500)`
- Expected: `{"total_requests": 3, "unique_visitors": 2, "error_requests": 3, "error_rate": 100.0, "malformed_lines": 0}`

### TC6 - Rounding down (1 error out of 3)

- Input: `LINE(10.0.0.1, 200)`, `LINE(10.0.0.2, 200)`, `LINE(10.0.0.3, 500)`
- Expected: `{"total_requests": 3, "unique_visitors": 3, "error_requests": 1, "error_rate": 33.33, "malformed_lines": 0}`

### TC7 - Rounding up (2 errors out of 3)

- Input: `LINE(10.0.0.1, 200)`, `LINE(10.0.0.2, 404)`, `LINE(10.0.0.3, 500)`
- Expected: `{"total_requests": 3, "unique_visitors": 3, "error_requests": 2, "error_rate": 66.67, "malformed_lines": 0}`
