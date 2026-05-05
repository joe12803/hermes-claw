---
name: feishu-workspace
description: "Feishu (飞书) Calendar, Messages, and Tasks via direct API (Tenant Access Token)."
version: 1.0.0
author: Nous Research
license: MIT
metadata:
  hermes:
    tags: [Feishu, 飞书, Calendar, Messages, Bot, API]
    related_skills: [google-workspace, yuanbao]
---

# Feishu Workspace

Interaction with Feishu (飞书) via its Open Platform API using a custom bot (`FEISHU_APP_ID`, `FEISHU_APP_SECRET`).

## Credentials

The skill expects the following environment variables (usually in `~/.hermes/.env`):
- `FEISHU_APP_ID`
- `FEISHU_APP_SECRET`
- `FEISHU_CHAT_ID` (Default target group/chat)

## Common Workflows

### 1. Authenticate (Get Tenant Access Token)

```python
import requests
url = 'https://open.feishu.cn/open-apis/auth/v3/app_access_token/internal'
payload = {'app_id': '...', 'app_secret': '...'}
token = requests.post(url, json=payload).json().get('app_access_token')
```

### 2. Read Calendar Events

**Endpoint:** `GET https://open.feishu.cn/open-apis/calendar/v4/calendars/primary/events`

**Required Scopes:**
- `calendar:calendar:readonly`
- `calendar:calendar`
- `calendar:calendar.event:read`

### 3. Send/Read Messages

**Endpoint (Send):** `POST https://open.feishu.cn/open-apis/im/v1/messages?receive_id_type=chat_id`
**Endpoint (Read):** `GET https://open.feishu.cn/open-apis/im/v1/messages?container_id_type=chat&container_id=<CHAT_ID>`

## Pitfalls

- **Access Denied (Scope Required):** Feishu APIs are strict. If you get a `99991672` error, the bot is missing a specific scope. Provide the user with the authorization URL provided in the error message response so they can enable it in the Feishu Open Platform.
- **Bot/User out of chat:** Error `230002` means the bot hasn't been invited to the group chat. Instruct the user to @mention the bot in the group or add it manually.
- **receive_id_type:** Always specify the `receive_id_type` (e.g., `chat_id`, `open_id`, `email`) when sending or querying messages.
