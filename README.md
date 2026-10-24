<div align="center">

# 🧪 Code Lab

**Personal sandbox, algorithmic experiments, high-performance utilities, and automated git workflows.**

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Code Style](https://img.shields.io/badge/Code%20Style-Clean%20%26%20Documented-00F5D4?style=for-the-badge)](https://github.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-7928CA?style=for-the-badge)](LICENSE)

<br/>

`code-lab` is my active engineering playground—a structured repository where I prototype architectural patterns, benchmark data structures, test system design concepts, and automate daily git tooling.

</div>

---

### 📂 Repository Blueprint

```text
code-lab/
├── algorithms/
│   ├── lru_cache.py            # O(1) Doubly-Linked List LRU eviction cache
│   └── sorting.py              # In-memory QuickSort & MergeSort benchmarks
├── utils/
│   ├── rate_limiter.py         # Token Bucket rate limiting engine for APIs
│   └── logger.py               # Zero-dependency ANSI structured color logger
├── workflows/
│   └── changelog_generator.py  # Git conventional commit changelog parser
├── LICENSE                     # MIT License
└── README.md                   # Lab documentation
```

---

### ⚡ Highlights & Modules

#### 1. Token Bucket Rate Limiter (`utils/rate_limiter.py`)
Thread-safe token bucket algorithm implementation designed to throttle burst traffic in high-concurrency environments.

```python
from utils.rate_limiter import TokenBucketRateLimiter

limiter = TokenBucketRateLimiter(capacity=10, refill_rate_per_sec=2.0)
if limiter.allow_request():
    # Process incoming traffic
    pass
```

#### 2. O(1) LRU Cache (`algorithms/lru_cache.py`)
Fast, production-grade memory cache combining a doubly linked list with a hash map for constant time $O(1)$ lookups and evictions.

```python
from algorithms.lru_cache import LRUCache

cache = LRUCache(capacity=2)
cache.put(1, "payload_alpha")
cache.put(2, "payload_beta")
cache.get(1) # Hit
```

#### 3. Conventional Commit Changelog Generator (`workflows/changelog_generator.py`)
Automated utility that inspects git history and auto-categorizes releases into Features, Fixes, and Chores.

---

### 🚀 Running the Benchmarks

```bash
# Clone the lab
git clone https://github.com/envyakki/code-lab.git
cd code-lab

# Run LRU Cache demo
python -m algorithms.lru_cache

# Run Token Bucket Rate Limiter demo
python -m utils.rate_limiter
```

---

### 👤 Author
Engineered by **[@envyakki](https://github.com/envyakki)**.
