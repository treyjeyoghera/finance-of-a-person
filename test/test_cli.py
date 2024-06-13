from click.testing import CliRunner
from cli import cli

def test_create_user():
    runner = CliRunner()
    result = runner.invoke(cli, input='testuser\ntestpassword\ntestpassword\n')
    assert result.exit_code == 0
    assert 'User created successfully' in result.output

if __name__ == '__main__':
    test_create_user()
