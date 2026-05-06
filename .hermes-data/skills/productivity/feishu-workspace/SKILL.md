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

## Document & Drive Operations (飞书文档/云盘)

This skill does **not** directly handle document or drive operations. For those, delegate a subagent with the appropriate toolset:

- **Documents (Doc, Sheet, Base):** `toolsets=['feishu_doc']` — create, read, edit, search, and manage online documents, spreadsheets, and multi-dimensional tables.
- **Cloud Drive (Drive, Wiki):** `toolsets=['feishu_drive']` — file/folder management, permissions, sharing, versioning, and wiki node operations.

For a detailed list of available operations, see [`references/feishu-doc-capabilities.md`](references/feishu-doc-capabilities.md).

### Alternative: `lark-oapi` Python SDK

The `lark-oapi` package (v1.6.0+) is installed in the environment. It provides programmatic access to all Lark/Feishu APIs including documents, drive, calendar, messages, and more. Use it when direct API calls are more appropriate than subagent delegation.

Example:
```python
import os
from lark_oapi import Client
client = Client.builder() \
    .app_id(os.environ['FEISHU_APP_ID']) \
    .app_secret(os.environ['FEISHU_APP_SECRET']) \
    .build()
# Then use client.docs, client.drive, client.sheets, etc.
```

### CLI Tools

No native `lark-cli` is installed by default. The npm package `@fanfanv5/feishu-cli` (v2.0.11) is available for installation if a dedicated CLI is needed.
