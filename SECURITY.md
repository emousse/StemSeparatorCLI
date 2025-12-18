# Security Policy

## Supported Versions

We release patches for security vulnerabilities. Which versions are eligible for receiving such patches depends on the CVSS v3.0 Rating:

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

If you discover a security vulnerability, please **do not** open a public issue. Instead, please report it via one of the following methods:

### Preferred Method
1. **Email**: Send details to the repository maintainer (see GitHub profile)
2. **GitHub Security Advisory**: Use GitHub's private vulnerability reporting feature (if enabled)

### What to Include
When reporting a vulnerability, please include:
- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Suggested fix (if any)

### Response Time
- **Initial Response**: Within 48 hours
- **Status Update**: Within 7 days
- **Fix Timeline**: Depends on severity (typically 30-90 days)

### Disclosure Policy
- We will acknowledge receipt of your report within 48 hours
- We will provide a detailed response within 7 days
- We will notify you when the vulnerability is fixed
- We will credit you in the security advisory (if you wish)

## Security Best Practices

### For Users
- Always download from official releases
- Verify checksums when available
- Keep your system and dependencies updated
- Review permissions requested by the application

### For Developers
- Follow secure coding practices
- Keep dependencies updated
- Review pull requests for security issues
- Report vulnerabilities responsibly

## Known Security Considerations

### Audio Processing
- All processing is done locally on your machine
- No audio data is sent to external servers
- Models are downloaded from trusted sources

### Permissions
- **macOS Screen Recording**: Required for system audio capture (macOS 13+)
- **File System Access**: Required to read/write audio files
- No network permissions required for core functionality

## Security Updates

Security updates will be released as:
- **Patch releases** (e.g., 1.0.1) for critical vulnerabilities
- **Minor releases** (e.g., 1.1.0) for important security improvements
- **Security advisories** published on GitHub

---

**Thank you for helping keep Stem Separator secure!**

