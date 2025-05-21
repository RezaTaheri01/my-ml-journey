from pathlib import Path
import re

# File paths
main_path = Path("README.md")
codes_path = Path("Codes/README.md")

# Read both files
main_content = main_path.read_text(encoding="utf-8")
codes_content = codes_path.read_text(encoding="utf-8").strip()

# Define markers
start_tag = "<!-- START_COLAB -->"
end_tag = "<!-- END_COLAB -->"

# Build replacement block
replacement = f"{start_tag}\n{codes_content}\n{end_tag}"

# Use regex to replace the entire block between the tags
new_main_content = re.sub(
    f"{start_tag}.*?{end_tag}",
    replacement,
    main_content,
    flags=re.DOTALL,
)

# Write updated content
main_path.write_text(new_main_content, encoding="utf-8")
print("✅ Main README updated with content from Codes/README.md.")
