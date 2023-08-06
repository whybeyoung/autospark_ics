from autospark_kit.tools.base_tool import BaseTool
from pydantic import BaseModel, Field
from typing import Type


def _query_knowledge(food_name):
    return "检索到相关知识: %s" % food_name


def _create_report(platform, period):
    content = ""
    return "%s ,时间: %s的报表如下: %s" % (platform, period, content)


class KnowledgeInput(BaseModel):
    query: str = Field(..., description="检索知识的内容")


class KnowledgeQueryTool(BaseTool):
    """
    BookFoodTool
    """
    name: str = "Knowledge Query Tool "
    args_schema: Type[BaseModel] = KnowledgeInput
    description: str = "帮助用户检索知识库"

    def _execute(self, query: str = None):
        return _query_knowledge(query)


class CreateReportInput(BaseModel):
    platform: str = Field(..., description="平台名称，用于指定平台运营数据报表生成")
    period: str = Field(..., description="报表时间段")


class GenerateReportTool(BaseTool):
    """
    GenerateReportTool
    """
    name: str = "Generate Report Tool"
    args_schema: Type[BaseModel] = CreateReportInput
    description: str = "一个帮助用户生成指定平台运营报表的工具"

    def _execute(self, platform: str = None, period: str = None):
        return _create_report(platform, period)


class CommandExecuteInput(BaseModel):
    command: str = Field(..., description="指令名称")


def _exec(cmd):
    print("executing cmd: %s" % cmd)
    print("executing cmd: %s Success" % cmd)


class CommandExeTool(BaseTool):
    """
    GenerateReportTool
    """
    name: str = "Command Exec Tool"
    args_schema: Type[BaseModel] = CommandExecuteInput
    description: str = "一个帮助用户调用支持指令的工具"

    def _execute(self, command):
        return _exec(command)


class CommandListInput(BaseModel):
    platform: str = Field(..., description="指令所属平台")


class CommandListTool(BaseTool):
    """
    GenerateReportTool
    """
    name: str = "Command List Tool"
    args_schema: Type[BaseModel] = CommandListInput
    description: str = "根据所属平台，生成当前所属平台支持指令的工具"

    def _execute(self, command):
        return _exec(command)
