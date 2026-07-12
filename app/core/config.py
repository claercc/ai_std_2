"""
项目配置管理模块

本模块使用 Pydantic Settings 实现配置的集中管理，支持从 .env 文件自动加载环境变量。

**设计思路：**
- 继承 BaseSettings 实现类型安全的配置读取
- 通过 env_file 指定从 .env 文件加载配置
- 使用类型提示确保配置项的类型正确
- 单例模式确保配置对象全局唯一

**使用方式：**
```python
from app.core.config import settings

# 访问配置项
api_key = settings.OPENAI_API_KEY
base_url = settings.OPENAI_BASE_URL
```

**替代方案（已注释）：**
早期使用 python-dotenv 直接读取环境变量的方式，
但 Pydantic Settings 提供了更强的类型检查和默认值支持。
"""

# 旧版配置方式（保留作为参考）
# from dotenv import load_dotenv
# import os
# load_dotenv()
# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL")
# MODEL_NAME = os.getenv("MODEL_NAME")

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    应用配置类
    
    继承自 Pydantic BaseSettings，自动从环境变量和 .env 文件加载配置。
    
    **配置项说明：**
    - OPENAI_API_KEY: OpenAI API 密钥，用于调用 OpenAI 服务
    - OPENAI_BASE_URL: OpenAI API 基础URL，支持自定义代理地址
    - MODEL_NAME: 默认使用的模型名称
    
    **配置优先级：**
    1. 环境变量（优先级最高）
    2. .env 文件中的变量
    3. 代码中定义的默认值（优先级最低）
    """
    
    # OpenAI API 密钥，从环境变量或 .env 文件读取
    OPENAI_API_KEY: str = ""
    
    # OpenAI API 基础URL，支持配置代理或自定义端点
    OPENAI_BASE_URL: str = ""
    
    # 默认使用的模型名称（如 gpt-3.5-turbo, gpt-4 等）
    MODEL_NAME: str = ""
    
    # Pydantic 配置类，指定配置来源和行为
    model_config = SettingsConfigDict(
        env_file=".env",       # 指定从 .env 文件加载配置
        extra="ignore"         # 忽略未定义的环境变量，避免启动报错
    )


# 创建配置类的单例实例，供全局使用
settings = Settings()