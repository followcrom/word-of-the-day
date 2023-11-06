# Word of the Day

## Overview

**Word of the Day** is a project designed to send a random word along with its definition, type, and an example sentence to a specified list of email recipients every day at a scheduled time using GitHub Actions.

![Word of the Day](https://www.followcrom.online/embeds/wotd.png "Word of the Day")

## Features

- **Daily Learning:** Receive a new word every day to expand your vocabulary.
- **Automated Emails:** The word of the day is automatically sent without any manual intervention.
- **Customizable:** Easy to add or remove words from the list, as well as to change the recipient list.

## How It Works

The project uses a Python script to select a random word from a CSV file and then sends an email to all listed recipients using SMTP. GitHub Actions is set up to run this script once every day at 12:30 UTC.

## Setup

To set up the project for your own use, follow these steps:

1. Clone the repository to your local machine.
2. Set up the required secrets (`GMAIL_ACCOUNT` and `GMAIL_PASSWORD`) in your GitHub repository settings.
3. Customize the `word_list.csv` with your desired words.
4. Update the recipient list in the `word_of_the_day.py` script.
5. Push changes to your repository to trigger the GitHub Action.

## Usage

Once set up, the GitHub Action will run automatically. You can modify the schedule in the `.github/workflows/word_of_the_day.yml` file if you wish to change the email delivery time.

## Requirements

- GitHub Account
- Python 3.x
- SMTP-compatible Email Account

## Dependencies

The `requirements.txt` file lists all the Python libraries needed to run the script. They can be installed using the following command:

`pip install -r requirements.txt`

## Contributing

Contributions to the "Word of the Day" project are welcome. Please ensure to update tests as appropriate.

## License

This project is open source and available under the MIT License. See the LICENSE file for details.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

## Contact

🌐 followCrom: [followcrom.online](https://followcrom.online/index.html) 🌐

📫 followCrom: [get in touch](https://followcrom.online/contact/contact.php) 📫
