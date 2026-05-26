# NetMind

> **AI 赋能的知识网络管理系统** — 不只是思维导图，而是支持跨图关联、知识沉淀与智能编排的企业级知识管理平台。

[**在线演示**](https://netmind-ai.onrender.com/) | [**Agent 脚本项目**](https://github.com/lan257/AgentBuild) | [**开发文档**](#开发文档)

<table>
<tr>
<td width="50%">

**🎯 为什么选择 NetMind？**

- ✅ **跨图关系网络**：节点可属于多个导图，支持依赖/引用/补充等多维关系
- ✅ **知识卡片系统**：Markdown 富文本，绑定内部引用，关联图谱一体化
- ✅ **AI Agent 自动化**：自动生成导图、重组结构、批量整理，而非仅 API 调用
- ✅ **企业级存储**：PostgreSQL 持久化，支持权限管理与变更追踪

</td>
<td width="50%">

**📊 与竞品的差异**

| 特性 | Mermaid | Markmap | SimpleMindMap | **NetMind** |
|------|--------|--------|--------------|-----------|
| 树形导图 | ✓ | ✓ | ✓ | ✓ |
| 跨图关系网络 | ✗ | ✗ | ✗ | **✓** |
| 知识卡片系统 | ✗ | ✗ | ✗ | **✓** |
| AI Agent 编排 | ✗ | ✗ | ✗ | **✓** |
| GitHub Stars | 88K | 12.8K | 12.2K | ⭐ 新 |

</td>
</tr>
</table>

---

## 核心能力

### 1️⃣ **跨图节点关联与关系图谱**

传统思维导图是**树形结构**，一个节点只能在一棵树里。NetMind 突破这个限制：

```
传统工具：
  需求导图 ─→ 设计导图 ─→ 技术文档
  （信息孤立）

NetMind：
  需求导图 ┐
  设计导图 ┼─→ 关系图谱 ←─→ 跨图搜索 & 关联管理
  技术文档┘
  （知识互联）
```

**具体能力：**
- 同一节点可属于不同导图，零冗余共享
- 建立多种关系：**依赖**（A 依赖 B）、**引用**（A 引用 B）、**补充**（A 补充 B）
- 关系图谱展示直接关联和二级关联，支持关系可视化
- 跨图节点带有所属导图信息，点击快速跳转
- 编辑时全库搜索节点，秒速插入引用

**适用场景：** 需求追踪、多项目协作、跨专题知识关联

---

### 2️⃣ **节点绑定知识卡片**

节点 = **结构**，知识卡片 = **内容**，分离设计避免混乱：

```
┌─ 导图（结构）
│  ├─ 需求拆解
│  ├─ 技术方案
│  └─ 验收标准
│
├─ 知识卡片（内容）
│  ├─ 需求背景、PRD 内容
│  ├─ 设计说明、接口定义、约束条件
│  └─ 测试用例、验收清单
│
└─ 关系图谱（连接）
   ├─ 节点间的依赖关系
   └─ 跨导图的关联
```

**知识卡片支持：**
- Markdown 富文本：标题、列表、代码块、表格、引用
- **内部节点引用**：`[[节点标题|节点ID]]` 形式跨节点导航
- 卡片内直接查看节点关联图谱
- 实时预览 & 编辑，支持版本历史（后续）

**适用场景：** 产品需求沉淀、技术方案文档、研发知识库

---

### 3️⃣ **AI Agent 自动化编排**（核心创新）

不止"调接口"，而是 **组合完整工作流**：

```
传统 AI：
  用户输入 → AI 生成文本 → 用户手动复制粘贴 → 手动编辑

NetMind Agent：
  用户确认 → Agent 自动生成导图 → Agent 自动建立关系 → Agent 自动优化结构
  → 用户预览确认 → 一键落地
```

**Agent 能力组合：**
- **导图生成**：输入需求 → 自动生成树形导图结构
- **节点梳理**：查询上下游关联 → 归纳边界 → 创建总结导图
- **关系重建**：自动识别节点依赖 → 建立跨图关系
- **结构重组**：分析现有导图 → 规划优化方案 → 自动移动/拆分/合并节点
- **批量整理**：扫描知识库 → 批量补充内容 → 自动建立关系

**安全机制：**
- 高风险操作（写入、删除）进入确认流程
- 查询类默认可直接执行
- 完整的执行日志与可追踪性

**适用场景：** 
- 需求变更自动影响关联文档
- 新成员快速理解项目知识体系
- 大规模知识库定期自动整理与重组

---

### 4️⃣ **自定义 Skill 沉淀**

把高频、固定、容易出错的流程变成可复用指令：

```python
# 示例：需求评审 Skill
[需求评审]
step1: 查询需求节点及其关联
step2: 检查：PRD 是否完整、技术方案是否绑定、风险是否标记
step3: 生成评审报告，建议补充点
step4: 如批准，自动更新状态 & 通知相关方
```

---

## 📋 完整功能清单

| 功能模块 | 详细能力 |
|---------|---------|
| **思维导图** | 创建/编辑/删除/导入/导出；树形节点；拖拽排序；画布缩放平移；图视图 & 列表视图 |
| **节点管理** | 父子关系；排序；内容编辑；画布位置保存；批量操作 |
| **知识卡片** | Markdown 编辑/预览；内部引用；富文本渲染；版本历史（规划中） |
| **关系图谱** | 任意节点间建立关系；多种关系类型；关系可视化；二级关联展示 |
| **全文搜索** | 节点标题 & 卡片内容搜索；支持模糊匹配；搜索结果预览 |
| **AI 清洗** | 自然语言 → 导图结构；文档片段 → 标准格式；需求说明 → 树形拆解 |
| **AI 问答** | 节点问答；全图问答；全局跨导图问答；应用帮助 |
| **AI Agent** | 工作流编排；多轮执行；Skill 沉淀；执行日志追踪 |
| **持久化存储** | PostgreSQL 关系型存储；导图、节点、关系、对话记录永久保存 |
| **API & 扩展** | Swagger API 文档；OpenAPI 完全支持；二次开发友好 |

---

## 🎯 适合用途

NetMind 特别适合需要**长期积累、持续重组、反复追问**的知识场景：

### 👔 **企业用途**
- **产品管理**：需求拆解、PRD 版本追踪、变更影响分析
- **研发知识库**：技术方案、接口文档、最佳实践沉淀
- **项目管理**：任务分解、依赖追踪、里程碑管理
- **质量管理**：测试用例库、缺陷关联、验收标准

### 👤 **个人用途**
- **学习笔记**：课程笔记、读书笔记、跨学科关联
- **研究整理**：文献综述、观点梳理、思路演进
- **个人 Wiki**：知识积累、思维框架、快速检索

---

## 🏗️ 技术架构

```
┌─────────────────────────────────────────────────────────┐
│                     前端 (Vue 3)                         │
│  可视化画布 | 卡片编辑 | 关系图谱 | 智能搜索 | 设置      │
└──────────────────────┬──────────────────────────────────┘
                       │ HTTP/WebSocket
┌──────────────────────▼──────────────────────────────────┐
│             后端 (.NET 8 Web API)                        │
│  导图管理 | 节点管理 | 关系管理 | AI 调用 | Agent 编排   │
└──────────────────────┬──────────────────────────────────┘
                       │
    ┌──────────────────┼──────────────────┐
    │                  │                  │
┌───▼────┐      ┌─────▼─────┐      ┌────▼──────┐
│PostgreSQL│    │ AI 模型   │      │ Agent    │
│ 数据库   │    │(OpenAI/  │      │ 运行时   │
│关系存储  │    │DeepSeek) │      │(Python)  │
└────────┘     └───────────┘      └──────────┘
```

| 层级 | 技术栈 |
|------|--------|
| **前端** | Vue 3 + Vite + Element Plus |
| **后端** | .NET 8 Web API + EF Core |
| **数据库** | PostgreSQL 12+ |
| **AI 模型** | OpenAI Chat Completions / DeepSeek / Ollama |
| **Agent 运行时** | Python 3.10+ |
| **部署** | Docker + Docker Compose（推荐）|

---

## 🚀 快速开始

### 前置要求

- **.NET 8 SDK**
- **Node.js 18+**
- **PostgreSQL 12+**
- **Python 3.10+**
- 可选：**Docker & Docker Compose**（推荐部署方案）

### 方案 A：Docker Compose 一键启动（推荐）

```bash
# 克隆项目
git clone https://github.com/lan257/netmind.git
cd netmind

# 启动所有服务（PostgreSQL + 后端 + 前端）
docker-compose up -d

# 访问应用
# 前端: http://localhost:5173
# 后端: http://127.0.0.1:5120
# Swagger: http://127.0.0.1:5120/swagger
```

### 方案 B：本地开发运行

#### 1. 初始化数据库

```bash
# 创建数据库
psql -h localhost -U postgres -c "CREATE DATABASE netmind;"

# 执行初始化脚本
psql -h localhost -U postgres -d netmind -f "文档/SQL/Init.sql"
```

#### 2. 配置后端

在 `src/NetMind.WebApi/` 新建 `appsettings.Local.json`：

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

#### 3. 启动应用

```bash
# 安装前端依赖
npm install --prefix src/NetMind.Frontend

# 启动后端（会自动启动前端开发服务）
dotnet run --project src/NetMind.WebApi/NetMind.WebApi.csproj
```

访问 `http://localhost:5173`

#### 4. 配置 AI 模型

打开前端 → **设置 → AI 大模型配置**，选择模型并填写 API Key：

- **DeepSeek Cloud**（推荐）：适合 Agent 与复杂推理
- **OpenAI**：GPT 3.5 / 4 系列
- **Ollama Local**：本地模型（仅支持简单任务，Agent 需确认兼容性）

#### 5. 配置 Agent（可选）

```bash
# 验证 Python
python --version

# 在前端「设置 → AgentBuild 脚本设置」中配置 Agent 路径
# 本地开发指向: /path/to/netmind/agent
```

---

## 📁 项目结构

```
netmind/
├── agent/                          # Agent 运行时与工具
│   ├── scripts/                    # 可执行脚本
│   ├── tools/                      # 工具定义与实现
│   └── skills/                     # 预置 Skill 库
├── src/
│   ├── NetMind.WebApi/             # 后端 Web API 入口
│   │   ├── Controllers/            # API 控制器
│   │   ├── Prompt/                 # AI Prompt 配置
│   │   └── appsettings.json        # 配置文件
│   ├── NetMind.Services/           # 业务逻辑
│   │   ├── MindMapService.cs       # 导图服务
│   │   ├── NodeService.cs          # 节点服务
│   │   ├── AiService.cs            # AI 清洗 & 问答
│   │   └── AgentService.cs         # Agent 编排
│   ├── NetMind.Repository/         # 数据访问层
│   ├── NetMind.Models/             # 数据模型
│   ├── NetMind.Common/             # 公共工具
│   └── NetMind.Frontend/           # Vue 3 前端
│       ├── src/
│       │   ├── components/         # 可视化组件
│       │   ├── views/              # 页面
│       │   ├── stores/             # Pinia 状态管理
│       │   └── api/                # API 调用
│       └── package.json
└── 文档/
    ├── SQL/                        # 数据库脚本
    │   ├── Init.sql                # 初始化
    │   └── P*.sql                  # 迁移脚本
    └── 项目/
        ├── 项目必读.md
        ├── 开发规范.md
        ├── 项目结构速查.md
        └── 后端API接口文档.md
```

---

## 📚 API 文档

启动后访问 **Swagger**：`http://127.0.0.1:5120/swagger`

### 核心接口概览

| 功能 | 端点 | 说明 |
|------|------|------|
| 健康检查 | `GET /api/system/health` | 检查服务状态 |
| **导图管理** | `GET/POST/PUT/DELETE /api/mind-maps` | 导图 CRUD |
| **节点管理** | `GET/POST/PUT/DELETE /api/nodes` | 节点 CRUD |
| **关系管理** | `GET/POST/PUT/DELETE /api/node-relations` | 关系 CRUD |
| 全文搜索 | `GET /api/nodes/search` | 搜索节点 |
| 导入导出 | `POST/GET /api/mind-map-transfer/*` | 导图转换 |
| **AI 清洗** | `POST /api/ai/clean` | 自然语言 → 导图 |
| **AI 问答** | `POST /api/ai/chat` | AI 问答 |
| **Agent** | `POST /api/agent/execute` | 执行 Agent 工作流 |
| 对话记录 | `GET /api/ai-conversation-records` | 查看历史 |

---

## 🔧 常用命令

```bash
# 后端构建
dotnet build src/NetMind.sln -c Release

# 后端发布
dotnet publish src/NetMind.WebApi/NetMind.WebApi.csproj -c Release -o publish/netmind

# 前端测试
npm run test --prefix src/NetMind.Frontend

# 前端构建
npm run build --prefix src/NetMind.Frontend

# Docker 构建
docker build -f Dockerfile -t netmind:latest .
```

---

## 📖 开发文档

**强烈建议按顺序阅读：**

1. **[项目必读](文档/项目必读.md)** — 理解 NetMind 的设计理念和核心概念
2. **[开发规范](文档/开发规范.md)** — 代码风格、提交规范、PR 流程
3. **[项目结构速查](文档/项目/项目结构速查.md)** — 快速定位代码位置
4. **[后端 API 文档](文档/项目/后端API接口文档.md)** — API 参数和响应格式

---

## 🤝 贡献指南

欢迎贡献！请提交 PR 或 Issue。关注以下方向：

- **跨图关系优化**：新的关系类型、关系查询优化
- **知识卡片增强**：编辑器功能、版本历史、协作评论
- **Agent 能力扩展**：新的自动化流程、Skill 库扩充
- **性能优化**：大规模知识库支持、查询性能优化
- **UI/UX 改进**：可视化优化、用户体验提升

---

## 📄 开源许可

本项目采用 [MIT License](LICENSE)

---

## 🗺️ 项目定位

NetMind **当前处于快速迭代阶段**，适合作为：

✅ **可运行原型** — 体验 AI 赋能知识管理的完整流程  
✅ **二次开发基础** — 基于 NetMind 定制企业知识系统  
✅ **AI 知识网络实验平台** — 探索 Agent + 知识管理的新可能  

---

## 💡 使用案例与最佳实践

### 案例 1：产品需求管理
```
1. 用户输入：【产品需求文档】
2. AI 清洗：自动生成需求导图 + 拆解用户故事
3. 建立关系：自动关联技术方案、测试用例、设计稿
4. Agent 任务：发现遗漏的需求、标记风险、生成评审报告
5. 结果：可维护的需求库 + 自动化评审流程
```

### 案例 2：新成员知识转移
```
1. 导入：现有的项目知识库、技术方案、接口文档
2. 关联：Agent 自动建立跨文档的知识关系
3. 导航：新成员通过关系图快速理解知识体系
4. 问答：基于整个知识库的智能 Q&A
5. 结果：知识快速沉淀 + 自动知识转移
```

---

## 🔗 相关资源

- 📺 [在线演示](https://netmind-ai.onrender.com/)
- 🛠️ [Agent 脚本项目](https://github.com/lan257/AgentBuild)
- 📚 [完整文档](文档/)
- 💬 [Issue & 讨论](https://github.com/lan257/netmind/issues)

---

**NetMind = 思维导图 + 知识卡片 + 关系网络 + AI Agent**

不只是工具，而是**知识工作的智能助手**。
