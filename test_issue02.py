import pytest
from morse import decode


@pytest.mark.parametrize("message, output", [
    ('-- .- .. -....- .--. -.-- - .... --- -. -....- ..--- ----- .---- ----.', 'MAI-PYTHON-2019'),
    ('... --- ...', 'SOS'),
    ('.... . .-.. .-.. --- --..-- / .-- --- .-. .-.. -..', 'HELLO, WORLD'),
])
def test_decode(message, output):
    assert decode(message) == output
