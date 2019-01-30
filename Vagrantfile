# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  # Base box to use
  config.vm.box = "bento/ubuntu-18.04"

  config.vm.provider "virtualbox" do |v|
    v.gui = false
    v.name = "IAIDSVM"
    v.memory = 1024
    v.cpus = 1
    v.customize ["modifyvm",:id,"--natdnshostresolver1","on"]
  end

  # Forwarded ports
  config.vm.network "forwarded_port", guest: 8000, host: 8111, host_ip:"0.0.0.0"
  config.vm.network "forwarded_port", guest: 80, host: 8112, host_ip:"127.0.0.1"
  config.vm.network "forwarded_port", guest: 443, host: 8113, host_ip:"127.0.0.1"
  config.vm.network "forwarded_port", guest: 3306, host: 8114, host_ip:"127.0.0.1"

  # Enable provisioning with a shell script.
  config.vm.provision :shell, :path => "provision.sh", :args => "true"

  # k-12 platform project files
  config.vm.synced_folder ".", "/home/vagrant/IAIDSWebsite"
  # Media directory, with write mode given to the vagrant account/group.
  #config.vm.synced_folder "media", "/srv/platform/media", create: true,
    #mount_options: ["dmode=775,fmode=775"]
end
