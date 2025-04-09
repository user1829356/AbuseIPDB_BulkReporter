# AbuseIPDB Bulk Reporter

This is a simple Python script to help you format and prepare bulk abuse reports for submission to [AbuseIPDB](https://www.abuseipdb.com/). The script takes a list of IP addresses from a CSV file and outputs a properly structured CSV file with the required fields: `IP`, `Categories`, `ReportDate`, and `Comment`.

---

## 🚀 Features

- Accepts a CSV file with a list of IPs (one per line)
- Allows selection of AbuseIPDB category IDs
- Converts human-readable timestamps into ISO 8601 format
- Outputs a new `output.csv` ready for upload to AbuseIPDB
- Timezone-aware (default: `Europe/Budapest`)

---

## 🧰 Requirements

Install required packages:

```bash
pip install -r requirements.txt
```

Contents of `requirements.txt`:

```
pytz
```

---

## 📝 Usage

```bash
python3 AbuseIPDB_bulkReport.py your_file.csv
```

Replace `your_file.csv` with your actual input file.

You’ll be prompted to:
1. Select AbuseIPDB category IDs (e.g., `3,7,18`)
2. Enter the attack timestamp in this format: `YYYY.MM.DD.HH:MM:SS`

---

## 📥 Input File Format

Your input `.csv` file should contain **one IP address per line**:

```
192.168.1.1
8.8.8.8
1.2.3.4
```

---

## 📤 Output File

After running the script, you'll get an `output.csv` file like this:

```
IP,Categories,ReportDate,Comment
192.168.1.1,"7,18","2025-04-09T22:00:00+02:00","Reported via script"
8.8.8.8,"7,18","2025-04-09T22:00:00+02:00","Reported via script"
1.2.3.4,"7,18","2025-04-09T22:00:00+02:00","Reported via script"
```

You can upload this directly to [AbuseIPDB’s Bulk Reporter](https://www.abuseipdb.com/bulk-report).

---

## 🌍 Timezone Handling

The script uses the `Europe/Budapest` timezone by default. To use a different timezone, modify this line in the script:

```python
local_tz = pytz.timezone('Europe/Budapest')
```

---

## ✅ Category IDs

When you run the script, it will display a list of AbuseIPDB categories like this:

```
ID    Title
1     DNS Compromise
2     DNS Poisoning
3     Fraud Orders
...
23    IoT Targeted
```

You can then enter one or more category IDs (e.g., `7,18` for Phishing and Brute-Force).

---

## 🪪 License

MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software.

---
