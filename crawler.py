import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import argparse
import os
import re

# Author and banner information
__author__ = "Hesam Aghajani"
__version__ = "1.0"
__description__ = "A Python web crawler that follows links up to a specified depth."

regex = re.compile(
    r'^(?:http|ftp)s?://'  # http:// or https://
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
    r'localhost|'  # localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
    r'(?::\d+)?'  # optional port
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)


def main(urls, depth):
    """
    Recursively crawls websites starting from a list of URLs up to a specified depth, collecting URLs.

    Args:
        urls (list): A list of URLs to start crawling from.
        depth (int): The depth to which the crawler should follow links. A depth of 0 means no further links will be followed.

    Returns:
        list: A list of unique URLs visited during the crawl.
    """
    visited = set()
    not_visited = set(urls)

    while not_visited and depth > 0:
        next_level = set()
        for url in not_visited:
            if 'http' not in url:
                url = 'http://' + url
            if url in visited:
                continue
            print(f"Crawling: {url} (Depth: {depth})")
            print('\n')
            try:
                response = requests.get(url)
                soup = BeautifulSoup(response.text, 'html.parser')
                if re.match(regex, url):
                    visited.add(url)

                links = [urljoin(url, a.get('href')) for a in soup.find_all('a', href=True)]
                next_level.update(link for link in links if link not in visited and re.match(regex, link))
            except:
                pass

        not_visited = next_level
        depth -= 1

    return list(set(visited | not_visited))


if __name__ == "__main__":
    banner = f"""
 ██████╗██████╗  █████╗ ██╗    ██╗██╗     ███████╗██████╗ 
██╔════╝██╔══██╗██╔══██╗██║    ██║██║     ██╔════╝██╔══██╗
██║     ██████╔╝███████║██║ █╗ ██║██║     █████╗  ██████╔╝
██║     ██╔══██╗██╔══██║██║███╗██║██║     ██╔══╝  ██╔══██╗
╚██████╗██║  ██║██║  ██║╚███╔███╔╝███████╗███████╗██║  ██║
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚══╝╚══╝ ╚══════╝╚══════╝╚═╝  ╚═╝                                                                                                   
 
Version: {__version__}
Author: {__author__}
Description: {__description__}
    """
    print(banner)

    parser = argparse.ArgumentParser(
        description=__description__,
        epilog=f"Author: {__author__} | Version: {__version__}",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("input", help="URL or path to the file containing URLs")
    parser.add_argument("-d", "--depth", type=int, default=2, help="Depth to which the crawler should follow links")
    parser.add_argument("-o", "--output_file", help="Path to the output file")
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")

    args = parser.parse_args()

    # Determine if input is a URL or a file path
    if os.path.isfile(args.input):
        with open(args.input, 'r') as f:
            urls = [line.strip() for line in f if line.strip()]
    else:
        urls = [args.input]

    result = main(urls, args.depth)

    if args.output_file:
        with open(args.output_file, 'w') as f:
            for url in result:
                f.write(url + '\n')
    else:
        for url in result:
            print(url)
    print('\n')
    print('Completed total unique URLs visited: ' + str(len(result)))
