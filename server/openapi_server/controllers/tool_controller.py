from openapi_server.models.tool import Tool  # noqa: E501
from openapi_server.models.tool_dependencies import ToolDependencies  # noqa: E501
from openapi_server.models.license import License


def get_tool():  # noqa: E501
    """Get tool information

    Get information about the tool # noqa: E501


    :rtype: Tool
    """
    tool = Tool(
        name="person-name-annotator-example",
        version="1.1.2",
        license=License.APACHE_2_0,
        repository="github:nlpsandbox/person-name-annotator-example",
        description="Example implementation of the NLP Sandbox Person " +
                    "Name Annotator",
        author="NLP Sandbox Team",
        author_email="team@nlpsandbox.io",
        url="https://github.com/nlpsandbox/person-name-annotator-example",
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
