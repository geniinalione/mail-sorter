from pathlib import Path
from .email_message import EmailMessage
from charset_normalizer import from_bytes
class UnreadableEmailError(Exception):
    pass
class EmailReader:
    def _parse_headers(self, header_block: str):
        data = {"from": "sender","от кого": "sender","ot kogo":"sender","subject":"subject","тема":"subject","tema":"subject"}
        result = {}
        for line in header_block.splitlines():
            tek = line.split(":",1)
            if len(tek) == 1:
                continue
            key = tek[0].strip().lower()
            znach = tek[1].strip()
            if key in data:
                result[data[key]] = znach
        return result
    
    def _extract_domain(self,sender:str):
        if "@" not in sender:
            return ""
        else:
            tek = sender.split("@")[-1]
            tek = tek.strip(" >")
            return tek
        
    def _split_headers_body(self,text:str):
        mail = text.split("\n\n",1)
        if len(mail) == 2:
            return (mail[0],mail[1])
        else:
            return(mail[0],"")
        
    def _extract_text(self,path:Path):
        try:
            tek = path.read_bytes()
            best = from_bytes(tek).best()
            cur = str(best)
            if best is None or len(cur.strip()) == 0:
                raise UnreadableEmailError(f"Сообщение {path.name} не читаемо")
            else:
                return cur
        except Exception:
            raise UnreadableEmailError(f"Сообщение {path.name} не читаемо")
    def read(self,path:Path) -> EmailMessage:
        text = self._extract_text(path)
        head,telo = self._split_headers_body(text)
        send_subj = self._parse_headers(head)
        domain = self._extract_domain(send_subj.get("sender",""))
        return EmailMessage(
            sender=send_subj.get("sender",""),
            subject=send_subj.get("subject",""),
            body = telo,
            domain=domain,
            source_path=path,
            raw=text,
        )