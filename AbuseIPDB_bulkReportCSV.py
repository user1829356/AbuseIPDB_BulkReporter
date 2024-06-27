import csv
import pytz
from datetime import datetime

def main():
    import sys
    if len(sys.argv) != 2:
        print("Usage: python3 AbuseIPDB_bulkReport.py Filename.csv")
        return

    filename = sys.argv[1]
    output_filename = 'output.csv'

    # Show category options
    print("Here are the available categories:")
    print("ID\tTitle")

    categories = {
    1: ("DNS Compromise", "Altering DNS records resulting in improper redirection."),
    2: ("DNS Poisoning", "Falsifying domain server cache (cache poisoning)."),
    3: ("Fraud Orders", "Fraudulent orders."),
    4: ("DDoS Attack", "Participating in distributed denial-of-service (usually part of botnet)."),
    5: ("FTP Brute-Force", ""),
    6: ("Ping of Death", "Oversized IP packet."),
    7: ("Phishing", "Phishing websites and/or email."),
    8: ("Fraud VoIP", ""),
    9: ("Open Proxy", "Open proxy, open relay, or Tor exit node."),
    10: ("Web Spam", "Comment/forum spam, HTTP referer spam, or other CMS spam."),
    11: ("Email Spam", "Spam email content, infected attachments, and phishing emails. Note: Limit comments to only relevant information (instead of log dumps) and be sure to remove PII if you want to remain anonymous."),
    12: ("Blog Spam", "CMS blog comment spam."),
    13: ("VPN IP", "Conjunctive category."),
    14: ("Port Scan", "Scanning for open ports and vulnerable services."),
    15: ("Hacking", ""),
    16: ("SQL Injection", "Attempts at SQL injection."),
    17: ("Spoofing", "Email sender spoofing."),
    18: ("Brute-Force", "Credential brute-force attacks on webpage logins and services like SSH, FTP, SIP, SMTP, RDP, etc. This category is separate from DDoS attacks."),
    19: ("Bad Web Bot", "Webpage scraping (for email addresses, content, etc) and crawlers that do not honor robots.txt. Excessive requests and user agent spoofing can also be reported here."),
    20: ("Exploited Host", "Host is likely infected with malware and being used for other attacks or to host malicious content. The host owner may not be aware of the compromise. This category is often used in combination with other attack categories."),
    21: ("Web App Attack", "Attempts to probe for or exploit installed web applications such as a CMS like WordPress/Drupal, e-commerce solutions, forum software, phpMyAdmin and various other software plugins/solutions."),
    22: ("SSH", "Secure Shell (SSH) abuse. Use this category in combination with more specific categories."),
    23: ("IoT Targeted", "Abuse was targeted at an 'Internet of Things' type device. Include information about what type of device was targeted in the comments.")
    }
    
    for id, title in categories.items():
        print(f"{id}\t{title}")

    # Instructions for entering categories
    print("\nEnter one or more category IDs separated by commas (e.g., 1,3,5):")

    # Get user input for categories
    category_input = input("Enter the category numbers: ")
    category_ids = category_input.split(',')
    formatted_categories = ",".join([str(int(id.strip())) for id in category_ids if int(id.strip()) in categories])

    # Get user input for the attack time
    attack_time_input = input("Enter the attack time (YYYY.MM.DD.HH:MM:SS): ")
    local_tz = pytz.timezone('Europe/Budapest')# should be changed if the event happened in another timezone
    naive_datetime = datetime.strptime(attack_time_input, '%Y.%m.%d.%H:%M:%S')
    local_datetime = local_tz.localize(naive_datetime, is_dst=None)
    iso_datetime = local_datetime.isoformat()

    # Read the CSV file, process and write to a new CSV file
    with open(filename, newline='') as csvfile, open(output_filename, 'w', newline='') as outputfile:
        reader = csv.reader(csvfile)
        writer = csv.writer(outputfile)
        writer.writerow(['IP', 'Categories', 'ReportDate', 'Comment'])  # Write headers
        for row in reader:
            ip = row[0]
            writer.writerow([ip, f'"{formatted_categories}"', iso_datetime, "Reported via script"])

    print("Output written to", output_filename)

if __name__ == "__main__":
    main()
