"""
Educational use only.
This script is intended for controlled lab environments.
Do not use on systems without explicit authorization.
"""

import time
import sys
import random

def brute_force(username, wordlist_file, silent=True):
    correct_password = "hunter2"

    try:
        with open(wordlist_file, "r") as file:
            passwords = file.read().splitlines()
    except FileNotFoundError:
        if not silent:
            print("❌ Error: Wordlist file not found.")
        return

    for guess in passwords:
        if not silent:
            print(f"🔍 Trying {guess} on {username}")
        time.sleep(random.uniform(0.3, 0.7))
        if guess == correct_password:
            print(f"✅ Cracked! Password for {username}: {guess}")
            break
    else:
        print(f"❌ No password found for {username}")

    if not silent:
        print("☠️  Brute-forcing simulation complete")

def wordlist(output_file, words):
    with open(output_file, "w") as file:
        for word in words:
            file.write(word + "\n")
    print(f"📒 Wordlist successfully created at {output_file}")

def lockout (attempts):
    correct_password = "qwerty"
    for attempt in attempts:
        if attempt == correct_password:
            print("✅ Access granted")
            return
        else:
            print("❌ Access denied")
    print("🔒 LOCKED OUT")

def show_help():
    print("❌ Error: You must specify a tool using --tool argument.")
    print("Menu Options:")
    print("--tool 1 = brute (requires --username and --wordlist)")
    print("--tool 2 = wordlist (requires --output and word list)")
    print("--tool 3 = lockout (requires --attempts)")
    print("--tool 4 = exit")
    print("\nExample:")
    print("python auth_test.py --tool 1 --username admin --wordlist word.txt --silent")

args = sys.argv

if len(args) < 2:
    show_help()
    sys.exit()

if "--tool" not in args:
    show_help()
    sys.exit()

tool_map = {
    "1": "brute",
    "2": "wordlist",
    "3": "lockout",
    "4": "exit"
}

tool_index = args.index("--tool") + 1
if tool_index >= len(args):
    show_help()
    sys.exit()

menu_choice = args[tool_index]

if menu_choice not in tool_map:
    print("❌ Invalid menu choice. Select 1, 2, 3, or 4.")
    sys.exit()

tool = tool_map[menu_choice]

if tool == "brute":
    if "--username" not in args or "--wordlist" not in args:
        print("❌ Error: You must provide --username and --wordlist.")
        sys.exit()

    username = args[args.index("--username") + 1]
    wordlist_file = args[args.index("--wordlist") + 1]
    silent = "--silent" in args
    brute_force(username, wordlist_file, silent)

elif tool == "wordlist":
    if "--output" not in args:
        print("❌ Error: You must provide --output followed by words.")
        sys.exit()

    output_file = args[args.index("--output") + 1]
    word_start = args.index("--output") + 2
    words = args[word_start:]

    if not words:
        print("❌ Error: No words provided to create wordlist.")
        sys.exit()

    wordlist(output_file, words)

elif tool == "lockout":
    if "--attempts" not in args:
        print("❌ Error: You must provide --attempts followed by passwords.")
        sys.exit()

    attempt_start = args.index("--attempts") + 1
    attempts = args[attempt_start:]

    if not attempts:
        print("❌ Error: No attempts provided.")
        sys.exit()

    lockout(attempts)

elif tool == "exit":
    print("👋 Exiting auth test Toolkit...")
    sys.exit()

print("\n🔄 Re-run the program with a new --tool argument to continue.\n")
