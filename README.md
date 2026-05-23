# NetMind

NetMind 是一个基于 AI 的知识网络构建与可视化工具，用于把文本、文档、需求和讨论内容整理成可维护的思维导图与知识图谱。它提供节点管理、关系管理、AI 结构化整理、上下文问答和 Agent 工具调用能力，适合用来沉淀项目知识、需求分析、产品方案和研发文档。

本仓库主要面向开发者，包含后端、前端、数据库脚本、文档和当前可运行的 Agent 脚本。普通用户建议使用发布页提供的安装包。

## 当前状态

- 后端、前端、数据库和 AI 基础功能已可本地运行。
- AI Agent 已接入工具调用链路，可以调用大部分 NetMind 应用接口，包括导图、节点、节点关系、文件读取/增量写入等能力。
- Agent 脚本已经放在仓库根目录的 `agent/` 下。运行应用时将 Agent 路径指向该目录即可。
- `agent/` 目录当前作为应用运行时脚本随仓库提供，一般不需要修改。完整的 Agent 脚本开发项目后续会单独开源。
- 写入、删除等高风险 Agent 工具会走确认流程；查询类工具默认可直接执行。

## 功能概览

- AI 清洗：把自然语言、需求说明和文档片段整理成标准导图结构。
- 需求结构化：基于上下文生成可导入、可编辑的知识节点。
- 思维导图：创建、编辑、删除、导入、导出导图和节点。
- 画布编辑：支持节点拖拽、缩放、平移、位置保存和视图切换。
- 知识卡片：支持 Markdown 内容展示、节点预览和关联关系查看。
- AI 问答：支持节点问答、全图问答、上下文问答、全局问答和应用帮助。
- AI Agent：支持工具规划、权限确认、工具执行、上下文记忆和多轮继续执行。
- 持久化存储：使用 PostgreSQL 保存导图、节点、关系和对话记录。

## Agent 能力

当前仓库内置的 Agent 运行时位于：

```text
agent/
├── src/
│   └── agent_kernel.py
├── .tool/
│   ├── domain_tool_bindings.json
│   ├── lists/
│   └── tools/
└── .skill/
    ├── domain_skill_bindings.json
    ├── lists/
    └── skills/
```

NetMind 后端通过 Python 启动 `agent/src/agent_kernel.py`，把当前问题、上下文、模型配置、工具权限结果和 NetMind API 地址传给 Agent。Agent 再根据 `.tool` 中的工具定义选择并执行工具。

当前 `netmind` 域已包含的主要工具类型：

- 导图：创建、查询、列表、更新、删除、级联删除。
- 节点：创建、查询、搜索、更新、删除子树、按导图列表查询。
- 节点关系：创建、查询、按导图查询、按节点查询、删除。
- 文件：读取文档、增量追加内容。
- 通用：时间查询、目录/文件读取类工具。

Agent 路径可以在前端「设置 → AgentBuild 脚本设置」中配置。对于本仓库源码运行，建议填写仓库内的 `agent` 绝对路径，例如：

```text
E:\Private\AAW+\NetMind\NetMind\agent
```

如果前端没有覆盖该路径，也可以在后端配置文件中调整 `AiAgent:AgentBuildPath`。

## 技术栈

| 层级 | 技术 |
| --- | --- |
| 后端 | .NET 8 Web API |
| 前端 | Vue 3 + Vite + Element Plus |
| 数据库 | PostgreSQL |
| AI 模型 | DeepSeek Cloud / OpenAI-compatible Chat Completions / Ollama Local |
| Agent 运行时 | Python 3.10+ |
| Agent 工具 | `.tool` 工具定义 + Python 工具脚本 |

> 注意：当前 Agent 模式仅支持 OpenAI-compatible Chat Completions 接口。Ollama 可用于普通 AI 清洗和问答；如果用于 Agent，需要确认接口兼容性。

## 开发环境

请先安装：

- .NET 8 SDK
- Node.js 18+
- PostgreSQL 12+
- Python 3.10+
- 可选：Ollama，本地模型调试时使用

## 本地启动

### 1. 准备数据库

创建数据库：

```sql
CREATE DATABASE netmind;
```

执行初始化脚本：

```powershell
psql -h localhost -p 5432 -U postgres -d netmind -f "文档/SQL/Init.sql"
```

如果需要从旧库升级，按文件名顺序执行 `文档/SQL/P*.sql` 迁移脚本。

运行后端前，通过 `PGSTR` 环境变量提供 PostgreSQL 连接字符串：

```powershell
$env:PGSTR="Host=localhost;Port=5432;Database=netmind;Username=postgres;Password=your_password;"
```

