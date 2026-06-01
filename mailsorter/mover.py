from pathlib import Path
import shutil

class FileMover:
    def __init__(self, output_dir: Path):
        self.output_dir = output_dir
    
    def _unique_path(self, target: Path) -> Path:
        if not target.exists():
            return target
        else:
            n = 1
            while True:
                new_name = target.stem + "_" + str(n) + target.suffix 
                new_target = target.parent / new_name
                if not new_target.exists():
                    return new_target        
                n += 1
    def move(self, category: str, source_path: Path) -> Path:
        end_dir = self.output_dir / category

        end_dir.mkdir(parents=True,exist_ok=True)

        return shutil.move(
            source_path, self._unique_path(end_dir / source_path.name)
        )