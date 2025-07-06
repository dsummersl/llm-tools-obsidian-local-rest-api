import llm


class ObsidianLocalRestAPI(llm.Toolbox):
    """
    A tool access an Obsidian vault via a REST API.
    """

    def __init__(self, api_key: str, url: str = "https://localhost:27124"):
        super().__init__()
        self.url = url
        self.api_key = api_key


@llm.hookimpl
def register_tools(register):
    register(ObsidianLocalRestAPI)
