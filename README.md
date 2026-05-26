# NetMind

NetMind 是一个面向个人和团队的 AI 知识网络工具。它把需求、文档、讨论记录、研究材料和项目知识沉淀为可维护的思维导图、知识卡片和节点关系图谱，并允许 AI Agent 在用户确认下规划和自动化完成复杂的知识整理工作。

这个开源版本的重点不是做一个普通画图工具，而是把“节点”作为可复用的知识单元：节点可以属于不同导图，可以互相关联，可以绑定一张可阅读的 Markdown 知识卡片，也可以被 Agent 检索、分析、重组并生成新的知识结构。

## 核心差异

### 1. 跨图节点关联与关系图谱

NetMind 支持在不同思维导图之间建立节点关系。一个节点不只存在于当前导图的树形层级中，也可以和数据库里的任意节点形成“依赖、引用、补充、冲突、来源”等关系。

- 关系图谱以当前节点为中心，展示直接关联节点和二级关联节点。
- 跨图节点会带有所属导图信息，并支持跳转回原导图。
- 编辑节点内容时可以全库搜索节点，并快速插入引用。
- 关系数据独立持久化，适合把多个专题、项目、需求和文档串成知识网络。

这让 NetMind 更适合长期知识积累，而不是一次性的导图绘制。

### 2. 节点绑定知识卡片

每个节点都可以绑定一张知识卡片。卡片内容使用 Markdown 表达，适合写需求背景、设计说明、接口约束、会议结论、任务拆解、引用材料和补充分析。

当前知识卡片支持常用 Markdown 富文本展示能力，包括：

- 标题、段落、列表、引用、分割线。
- 加粗、斜体、删除线、行内代码。
- 代码块、表格、外部链接。
- `[[节点标题|节点ID]]` 形式的内部节点引用。
- 卡片内直接查看节点关联图谱。

导图负责结构，知识卡片负责内容，关系图谱负责跨主题连接。

### 3. Agent 可组合能力管理整个导图应用

NetMind 内置 Agent 运行链路。它的价值不只是“可以调用接口”，而是可以把导图、节点、关系、搜索和写入能力组合成完整工作流，自动规划并执行普通用户手动操作成本很高的复杂整理任务。

例如：

- 从一个节点出发，查询它的上下游关联节点和跨图引用，归纳主题边界，再创建一张新的思维导图来描述该节点相关的完整内容。
- 围绕一个目标持续生成新节点、补充节点内容、建立节点关系，直到形成可阅读、可维护的目标导图。
- 梳理整张思维导图后，规划重组方案，并通过移动子树、拆分节点、合并节点、调整关系等操作重构导图。
- 对已有知识网络做批量整理，把原本需要个人反复查看、复制、修改的工作变成可确认、可追踪的 Agent 执行流程。

这些自动化能力建立在基础工具之上：导图创建与更新、节点查询与搜索、节点创建与改写、节点关系创建与删除、文件读取与增量写入等。用户还可以新增自定义 Skill，把固定需求修改、导图重组规范、节点拆分规则、验收检查步骤沉淀为稳定流程，让 Agent 按明确步骤和约束执行，减少每次临场推理带来的偏差。

写入、删除等高风险操作会进入确认流程；查询类工具默认可直接执行。它的目标是让 AI 能完整管理思维导图应用的工作过程，而不是只给出一段整理建议后让用户手动修改。

## 功能概览

- 思维导图管理：创建、编辑、删除、导入、导出导图。
- 节点管理：树形节点、父子结构、排序、内容、画布位置保存。
- 可视化画布：支持节点拖拽、缩放、平移、图视图和列表视图切换。
- 跨图关系：支持任意节点之间建立关系，并在卡片和画布中查看。
- 知识卡片：节点内容 Markdown 化，支持阅读、编辑、预览和内部引用。
- AI 清洗：把自然语言、文档片段和需求说明整理为标准导图结构。
- AI 问答：支持节点问答、全图问答、全局问答和应用帮助。
- AI Agent：支持把基础应用能力组合为自动化工作流，完成导图生成、节点梳理、关系重建、结构重组和多轮执行。
- 自定义 Skill：支持把高频、固定、容易出错的整理流程沉淀为可复用指令，约束 Agent 的步骤、范围和检查点。
- 持久化存储：使用 PostgreSQL 保存导图、节点、关系和 AI 对话记录。
- API 文档：后端提供 Swagger 页面，便于二次开发和集成。

## 适合用途

NetMind 适合用在需要长期积累、持续重组和反复追问的知识场景：

- 产品需求拆解与需求变更追踪。
- 项目知识库、研发文档和接口说明沉淀。
- 个人研究笔记、读书笔记、课程笔记。
- 多项目、多专题之间的知识关联整理。
- 让 AI 基于已有知识结构自动生成新导图、重组旧导图，并在确认后直接完成批量编辑。

## 开源版定位

当前仓库面向开发者和自托管用户，包含：

- .NET 8 后端 API。
- Vue 3 前端应用。
- PostgreSQL 初始化与迁移脚本。
- AI Prompt 配置。
- 当前可运行的 Agent 脚本与工具定义。
- 自定义 Skill 定义与示例。
- 项目说明文档。

`agent/` 目录目前作为运行时随仓库提供，一般只需要配置路径即可使用。除非正在调试 Agent 工具、权限或执行链路，通常不需要修改它。

## 技术栈

