# Subdomain Enumeration Tool

A simple Python-based subdomain enumeration tool designed to discover subdomains of a given domain using a wordlist. It uses DNS resolution to detect live subdomains and handles wildcard DNS detection.

## Features
- Enumerates subdomains using a wordlist.
- Detects wildcard DNS and avoids enumeration if a wildcard is present.
- Asynchronous DNS resolution for fast enumeration.
- Graceful handling of `Ctrl + C` (SIGINT) to stop the process cleanly.

## Requirements

Before running the tool, you need to install the following Python libraries:

- `dnspython`
- `asyncio`
- `colorama`
- `optparse`

You can install them using pip:

```
pip install -r requirements.txt
```
## The required libraries:

- `dnspython`
- `asyncio`
- `colorama`
- `optparse`
## installation
- **1.Clone the repository**:
```
git clone https://github.com/hemaabokila/subdomain.git
cd subdomain
sudo mv wordlistsub.txt /usr/share/wordlists/wordlistsub.txt
pip install -r requirements.txt
sudo mv subdomain.py /usr/bin/subdomain && chmod +x /usr/bin/subdomain
```
- **2.Run the script with the following options**:
```
subdomain -d <bomain>
subdomain -d <bomain> -w <wordlist>

```


## Example:
- **To scan a target machine (google.com)**:


```
subdomain -d google.com
```

## Example Output
- **After scanning, the tool will show results like this (for subdomain)**
```
    
[+] Found subdomain: www.google.com
[+] Found subdomain: mail.google.com
[+] Found subdomain: smtp.google.com
```

## Author
- **Developed by Ibrahem abo kila**
- **Feel free to reach out for any questions or suggestions!**
  - `LinkedIn: Connect with me`
  - `YouTube: Watch my videos`





