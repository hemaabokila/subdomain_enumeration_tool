#!/usr/bin/python3
import signal
from optparse import OptionParser
import asyncio
import dns.resolver
from colorama import Fore, Style

def wordlist(file_name):
    with open(file_name,"r") as file:
        wordlist = file.read().splitlines()
        return wordlist
    
def wildcard(domain):
    try:
        random_subdomain = f"random-{domain}"
        dns.resolver.resolve(random_subdomain, 'A')
        print(f"{Fore.GREEN}[-] Wildcard detected for {domain}{Style.RESET_ALL}")
        return True
    except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer, dns.exception.Timeout):
        return False
    
async def resolve_dns(subdomain, domain, dis_subdomains, semaphore):
    full_domain = f"{subdomain}.{domain}"
    try:
        async with semaphore:
            dns.resolver.resolve(full_domain, 'A')
            dis_subdomains.append(full_domain)
            print(f"{Fore.GREEN}[+] Found subdomain: {full_domain}{Style.RESET_ALL}")
    except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer):
        pass

async def main(domain, wordlist_file):
    print(F"""
{Fore.BLUE}
 ____  _   _ ____  ____   ___  __  __    _    ___ _   _ 
/ ___|| | | | __ )|  _ \ / _ \|  \/  |  / \  |_ _| \ | |
\___ \| | | |  _ \| | | | | | | |\/| | / _ \  | ||  \| |
 ___) | |_| | |_) | |_| | |_| | |  | |/ ___ \ | || |\  |
|____/ \___/|____/|____/ \___/|_|  |_/_/   \_\___|_| \_|                                
{Style.RESET_ALL}
---------------------------------------------
Developed by: Ibrahem abo kila
---------------------------------------------
    """)
    if not wordlist_file:
        subdomains = wordlist("/usr/share/wordlists/wordlistsub.txt")
    else:
        subdomains = wordlist(wordlist_file)

    if not subdomains:
        return

    if wildcard(domain):
        print(f"{Fore.RED}Wildcard detected for {domain}. Stopping enumeration.{Style.RESET_ALL}")
        return

    semaphore = asyncio.Semaphore(50)
    dis_subdomains = []
    tasks = []
    for subdomain in subdomains:
        tasks.append(resolve_dns(subdomain, domain, dis_subdomains, semaphore))
    
    await asyncio.gather(*tasks)

def exit_gracefully():
    print(f"{Fore.RED}\nProcess interrupted. Exiting gracefully...{Style.RESET_ALL}")
    exit(0)

if __name__ == "__main__":
    parser = OptionParser(F"""
{Fore.BLUE}
 ____  _   _ ____  ____   ___  __  __    _    ___ _   _ 
/ ___|| | | | __ )|  _ \ / _ \|  \/  |  / \  |_ _| \ | |
\___ \| | | |  _ \| | | | | | | |\/| | / _ \  | ||  \| |
 ___) | |_| | |_) | |_| | |_| | |  | |/ ___ \ | || |\  |
|____/ \___/|____/|____/ \___/|_|  |_/_/   \_\___|_| \_|                                
{Style.RESET_ALL}
---------------------------------------------
subdomain -d or --domain     >>   Target hostname "example.com"
subdomain -d or --wordlist   >>   Path to the wordlist
---------------------------------------------
Developed by: Ibrahem abo kila
---------------------------------------------
    """)
    parser.add_option("-d", "--domain", dest="domain", help=" example.com)")
    parser.add_option("-w", "--wordlist", dest="wordlist_file", help="Path to the wordlist")
    (options, args) = parser.parse_args()

    if not options.domain:
        print(parser.usage)
        print(f"{Fore.RED}Please provide a domain using -d or --domain{Style.RESET_ALL}")
    else:
        try:
            loop = asyncio.get_event_loop()
            loop.add_signal_handler(signal.SIGINT, exit_gracefully)
            loop.run_until_complete(main(options.domain, options.wordlist_file))
        except KeyboardInterrupt:
            print(f"{Fore.RED}\nExiting...{Style.RESET_ALL}")
        finally:
            loop.close()
