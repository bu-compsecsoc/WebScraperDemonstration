# Web Scraper 

- webcrawler.py: This project contains a web scraper & crawler which takes a link from the user and collects all email addresses on the page and stores them in a json file.
The crawler will then alter the URL of the website to navigate through pagination.
It is currently hard coded to stop after 35 pages.

- **Drivers** can be located in the [web drivers](web drivers) folder, move the driver you require to the main directory



## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

This project requires a few external dependencies which can be installed using the follow commands:
- **pip install selenium**
- **pip install beautifulsoup4**
- **pip install validate_email**

## Usage

- webCrawler.py: Create a json file called **"emailADdresses.json"** Run the python file and enter the target URL. If you would like to change the amount of pages it searches through. Change **"if self.pagesOpened >= 35:"** (located on **line 33**, within the **click_next_page()** function) to your desired amount.

## Contributing

You are welcome to make changes however you see fit, however ensure your **output json file** is **included** within **".gitignore"**

## License

This project is licensed under the [MIT License](LICENSE) - see [LICENSE](LICENSE) file for details.