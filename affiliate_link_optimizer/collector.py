import logging
from typing import Dict, List, Optional
from datetime import datetime

logger = logging.getLogger(__name__)

class MetricCollector:
    """Collects performance metrics from various platforms for affiliate links."""
    
    def __init__(self, platforms: List[str], api_keys: Dict[str, str]) -> None:
        self.platforms = platforms
        self.api_keys = api_keys
        
    async def fetch_metrics(self, link_id: str) -> Optional[Dict]:
        """Fetches performance metrics for a specific affiliate link."""
        try:
            # Simulated data collection logic
            metrics = {
                'clicks': 1234,
                'conversions': 123,
                'ctr': 0.0987,
                'revenue': 123.45,
                'timestamp': datetime.now().isoformat()
            }
            logger.info(f"Metrics collected for link {link_id}")
            return metrics
        except Exception as e:
            logger.error(f"Failed to collect metrics for link {link_id}: {str(e)}")
            return None

    async def periodic_collection(self, interval: int) -> None:
        """Periodically collects metrics at specified intervals."""
        try:
            while True:
                for platform in self.platforms:
                    # Assume `api_key` is required for each platform
                    if platform not in self.api_keys:
                        logger.warning(f"No API key available for {platform}")
                        continue
                    await self.fetch_metrics(platform)
                await asyncio.sleep(interval)
        except Exception as e:
            logger.error(f"Collection loop failed: {str(e)}")