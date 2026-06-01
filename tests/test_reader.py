import pytest
from pathlib import Path
from mailsorter.email_message import EmailMessage
from mailsorter.reader import EmailReader, UnreadableEmailError
def test_unreadable_file():
    reader = EmailReader()
    path_to = Path("tests/fixtures/empty.txt")
    with pytest.raises(UnreadableEmailError):
        reader.read(path_to)
def test_valid_email_read():
    reader = EmailReader()
    path_to = Path("tests/fixtures/valid_email.txt")
    mesg = reader.read(path_to)
    assert mesg.sender == "worker@company.ru"
    assert mesg.subject == "Запрос доступа"
    assert mesg.domain == "company.ru"
    assert "Привет, дай мне права" in mesg.body
def test_read_no_subject():
    reader = EmailReader()
    path_to = Path("tests/fixtures/no_subject.txt")
    mesg = reader.read(path_to)
    assert mesg.subject == ""
    assert mesg.sender == "hr@corp.local"
