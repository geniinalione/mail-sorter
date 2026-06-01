import pytest
from pathlib import Path
from mailsorter.email_message import EmailMessage
from mailsorter.classifier import Classifier

def test_spam_priority_over_automated():
    classifier = Classifier()
    msg = EmailMessage(
        sender="no-reply@monitoring.internal",
        domain="monitoring.internal",
        subject="Выиграй айфон срочно!",
        body="Перейдите по ссылке, чтобы забрать приз",
        source_path=Path("dummy.txt"),
        raw=""
    )
    assert classifier.classify(msg) == "spam"

def test_empty_domain_goes_to_unsorted():
    classifier = Classifier()
    msg = EmailMessage(
        sender="strange_sender_without_at",
        domain="",
        subject="Непонятный вопрос",
        body="Просто какой-то текст без маркеров",
        source_path=Path("dummy.txt"),
        raw=""
    )
    assert classifier.classify(msg) == "unsorted"
