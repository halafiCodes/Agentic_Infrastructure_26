
# Fix verify_completion.py

#!/usr/bin/env python3
"""
Verify that Project Chimera is complete and ready for submission.
"""

import os
import json
import sys
from pathlib import Path


def check_directory_structure():
    """Check that all required directories exist"""
    print("📁 Checking directory structure...")

    required_dirs = [
        "specs",
        "skills",
        "tests",
        "research",
        ".github/workflows",
        ".cursor/rules",
        "docker",
        "docs",
    ]

    missing = []
    for dir_path in required_dirs:
        if not os.path.exists(dir_path):
            missing.append(dir_path)

    if missing:
        print(f"❌ Missing directories: {missing}")
        return False
    else:
        print("✅ All directories present")
        return True


def check_spec_files():
    """Check that all spec files exist"""
    print("\n📝 Checking specification files...")

    spec_files = [
        "specs/_meta.md",
        "specs/functional.md",
        "specs/technical.md",
        "specs/openclaw_integration.md",
    ]

    missing = []
    for file_path in spec_files:
        if not os.path.exists(file_path):
            missing.append(file_path)

    if missing:
        print(f"❌ Missing spec files: {missing}")
        return False
    else:
        print("✅ All spec files present")
        return True


def check_test_files():
    """Check that TDD test files exist"""
    print("\n🧪 Checking test files...")

    test_files = [
        "tests/test_trend_fetcher.py",
        "tests/test_skills_interface.py",
        "tests/run_tests.py",
    ]

    missing = []
    for file_path in test_files:
        if not os.path.exists(file_path):
            missing.append(file_path)

    if missing:
        print(f"❌ Missing test files: {missing}")
        return False
    else:
        print("✅ All test files present")
        return True


def check_infrastructure_files():
    """Check Docker, CI/CD, and automation files"""
    print("\n🔧 Checking infrastructure files...")

    infra_files = [
        "Dockerfile",
        "Makefile",
        ".github/workflows/main.yml",
        ".coderabbit.yaml",
        "CLAUDE.md",
    ]

    missing = []
    for file_path in infra_files:
        if not os.path.exists(file_path):
            missing.append(file_path)

    if missing:
        print(f"❌ Missing infrastructure files: {missing}")
        return False
    else:
        print("✅ All infrastructure files present")
        return True


def check_mcp_config():
    """Check MCP configuration"""
    print("\n🔗 Checking MCP configuration...")

    mcp_files = [".vscode/mcp.json", ".cursor/mcp.json"]

    all_good = True
    for file_path in mcp_files:
        if os.path.exists(file_path):
            print(f"✅ {file_path} present")
            try:
                with open(file_path, "r") as f:
                    config = json.load(f)
                    if "tenxfeedbackanalytics" in str(config):
                        print(f"   ✅ tenxfeedbackanalytics configured")
                    else:
                        print(f"   ⚠️  tenxfeedbackanalytics not found in config")
                        all_good = False
            except (json.JSONDecodeError, FileNotFoundError, KeyError):
                print(f"   ❌ Error reading {file_path}")
                all_good = False
        else:
            print(f"❌ {file_path} missing")
            all_good = False

    return all_good


def main():
    """Main verification"""
    print("=" * 60)
    print("PROJECT CHIMERA - FINAL VERIFICATION")
    print("=" * 60)

    checks = [
        ("Directory Structure", check_directory_structure()),
        ("Specification Files", check_spec_files()),
        ("Test Files (TDD)", check_test_files()),
        ("Infrastructure Files", check_infrastructure_files()),
        ("MCP Configuration", check_mcp_config()),
    ]

    print("\n" + "=" * 60)
    print("VERIFICATION SUMMARY:")
    print("=" * 60)

    passed = sum(1 for name, result in checks if result)
    total = len(checks)


    for name, result in checks:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} {name}")

    print("\n" + "=" * 60)
    if passed == total:
        print("🎉 PROJECT CHIMERA COMPLETE AND READY FOR SUBMISSION!")
        print("\nWhat to submit:")
        print("1. GitHub repository link")
        print("2. Loom video (5 mins max) showing:")
        print("   - Spec structure walkthrough")
        print("   - Failing tests running")
        print("   - IDE agent context demonstration")
        print("   - MCP connection verification")
        return 0
    else:
        print(f"⚠️  {passed}/{total} checks passed")
        print("Some requirements are missing.")
        return 1


if __name__ == "__main__":
    sys.exit(main())