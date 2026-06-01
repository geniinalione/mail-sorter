from collections import Counter
import logging
from pathlib import Path

class StatsCollector:
    def __init__(self):
        self.collect = Counter()
    
    def add(self, category: str) -> None:
        self.collect[category] += 1
    
    def summary(self) -> str:
        result = ""
        total = 0
        for category, num in self.collect.most_common():
            result += f"{category}: {num}\n"
            total += num
        result += f"Всего писем отсортировано: {total}"
        return result
    
def setup_logging(log_path: Path) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        filename=str(log_path),
        filemode="w"
    )                
