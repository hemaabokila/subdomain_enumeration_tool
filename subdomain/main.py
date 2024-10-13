import signal
import argparse
import asyncio
import dns.resolver
from colorama import Fore, Style
import os

class Subdomain:
    def __init__(self, domain, file_name=None):
        self.domain = domain
        self.file_name = file_name
        self.wordlist_file = os.path.join("wordlist/wordlist.txt")

    def load_wordlist(self, dist_file):
        with open(dist_file, "r") as file:
            wordlist = file.read().splitlines()
            return wordlist

    def wildcard(self):
        try:
            random_subdomain = f"random-{self.domain}"
            dns.resolver.resolve(random_subdomain, 'A')
            print(f"{Fore.GREEN}[-] Wildcard detected for {self.domain}{Style.RESET_ALL}")
            return True
        except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer, dns.exception.Timeout):
            return False

    async def resolve_dns(self, subdomain, dis_subdomains, semaphore):
        full_domain = f"{subdomain}.{self.domain}"
        try:
            async with semaphore:
                dns.resolver.resolve(full_domain, 'A')
                dis_subdomains.append(full_domain)
                print(f"{Fore.GREEN}[+] Found subdomain: {full_domain}{Style.RESET_ALL}")
        except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer):
            pass

    async def run(self):
        print(F"""
    {Fore.BLUE}
     ____  _   _ ____  ____   ___  __  __    _    ___ _   _ 
    / ___|| | | | __ )|  _ \\ / _ \\|  \\/  |  / \\  |_ _| \\ | |
    \\___ \\| | | |  _ \\| | | | | | | |\\/| | / _ \\  | ||  \\| |
     ___) | |_| | |_) | |_| | |_| | |  | |/ ___ \\ | || |\\  |
    |____/ \\___/|____/|____/ \\___/|_|  |_/_/   \\_\\___|_| \\_|                                 
    {Style.RESET_ALL}
    ---------------------------------------------
    Developed by: Ibrahem abo kila
    ---------------------------------------------
        """)

        if not self.file_name:
            subdomains = self.load_wordlist(self.wordlist_file)
        else:
            subdomains = self.load_wordlist(self.file_name)

        if not subdomains:
            return

        if self.wildcard():
            print(f"{Fore.RED}Wildcard detected for {self.domain}. Stopping enumeration.{Style.RESET_ALL}")
            return

        semaphore = asyncio.Semaphore(50)
        dis_subdomains = []
        tasks = []
        for subdomain in subdomains:
            tasks.append(self.resolve_dns(subdomain, dis_subdomains, semaphore))

        await asyncio.gather(*tasks)

    def exit_gracefully(self):
        print(f"{Fore.RED}\nProcess interrupted. Exiting gracefully...{Style.RESET_ALL}")
        exit(0)

def main():
    parser = argparse.ArgumentParser(description='Subdomain Enumeration Tool')
    parser.add_argument("domain", type=str, help="example.com")
    parser.add_argument("-w", "--wordlist", type=str, help="Path to the wordlist")
    args = parser.parse_args()

    if not args.domain:
        print(parser.usage)
        print(f"{Fore.RED}Please provide a domain using -d or --domain{Style.RESET_ALL}")
    else:
        try:
            loop = asyncio.get_event_loop()
            loop.add_signal_handler(signal.SIGINT, Subdomain.exit_gracefully)
            checker = Subdomain(domain=args.domain, file_name=args.wordlist)
            loop.run_until_complete(checker.run())
        except KeyboardInterrupt:
            print(f"{Fore.RED}\nExiting...{Style.RESET_ALL}")
        finally:
            loop.close()

if __name__ == "__main__":
    main()
