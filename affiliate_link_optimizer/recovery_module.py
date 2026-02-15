import logging
from typing import Dict, Optional
from retry_core import RecoveryCore

logger = logging.getLogger(__name__)

class LinkRecoveryModule:
    """Handles recovery from failed link placements or broken links."""
    
    def __init__(self, core: RecoveryCore) -> None:
        self.core = core
        
    async def recover_link(self, link_id: str) -> Optional[Dict]:
        """Attempts to recover a failed affiliate link."""
        try:
            if not await self.core.is_link_available(link_id):
                logger.info(f"Attempting recovery for {link_id}")
                return await self.core.recover_link(link_id)
            return {'status': 'ok', 'message': 'Link is functioning'}
        except Exception as e:
            logger.error(f"Recovery failed for {link_id}: {str(e)}")