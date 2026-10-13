class ClaimError(Exception):
    """Base exception for expense-claim problems."""
class ReceiptRequiredError(ClaimError):
    pass
def submit_claim(amount, has_receipt):
    if amount <= 0:
        raise ClaimError("claim amount must be positive")
    if amount > 1000 and not has_receipt:
        raise ReceiptRequiredError("a receipt is required above 1000")
