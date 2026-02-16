import subprocess
import sys

cmd= ['ping','127.0.0.1']

proc=subprocess.run(cmd,capture_output=True,text=True,encoding='cp850')


print('STDERR: ',proc.stderr)

print('STDOUT:')
print(proc.stdout)

print('RETURN CODE: ',proc.returncode)  #return code =0, comando executado sem nenhum erro

print(sys.platform)
if sys.platform == "win32":
    print('voçê está em windows')
    cmd= ['dir']
    encoding = 'cp850'
elif sys.platform == "linux" or "linux2":
    print('voçê esta em linux')
    cmd= ['dir']
    encoding = 'utf-8'
elif sys.platform == "darwin":
    print('voçê esta no MAC')
    