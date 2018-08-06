from fabric.api import env, run
from fabric.operations import sudo

GIT_REPO = "" 

env.user = 'jcj' 
env.password = 'cj125741380'

# 填写你自己的主机对应的域名
env.hosts = ['jcj.techchang.rocks']

# 一般情况下为 22 端口，如果非 22 端口请查看你的主机服务提供商提供的信息
env.port = '22'


def deploy():
    source_folder = '/home/jcj/sites/jcj.techchang.rocks/A-starter-blog-test/' 

    run('cd %s && git pull' % source_folder) 
    run("""
        cd {} &&
        ../env/bin/pip install -r requirements.txt &&
        ../env/bin/python3 manage.py collectstatic --noinput &&
        ../env/bin/python3 manage.py migrate
        """.format(source_folder))  
    sudo('restart gunicorn-jcj.techchang.rocks') 
    sudo('service nginx reload')
