import json
import os
from typing import List, Dict, Any
from .log_config import setup_logger


logger = setup_logger('utils')


def load_transactions(file_path: str) -> List[Dict[str, Any]]:
    """
    Загружает данные о финансовых транзакциях из JSON-файла
    """
    logger.info(f"load_transactions: {file_path}")

    if not os.path.exists(file_path):
        logger.warning(f"File not found: {file_path}")
        return []

    if os.path.getsize(file_path) == 0:
        logger.warning(f"File is empty: {file_path}")
        return []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        if isinstance(data, list):
            logger.info(f"Uploaded {len(data)} transactions from {file_path}")
            return data
        else:
            logger.warning(f"File {file_path} does not contain a list ( {type(data)})")
            return []

    except json.JSONDecodeError:
        logger.error(f"Decoding error: {file_path}")
        return []
    except Exception as e:
        logger.error(f"Error loading {file_path}: {e}")
        return []