| 层级 | 技术 |
| --- | --- |
| 前端 | Vue 3 + Vite + Element Plus |
| 后端 | .NET 8 Web API |
| 数据库 | PostgreSQL |
| AI 模型 | DeepSeek Cloud / OpenAI-compatible Chat Completions / Ollama Local |
| Agent 运行时 | Python 3.10+ |
| Agent 工具 | `.tool` 工具定义 + Python 工具脚本 |

> Agent 模式当前要求模型接口兼容 OpenAI Chat Completions。Ollama 可用于普通 AI 清洗和问答；如果要用于 Agent，需要自行确认接口兼容性。

## 目录结构

| 路径 | 说明 |
| --- | --- |
| `agent/` | 当前可运行的 Agent 脚本、工具定义和工具脚本 |
| `src/NetMind.sln` | .NET 解决方案入口 |
| `src/NetMind.WebApi/` | 后端 Web API、配置、Swagger、Prompt 文件 |
| `src/NetMind.Services/` | 业务逻辑、AI 清洗和 Agent 调用编排 |
| `src/NetMind.Repository/` | PostgreSQL 数据访问 |
| `src/NetMind.Models/` | DTO、实体和 ViewModel |
| `src/NetMind.Common/` | 通用响应、日志抽象等公共能力 |
| `src/NetMind.Frontend/` | Vue 3 前端项目 |
| `文档/SQL/` | 数据库初始化和迁移脚本 |
| `文档/项目/` | 项目结构、接口和研发说明 |

## 本地运行

### 环境要求

请先安装：

- .NET 8 SDK
- Node.js 18+
- PostgreSQL 12+
- Python 3.10+
- 可选：Ollama，本地模型调试时使用

### 1. 初始化数据库

创建数据库：

```sql
CREATE DATABASE netmind;
```

执行初始化脚本：

```powershell
psql -h localhost -p 5432 -U postgres -d netmind -f "文档/SQL/Init.sql"
```

如果是从旧版本升级，按文件名顺序执行 `文档/SQL/P*.sql` 迁移脚本。

### 2. 配置后端

建议在 `src/NetMind.WebApi/` 下新建本地配置文件 `appsettings.Local.json`。该文件已被 `.gitignore` 忽略，不会提交到仓库。

```json
{
  "ConnectionStrings": {
    "Postgres": "Host=localhost;Port=5432;Database=netmind;Username=postgres;Password=your_password;"
  },
  "App": {
    "BaseUrl": "http://127.0.0.1:5120"
  },
  "AiAgent": {
    "AgentBuildPath": "../../agent"
  }
}
```

也可以用环境变量覆盖数据库连接：

```powershell
$env:ConnectionStrings__Postgres="Host=localhost;Port=5432;Database=netmind;Username=postgres;Password=your_password;"
```

### 3. 安装前端依赖

```powershell
npm install --prefix src\NetMind.Frontend
```

### 4. 启动应用

```powershell
dotnet run --project src\NetMind.WebApi\NetMind.WebApi.csproj
```

开发环境下，后端会尝试自动启动前端开发服务。

- 前端默认地址：`http://localhost:5173`
- 后端默认地址：`http://127.0.0.1:5120`
- Swagger：`http://127.0.0.1:5120/swagger`

如果端口被占用，可以通过环境变量调整后端监听地址：

```powershell
$env:ASPNETCORE_URLS="http://127.0.0.1:5119"
dotnet run --project src\NetMind.WebApi\NetMind.WebApi.csproj
```

### 5. 配置 AI 模型

打开前端「设置 → AI 大模型配置」，选择或新增模型，并填写 API Key。

默认配置包含：

- DeepSeek Cloud：云端模型，适合 AI 清洗、问答和 Agent。
- Ollama Local：本地模型，适合普通清洗和问答调试。

API Key 会由前端加密后提交到后端，不建议写入配置文件或仓库。

### 6. 配置 Agent

确认 Python 可用：

```powershell
py --version
```

如果没有 Windows Python Launcher，可以使用 `python --version`，并在配置中把 `AiAgent:PythonExecutable` 改为 `python` 或 Python 可执行文件绝对路径。

源码运行时，Agent 根目录建议指向仓库内的 `agent/`：

```text
E:\Private\AAW+\NetMind\NetMind\agent
```

可以在前端「设置 → AgentBuild 脚本设置」中覆盖该路径，也可以在 `appsettings.Local.json` 中配置 `AiAgent:AgentBuildPath`。

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

后端发布：

```powershell
dotnet publish src\NetMind.WebApi\NetMind.WebApi.csproj -c Release -o publish/netmind
```

## 主要接口

| 能力 | 接口 |
| --- | --- |
| 健康检查 | `GET /api/system/health` |
| 导图 | `GET/POST/PUT/DELETE /api/mind-maps` |
| 节点 | `GET/POST/PUT/DELETE /api/nodes` |
| 节点搜索 | `GET /api/nodes/search` |
| 节点关系 | `GET/POST/PUT/DELETE /api/node-relations` |
| 导入导出 | `/api/mind-map-transfer/*` |
| AI 清洗与问答 | `/api/ai/*` |
| AI 对话记录 | `/api/ai-conversation-records` |

完整接口可在启动后访问 Swagger。

## 开发文档

建议先阅读：

- `文档/项目必读.md`
- `文档/开发规范.md`
- `文档/项目/项目结构速查.md`
- `文档/项目/后端API接口文档.md`

## 说明

NetMind 当前仍处于快速迭代阶段。开源版更适合作为可运行原型、二次开发基础和 AI 知识网络实验平台使用。欢迎围绕跨图关系、知识卡片、Agent 工具调用、模型适配和自托管体验继续扩展。
