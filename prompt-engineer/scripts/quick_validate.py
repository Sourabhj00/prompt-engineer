#!/usr/bin/env python3
"""
Quick validation script for skills - minimal version.

Validates SKILL.md structure, frontmatter fields, naming conventions,
and referenced file existence.
"""

import sys
import re
from pathlib import Path


def validate_skill(skill_path):
    """Basic validation of a skill."""
    skill_path = Path(skill_path)

    # Check SKILL.md exists
    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        return False, "SKILL.md not found"

    # Read and validate frontmatter
    content = skill_md.read_text()
    if not content.startswith("---"):
        return False, "No YAML frontmatter found"

    # Extract frontmatter
    match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return False, "Invalid frontmatter format"

    frontmatter_text = match.group(1)

    # Parse frontmatter manually (no yaml dependency)
    fields = {}
    current_key = None
    current_value_lines = []

    for line in frontmatter_text.split("\n"):
        # Check for new key
        key_match = re.match(r"^(\w[\w-]*):\s*(.*)", line)
        if key_match:
            # Save previous key
            if current_key:
                fields[current_key] = " ".join(current_value_lines).strip()
            current_key = key_match.group(1)
            value = key_match.group(2).strip()
            if value in (">", "|", ">-", "|-"):
                current_value_lines = []
            else:
                current_value_lines = [value.strip('"').strip("'")]
        elif current_key and (line.startswith("  ") or line.startswith("\t")):
            current_value_lines.append(line.strip())

    if current_key:
        fields[current_key] = " ".join(current_value_lines).strip()

    # Check required fields
    if "name" not in fields:
        return False, "Missing 'name' in frontmatter"
    if "description" not in fields:
        return False, "Missing 'description' in frontmatter"

    name = fields["name"]
    description = fields["description"]

    # Validate name: kebab-case
    if not re.match(r"^[a-z0-9-]+$", name):
        return False, f"Name '{name}' should be kebab-case (lowercase letters, digits, and hyphens only)"
    if name.startswith("-") or name.endswith("-") or "--" in name:
        return False, f"Name '{name}' cannot start/end with hyphen or contain consecutive hyphens"
    if len(name) > 64:
        return False, f"Name is too long ({len(name)} characters). Maximum is 64 characters."

    # Validate description
    if "<" in description or ">" in description:
        return False, "Description cannot contain angle brackets (< or >)"
    if len(description) > 1024:
        return False, f"Description is too long ({len(description)} characters). Maximum is 1024 characters."

    # Check referenced files exist
    referenced_files = [
        skill_path / "references" / "checklist.md",
        skill_path / "examples" / "before-after.md",
    ]
    for ref_file in referenced_files:
        if not ref_file.exists():
            return False, f"Referenced file not found: {ref_file.relative_to(skill_path)}"

    return True, "Skill is valid!"


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python quick_validate.py <skill_directory>")
        sys.exit(1)

    valid, message = validate_skill(sys.argv[1])
    print(message)
    sys.exit(0 if valid else 1)
