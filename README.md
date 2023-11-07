# Word of the Day

## Overview

**Word of the Day** uses a Python script to select a random word from a CSV file. That word, along with its definition and example sentences, are emailed to a list recipients. The email lands in their inboxes every day at a scheduled time, using GitHub Actions.

<div align="center">
  <img src="https://www.followcrom.online/embeds/wotd.png" width="250">
</div>

## Setup

To set up the project for your own use, follow these steps:

1. Clone the repository to your local machine:
   `git clone https://github.com/followcrom/word-of-the-day.git`
2. Create environmental variables with the following Repository secrets in your GitHub repository settings:
   `GMAIL_ACCOUNT`
   `GMAIL_PASSWORD`
   `EMAIL_LIST`.
3. Customize the `complete_words.csv` with your own words.

## Usage

Once set up, the GitHub Action will run automatically. You can modify the schedule in the `.github/workflows/word_of_the_day.yml` file if you wish to change the email delivery time.

## Requirements

- GitHub Account
- Python 3.x
- SMTP-compatible Email Account

## Dependencies

The `requirements.txt` file lists all the Python libraries needed to run the script. They can be installed using the following command:

`pip install -r requirements.txt`

## Contact

🌐 followCrom: [followcrom.online](https://followcrom.online/index.html) 🌐

📫 followCrom: [get in touch](https://followcrom.online/contact/contact.php) 📫

## Contributing

😊 Contributions to the **Word of the Day** project are welcome. 😊

👷 Feel free to open a pull request or branch from this project. 👷

## License

This project is open source and available under the MIT License.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
