from pathlib import Path
from .reader import EmailReader, UnreadableEmailError
from .classifier import Classifier
from .mover import FileMover
from .stats import StatsCollector
class Pipeline:
    def __init__(self,inbox_path):
        self.inbox = Path(inbox_path)
        self.reader = EmailReader()
        self.classifier = Classifier()
        self.mover = FileMover(Path("output"))
        self.stats = StatsCollector()
    def run(self):
        for line in self.inbox.iterdir():
            if line.name == ".DS_Store" or line.is_dir():
                continue
            else:
                try:
                    mesg = self.reader.read(line)
                    clas = self.classifier.classify(mesg)
                    self.mover.move(clas, line)
                    self.stats.add(clas)
                except UnreadableEmailError:
                    self.mover.move("corrupted", line)
                    self.stats.add("corrupted")
        print(self.stats.summary())
if __name__ == "__main__":
    Pipeline("data/inbox").run()