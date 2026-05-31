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
        
    """def _extract_text(self,path:Path):"""
