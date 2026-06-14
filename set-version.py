"""Pre-render script : génère pdf-version.tex avec le tag git courant."""
import os
import subprocess

# En CI lors d'un push de tag, GITHUB_REF_NAME contient le tag exact (ex: v0.1.14)
github_ref = os.environ.get("GITHUB_REF", "")
github_ref_name = os.environ.get("GITHUB_REF_NAME", "")

if github_ref.startswith("refs/tags/"):
    version = github_ref_name.lstrip("v")
else:
    try:
        version = subprocess.check_output(
            ["git", "describe", "--tags", "--abbrev=0"],
            text=True,
            stderr=subprocess.DEVNULL,
        ).strip().lstrip("v")
    except (subprocess.CalledProcessError, FileNotFoundError):
        version = "dev"

with open("pdf-version.tex", "w") as f:
    f.write(f"\\renewcommand{{\\projectversion}}{{{version}}}\n")

print(f"[set-version] Version PDF : {version}")
