# Subdomain Enumeration Tool
[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
A simple Python-based subdomain enumeration tool designed to discover subdomains of a given domain using a wordlist. It uses DNS resolution to detect live subdomains and handles wildcard DNS detection.

## Features
- Enumerates subdomains using a wordlist.
- Detects wildcard DNS and avoids enumeration if a wildcard is present.
- Asynchronous DNS resolution for fast enumeration.
- Graceful handling of `Ctrl + C` (SIGINT) to stop the process cleanly.

## Requirements

Before running the tool, you need to install the following Python libraries:

- `dnspython`
- `signal`
- `os`
- `asyncio`
- `colorama`
- `argparse`


## installation
- **1.Clone the repository**:
```
git clone https://github.com/hemaabokila/subdomain_enumeration_tool.git
cd subdomain_enumeration_tool
sudo pip install .

```
- **2.Run the script with the following options**:
```
sub <bomain>
sub <bomain> -w <wordlist>

```


## Example:
- **To scan a target machine (google.com)**:


```
sub google.com
```

## Example Output
- **After scanning, the tool will show results like this (for subdomain)**
```
    
[+] Found subdomain: www.google.com
[+] Found subdomain: mail.google.com
[+] Found subdomain: smtp.google.com
```
## License
This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
## Author
- **Developed by Ibrahem abo kila**
- **Feel free to reach out for any questions or suggestions!**
  - `LinkedIn: Connect with me`
  - `YouTube: Watch my videos`





