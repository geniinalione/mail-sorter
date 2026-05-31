from pathlib import Path
class EmailMessage:
    def __init__(self, sender, domain, subject, body, source_path, raw):
        self.sender = sender
        self.domain = domain
        self.subject = subject
        self.body = body
        self.source_path = source_path
        self.raw = raw