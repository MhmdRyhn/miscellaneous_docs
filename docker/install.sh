# Install Docker Community Edition
sudo apt-get update -y
sudo apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo apt-key fingerprint 0EBFCD88
sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt-get update -y
sudo apt-get install -y docker-ce docker-ce-cli containerd.io
echo "Available Docker versions are listed bellow:"
apt-cache madison docker-ce
echo "Enter your desired version from the above version list. For example: 5:19.03.8~3-0~ubuntu-bionic"
read version
sudo apt-get install -y docker-ce=$version docker-ce-cli=$version containerd.io
# Optional Step
echo "Verify your installation by running this command: sudo docker run hello-world"
# Run docker without sudo preference
sudo groupadd docker
sudo usermod -aG docker $USER
# If you run through unix socket permission denied issue when pulling images, run this command.
sudo chmod 666 /var/run/docker.sock
