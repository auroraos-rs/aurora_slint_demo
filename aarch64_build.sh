#!/bin/bash

set -e

if [ -z "$PSDK_DIR" ]; then
    echo '`PSDK_DIR` not found.';
    exit 1;
fi


CURRENT_DIR="$(pwd)";
TARGET=aarch64-unknown-linux-gnu

aurora_psdk="$PSDK_DIR/sdk-chroot"
PKG_VERSION="$(cargo pkgid | cut -d '@' -f 2)"

mkdir -p RPMS/

cross build --release --target $TARGET
# cargo generate-rpm -a aarch64 --target $TARGET -o RPMS/

cp target/$TARGET/release/slint_aurora_demo ./com.lmaxyz.SlintAuroraDemo
$aurora_psdk mb2 --target AuroraOS-5.2.0.75-base-aarch64 build
rm ./com.lmaxyz.SlintAuroraDemo

$aurora_psdk rpmsign-external sign -k $PSDK_DIR/../../certs/lmaxyz_key.pem -c $PSDK_DIR/../../certs/lmaxyz_cert.pem "$CURRENT_DIR/RPMS/com.lmaxyz.SlintAuroraDemo-$PKG_VERSION-1.aarch64.rpm"
$aurora_psdk rpm-validator -p regular "$CURRENT_DIR/RPMS/com.lmaxyz.SlintAuroraDemo-$PKG_VERSION-1.aarch64.rpm"
