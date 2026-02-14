#!/usr/bin/env python3
import os, sys, socket, hashlib, base64, random, string, shutil, subprocess, time, platform, uuid

def pause(): input("\nEnter...")
def clear(): os.system("clear")
def update(): os.system("pkg update -y && pkg upgrade -y")
def install_pkg(): os.system(f"pkg install {input()} -y")
def remove_pkg(): os.system(f"pkg uninstall {input()} -y")
def sys_info(): print(platform.platform())
def cpu_info(): os.system("lscpu")
def ram(): os.system("free -h")
def storage(): os.system("df -h")
def ip_local(): os.system("ip a")
def ip_public(): os.system("curl ifconfig.me")
def ping(): os.system(f"ping -c 4 {input()}")
def make_file(): open(input(), "w").close()
def make_dir(): os.makedirs(input(), exist_ok=True)
def delete_path(): p=input(); shutil.rmtree(p) if os.path.isdir(p) else os.remove(p)
def list_files(): os.system("ls -lah")
def search_file(): os.system(f"find . -name {input()}")
def compress(): os.system(f"zip -r {input()}.zip {input()}")
def extract(): os.system(f"unzip {input()}")
def nano(): os.system(f"nano {input()}")
def vim(): os.system(f"vim {input()}")
def git_clone(): os.system(f"git clone {input()}")
def run_py(): os.system(f"python {input()}")
def pip_install(): os.system(f"pip install {input()}")
def pip_list(): os.system("pip list")
def pip_upgrade(): os.system("pip list --outdated --format=freeze | cut -d = -f 1 | xargs -n1 pip install -U")
def make_project(): n=input(); os.makedirs(n, exist_ok=True); open(f"{n}/main.py","w").write("print('Hello')")
def password(): l=int(input()); print("".join(random.choice(string.ascii_letters+string.digits) for _ in range(l)))
def multi_pass(): c=int(input()); l=int(input()); [print("".join(random.choice(string.ascii_letters) for _ in range(l))) for _ in range(c)]
def hash_sha256(): print(hashlib.sha256(input().encode()).hexdigest())
def hash_md5(): print(hashlib.md5(input().encode()).hexdigest())
def b64e(): print(base64.b64encode(input().encode()).decode())
def b64d(): print(base64.b64decode(input().encode()).decode())
def timer(): time.sleep(int(input()))
def countdown(): s=int(input()); [print(i) or time.sleep(1) for i in range(s,0,-1)]
def http_header(): os.system(f"curl -I {input()}")
def dns(): os.system(f"nslookup {input()}")
def whois(): os.system(f"whois {input()}")
def neofetch(): os.system("neofetch")
def tree(): os.system("tree")
def uptime(): os.system("uptime")
def date(): os.system("date")
def cal(): os.system("cal")
def echo(): print(input())
def write_file(): f=input(); t=input(); open(f,"w").write(t)
def append_file(): f=input(); t=input(); open(f,"a").write(t)
def read_file(): print(open(input()).read())
def lines_count(): print(len(open(input()).readlines()))
def word_count(): os.system(f"wc {input()}")
def sort_file(): os.system(f"sort {input()}")
def chmod(): os.system(f"chmod 777 {input()}")
def env(): os.system("printenv")
def processes(): os.system("ps aux")
def kill(): os.system(f"kill {input()}")
def history(): os.system("history")
def clear_cache(): os.system("rm -rf ~/.cache/*")
def disk_usage(): os.system("du -h")
def hostname(): os.system("hostname")
def users(): os.system("who")
def top(): os.system("top")
def wget(): os.system(f"wget {input()}")
def curl(): os.system(f"curl {input()}")
def tar_c(): os.system(f"tar -cvf {input()}.tar {input()}")
def tar_x(): os.system(f"tar -xvf {input()}")
def python_version(): os.system("python --version")
def node_version(): os.system("node -v")
def php_version(): os.system("php -v")
def gcc_version(): os.system("gcc --version")
def touch(): os.system(f"touch {input()}")
def move(): os.system(f"mv {input()} {input()}")
def copy(): os.system(f"cp {input()} {input()}")
def rename(): os.system(f"mv {input()} {input()}")
def alias(): os.system("alias")
def path(): print(os.getcwd())
def change_dir(): os.chdir(input())
def random_number(): print(random.randint(1,1000000))
def uuid_func(): print(uuid.uuid4())
def sleep(): time.sleep(2)
def factorial(): n=int(input()); f=1; [f:=f*i for i in range(1,n+1)]; print(f)
def fibonacci(): n=int(input()); a,b=0,1; [print(a) or (a,b:=(b,a+b)) for _ in range(n)]
def prime_check(): n=int(input()); print(all(n%i for i in range(2,n)) and n>1)
def reverse(): print(input()[::-1])
def upper(): print(input().upper())
def lower(): print(input().lower())
def replace(): t=input(); o=input(); n=input(); print(t.replace(o,n))
def length(): print(len(input()))
def exit_tool(): sys.exit()

