# Ubuntu 22.04

# install pip

sudo apt install python3-pip -y

# install python3-venv

sudo apt install python3.10-venv -y

# setup virtual environment

python3 -m venv venv

. venv/bin/activate

or

source venv/bin/activate

# install boto3

pip3 install boto3

# save dependecies in requirements.txt

pip3 freeze > requirements.txt

# install dependencies:

pip install -r requirements.txt

# Install AWS CLI 

check out https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html#cliv2-linux-install

curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"

unzip awscliv2.zip

sudo ./aws/install

/usr/local/bin/aws --version

# Create IAM User with proper Role and Policies 
# Go for Acess Key and Secret Key


# Then Run the command and give necessary details
aws configure
