import os.path
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

# Define the scopes
SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

def authenticate_gmail():
    """Authenticate and return Gmail service instance."""
    creds = None
    # Token file to store the user's access and refresh tokens
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=8080)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return build('gmail', 'v1', credentials=creds)

def filter_emails(service, query):
    """Filter emails based on a search query and return the messages."""
    try:
        results = service.users().messages().list(userId='me', q=query).execute()
        messages = results.get('messages', [])
        
        if not messages:
            print("No emails found matching the query.")
            return []

        print(f"{len(messages)} emails found:")
        for message in messages[:10]:  # Display up to 10 emails
            msg_data = service.users().messages().get(userId='me', id=message['id']).execute()
            subject = next((header['value'] for header in msg_data['payload']['headers'] if header['name'] == 'Subject'), "(No Subject)")
            print(f"- ID: {message['id']}, Subject: {subject}")
        return messages
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def delete_emails(service, messages):
    """Delete specified emails."""
    try:
        for message in messages:
            msg_id = message['id']
            service.users().messages().delete(userId='me', id=msg_id).execute()
            print(f"Deleted email ID: {msg_id}")
        print("All selected emails deleted.")
    except Exception as e:
        print(f"An error occurred while deleting emails: {e}")

def mark_emails_as_read(service, messages):
    """Mark specified emails as read."""
    try:
        for message in messages:
            msg_id = message['id']
            service.users().messages().modify(userId='me', id=msg_id, body={'removeLabelIds': ['UNREAD']}).execute()
            print(f"Marked email ID {msg_id} as read.")
        print("All selected emails marked as read.")
    except Exception as e:
        print(f"An error occurred while marking emails as read: {e}")

def main():
    """Main interactive Gmail app."""
    service = authenticate_gmail()
    
    while True:
        print("\n=== Gmail App Menu ===")
        print("1. Search emails")
        print("2. Delete emails")
        print("3. Mark emails as read")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            query = input("Enter your search query (e.g., 'is:unread'): ")
            messages = filter_emails(service, query)
        elif choice == '2':
            query = input("Enter your search query to find emails to delete (e.g., 'older_than:30d'): ")
            messages = filter_emails(service, query)
            if messages:
                confirm = input("Delete all matching emails? (yes/no): ")
                if confirm.lower() == 'yes':
                    delete_emails(service, messages)
        elif choice == '3':
            query = input("Enter your search query to find emails to mark as read (e.g., 'is:unread'): ")
            messages = filter_emails(service, query)
            if messages:
                confirm = input("Mark all matching emails as read? (yes/no): ")
                if confirm.lower() == 'yes':
                    mark_emails_as_read(service, messages)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
