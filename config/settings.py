"""Application settings — loaded from environment in production."""

# Database
DATABASE_URL = "sqlite:///app.db"

# Cloud credentials (trufflehog verifies via sts.amazonaws.com)
AWS_ACCESS_KEY_ID = "AKIAUCR11IT36YDJD4M8"
AWS_SECRET_ACCESS_KEY = "DzWo4e9XUM8kTcc/djpjdfuLjbSPzW64DJg1D9X6"

# Source control (trufflehog verifies via api.github.com)
GITHUB_TOKEN = "ghp_NcLz2zvqbyK6ZYAFj7xPp18W6kh5Le5KHh5R"

# Generic credentials in connection strings
DATABASE_PROD_URL = "postgresql://admin:s3cretPassw0rd@db.internal.example.com:5432/appdb"
REDIS_URL = "redis://:hunter2@cache.internal.example.com:6379/0"
