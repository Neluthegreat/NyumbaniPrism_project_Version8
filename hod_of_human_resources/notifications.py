def send_payment_email(employee_email, subject, message):
    """
    Sends an email notification to the employee.
    In a real-world scenario, this would use Django's email backend
    or a third-party service like SendGrid or Mailgun.
    """
    # Simulate sending email
    print("=== EMAIL NOTIFICATION SIMULATION ===")
    print(f"To: {employee_email}")
    print(f"Subject: {subject}")
    print(f"Message: {message}")
    print("Email sent successfully (simulated).")
    print("-" * 40)
    return True  # Return success status

def send_payment_sms(employee_phone, message):
    """
    Sends an SMS notification to the employee.
    In a real-world scenario, this would use a service like Twilio or Vonage.
    """
    # Simulate sending SMS
    print("=== SMS NOTIFICATION SIMULATION ===")
    print(f"To: {employee_phone}")
    print(f"Message: {message}")
    print("SMS sent successfully (simulated).")
    print("-" * 40)
    return True  # Return success status
