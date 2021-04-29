import subprocess

def run(args, cwd):
    s = subprocess.run(args,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE,
                       encoding="utf-8",
                       cwd=cwd)
    print(s.stdout)
    print(s.stderr)
    return s

def test_ver(tmp_path):
    s = run(['python3', '--version'], tmp_path)
    assert s.returncode == 0
