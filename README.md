Gmail Email Management App   
This Python app interacts with Gmail to help you manage your inbox efficiently. With this tool, you can search, mark, and delete emails directly from the command line.

Features
- Search Emails: Filter emails using custom Gmail queries (e.g., unread emails or those older than 30 days).  
- Mark Emails as Read: Quickly clean up your inbox by marking selected emails as read.  
- Delete Emails: Safely delete emails that match specific criteria.  


Getting Started

Prerequisites
1. Python 3.8 or above: Make sure Python is installed on your machine. [Download Python](https://www.python.org/downloads/).  
2. Required Python Libraries: Install the following libraries using `pip`:
   ```bash
   pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
   ```
3. Google Cloud Console Setup:
   - Enable the Gmail API for your Google Cloud project.
   - Download your `credentials.json` file from the Cloud Console and place it in the project directory.


How to Use

1. Clone this repository:
   ```bash
   git clone https://github.com/Jfsmith7125/gmail_manager.git
   cd gmail_manager
   ```

2. Add your `credentials.json` file to the project directory.

3. Run the app:
   ```bash
   python main.py
   ```

4. Follow the interactive menu:
   - Enter search queries (e.g., `is:unread`, `older_than:30d`) to filter emails.
   - Choose actions like marking emails as read or deleting them.

Example Queries
Here are some Gmail search queries you can try:
- Find unread emails: `is:unread`
- Find emails older than 30 days: `older_than:30d`
- Find emails with attachments: `has:attachment`
- Find emails from a specific sender: `from:example@gmail.com`

Project Structure
- `main.py`: The main script containing all the logic for interacting with Gmail.
- `credentials.json`: Your Google API credentials file (not included in the repository).  

Roadmap
Planned features for future versions:
- Exporting email data to CSV.
- Archiving emails instead of deleting.
- Adding pagination for large search results.

License
This project is licensed under the MIT License. Feel free to use, modify, and share.




