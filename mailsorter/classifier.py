from .email_message import EmailMessage
class Classifier:
    critical_words = ["массов","сбой","критич"]
    spam_words = ["выигр", "скидк", "акци", "заблокир", "перейдите", "истекает", "бесплатно", "розыгрыш","внимание"]
    def classify(self, msg: EmailMessage) -> str:
        if self._is_spam(msg):
            return "spam"
        if self._is_critical(msg):
            return "critical"
        if self._is_automated(msg):
            return "automated"
        if self._is_finance(msg):
            return "finance"
        if self._is_hr(msg):
            return "hr"
        if self._is_external(msg):
            return "external"
        if self._is_support(msg):
            return "support"
        return "unsorted"
    def _is_spam(self,msg: EmailMessage):
        text = (msg.subject + " " + msg.body).lower()
        for word in self.spam_words:
            if word in text:
                return True
        return False
    def _is_critical(self,msg:EmailMessage):
        text = (msg.subject + " " + msg.body).lower()
        for word in self.critical_words:
            if word in text:
                return True
        return False
    def _is_automated(self, msg: EmailMessage):
        return msg.domain.lower().endswith(".internal")
    def _is_finance(self,msg:EmailMessage):
        return False
    def _is_hr(self,msg:EmailMessage):
        return False
    def _is_external(self,msg:EmailMessage):
        return False
    def _is_support(self,msg:EmailMessage):
        return False