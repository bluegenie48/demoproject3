"""Application settings — loaded from environment in production."""

# Database
DATABASE_URL = "sqlite:///app.db"

# Cloud credentials (trufflehog verifies via sts.amazonaws.com)
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

# Source control (trufflehog verifies via api.github.com)
GITHUB_TOKEN = "ghp_ABCDEFGHIJKLMNOPQRSTUVWXYZabcdef12"

# Generic credentials in connection strings
DATABASE_PROD_URL = "postgresql://admin:s3cretPassw0rd@db.internal.example.com:5432/appdb"
REDIS_URL = "redis://:hunter2@cache.internal.example.com:6379/0"
