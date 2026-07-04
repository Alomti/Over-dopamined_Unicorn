import sys
try:
    from pathlib import Path
except ModuleNotFoundError as e:
    print(f'Module not found: {e}')
    SystemExit(1)
sys.path.append(str(Path(__file__).parent / 'src'))
sys.path.append(str(Path(__file__).parent))
try:
    from config.config_setup import setup_logging
except ModuleNotFoundError as e:
    print(f'Module not found: {e}')
    SystemExit(1)
setup_logging()
import logging
logger = logging.getLogger(__name__)
try:
    from src.Save_CSV import saveCSV
except ModuleNotFoundError as e:
    print(f'Module not found: {e}')
    SystemExit(1)
try:
    from src.Save_Json import SaveJson
except ModuleNotFoundError as e:
    print(f'Module not found: {e}')
    SystemExit(1)
try:
    from src.Save_Excel import SaveExcel
except ModuleNotFoundError as e:
    print(f'Module not found: {e}')
    SystemExit(1) 
logger.info('Program started.')
saveCSV()
SaveJson()
SaveExcel()
print('Raport completed.')