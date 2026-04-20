from pathlib import Path
import shutil
from datetime import datetime

# --- CONFIGURATION ---
INVOICE_FOLDER = Path("invoices")
ARCHIVED_FOLDER = INVOICE_FOLDER / "archived"
EXCEPTIONS_FOLDER = INVOICE_FOLDER / "exceptions"
REPORT_FILE = INVOICE_FOLDER / "processing_report.txt"

# --- SETUP FOLDERS ---
ARCHIVED_FOLDER.mkdir(parents=True, exist_ok=True)
EXCEPTIONS_FOLDER.mkdir(parents=True, exist_ok=True)

def validate_invoice(content, filename):
    """Validates Invoice content.
        Returns (is_valid, reason) 
    """
    required_fields = ["Invoice Number","Vendor","Amount","Date"]

    for field in required_fields:
        if field not in content:
            return False, f"Missing field: {field}"
        
    # Extract and validate amount
    for line in content.splitlines():
        if line.startswith("Amount"):
            try:
                amount = float(line.split(":")[1].strip())
                if amount <= 0:
                    return False, "Amount must be greater than 0"
            except ValueError:
                return False, "Amount is not a valid number"

    return True, "Valid"

def process_invoices():
    """
    Reads all .txt invoices from folder,
    validates each one, moves to archived or exceptions,
    generates timestamped report.
    """

# glob() replaces your manual loop + endswith() check
    try:
        invoice_files = list(INVOICE_FOLDER.glob("*.txt"))
    except OSError as e:
        print(f"❌ Cannot access invoice folder: {e}")
        return # Stop here
    

    # if not invoice_files:
    #     print("No invoices found to process.")
    #     return

    
    print(f"Found {len(invoice_files)} invoice(s) to process.\n")
    results = []

    for invoice_path in invoice_files:
        invoice_id = invoice_path.stem
        print(f"Processing: {invoice_path.name}")
    
        try:
            content = invoice_path.read_text(encoding="utf-8")
            is_valid, reason = validate_invoice(content, invoice_path.name)

            if is_valid:
                destination = ARCHIVED_FOLDER / invoice_path.name
                try:
                    shutil.move(str(invoice_path), str(destination))
                    status = "ARCHIVED"
                except (OSError, shutil.Error) as e:
                    print(f"  ❌ Could not move {invoice_path.name}: {e}")
                    status = "EXCEPTION"
                    reason = f"Move failed: {e}"
            else:
                destination = EXCEPTIONS_FOLDER / invoice_path.name
                try:
                    shutil.move(str(invoice_path), str(destination))
                    status = "EXCEPTION"
                except (OSError, shutil.Error) as e:
                    print(f"  ❌ Could not move {invoice_path.name}: {e}")
                    status = "EXCEPTION"
                    reason = f"Move failed: {e}"

        except FileNotFoundError:
            print(f"  ⚠️ File vanished mid-run: {invoice_path.name}")
            status = "EXCEPTION"
            reason = "File not found during read"

        finally:
            # ← Runs for EVERY invoice, always
            print(f"  🔄 Attempted: {invoice_path.name}")
            results.append({
                "invoice_id": invoice_id,
                "status": status,
                "reason": reason,
                "filename": invoice_path.name
            })
            print(f"  Status : {status}")
            print(f"  Reason : {reason}\n")


    # --- GENERATE REPORT ---
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    archived_count = sum(1 for r in results if r["status"] == "ARCHIVED")
    exception_count = sum(1 for r in results if r["status"] == "EXCEPTION")

    report_lines = [
        f"INVOICE PROCESSING REPORT",
        f"Generated : {timestamp}",
        f"Total     : {len(results)}",
        f"Archived  : {archived_count}",
        f"Exceptions: {exception_count}",
        f"{'─' * 40}"
    ]

    for r in results:
        report_lines.append(f"{r['invoice_id']} | {r['status']} | {r['reason']}")

    report_text = "\n".join(report_lines)

    # .write_text() replaces open() + write() + close()
    try:
        REPORT_FILE.write_text(report_text, encoding="utf-8")
        print(report_text)
        print(f"\nReport saved to: {REPORT_FILE}")
    except OSError as e:
        print(f"❌ Could not save report: {e}")


if __name__ == "__main__":
    process_invoices()