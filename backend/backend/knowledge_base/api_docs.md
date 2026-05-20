# API Documentation

## API Versions

### v1
- Deprecated
- Sunset date: December 31

### v2
- Current supported version
- Includes OAuth2 support

---

## Authentication

Required headers:
- Authorization: Bearer TOKEN
- X-API-Version

---

## Rate Limits

### Starter
- 100 requests/minute

### Standard
- 1000 requests/minute

### Enterprise
- Custom limits

---

## Breaking Changes in v2

Changes:
- pagination schema updated
- webhook payloads changed
- stricter validation

---

## Error Codes

| Code | Meaning |
|------|---------|
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 429 | Rate Limited |
| 500 | Internal Server Error |