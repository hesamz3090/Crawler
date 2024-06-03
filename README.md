# Crawler
A Python web crawler that follows links up to a specified depth.

## About Crawler
this Python web crawler fetches a webpage and recursively follows links up to a specified depth, using the requests and BeautifulSoup libraries. It maintains a set of visited URLs to avoid revisits and prints the total number of unique URLs visited.

## Installation
```
git clone https://github.com/hesamz3090/Crawler.git
```
- Installation on Windows:
```
c:\python3\python.exe -m pip install .
```
- Installation on Linux
```
sudo pip install .
```

## Dependencies:
Crawler depends on the `requests`,`bs4` python modules.
These dependencies can be installed using the requirements file:


## Usage
| Short Form | Long Form | Description                                     |
|------------|-----------|-------------------------------------------------|
| -i         | --input   | URL or path to the file containing URLs         |
| -o         | --output  | Path to the output file                         |
| -d         | --depth   | Depth to which the crawler should follow links  |
| -v         | --version | Show program's version number and exit          |
| -h         | --help    | Show this help message and exit                 |

### Examples

* To crawl a single URL up to a specified depth:
```python crawler.py "http://example.com" --depth 3```

* To crawl all URLs listed in urls.txt up to a specified depth:
``python crawler.py urls.txt --depth 2``

## Using Crawler as a module in your python scripts

**Example**

```python
import crawler 
response_list = crawler.main(["http://example.com"], 2)
```
The main function will return a list of unique responses

**Function Usage:**
* **urls**: Path to the file containing URLs.
* **depth**: Depth to which the crawler should follow links
* **output_file**: Path to the output file.

## License
Crawler is licensed under the MIT license.take a look at the [LICENSE](https://github.com/hesamz3090/Crawler/blob/main/LICENSE) for more information.

## Version
**Current version is 1.0**