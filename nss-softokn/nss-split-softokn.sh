#!/bin/sh
#
# Splits NSS into nss-util and nss-softokn
# Takes as command line input the version of nss
# and assumes that a file nss-${nss_version}-stripped.tar.bz2
# exits in the current directory

set -e

if test -z $1
then
  echo "usage: $0 nss-version"
  exit
fi

export name=nss
export version=$1

echo "Extracting ${name}-${version}-stripped.tar.bz2"

tar -xjf ${name}-${version}-stripped.tar.bz2

# the directory will be named ${name}-${version}

nss_source_dir=${name}-${version}
softokn_dir=${name}-softokn-${version}

# make_nss_softokn
#-------------------------------------------------
# create the nss-softokn subset consisting of
#   mozilla/dbm                      --- full directory
#   mozilla/security                 --- top empty
#   mozilla/security/coreconf        --- full directory
#   mozilla/security/nss             --- top files only
#   mozilla/security/nss/lib         --- top files only
#   mozilla/security/nss/lib/freebl  --- full directory
#   mozilla/security/nss/lib/softoken --- full directory
#-------------------------------------------------------

WORK_DIR=work
rm -rf ${WORK_DIR}
mkdir ${WORK_DIR}

# copy everything
cp -a ${nss_source_dir} ${WORK_DIR}/${softokn_dir}

# remove subdirectories that we don't want
rm -rf ${WORK_DIR}/${softokn_dir}/mozilla/security/nss/cmd
rm -rf ${WORK_DIR}/${softokn_dir}/mozilla/security/nss/tests
rm -rf ${WORK_DIR}/${softokn_dir}/mozilla/security/nss/lib
rm -rf ${WORK_DIR}/${softokn_dir}/mozilla/security/nss/pkg
# start with an empty lib directory and copy only what we need
mkdir ${WORK_DIR}/${softokn_dir}/mozilla/security/nss/lib
# copy entire freebl and softoken directories recursively
cp -a ${nss_source_dir}/mozilla/security/nss/lib/freebl ${WORK_DIR}/${softokn_dir}/mozilla/security/nss/lib/freebl
cp -a ${nss_source_dir}/mozilla/security/nss/lib/softoken ${WORK_DIR}/${softokn_dir}/mozilla/security/nss/lib/softoken
# On boostrapping we may need to copy util because some headers have changed
# Alternatively, we can bootsrap by rebasing nss and nss-util first and
# when the system is boostrap then rebase nss-sotokn
# cp -a ${nss_source_dir}/mozilla/security/nss/lib/util ${WORK_DIR}/${softokn_dir}/mozilla/security/nss/lib/util

# and some Makefiles and related files
cp ${nss_source_dir}/mozilla/security/nss/Makefile ${WORK_DIR}/${softokn_dir}/mozilla/security/nss
cp ${nss_source_dir}/mozilla/security/nss/manifest.mn ${WORK_DIR}/${softokn_dir}/mozilla/security/nss
cp ${nss_source_dir}/mozilla/security/nss/trademarks.txt ${WORK_DIR}/${softokn_dir}/mozilla/security/nss
cp ${nss_source_dir}/mozilla/security/nss/lib/Makefile ${WORK_DIR}/${softokn_dir}/mozilla/security/nss/lib
cp ${nss_source_dir}/mozilla/security/nss/lib/manifest.mn ${WORK_DIR}/${softokn_dir}/mozilla/security/nss/lib

# we do need shlibsign from cmd and other things
mkdir ${WORK_DIR}/${softokn_dir}/mozilla/security/nss/cmd
# copy some files at the top and selected subdirectories
cp -p ${nss_source_dir}/mozilla/security/nss/cmd/Makefile ${WORK_DIR}/${softokn_dir}/mozilla/security/nss/cmd
cp -p ${nss_source_dir}/mozilla/security/nss/cmd/manifest.mn ${WORK_DIR}/${softokn_dir}/mozilla/security/nss/cmd
cp -p ${nss_source_dir}/mozilla/security/nss/cmd/platlibs.mk ${WORK_DIR}/${softokn_dir}/mozilla/security/nss/cmd
cp -p ${nss_source_dir}/mozilla/security/nss/cmd/platrules.mk ${WORK_DIR}/${softokn_dir}/mozilla/security/nss/cmd

cp -a ${nss_source_dir}/mozilla/security/nss/cmd/shlibsign ${WORK_DIR}/${softokn_dir}/mozilla/security/nss/cmd/shlibsign
#
# copy the bltest, fipstests, lib, and subdirectories for testing
#for d in "bltest fipstest lib shlibsign"; do
src=${nss_source_dir}/mozilla/security/nss/cmd
dst=${WORK_DIR}/${softokn_dir}/mozilla/security/nss/cmd
# uncomment this line when we are to resume testing as part of the build
# for bootstrapping make it ts=" " so they don't get copied
ts="bltest fipstest lib"
for t in $ts; do
  cp -a ${src}/$t ${dst}/$t
done


# we also need some test scripts and dtest data from tests
mkdir ${WORK_DIR}/${softokn_dir}/mozilla/security/nss/tests

# copy the files at the top
fs="all.sh clean_tbx core_watch dll_version.sh header jssdir \
jss_dll_version.sh jssqa mksymlinks \
nssdir nsspath nssqa path_uniq platformlist \
platformlist.tbx qaclean qa_stage qa_stat \
README.txt run_niscc.sh set_environment"
for f in $fs; do
 cp -p ${nss_source_dir}/mozilla/security/nss/tests/$f \
       ${WORK_DIR}/${softokn_dir}/mozilla/security/nss/tests
done

# copy the subdirectories that we need
cp -a ${nss_source_dir}/mozilla/security/nss/tests/common \
      ${WORK_DIR}/${softokn_dir}/mozilla/security/nss/tests
cp -a ${nss_source_dir}/mozilla/security/nss/tests/cipher \
      ${WORK_DIR}/${softokn_dir}/mozilla/security/nss/tests

pushd ${WORK_DIR}
# the compressed tar ball for nss-softokn
tar -cjf ../${name}-softokn-${version}-stripped.tar.bz2 ${softokn_dir}
popd

# cleanup after ourselves
rm -fr ${nss_source_dir}
rm -rf ${WORK_DIR}



