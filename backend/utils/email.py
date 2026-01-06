import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from core.config import settings

def send_email(email_to: str, subject: str, html_content: str):
    if not settings.SMTP_HOST:
        print("DEBUG: SMTP_HOST is not set. Check if your .env file is being loaded correctly.")
        return

    print(f"DEBUG: Attempting to send email to {email_to} via {settings.SMTP_HOST}...")
    
    message = MIMEMultipart()
    message["From"] = f"{settings.EMAILS_FROM_NAME} <{settings.EMAILS_FROM_EMAIL}>"
    message["To"] = email_to
    message["Subject"] = subject
    message.attach(MIMEText(html_content, "html"))

    try:
        # Use SMTP_SSL for port 465, regular SMTP for others (like 587)
        if settings.SMTP_PORT == 465:
            server_class = smtplib.SMTP_SSL
        else:
            server_class = smtplib.SMTP

        with server_class(settings.SMTP_HOST, settings.SMTP_PORT) as server:
            server.set_debuglevel(0)
            if settings.SMTP_PORT == 587:
                server.starttls()
            
            if settings.SMTP_USER and settings.SMTP_PASSWORD:
                server.login(settings.SMTP_USER, settings.SMTP_PASSWORD)
            
            server.send_message(message)
            print(f"SUCCESS: Email sent to {email_to}")
    except Exception as e:
        print(f"ERROR: Failed to send email: {type(e).__name__}: {e}")

def send_otp_email(email_to: str, otp_code: str):
    subject = "Verification Code for Unibuy"
    html_content = f"""
    <html>
        <body>
            <h2>Welcome to Unibuy!</h2>
            <p>Your verification code is: <strong>{otp_code}</strong></p>
            <p>This code will expire in 5 minutes.</p>
            <p>If you did not sign up for Unibuy, please ignore this email.</p>
        </body>
    </html>
    """
    send_email(email_to, subject, html_content)

def send_password_reset_email(email_to: str, otp_code: str):
    subject = "Password Reset Code for Unibuy"
    html_content = f"""
    <html>
        <body>
            <h2>Password Reset Request</h2>
            <p>Your password reset code is: <strong>{otp_code}</strong></p>
            <p>This code will expire in 5 minutes.</p>
            <p>If you did not request a password reset, please ignore this email.</p>
        </body>
    </html>
    """
    send_email(email_to, subject, html_content)
