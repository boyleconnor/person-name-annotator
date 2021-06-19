from openapi_server.models.tool import Tool  # noqa: E501
from openapi_server.models.tool_dependencies import ToolDependencies  # noqa: E501
from openapi_server.models.license import License


def get_tool():  # noqa: E501
    """Get tool information

    Get information about the tool # noqa: E501


    :rtype: Tool
    """
    tool = Tool(
        name="connor-person-name-annotator",
        version="0.1.6",
        license=License.APACHE_2_0,
        repository="github:cascadianblue/person-name-annotator",
        description="Connor Boyle",
        author="Connor Boyle",
        author_email="connorbo@gmail.com",
        url="https://github.com/cascadianblue/person-name-annotator",
        type="nlpsandbox:person-name-annotator",
        api_version="1.1.2"
    )
    return tool, 200


def get_tool_dependencies():  # noqa: E501
    """Get tool dependencies

    Get the dependencies of this tool # noqa: E501


    :rtype: ToolDependencies
    """
    return ToolDependencies(tools=[]), 200
