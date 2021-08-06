import itm
import pytest

def test_normaliseAgentVersion():
    tests = [
        {
            "input": "06.30.07.00",
            "expect": 6.37
        },
        {
            "input": "063007000",
            "expect": 6.37
        },
        {
            "input": "06.30.03.00",
            "expect": 6.33
        },
        {
            "input": "063003000",
            "expect": 6.33
        }
    ]

    for test in tests:
        version = test["input"]
        expected = test["expect"]
        got = itm.normaliseAgentVersion(version)

        assert got == expected

def test_normaliseAgentVersion_exceptions():
    tests = ["0637", "0000", "6.37", "", 8, "      ", "000000000000"]

    for test in tests:
        with pytest.raises(ValueError, match=f"Unknown or invalid agent version: {test}"):
            itm.normaliseAgentVersion(test)
