# 聚合代理池 | Proxy-all

这是一个自动更新的全球免费代理列表项目。通过 GitHub Actions 每 2 小时自动抓取并分类存储，确保代理列表的实时性与可用性。

## 🚀 代理列表 (Proxy Lists)

所有代理均以 `IP:PORT` 格式存储，您可以直接通过以下链接获取：

| 协议 (Protocol) | 状态 (Status) | 下载地址 (Raw Link) |
| :--- | :--- | :--- |
| **HTTP** | ![Update](https://github.com/cury-w/proxy-all/actions/workflows/update-proxies.yml/badge.svg) | [http.txt](https://raw.githubusercontent.com/cury-w/proxy-all/master/proxy/http.txt) |
| **SOCKS4** | ![Update](https://github.com/cury-w/proxy-all/actions/workflows/update-proxies.yml/badge.svg) | [socks4.txt](https://raw.githubusercontent.com/cury-w/proxy-all/master/proxy/socks4.txt) |
| **SOCKS5** | ![Update](https://github.com/cury-w/proxy-all/actions/workflows/update-proxies.yml/badge.svg) | [socks5.txt](https://raw.githubusercontent.com/cury-w/proxy-all/master/proxy/socks5.txt) |

## ✨ 项目特点 (Features)

- **自动更新**：每 2 小时自动运行抓取脚本。
- **智能分类**：自动识别并分类 HTTP、SOCKS4、SOCKS5 协议。
- **数据清洗**：自动过滤无效 IP（如 `0.0.0.0`、`127.0.0.1`）及私有局域网 IP。
- **极速部署**：基于 GitHub Actions，无需维护服务器。

## 📂 项目结构 (Structure)

```text
.
├── .github/workflows/      # GitHub Actions 自动化配置
├── proxy/
│   ├── fetcher.py         # 核心抓取脚本
│   ├── http.txt           # HTTP 代理列表
│   ├── socks4.txt         # SOCKS4 代理列表
│   └── socks5.txt         # SOCKS5 代理列表
└── README.md              # 项目说明文档
```

## 🙏 特别鸣谢 (Acknowledgements)

本项目的数据来源于以下优秀的开源代理项目及 API。衷心感谢这些作者的无私分享：

- [TheSpeedX/PROXY-List](https://github.com/TheSpeedX/PROXY-List)
- [ShiftyTR/Proxy-List](https://github.com/ShiftyTR/Proxy-List)
- [monosans/proxy-list](https://github.com/monosans/proxy-list)
- [Geonode Proxy API](https://proxylist.geonode.com/)

感谢这些开发者为社区提供的稳定代理源！

---
*免责声明：本项目仅供学习与技术研究使用，请勿用于非法用途。代理可用性受网络环境影响，不保证 100% 可用。*
