# Log Report

An Apache-style access log is located at `/app/access.log`. Parse it and produce a JSON summary report.

## Success Criteria

1. Read and parse every line of `/app/access.log`.
2. Write a valid JSON file to `/app/report.json`.
3. The JSON object must contain exactly these keys:
   - `total_requests` — integer, the total number of log entries.
   - `unique_ips` — integer, the count of distinct client IP addresses.
   - `top_path` — string, the request path that appears most often.
