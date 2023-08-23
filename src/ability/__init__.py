import os


TARGET_REPO_DIR = "target_repo"


def main():
    # Secret file
    secret_file = os.path.join(TARGET_REPO_DIR, "secret.txt")

    # Create a file in the target repo
    with open(secret_file, "w", encoding="utf-8") as f:
        f.write("630")