### 2. 安装前端依赖

```powershell
cd src\NetMind.Frontend
npm install
cd ..\..
```

### 3. 配置 AI 模型

使用 DeepSeek Cloud 时配置 API Key：

```powershell
$env:DEEPSEEK_API_KEY="你的 DeepSeek API Key"
```

也可以在前端「设置 → 内置模型 API Key」里为本机浏览器临时覆盖 Key。

使用本地模型时，请先启动 Ollama，并确认 `src/NetMind.WebApi/appsettings*.json` 中配置的模型已在本机拉取。

真实 API Key 不应写入仓库。开发时优先使用环境变量或前端本地设置。

### 4. 配置 Agent

确认本机可以运行 Python：

```powershell
py --version
```

如果没有 Windows Python Launcher，可改用 `python --version` 测试，并在后端配置中把 `AiAgent:PythonExecutable` 改为可执行文件名或 `python.exe` 绝对路径。

将 Agent 根目录设置为仓库内的 `agent` 目录。可选方式：

- 前端设置：打开「设置 → AgentBuild 脚本设置」，填写 `agent` 目录的绝对路径。
- 后端配置：修改 `src/NetMind.WebApi/appsettings*.json` 中的 `AiAgent:AgentBuildPath`。

### 5. 启动后端

```powershell
dotnet run --project src\NetMind.WebApi\NetMind.WebApi.csproj
```

开发环境下，后端会尝试自动启动前端开发服务。默认访问地址：

```text
http://localhost:5173
```

接口文档：

```text
http://localhost:5120/swagger
```

如果端口被占用，可以通过环境变量调整后端监听地址：

```powershell
$env:ASPNETCORE_URLS="http://127.0.0.1:5119"
dotnet run --project src\NetMind.WebApi\NetMind.WebApi.csproj
```

## 常用命令

后端构建：

```powershell
dotnet build src\NetMind.sln -c Release -v minimal
```

前端测试：

```powershell
npm run test --prefix src\NetMind.Frontend
```

前端构建：

```powershell
npm run build --prefix src\NetMind.Frontend
```

## 目录说明

| 路径 | 说明 |
| --- | --- |
| `agent/` | 当前可运行的 Agent 脚本、工具定义和工具脚本 |
| `src/NetMind.sln` | .NET 解决方案入口 |
| `src/NetMind.WebApi/` | 后端 Web API、配置、Swagger、Prompt 文件 |
| `src/NetMind.Services/` | 业务逻辑和 AI/Agent 调用编排 |
| `src/NetMind.Repository/` | PostgreSQL 数据访问 |
| `src/NetMind.Models/` | DTO、实体和 ViewModel |
| `src/NetMind.Common/` | 通用响应和日志抽象 |
| `src/NetMind.Frontend/` | Vue 3 前端项目 |
| `文档/SQL/` | 数据库初始化和迁移脚本 |
| `文档/项目必读.md` | 项目文档入口 |

## 配置说明

主要配置文件：

- `src/NetMind.WebApi/appsettings.json`
- `src/NetMind.WebApi/appsettings.Development.json`

常用环境变量：

| 变量 | 说明 |
| --- | --- |
| `PGSTR` | PostgreSQL 完整连接字符串，后端运行必需 |
| `DEEPSEEK_API_KEY` | DeepSeek Cloud API Key，使用 DeepSeek 时需要 |
| `ASPNETCORE_URLS` | 可选，覆盖后端监听地址 |

常用 Agent 配置：

| 配置项 | 说明 |
| --- | --- |
| `AiAgent:AgentBuildPath` | Agent 根目录，源码运行建议指向仓库内 `agent/` |
| `AiAgent:PythonExecutable` | Python 启动命令，默认 `py` |
| `AiAgent:TimeoutSeconds` | Agent 单轮执行超时时间 |
| `AiAgent:SkillRuntimeTimeoutSeconds` | 单个工具执行超时时间 |

## 开发文档

开发前建议先阅读：

- `文档/项目必读.md`
- `文档/开发规范.md`
- `文档/项目/项目结构速查.md`
- `文档/项目/后端API接口文档.md`

## 开发边界

- 本仓库可以直接运行当前 Agent 能力，但 `agent/` 更接近运行时交付物。
- 日常业务开发通常只需要改后端、前端、数据库脚本和 Prompt 配置。
- 除非正在调试 Agent 调用链路、工具定义或工具权限，否则一般不需要修改 `agent/`。
- 完整的 Agent 脚本开发、工具脚手架和工程化维护方式会在后续独立开源项目中提供。

