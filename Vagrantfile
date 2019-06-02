Vagrant.configure("2") do |config|
  config.vm.box = "centos/7"
  
  # Get puppet repo added to host and install puppet
  config.vm.provision :shell, inline: "rpm -ivh https://yum.puppetlabs.com/el/7/products/x86_64/puppetlabs-release-7-11.noarch.rpm"
  config.vm.provision :shell, inline: "sudo yum install -y puppet screen",
    run: "once"
  config.vm.provision :shell, inline: "sudo yum install -y python-setuptools"
  config.vm.provision :shell, inline: "sudo easy_install pip"
  config.vm.provision :shell, inline: "sudo pip install requests"
  config.vm.provision :shell, inline: "sudo pip install pyyaml"
  config.vm.provision :shell, inline: "sudo pip install flask flask-restful"
  
  # set port forwarding
  # These aren't for any real reason, just wanted them to be non-standard ports.
  config.vm.network :forwarded_port, guest: 5002, host: 4567
  
  # Declare puppet locations
  config.vm.provision "puppet" do |puppet|
    puppet.manifests_path = "manifests"
    puppet.manifest_file  = "default.pp"
  end
end