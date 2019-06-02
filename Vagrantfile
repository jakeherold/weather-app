Vagrant.configure("2") do |config|
  config.vm.box = "centos/7"
  #config.vm.provision :shell, inline: "sudo yum update && sudo yum install -y puppet"
  
  # Get puppet repo added to host and install puppet
  config.vm.provision :shell, inline: "rpm -ivh https://yum.puppetlabs.com/el/7/products/x86_64/puppetlabs-release-7-11.noarch.rpm"
  config.vm.provision :shell, inline: "sudo yum install -y puppet",
    run: "once"
  config.vm.provision :shell, inline: "sudo yum install -y python-setuptools"
  config.vm.provision :shell, inline: "sudo easy_install pip"
  config.vm.provision :shell, inline: "sudo pip install requests"
  
  # set port forwarding
  # Shows normal web content at 127.0.0.1:4567 on the host
  config.vm.network :forwarded_port, guest: 80, host: 4567
  
  # Declare puppet locations
  config.vm.provision "puppet" do |puppet|
    puppet.manifests_path = "manifests"
    puppet.manifest_file  = "default.pp"
  end
end