import pytest
from pathlib import Path
from mailsorter.email_message import EmailMessage
from mailsorter.classifier import Classifier

@pytest.mark.parametrize("subject, body, domain, expected_category", [
    ("Внимание! Выиграй приз", "Скидки тут", "spam.com", "spam"),
    ("Критический сбой системы", "Все падает", "company.ru", "critical"),
    ("Обычная тема", "Текст", "monitoring.internal", "automated"),
    ("Счет на оплату", "Жду денег за договор", "partner.ru", "finance"),
    ("График отпусков", "Больничный лист", "corp.local", "hr"),
    ("Нужен доступ", "Перестал открываться сайт", "company.ru", "support"),
    ("Важный вопрос", "Письмо от клиента", "client.biz", "external"),
    ("Привет", "Как дела?", "company.ru", "unsorted")
])
def test_classification_rules(subject, body, domain, expected_category):
    classifier = Classifier()
    msg = EmailMessage(
        sender="test@test.com",
        domain=domain,
        subject=subject,
        body=body,
        source_path=Path("dummy.txt"),
        raw=""
    )
    assert classifier.classify(msg) == expected_category
