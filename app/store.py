from typing import List, Dict, Any
import asyncio

_db: List[Dict[str, Any]] = []
_id_counter = 0
_lock = asyncio.Lock()

async def add_feedback(message: str, tags: List[str]) -> Dict[str, Any]:
    global _id_counter
    async with _lock:
        _id_counter += 1
        fb = {"id": _id_counter, "message": message, "tags": tags}
        _db.append(fb)
    return fb

async def list_feedback() -> List[Dict[str, Any]]:
    # shallow copy to avoid mutation issues
    async with _lock:
        return list(_db)
