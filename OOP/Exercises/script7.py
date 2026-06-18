'''Exercise 7: Bank Charges

Create a BankAccount class.

Requirements:

Instance attributes:

owner
balance

Static method:

calculate_transfer_fee(amount)

Rule:

Transfers below ₦5,000 → ₦10 fee
₦5,000–₦50,000 → ₦25 fee
Above ₦50,000 → ₦50 fee

Example:

print(BankAccount.calculate_transfer_fee(3000))
print(BankAccount.calculate_transfer_fee(20000))

Expected understanding:

Using static methods for business rules.'''