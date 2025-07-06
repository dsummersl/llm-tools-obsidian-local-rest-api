import pytest
from plugin.llm_tools_obsidian_local_rest_api import ObsidianLocalRestAPI


@pytest.fixture(scope="module")
def vcr_config():
    return {
        "filter_headers": [("authorization")],
    }


def test_constructor():
    api = ObsidianLocalRestAPI(api_key="test_api_key")
    assert api is not None
