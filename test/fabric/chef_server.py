from fabric.api import env, run, task
from envassert import detect, file, group, package, port, process, service, \
    user


@task
def check():
    env.platform_family = detect.detect()

    assert package.installed("chef-server")
    assert file.exists("/etc/chef-server/chef-server.rb")
    assert port.is_listening(80)
    assert port.is_listening(443)
    assert user.exists("chef_server")
    assert group.is_exists("chef_server")
    assert user.is_belonging_group("chef_server", "chef_server")
    assert process.is_up("nginx")
    assert process.is_up("postgres")
    assert service.is_enabled("nginx")
    assert service.is_enabled("postgres")
