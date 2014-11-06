from fabric.api import run, put, sudo

def pushfile(pushfile, filepath='./docs/', tempdir='/tmp/'):
    run('mkdir -p %s' % tempdir)
    put('%s%s' % (filepath, pushfile), '%s' % tempdir)

def install_pkgs(rpm=''):
    clean_yum()
    sudo('yum -d 1 -y install %s' rpm)

def set_service(name, op='start'):
    if exists('/etc/init.d/' + name):
        if op == 'start':
            sudo('chkconfig ' + name + ' on')
            sudo('service ' + name + ' restart')
        elif op == 'stop':
            sudo('chkconfig ' + name + ' off')
            sudo('service ' + name + ' stop')

def set_date():
    sudo('service ntpd stop')
    sudo('ntpdate -b 192.168.1.190 && service ntpd start')

def prep_yum():
    repofile = 'local-cent6.repo'
    pushfile(repofile)
    #sudo('mkdir -p /etc/yum.repos.d/old && find /etc/yum.repos.d/ -maxdepth 1 -type f \( ! -iname "local-cent6.repo" \) -exec mv -f {} /etc/yum.repos.d/old \;')
    sudo('cp -f /tmp/sysop/%s /etc/yum.repos.d/' % repofile)
    clean_yum()

def clean_yum():
    sudo('yum clean all && yum repolist -d 1')

'''
def prep_yum(arch = 'cent', reposerver = '127.0.0.1'):
    clean_yum()
    if arch == 'cent': set.yum()
    ins_pkgs = 'system-config-network-tui wget vim git sysstat perl ntp yum-plugin-priorities htop lsof mlocate man openssh-client nc lynx htop bind-utils nfs-utils nfs-utils-lib acpid lrzsz parted tcpdump'
    sudo('yum -y -d 1 install '+ ins_pkgs)
'''