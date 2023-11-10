import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Read the Excel file
words_df = pd.read_csv("./data/complete_words.csv")


# Function to get a random word and its details
def get_word_of_the_day(df):
    word_row = df.sample().iloc[0]
    return word_row


# Select the word of the day
word_of_the_day = get_word_of_the_day(words_df)


# Function to format word details, omitting any NaN values
def format_word_details(word_row):
    details = "<html><body>"
    details += "<img src='https://followcrom.online/images/djrr.jpg' alt='Image' style='width:100%;max-width:600px;'>"
    details += f"<h2>Word of the Day: <b>{(word_row['word']).upper()}</b> ({word_row['word_type']})</h2>"
    if not pd.isna(word_row["definition"]):
        details += f"<p><b>Definition:</b> {word_row['definition']}</p>"
    if not pd.isna(word_row["examples"]):
        details += f"<p><b>Take it for a spin:</b> {word_row['examples']}</p>"

    # End of the HTML body
    details += "</body></html>"
    return details


# Format the word of the day into an email body
word_details = format_word_details(word_of_the_day)

print(word_details)  # For testing, to see the output in your console


# Function to send email with the word of the day
def send_email(word_details):
    fromaddr = os.getenv("GMAIL_ACCOUNT")
    toaddr = os.getenv("EMAIL_LIST").split(",")
    msg = MIMEMultipart()
    msg["From"] = "LEXicon John"
    msg["To"] = ", ".join(toaddr)

    # Format the date to add to the email subject
    date_str = datetime.datetime.now().strftime("%Y-%m-%d")
    msg["Subject"] = f"Word of the Day for {date_str}"

    body = word_details
    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(fromaddr, os.getenv("GMAIL_PASSWORD"))
        server.send_message(msg)
        server.quit()
        print("Email sent successfully")

    except smtplib.SMTPException as e:
        print(f"Failed to send email: {e}")


# Send the email with the word of the day
send_email(word_details)
