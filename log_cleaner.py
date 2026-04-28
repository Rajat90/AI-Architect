raw_logs = [
    "  Invoice_Bot | FAILED | FileNotFoundError  ",
    "HR-Bot | SUCCESS | None",
    "  invoice_bot | FAILED | ValueError  ",
    "Payroll_Bot|FAILED|OSError",
    "  HR-Bot | failed | TimeoutError  ",
    "PAYROLL_BOT | SUCCESS | None",
]

name_map = {
    "invoice_bot": "Invoice_Bot",
    "hr_bot": "HR_Bot",
    "payroll_bot": "Payroll_Bot"
}

def clean_logs(raw_logs):

    # Using a list comprehension, strip leading/trailing whitespace from every entry.
    stripped_logs = [logs.strip() for logs in raw_logs]
    

    # Each entry is now a string with | as separator. Using a list comprehension, split every entry into a list of 3 fields.
    #split_logs = [logs.split("|") for logs in stripped_logs ]
    split_logs = [[field.strip() for field in logs.split("|")] for logs in stripped_logs]
    
#Using a list comprehension, build a list of dicts from split_logs. While building, clean each field:

    cleaned_logs = [
        {
            "bot": name_map.get(fields[0].replace("-", "_").lower(), fields[0]),
            "status": fields[1].strip().upper(),
            "error": fields[2].strip()
        }
        for fields in split_logs
    ]
    return cleaned_logs


if __name__ == "__main__":
    cleaned_logs = clean_logs(raw_logs)
    for log in cleaned_logs:
        print(log)