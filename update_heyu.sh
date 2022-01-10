
dir="/root"
git_url="https://github.com/fabie37/Heyu.git"
project_name="Heyu"
domain="www.catinella.co.uk"


echo
echo $(date)
echo "Updating the $project_name api. Hold on..."

if [ -d "$dir/$project_name" ]
then
    echo "Deleting old project folder..."
    rm -rf "$dir/$project_name"
else
    echo "Dir:$dir is clean."
fi

echo "Downloading latest project..."
cd $dir
git clone $git_url
cd $dir/$project_name
make install
pm2 delete $project_name
pm2 start "make test_api_server" --name "$project_name"
echo "Alright! Go to $domain:6000 to test it out."
