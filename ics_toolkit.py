from abc import ABC
from autospark_kit.tools.base_tool import BaseToolkit, BaseTool
from typing import Type, List
from ics_tool import KnowledgeQueryTool,GenerateReportTool,CommandListTool,CommandExeTool


class AIICSToolkit(BaseToolkit, ABC):
    name: str = "Intelligent customer service Toolkit"
    description: str = "一个智能客服工具合集"

    def get_tools(self) -> List[BaseTool]:
        return [KnowledgeQueryTool(), GenerateReportTool(),CommandListTool(),CommandExeTool()]

    def get_env_keys(self) -> List[str]:
        return ["Account", "Platform"]
