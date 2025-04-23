import re
import sys
from pathlib import Path

def process_terminal_output(data: bytes) -> str:
  """Simulate terminal output by applying control characters like backspace and ANSI escape handling."""

  # Decode to UTF-8 with replacement for safety
  text = data.decode('utf-8', errors='replace')

  # Remove ANSI escape sequences (e.g., color codes, cursor movement)
  text = re.sub(r'\x1B\[[0-9;?]*[a-zA-Z]', '', text)

  # Apply backspace: simulate what appears on screen
  buffer = []
  for char in text:
    if char == '\x08':  # backspace character
    if buffer:
      buffer.pop()
    else:
      buffer.append(char)

  return ''.join(buffer)

def main(input_file: str, output_file: str):
  path = Path(input_file)
  out_path = Path(output_file)

  with path.open("rb") as f:
    raw_data = f.read()

  cleaned = process_terminal_output(raw_data)

  with out_path.open("w", encoding="utf-8") as f:
    f.write(cleaned)

  print(f"Cleaned output written to: {output_file}")

if __name__ == "__main__":
  if len(sys.argv) != 3:
    print("Usage: python clean_script_log.py <input_file> <output_file>")
    sys.exit(1)
  
  main(sys.argv[1], sys.argv[2])
