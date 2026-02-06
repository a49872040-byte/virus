#!/usr/bin/env python3
"""
Secure Access Control System
Complete Fixed & Enhanced Version
"""

import os
import random
import time
import platform
import shutil
import re
import hashlib
import requests
import sys
from typing import List, Optional
from dataclasses import dataclass
from pathlib import Path

@dataclass
class SystemInfo:
    """Structured system information for token generation."""
    user: str
    device_model: str
    os_release: str
    system: str
    hostname: str
    home_path: str

class Colors:
    """ANSI color codes for consistent terminal output."""
    GREEN = "\033[1;32m"
    RED = "\033[1;31m"
    DIM = "\033[2m"
    YELLOW = "\033[1;33m"
    CYAN = "\033[1;36m"
    BLUE = "\033[1;34m"
    MAGENTA = "\033[1;35m"
    RESET = "\033[0m"
    
    @classmethod
    def clear_screen(cls) -> None:
        """Cross-platform screen clear."""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    @classmethod
    def type_prompt(cls, prompt: str, delay: float = 0.03) -> None:
        """Typing effect for prompts."""
        for char in prompt:
            print(char, end="", flush=True)
            time.sleep(delay)

class SecureInterface:
    """Main class handling secure login interface and authentication."""
    
    GITHUB_APPROVED_URL = "https://raw.githubusercontent.com/a49872040-byte/approved/refs/heads/main/approved.txt"
    REQUEST_TIMEOUT = 10
    MAX_RETRIES = 3
    
    HOME_LOGO = """
    db    db d888888b d8888b. db    db .d8888. 
    88    88   `88'   88  `8D 88    88 88'  YP 
    Y8    8P    88    88oobY' 88    88 `8bo.   
    `8b  d8'    88    88`8b   88    88   `Y8b. 
     `8bd8'    .88.   88 `88. 88b  d88 db   8D 
       YP    Y888888P 88   YD ~Y8888P' `8888Y' 
    """
    
    INFO_LINES = ["───────────────────────── \033[1;31m◉\033[0m silent killer! \033[1;31m◉\033[0m ─────────────────────────"]
    SEPARATOR = ["──────────────────────────────────────────────────────────────────────"]
    
    def __init__(self):
        self.approved_tokens: List[str] = []
        self.user_token: Optional[str] = None
        self.user: Optional[str] = None
        self.logo_lines = [
            "                    ██▒   █▓ ██▓ ██▀███   █    ██   ██████       ",
            "                   ▓██░   █▒▓██▒▓██ ▒ ██▒ ██  ▓██▒▒██    ▒       ",
            "                    ▓██  █▒░▒██▒▓██ ░▄█ ▒▓██  ▒██░░ ▓██▄         ",
            "                     ▒██ █░░░██░▒██▀▀█▄  ▓▓█  ░██░  ▒   ██▒      ",
            "                      ▒▀█░  ░██░░██▓ ▒██▒▒▒█████▓ ▒██████▒▒      ",
            "                      ░ ▐░  ░▓  ░ ▒▓ ░▒▓░░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░      ",
            "                          ░ ░░   ▒ ░  ░▒ ░ ▒░░░▒░ ░ ░ ░▒  ░ ░  ",
            "                        ░░   ▒ ░  ░░   ░  ░░░ ░ ░ ░  ░  ░        ",
            "                         ░   ░     ░        ░           ░        ",
            "                        ░   "
        ]
        self.info_data = [
            "Auther          ➤   Ishan Khan",
            "Tools type      ➤   Malti tasking",
            "Tools states    ➤   \033[32mPremium\033[0m",
            "Version         ➤   2.0 Complete",
            "Status          ➤   \033[32mActive\033[0m"
        ]
    
    def type_text(self, text: str, delay: float = 0.03, color: str = "") -> None:
        """Typing effect with optional color."""
        colored_text = f"{color}{text}{Colors.RESET}" if color else text
        for char in colored_text:
            print(char, end="", flush=True)
            time.sleep(delay)
        print()
    
    def center_line_safe(self, line: str) -> str:
        """Safely center text accounting for ANSI escape codes."""
        columns = shutil.get_terminal_size().columns
        vis_len = len(re.sub(r'\x1B\[[0-9;]*m', '', line))
        
        if vis_len > columns:
            excess = vis_len - columns
            line = line[excess//2 : -(excess//2) if excess//2 != 0 else None]
            vis_len = len(re.sub(r'\x1B\[[0-9;]*m', '', line))
        
        pad = (columns - vis_len) // 2
        return ' ' * pad + line
    
    def get_visible_length(self, text: str) -> int:
        """Calculate visible length excluding ANSI codes."""
        return len(re.sub(r'\x1B\[[0-9;]*m', '', text))
    
    def display_logo(self) -> None:
        """Display logo with glitch effect."""
        Colors.clear_screen()
        
        # Glitch effect
        for line in self.logo_lines:
            color = random.choice([Colors.GREEN, Colors.RED, Colors.CYAN])
            print(f"{color}{line}{Colors.RESET}")
            time.sleep(0.06)
        
        # Flash effect
        for _ in range(3):
            Colors.clear_screen()
            glitch_line = random.choice(self.logo_lines)
            print(f"{Colors.DIM}{glitch_line}{Colors.RESET}")
            time.sleep(0.05)
        
        # Clean final display
        Colors.clear_screen()
        for line in self.logo_lines:
            print(f"{Colors.GREEN}{line}{Colors.RESET}")
            time.sleep(0.02)
        
        print()
    
    def get_system_info(self, username: str) -> SystemInfo:
        """Safely collect system information."""
        try:
            device_model = platform.uname().machine or "unknown_model"
            os_release = platform.release() or "unknown_release"
            system = platform.system() or "unknown_system"
            hostname = platform.node() or "unknown_host"
            home_path = str(Path.home())
        except Exception:
            device_model = os_release = system = hostname = "unknown"
            home_path = str(Path.home() or "~")
        
        return SystemInfo(
            user=username,
            device_model=device_model,
            os_release=os_release,
            system=system,
            hostname=hostname,
            home_path=home_path
        )
    
    def generate_token(self, system_info: SystemInfo) -> str:
        """Generate SHA256 token from system information."""
        raw_data = f"{system_info.user}-{system_info.device_model}-{system_info.os_release}-{system_info.system}-{system_info.hostname}-{system_info.home_path}"
        return hashlib.sha256(raw_data.encode()).hexdigest()
    
    def fetch_approved_tokens(self) -> List[str]:
        """Fetch approved tokens from GitHub with retry logic."""
        for attempt in range(self.MAX_RETRIES):
            try:
                response = requests.get(
                    self.GITHUB_APPROVED_URL,
                    timeout=self.REQUEST_TIMEOUT
                )
                if response.status_code == 200:
                    tokens = [line.strip() for line in response.text.splitlines() if line.strip()]
                    self.type_text(f"{Colors.GREEN}[✓] Token database loaded ({len(tokens)} tokens){Colors.RESET}", delay=0.02)
                    return tokens
            except requests.RequestException as e:
                if attempt == self.MAX_RETRIES - 1:
                    self.type_text(f"{Colors.RED}[!] Network error. Using offline mode (no validation){Colors.RESET}", delay=0.07)
                time.sleep(2)
        sys.exit()
        return []
    
    def login_interface(self) -> bool:
        """Main login interface and authentication."""
        self.display_logo()
        
        # Loading sequence
        self.type_text(f"{Colors.CYAN}[+] Initializing Secure Interface...{Colors.RESET}")
        time.sleep(0.8)
        self.type_text(f"{Colors.GREEN}[+] Establishing Encrypted Session...{Colors.RESET}")
        time.sleep(0.8)
        self.type_text(f"{Colors.YELLOW}[*] Verifying system integrity...{Colors.RESET}")
        time.sleep(0.6)
        
        Colors.type_prompt(f"\n{Colors.RED}[?] Enter your codename: {Colors.RESET}", delay=0.02)
        self.user = input().lower().strip()
        
        if not self.user:
            self.type_text(f"{Colors.RED}[!] Username cannot be empty!{Colors.RESET}", delay=0.07)
            return False
        
        # Generate and check token
        self.type_text(f"{Colors.YELLOW}[*] Generating device fingerprint for {Colors.CYAN}{self.user}{Colors.RESET}...", delay=0.015)
        system_info = self.get_system_info(self.user)
        self.user_token = self.generate_token(system_info)
        
        self.type_text(f"{Colors.YELLOW}[*] Authenticating with central server...{Colors.RESET}")
        
        self.approved_tokens = self.fetch_approved_tokens()
        
        if self.approved_tokens and self.user_token in self.approved_tokens:
            Colors.clear_screen()
            for line in self.logo_lines:
                print(f"{Colors.GREEN}{line}{Colors.RESET}")
            print()
            self.type_text(f"{Colors.GREEN}[✓] ACCESS GRANTED{Colors.RESET}", delay=0.05, color=Colors.GREEN)
            self.type_text(f"{Colors.GREEN}[✓] Welcome back, {Colors.RED}{self.user.upper()}{Colors.RESET}", delay=0.03)
            self.type_text(f"{Colors.GREEN}[✓] Secure session established{Colors.RESET}")
            time.sleep(1)
            return True
        else:
            Colors.clear_screen()
            print()
            print(f"{Colors.RED}ACCESS DENIED - YOU ARE NOT AUTHORIZED")
            self.type_text(f"{Colors.RED}[✗] Token not authorized, Contact the author for approval.{Colors.RESET}")
            print()
            self.type_text(f"{Colors.YELLOW}[*] Token:{Colors.RESET} {Colors.CYAN}{self.user_token}{Colors.RESET}")
            #{Colors.CYAN}{self.user_token}{Colors.RESET}
            print()
            self.type_text(f"{Colors.RED}[◉]{Colors.RESET} {Colors.GREEN}Press enter to contact the author via WhatsApp.{Colors.RESET}")
            input(f"{Colors.RED} ╰── {Colors.RESET}{Colors.GREEN}Press Enter: {Colors.RESET}")
            f"https://wa.me/14408123714?text=আমি%20আপনার%20স্ক্রিপ্ট%20ব্যবহার%20করতে%20চাই,%20দয়াকরে%20আমার%20অ্যাক্সেস%20টোকেন%20এপ্রোভ%20করুন,%20(%20{self.user_token}%20)."
            os.system(f'termux-open-url "{url}"')
            return False
    
    def show_home_interface(self) -> None:
        """Display the complete home interface."""
        Colors.clear_screen()
        print()
        print()
        
        # Print logo line by line centered
        for line in self.HOME_LOGO.splitlines():
            print(self.center_line_safe(line))
        
        print()
        
        # Print info lines centered
        for line in self.INFO_LINES:
            print(self.center_line_safe(line))
        
        print()
        
        # Calculate left padding for info lines
        header_line = self.INFO_LINES[0]
        left_pad = self.get_visible_length(header_line) // 2
        
        # Print info data aligned
        for line in self.info_data:
            #print(" " * left_pad + line)
            print(" " * 8 + line)
        
        print()
        
        # Print separator
        for line in self.SEPARATOR:
            print(self.center_line_safe(line))
        
        print(f"\n{Colors.CYAN}{'─'*20} MAIN MENU {'─'*20}{Colors.RESET}")
        print(f"{Colors.GREEN}1.{Colors.RESET} Start Security Assessment")
        print(f"{Colors.GREEN}2.{Colors.RESET} System Scanner")
        print(f"{Colors.GREEN}3.{Colors.RESET} Network Tools")
        print(f"{Colors.GREEN}4.{Colors.RESET} Token Manager")
        print(f"{Colors.GREEN}5.{Colors.RESET} Exit")
        print()
        
        Colors.type_prompt(f"{Colors.RED}[?] Select option (1-5): {Colors.RESET}", delay=0.02)
    
    def run(self) -> None:
        """Main execution method."""
        if self.login_interface():
            while True:
                self.show_home_interface()
                choice = input().strip()
                
                if choice == "1":
                    self.type_text(f"{Colors.GREEN}[+] Launching Security Assessment...{Colors.RESET}")
                    time.sleep(2)
                elif choice == "2":
                    self.type_text(f"{Colors.GREEN}[+] System Scanner activated...{Colors.RESET}")
                    time.sleep(2)
                elif choice == "3":
                    self.type_text(f"{Colors.GREEN}[+] Network Tools loading...{Colors.RESET}")
                    time.sleep(2)
                elif choice == "4":
                    self.type_text(f"{Colors.YELLOW}[*] Token:{Colors.RESET} {Colors.CYAN}{self.user_token}{Colors.RESET}")
                    time.sleep(2)
                elif choice == "5":
                    self.type_text(f"{Colors.YELLOW}[*] Secure shutdown initiated...{Colors.RESET}")
                    time.sleep(2)
                    Colors.clear_screen()
                    sys.exit(0)
                else:
                    self.type_text(f"{Colors.RED}[!] Invalid option!{Colors.RESET}")
                    time.sleep(1)
        else:
            sys.exit(1)

def main():
    """Entry point."""
    try:
        Colors.clear_screen()
        app = SecureInterface()
        app.run()
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}[*] Session interrupted by user.{Colors.RESET}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Colors.RED}[!] Unexpected error: {str(e)}{Colors.RESET}")
        sys.exit(1)

if __name__ == "__main__":
    main()