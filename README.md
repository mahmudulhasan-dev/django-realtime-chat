# Django Realtime Chat

A backend-focused Django project designed to demonstrate clean architecture,
custom authentication, and real-time communication using Django Channels.

This project is being developed incrementally with clear commits to reflect
real-world engineering workflow.

## 🛠 Installation & Environment Notes

### Prerequisites
* **Python Version:** 3.9.x (Note: Issues detected with 3.9.0)
* **OS:** Windows (Tested on VS Code / Git Bash)

### Known Issue: Cryptography & DLL Load Failure
If you encounter an `ImportError: DLL load failed while importing _rust` when starting the server, this is due to a known compatibility issue between older Python 3.9 versions on Windows and modern Rust-based wheels.

**Decision:** I have pinned `cryptography==3.4.8` and `pyopenssl==21.0.0` to ensure the project remains stable on Windows environments without requiring a full Python upgrade to 3.12.

**To fix manually:**
```bash
pip uninstall cryptography pyopenssl -y
pip install --no-cache-dir cryptography==3.4.8 pyopenssl==21.0.0

## Current Features

- Custom user authentication system (mobile number based)
- Shared `BaseModel` for consistent timestamps and UUIDs
- Modular app structure following best practices
- Environment-based configuration (`.env`)
- Git-friendly, production-ready setup

## Planned Features

- Real-time one-to-one and group chat using WebSockets
- Message persistence and read status
- Token-based authentication for WebSocket connections
- REST APIs for chat room and message management

## Tech Stack

- Django
- Django REST Framework
- Django Channels
- Redis (for channel layer – planned)
- PostgreSQL / MySQL (configurable)

## Folder Structure

- config/          # Django project settings
- core/            # Shared BaseModel, utils
- accounts/        # Custom user system
- chat/            # Chat feature app

## Status

🚧 **Active development**  
This repository reflects daily progress and real engineering decisions rather
than a one-shot tutorial project.