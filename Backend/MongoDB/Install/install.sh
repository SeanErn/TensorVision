#!/bin/bash

function arm {
    echo "[INFO] Running in ARM mode..."
    echo "[TAR] Extracting Archive..."
    tar -zxvf ./Backend/MongoDB/Install/dependencies/MongoDB-ARM.tgz --directory ./Backend/MongoDB/Install/

    echo "[MKDIR] Creating symbolic links to bin..."
    sudo cp  ~/TensorflowForCoprocessors/Backend/MongoDB/Install/mongodb-linux-aarch64-ubuntu2204-6.0.8/bin/mongos /usr/local/bin/mongos
    sudo cp  ~/TensorflowForCoprocessors/Backend/MongoDB/Install/mongodb-linux-aarch64-ubuntu2204-6.0.8/bin/mongod /usr/local/bin/mongod
    
    echo "[MKDIR] Creating mongo directory for DB files..."
    sudo mkdir -p /var/lib/mongo

    echo "[MKDIR] Creating mongo directory for DB logs..."
    sudo mkdir -p /var/log/mongodb

    echo "[CHOWN] Changing ownership of directories to TensorflowForCoprocessors..."
    sudo chown ${USER} /var/lib/mongo
    sudo chown ${USER} /var/log/mongodb

    echo "[Mongo] Starting MongoDB..."
    mongod --dbpath /var/lib/mongo --logpath /var/log/mongodb/mongod.log --fork

    rmdir ./Backend/MongoDB/Install/mongodb-linux-aarch64-ubuntu2204-6.0.8

    # Run on startup via crontab
    echo "@reboot root mongod --dbpath /var/lib/mongo --logpath /var/log/mongodb/mongod.log --fork" | sudo tee -a /etc/crontab

}

function x86 {
    echo "[INFO] Running in x64 mode..."
    tar -zxvf ./Backend/MongoDB/Install/dependencies/MongoDB-x86.tgz --directory ./Backend/MongoDB/Install/

    echo "[MKDIR] Creating symbolic links to bin..."
    sudo cp ~/TensorflowForCoprocessors/Backend/MongoDB/Install/mongodb-linux-x86_64-ubuntu2204-6.0.8/bin/mongos /usr/local/bin/mongos
    sudo cp  ~/TensorflowForCoprocessors/Backend/MongoDB/Install/mongodb-linux-x86_64-ubuntu2204-6.0.8/bin/mongod /usr/local/bin/mongod

    echo "[MKDIR] Creating mongo directory for DB files..."
    sudo mkdir -p /var/lib/mongo

    echo "[MKDIR] Creating mongo directory for DB logs..."
    sudo mkdir -p /var/log/mongodb

    echo "[CHOWN] Changing ownership of directories to TensorflowForCoprocessors..."
    sudo chown ${USER} /var/lib/mongo
    sudo chown ${USER} /var/log/mongodb

    echo "[Mongo] Starting MongoDB..."
    sudo mongod --dbpath /var/lib/mongo --logpath /var/log/mongodb/mongod.log --fork

    rmdir ./Backend/MongoDB/Install/mongodb-linux-x86_64-ubuntu2204-6.0.8

    # Run on startup via crontab
    echo "@reboot root mongod --dbpath /var/lib/mongo --logpath /var/log/mongodb/mongod.log --fork" | sudo tee -a /etc/crontab
}

# Check flags and run apropriate mode
if getopts x86: flag
then
    x86
else
    arm
fi

