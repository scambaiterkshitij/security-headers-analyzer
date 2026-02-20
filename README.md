# Security Headers Analyzer

Security Headers Analyzer is a Python command-line tool designed to inspect HTTP security headers and evaluate the security posture of a web application. The tool analyzes response headers, checks SSL/TLS availability, and provides a basic security assessment based on industry-recommended header configurations.

This project is intended for educational purposes, research, and authorized security testing only.

Overview

Web applications rely on properly configured HTTP security headers to defend against common web-based attacks such as Cross-Site Scripting (XSS), Clickjacking, MIME type sniffing, downgrade attacks, and insecure content loading.

Security Headers Analyzer automates the process of retrieving and evaluating these headers from a target URL. It helps developers, students, and security enthusiasts understand how security headers contribute to web application protection and where misconfigurations may exist.

Key Objectives

- Identify missing or misconfigured security headers
- Improve awareness of secure web configuration practices
- Provide a simple and lightweight assessment tool
- Serve as a learning project for web security fundamentals

Features

- Fetch and analyze HTTP response headers
- Check presence and value of critical security headers
- Validate HTTPS and SSL/TLS availability
- Display HTTP status codes
- Provide a basic security scoring mechanism
- Clean and simple command-line interface
- Easily extendable modular code structure

Security Headers Checked

The tool currently evaluates the following headers:

- Content-Security-Policy (CSP)
- X-Frame-Options
- X-XSS-Protection
- Strict-Transport-Security (HSTS)
- X-Content-Type-Options
- Referrer-Policy (if implemented)
- Permissions-Policy (if implemented)

Installation

Clone the repository:

git clone https://github.com/scambaiterkshitij/security-headers-analyzer.git

Navigate to the project directory:

cd security-headers-analyzer

Install required dependencies:

pip install -r requirements.txt

Usage

Run the script by providing a target URL:

python headers_checker.py https://example.com

Replace the example URL with the domain you want to analyze.

The tool will retrieve the response headers and display the analysis results in the terminal.

How It Works

1. Sends an HTTP/HTTPS request to the target.
2. Collects response headers from the server.
3. Compares header presence against recommended security headers.
4. Evaluates configuration strength.
5. Outputs results in a structured format.

Use Cases

- Learning web application security basics
- Quick header inspection during security assessments
- Developer self-auditing before production deployment
- Academic cybersecurity projects

Limitations

- Provides only basic header analysis
- Does not perform deep vulnerability scanning
- Does not replace professional security testing tools

Warning

This tool must only be used on systems and websites you own or have explicit authorization to test. Unauthorized security testing may violate laws, terms of service, or local regulations. The author assumes no responsibility for misuse or illegal activities performed using this tool.

License

Specify your preferred license here (for example, MIT License).
