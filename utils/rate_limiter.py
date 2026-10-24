"""
Token Bucket Rate Limiter
Standard production pattern for API request throttling.
"""

import time
from threading import Lock

class TokenBucketRateLimiter:
    def __init__(self, capacity: int, refill_rate_per_sec: float):
        self.capacity = capacity
        self.refill_rate = refill_rate_per_sec
        self.tokens = capacity
        self.last_refill = time.time()
        self.lock = Lock()

    def allow_request(self, tokens: int = 1) -> bool:
        with self.lock:
            now = time.time()
            elapsed = now - self.last_refill
            self.tokens = min(self.capacity, self.tokens + elapsed * self.refill_rate)
            self.last_refill = now

            if self.tokens >= tokens:
                self.tokens -= tokens
                return True
            return False

if __name__ == "__main__":
    limiter = TokenBucketRateLimiter(capacity=5, refill_rate_per_sec=2.0)
    for i in range(8):
        allowed = limiter.allow_request()
        print(f"Request #{i+1}: {'ALLOW' if allowed else 'THROTTLE'}")
        time.sleep(0.15)
