import unittest
import subprocess

from ScriptCleanup import 

class TestScriptCleanup(unittest.TestCase):

    help_text = """usage: Utf8toUrl.py [-h] [--include-quotes] [--include INCLUDE] [text]

Convert UTF-8 text to URL encoding with optional filtering.

positional arguments:
  text               The text to convert (or leave empty to read from stdin)

options:
  -h, --help         show this help message and exit
  --include-quotes   Always encode quotes as %22 or %27
  --include INCLUDE  Regex pattern to determine which characters should be
                     URL-encoded
"""

    def test_no_args(self):
        """Should print out the help and exit with an error (1)."""
        result = subprocess.run(
            ["python3", "Utf8toUrl.py"],
            capture_output=True,
            text=True
        )

        # Verify the help message
        self.assertMultiLineEqual(result.stdout, self.help_text)

        # Verify the script exits with status code 1
        self.assertEqual(result.returncode, 1)
 
    def test_dash_h(self):
        """Should print out the help and exit."""
        result = subprocess.run(
            ["python3", "Utf8toUrl.py", "-h"],
            capture_output=True,
            text=True
        )

        # Verify the help message
        self.assertMultiLineEqual(result.stdout, self.help_text)

    def test_default_encoding(self):
        """Should use "[^a-zA-Z0-9/.:]" as regex."""
        result = subprocess.run(
            ["python3", "Utf8toUrl.py", "http://www.just-to-try.com/?doit.php:whynot 192.168.1.1 ' -- !! "],
            capture_output=True,
            text=True
        )
        # Verify the default encoding
        self.assertEqual(result.stdout, 
                         "http://www.just%2dto%2dtry.com/%3fdoit.php:whynot%20192.168.1.1%20%27%20%2d%2d%20%21%21%20\n")

if __name__ == '__main__':
    unittest.main()