funcs_with_desc = [
    (update,"Update Termux"),
    (install_pkg,"Install Package"),
    (remove_pkg,"Remove Package"),
    (sys_info,"System Info"),
    (cpu_info,"CPU Info"),
    (ram,"RAM Info"),
    (storage,"Storage Info"),
    (ip_local,"Local IP"),
    (ip_public,"Public IP"),
    (ping,"Ping Host"),
    (make_file,"Make File"),
    (make_dir,"Make Folder"),
    (delete_path,"Delete Path"),
    (list_files,"List Files"),
    (search_file,"Search File"),
    (compress,"Compress Folder"),
    (extract,"Extract Zip"),
    (nano,"Edit File Nano"),
    (vim,"Edit File Vim"),
    (git_clone,"Git Clone"),
    (run_py,"Run Python"),
    (pip_install,"Pip Install"),
    (pip_list,"Pip List"),
    (pip_upgrade,"Pip Upgrade"),
    (make_project,"Make Project"),
    (password,"Generate Password"),
    (multi_pass,"Multiple Passwords"),
    (hash_sha256,"SHA256 Hash"),
    (hash_md5,"MD5 Hash"),
    (b64e,"Base64 Encode"),
    (b64d,"Base64 Decode"),
    (timer,"Timer"),
    (countdown,"Countdown"),
    (http_header,"HTTP Header"),
    (dns,"DNS Lookup"),
    (whois,"Whois Lookup"),
    (neofetch,"Neofetch"),
    (tree,"Tree View"),
    (uptime,"Uptime"),
    (date,"Date"),
    (cal,"Calendar"),
    (echo,"Echo Text"),
    (write_file,"Write File"),
    (append_file,"Append File"),
    (read_file,"Read File"),
    (lines_count,"Lines Count"),
    (word_count,"Word Count"),
    (sort_file,"Sort File"),
    (chmod,"Chmod 777"),
    (env,"Environment"),
    (processes,"Processes"),
    (kill,"Kill Process"),
    (history,"History"),
    (clear_cache,"Clear Cache"),
    (disk_usage,"Disk Usage"),
    (hostname,"Hostname"),
    (users,"Users"),
    (top,"Top Processes"),
    (wget,"Download Wget"),
    (curl,"Download Curl"),
    (tar_c,"Tar Create"),
    (tar_x,"Tar Extract"),
    (python_version,"Python Version"),
    (node_version,"Node Version"),
    (php_version,"PHP Version"),
    (gcc_version,"GCC Version"),
    (touch,"Touch File"),
    (move,"Move File"),
    (copy,"Copy File"),
    (rename,"Rename File"),
    (alias,"Show Alias"),
    (path,"Current Path"),
    (change_dir,"Change Directory"),
    (random_number,"Random Number"),
    (uuid_func,"UUID Generator"),
    (sleep,"Sleep 2s"),
    (factorial,"Factorial"),
    (fibonacci,"Fibonacci"),
    (prime_check,"Prime Check"),
    (reverse,"Reverse Text"),
    (upper,"Upper Text"),
    (lower,"Lower Text"),
    (replace,"Replace Text"),
    (length,"Text Length"),
    (exit_tool,"Exit Tool")
]

while True:
    clear()
    for i, (_, desc) in enumerate(funcs_with_desc):
        print(f"[{i+1}] {desc}")
    choice = input(">> ")
    if choice.isdigit() and 1 <= int(choice) <= len(funcs_with_desc):
        clear()
        funcs_with_desc[int(choice)-1][0]()
        pause()
