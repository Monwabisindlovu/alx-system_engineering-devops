0x0F. Load balancer
Overview
This project focuses on improving our web stack for redundancy and scalability by doubling the number of web servers and introducing a load balancer. The goal is to enhance infrastructure reliability and handle increased traffic. Bash scripts are required to automate the configuration of new Ubuntu servers to meet project specifications.

Concepts
Load balancer
Web stack debugging
Background Context
Additional servers have been provided:

gc-[STUDENT_ID]-web-02-XXXXXXXXXX
gc-[STUDENT_ID]-lb-01-XXXXXXXXXX
Tasks
0. Double the number of webservers
Configure web-02 to be identical to web-01 using a Bash script (0-custom_http_response_header). Nginx should include a custom header (X-Served-By) in its HTTP response.

Requirements:

Configure Nginx on web-01 and web-02.
Custom HTTP header name: X-Served-By.
Custom HTTP header value: Hostname of the server Nginx is running on.
Write a Bash script to configure a new Ubuntu machine accordingly (0-custom_http_response_header).
Ignore SC2154 for Shellcheck.
