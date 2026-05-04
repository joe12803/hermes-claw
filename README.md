# Hermes Claw: 长期记忆 + 跨 Agent 共享

本项目参考了 `liyupi/github-claw` 的设计理念，旨在通过 GitHub 仓库实现 AI 智能体（Hermes, Copilot, Claude Code）之间的**数据对齐**与**长期记忆共享**。

## 核心设计

1.  **记忆共享 (`/memory`)**: 存储 Agent 生成的长期记忆文件。
2.  **会话存档 (`/sessions`)**: 自动同步的聊天记录。
3.  **技能中心 (`/skills`)**: 跨 Agent 可用的技能包（SKILL.md）。
4.  **Copilot 增强**: 仓库根目录包含 `AGENTS.md` 和 `.cursorrules`（待添加），让 Copilot 在读取本仓库时能自动理解之前的背景和 Agent 偏好。

## 如何让 Copilot 读取记忆？

当你在 VS Code 中使用 Copilot Chat 或 Cursor 时，只需：
1.  打开本仓库。
2.  Copilot 会自动索引 `memory/` 和 `sessions/` 目录。
3.  你可以直接问它：“根据之前的聊天记录，我目前的项目进度是什么？”或者“Agent 之前保存了哪些关于我的偏好？”

## 自动同步

本项目通过 GitHub Actions 实现每 10 分钟一次的自动热备份，确保你的“数字灵魂”永不丢失。
