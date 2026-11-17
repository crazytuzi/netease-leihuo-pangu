# 倩女幽魂残端研究 / NetEase Leihuo Legacy Build Research

![商标与版权 / Trademark & Copyright](TrademarkCopyright.jpg)

<font color="#FF0000" size="4"><b>版权归网易雷火所有。本仓库仅作个人研究与技术存档，不用于任何商业用途，亦不代表官方任何立场。</b></font>

<font color="#FF0000" size="4"><b>Copyright belongs to NetEase Leihuo. This repository is kept solely for personal research and technical archiving; it is not for any commercial use and does not represent any official position.</b></font>

---

## 一、项目说明 / Project Notes

**中文**

本仓库收录的是一份**内部 N 年前的测试版本**（二测阶段客户端安装包 0.9.13 及其同期的残缺服务端），**不是现在的最新版本**。文件按原样归档，未做任何解包、重新打包或内容改写；大文件按字节切片存放，恢复方式见《重组说明.md》。

用途只有一个：留存这段历史版本的原始形态，便于回溯早期版本的资源结构、协议形态与场景表现。

**English**

This repository holds an **internal test build from N years ago** (the second closed-beta client installer 0.9.13 and its contemporary incomplete server), **not the current latest version**. Files are archived exactly as received — no unpacking, repacking, or content rewriting; large files are stored as byte-level split parts, see `重组说明.md` (Reassembly Notes) for how to restore them.

Its only purpose is to preserve this historical build in its original form, so the early resource layout, protocol shape and scene presentation stay traceable.

---

## 二、分支说明 / Branch Notes

**中文**

| 分支 | 用途 |
|---|---|
| `master` | **主分支（建议分支）**。默认查看、下载和引用都走这里，内容为稳定归档版。 |
| `剧情分支`（建议命名 `story`） | 剧情向改动与剧情资料整理专用分支。涉及任务线、对白、场景剧情的研究性改动放这里，避免污染主分支归档。 |

建议分支的含义：主分支只保存"能直接拿来用"的稳定内容；任何实验性的剧情改造都另开分支，便于随时丢弃或对比。

**English**

| Branch | Purpose |
|---|---|
| `master` | **Main branch (recommended branch)**. Use it for viewing, downloading and referencing — it holds the stable archive. |
| `剧情分支` (suggested name `story`) | Dedicated to story-related changes and story material. Task lines, dialogue and scene-story experiments live here so the archive on main stays clean. |

"Recommended branch" means: main keeps only content that is ready to use; any experimental story rework goes to its own branch, so it can be dropped or diffed at any time.

---

## 三、内容清单 / Contents

| 路径 | 说明 |
|---|---|
| `OriginalServerNndClient/倩女幽魂OL残缺服务端.zip.part01..part11` | 残缺服务端压缩包，863 MB，按 80 MB 切片 |
| `OriginalServerNndClient/倩女幽魂二测客户端安装包-0.9.13.exe.part01..part10` | 二测客户端安装包，752 MB，按 80 MB 切片 |
| `SceneRendering/` | 该版本场景渲染截图 7 张 |
| `TrademarkCopyright.jpg` | 商标与版权标识，展示于本文开头 |
| `文件哈希与MD5.md` | 全部文件与分片的 MD5 / SHA-1 / SHA-256 |
| `重组说明.md` | 分片还原步骤（`copy /b` 与 `cat` 两种写法） |
| `rebuild_big_files.py` | 自动还原脚本，内置期望大小与 SHA-256，还原后自校验 |

---

## 四、关于代码构成 / On the Code

**中文**

本仓库中的代码由三部分构成：

1. **原版残缺副本**：上述服务端与客户端的原始文件，与官方版本一致的部分不做任何改动；
2. **二次开发的创新实现副本**：包含基于该残缺副本延伸出的自研实现代码，**不限于加密相关**（加解密、打包、资源重组），也包括工具链、配置与脚本层面的改造；这部分仅作技术记录，不主张任何权利，全部归属原版权方；
3. **公开资料整理**：通过网络检索汇总的作品品鉴、玩家反馈与核心玩法梳理，用于理解该版本的设计取向。

创新实现部分的价值在于"记录早期版本能被怎样理解和复现"，不构成对原作品的替代，也不改变原作品的版权归属。

**English**

The code here has three layers:

1. **Original incomplete copies** — the server and client files above, untouched wherever they match the official build;
2. **Derivative innovative implementations** — self-developed code built on top of those copies, **not limited to encryption** (encrypt/decrypt, packing, resource reassembly) but also tooling, configuration and scripting changes; kept purely as a technical record, claiming no rights, all ownership stays with the original rights holder;
3. **Public material digest** — reviews, player feedback and core-gameplay notes gathered from public web sources, used to understand the design direction of this build.

The value of the derivative work is documenting *how this early build can be understood and reproduced*; it does not replace the original work and does not alter its ownership.

---

## 五、核心玩法与玩家反馈摘要 / Gameplay & Player Feedback

**中文（网络检索品鉴整理）**

- 核心循环：门派与职业差异化的回合制战斗 + 剧情任务驱动的地图推进，装备强化与生活技能构成长期养成线。
- 早期版本的辨识度来自场景美术与剧情演出，二测阶段的资源完成度和现在的版本差距明显，属于典型的"骨架先立、内容后填"形态。
- 玩家反馈集中在两类：一是早期版本的怀旧价值（场景、音乐、任务文本），二是残缺端带来的稳定性问题（资源不齐、逻辑断点）。
- 本仓库不改这些问题，只做记录，便于和后续版本对照研究。

**English**

- Core loop: class-differentiated turn-based combat plus story-driven map progression; gear upgrading and life skills form the long-term progression line.
- This build's identity came from scene art and story presentation; the second beta's asset completeness is visibly far from today's version — a classic "skeleton first, content later" state.
- Player feedback clusters in two areas: nostalgia value of the early build (scenes, music, quest text), and stability limits of an incomplete server (missing assets, broken logic).
- This repository does not fix those issues — it only records them for comparison with later versions.

---

## 六、使用与免责 / Usage & Disclaimer

**中文**：仅限个人学习、研究与技术存档。请勿用于商业运营、二次发行或任何侵犯网易雷火权益的行为。若版权方要求，仓库可立即下架。

**English**: For personal study, research and technical archiving only. Do not use it for commercial operation, redistribution, or anything infringing NetEase Leihuo's rights. The repository will be taken down immediately upon request from the rights holder.
