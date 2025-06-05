```markdown
# 🧠 gpt-cli

A minimal command-line assistant that streams responses from GPT-4 directly into your terminal — in plain text, in three structured parts, or as a runnable shell command.

## ✨ Features

- Ask any question and get:
  - 🔹 A concise summary
  - 📜 A relevant command/script
  - 🧠 3 suggested follow-up questions
- Stream responses as they’re generated
- Special `"command ..."` mode that extracts shell-ready commands
- Optional clipboard copy using `pyperclip`
- Built for GPT-4 (requires OpenAI API key)

---

## 🚀 Quick Start

### 1. Clone the repo

```bash
git clone https://github.com/yourname/gpt-cli.git
cd gpt-cli
```

### 2. Set up a Python virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

If you're installing system-wide or already in a virtual environment, just run:

```bash
pip install openai pyperclip
```

### 3. Export your OpenAI API key

```bash
export OPENAI_API_KEY=sk-...
```

To make it persistent, add it to your shell config (`~/.bashrc`, `~/.zshrc`, etc.):

```bash
echo 'export OPENAI_API_KEY=sk-...' >> ~/.zshrc
source ~/.zshrc
```

---

## 🖊️ Example Usage

### Ask a question

```bash
gpt "How do I serve a folder in Python?"
```

### Extract a shell command

```bash
gpt "command show current git branch"
```

Expected output:

```bash
Command: git rev-parse --abbrev-ref HEAD
📋 Command copied to clipboard.
```

### Something dangerous

Comes with a warning!

```bash
gpt "command: delete file"
```

Expected output:

```bash
Command: rm filename

Warning: Be careful with this command, it will permanently delete the specified file.

💡 Extracted command: `rm filename`
📋 Command copied to clipboard.
```

Warning about this warning: Not all dangerous commands are caught,
so **always review before running**.

---

## 📂 Making the Script Executable

If you want to run it as `gpt` globally:

```bash
chmod +x gpt
ln -s $(pwd)/gpt ~/.local/bin/gpt
```

Ensure `~/.local/bin` is in your `$PATH`.

---

## ⚙️ Shebang Flexibility

Instead of hardcoding a specific virtual environment, you can use this **portable shebang** at the top of the `gpt` script:

```python
#!/usr/bin/env python3
```

This uses whichever `python3` is currently active in your environment or shell.

> 🧠 Tip: If you're using a virtualenv, just activate it before running the script. This keeps the script portable and friendly across machines.

---

## 🧩 Requirements

- Python 3.7+
- An OpenAI account with API access
- `openai` and `pyperclip` Python packages

Install them manually if needed:

```bash
pip install openai pyperclip
```

---

## 🛡️ Safety Note

In `"command"` mode, GPT outputs are parsed and copied — but **you are responsible for what you run**. Use caution, especially when piping to shell.

---

## 📘 License

MIT License — free for personal and professional use.

---

## 🙋‍♂️ Why use this?

1. Why structure GPT output into summary/script/follow-ups?
2. Why separate `"command"` mode from normal prompts?
3. Why not just use ChatGPT or curl? This is faster, keyboard-friendly, and integrates easily into dev workflows.

```

## 🙌 Contributing
Contributions are welcome! Please open an issue or submit a pull request if you have ideas for improvements or new features.
