# Security Headers Analyzer

This is a simple Python-based tool that checks important HTTP security headers of a website.

I built this project while learning web security and understanding how security headers protect web applications.

## What This Tool Does

- Sends a request to the given URL
- Checks for common security headers
- Displays which headers are present and which are missing
- Shows basic server information

## Security Headers Checked

- Content-Security-Policy
- X-Frame-Options
- X-XSS-Protection
- Strict-Transport-Security
- X-Content-Type-Options

## Requirements

Python 3.x

Install required package:

pip install -r requirements.txt

## How to Run

python scanner.py

Then enter the target URL (example: https://example.com)

## Example Output

[+] X-Frame-Options Found  
[-] Content-Security-Policy Missing  

## Purpose

This tool is created for learning and educational purposes only.  
Use it only on websites you own or have permission to test.

## Future Improvements

- Add CLI arguments support
- Generate JSON report
- Add SSL certificate analysis
- Add colored terminal output

---

Author: scambaiterkshitij
