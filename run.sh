export SETTINGS=config.DevelopmentConfig

#get the absolute path to the directory that this script is in
dir=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
cd $dir

python run.py
