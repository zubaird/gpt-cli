#!/home/zubaird/.gpt-cli-env/bin/python
import sys
import os
from openai import OpenAI

client = OpenAI()

def format_response(text):
    primary = text.split('---')[0].strip()
    secondary = text.split('---')[1].strip() if '---' in text else ''
    tertiary = text.split('---')[2].strip() if text.count('---') > 1 else ''
    return primary, secondary, tertiary

def extract_command(text):
    """Extracts a command from GPT response that starts with 'Command:'"""
    for line in text.splitlines():
        if line.startswith("Command:"):
            return line[len("Command:"):].strip()
    return None

def copy_to_clipboard(command):
    try:
        import pyperclip
        pyperclip.copy(command)
        print("📋 Command copied to clipboard.")
    except ImportError:
        print("⚠️  Install 'pyperclip' for clipboard support: pip install pyperclip")

def main():
    if len(sys.argv) < 2:
        print("Usage: gpt <your question>")
        return

    query = ' '.join(sys.argv[1:])
    is_command_mode = query.strip().lower().startswith("command")

    # Generate the prompt
    if is_command_mode:
        prompt = f"""
You are a helpful CLI assistant. Respond to this request:

"{query}"

Respond only with the exact command that should be run in the terminal, like this:
Command: <command>

If the command might be dangerous, add a warning on a new line.
Do NOT include any explanation, markdown, or commentary.
"""
    else:
        prompt = f"""
You are a helpful CLI assistant. Respond to this question:

"{query}"

1. Start with a short, direct summary (≤300 characters).
2. Follow with relevant command-line instructions or script.
3. End with 3 short follow-up questions, numbered.

Separate each section with '---'.
"""

    # Stream GPT response
    stream = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
        stream=True,
    )

    output = ""
    for chunk in stream:
        content = chunk.choices[0].delta.content
        if content:
            print(content, end='', flush=True)
            output += content
    print()

    # Handle command mode
    if is_command_mode:
        command = extract_command(output)
        if command:
            print(f"\n💡 Extracted command: `{command}`")
            copy_to_clipboard(command)
            # Optionally run it: UNCOMMENT CAREFULLY
            # import subprocess
            # subprocess.run(command, shell=True)
        else:
            print("❌ No valid command found.")
    else:
        primary, secondary, tertiary = format_response(output)
        print(f"\n🔹 {primary}\n")
        print("📜 Solution:\n")
        print(secondary)
        print("\n🧠 Follow-ups:\n")
        print(tertiary)

if __name__ == "__main__":
    main()
