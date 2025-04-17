from prefect.blocks.core import Block
from prefect.blocks.system import Secret
from prefect.filesystems import GitHub

# Create GitHub block
github_block = GitHub(
    repository="https://github.com/radhigulati/prefectcicd.git",
    reference={"branch": "main"},
    token=Secret.load("github-token").get()
)

# Save the block
github_block.save("repo") 