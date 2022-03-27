import subprocess

from hooks.pre_gen_project import MESSAGE_COLOR, RESET_ALL

print(f"{MESSAGE_COLOR}Almost done!")
print(f"Initializing a git repository...{RESET_ALL}")

subprocess.call(['git', 'init'])
subprocess.call(['git', 'add', '*'])
subprocess.call(['git', 'commit', '-m', 'Initial commit'])
subprocess.call(['conda', 'env', 'create','--file','{{ cookiecutter.project_slug }}/environment.yml'])

print(f"{MESSAGE_COLOR}The beginning of your destiny is defined now! Create and have fun!{RESET_ALL}")
