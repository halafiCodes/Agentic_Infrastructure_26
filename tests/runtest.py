#!/usr/bin/env python3
"""
Test Runner for Project Chimera
Purpose: Run all tests and verify they fail as expected (TDD approach)
"""

import subprocess
import sys
import os


def run_pytest(test_file):
    """Run pytest on a specific test file"""
    print(f"\n{'='*60}")
    print(f"Running: {test_file}")
    print("=" * 60)

    result = subprocess.run(
        [sys.executable, "-m", "pytest", test_file, "-v"],
        capture_output=True,
        text=True,
    )

    print(result.stdout)
    if result.stderr:
        print("STDERR:", result.stderr)

    return result.returncode


def main():
    """Main test runner"""
    print("🧪 PROJECT CHIMERA - TEST DRIVEN DEVELOPMENT")
    print("These tests SHOULD FAIL - they define 'empty slots' for AI agents to fill")
    print("=" * 80)

    test_files = ["tests/test_trend_fetcher.py", "tests/test_skills_interface.py"]

    total_tests = 0
    passed_tests = 0
    failed_tests = 0

    for test_file in test_files:
        if os.path.exists(test_file):
            exit_code = run_pytest(test_file)
            total_tests += 1

            # In TDD, we expect tests to fail initially
            if exit_code != 0:
                print(f"✅ {test_file}: FAILED as expected (TDD approach)")
                failed_tests += 1
            else:
                print(f"⚠️  {test_file}: PASSED unexpectedly")
                passed_tests += 1
        else:
            print(f"❌ {test_file}: Test file not found")

    print(f"\n{'='*80}")
    print("TEST SUMMARY:")
    print(f"Total test files: {total_tests}")
    print(f"Tests failed as expected: {failed_tests}")
    print(f"Tests passed unexpectedly: {passed_tests}")

    if failed_tests > 0 and passed_tests == 0:
        print("\n🎉 PERFECT TDD STATUS!")
        print("All tests are failing as expected.")
        print("AI agents now have clear 'goal posts' to implement.")
        return 0
    else:
        print("\n⚠️  Check test status")
        return 1


if os.name == "main":
    sys.exit(main())