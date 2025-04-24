import pytest
from security_chainsaw.patcher import PatchGenerator

@pytest.fixture
def sample_findings(tmp_path):
    file = tmp_path / "test.py"
    file.write_text(
        'def foo():\n'
        '    password = "secret"\n'
    )
    return [{'file': str(file), 'line': 2}]


def test_generate_patches_creates_diff(sample_findings):
    patcher = PatchGenerator(sample_findings)
    patches = patcher.generate_patches()
    assert isinstance(patches, list)
    assert len(patches) == 1
    diff = patches[0]['diff']
    assert 'password =' in diff
    assert 'os.getenv' in diff