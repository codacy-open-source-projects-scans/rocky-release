# Note to packagers/builders:
#
# If you wish to build the LookAhead or Beta variant of this package, make sure
# that you are setting --with=rlbeta or --with=rllookahead on your mock
# command. See the README for more information.

%bcond_with rlbeta
%bcond_with rllookahead
%bcond_with rloverride

%define debug_package %{nil}

# Product information
%define product_family Rocky Linux
%define variant_titlecase Server
%define variant_lowercase server

# Distribution Name and Version
%define distro_name  Rocky Linux
%define distro       %{distro_name}
%define distro_code  Blue Onyx
%define major        9
%define minor        7
%define rocky_rel    1%{?rllh:.%{rllh}}%{!?rllh:.3}
%define rpm_license  BSD-3-Clause
%define dist         .el%{major}
%define home_url     https://rockylinux.org/
%define bug_url      https://bugs.rockylinux.org/
%define debug_url    https://debuginfod.rockylinux.org/
%define dist_vendor  RESF
%define vendor_url   https://resf.org/

%define contentdir   pub/rocky
%define sigcontent   pub/sig
%define rlosid       rocky

%define os_bug_name  Rocky-Linux-%{major}
%define support_end  2032-05-31

################################################################################
# Rocky LookAhead Section
#
# Reset defines for LookAhead variant. Default is stable if 0 or undefined.
%if %{with rllookahead}
%define minor        7
%define contentdir   pub/rocky-lh
%define rltype       -lookahead
%define rlstatement  LookAhead
%endif
# End Rocky LookAhead Section
################################################################################

################################################################################
# Rocky Beta Section
#
# Reset defines for Beta variant. Default is stable if 0 or undefined.
# We do NOT override the minor version number here.
%if %{with rlbeta}
%define contentdir   pub/rocky-beta
%define rltype       -beta
%define rlstatement  Beta
%endif
# End Rocky Beta Section
################################################################################

################################################################################
# Rocky Override Section
#
# Resets only the dist tag for the override package. All this does is ensure
# that only the rhel macros and settings are provided - This is useful in the
# case of a build that cannot be properly debranded (eg dotnet).
%if %{with rloverride}
%define dist         .el%{major}.override
%define rlosid       rhel
%endif
# End Rocky Override Section
################################################################################

%define base_release_version %{major}
%define dist_release_version %{major}
%define full_release_version %{major}.%{minor}

%ifarch ppc64le
%define tuned_profile :server
%endif

# Avoids a weird anaconda problem
%global __requires_exclude_from %{_libexecdir}

# conditional section for future use

Name:           rocky-release%{?rltype}
Version:        %{full_release_version}
Release:        %{rocky_rel}%{dist}
Summary:        %{distro_name} release files
Group:          System Environment/Base
License:        %{rpm_license}
URL:            https://rockylinux.org
BuildArch:      noarch

# What do we provide? Some of these needs are a necesity (think comps and
# groups) and things like EPEL need it.
Provides:       rocky-release = %{version}-%{release}
Provides:       rocky-release(upstream) = %{full_release_version}
Provides:       redhat-release = %{version}-%{release}
Provides:       system-release = %{version}-%{release}
Provides:       system-release(releasever) = %{major}
Provides:       system-release(releasever_major) = %{major}
Provides:       system-release(releasever_minor) = %{minor}
Provides:       centos-release = %{version}-%{release}
Provides:       centos-release(upstream) = %{full_release_version}

## Required by libdnf
Provides:       base-module(platform:el%{major})

## This makes lorax/pungi/anaconda happy
Provides:       rocky-release-eula  = %{version}-%{release}
Provides:       redhat-release-eula = %{version}-%{release}
Provides:       centos-release-eula = %{version}-%{release}

# What are our requirements?
Requires:       rocky-repos(%{major})

# GPG Keys (100-199)
Source101:      RPM-GPG-KEY-Rocky-%{major}
Source102:      RPM-GPG-KEY-Rocky-%{major}-Testing

# Release Sources (200-499)
Source200:      EULA
Source201:      LICENSE
Source202:      Contributors
Source203:      COMMUNITY-CHARTER

# !! Stable !!
Source300:      85-display-manager.preset
Source301:      90-default.preset
Source302:      90-default-user.preset
Source303:      99-default-disable.preset
Source304:      50-redhat.conf

# !! LookAhead !!
Source400:      85-display-manager.preset.lh
Source401:      90-default.preset.lh
Source402:      90-default-user.preset.lh
Source403:      99-default-disable.preset.lh
Source404:      50-redhat.conf.lh

# Repo Sources (1200-1299)
Source1200:     rocky.repo
Source1201:     rocky-addons.repo
Source1202:     rocky-extras.repo
Source1203:     rocky-devel.repo

# Add ons (1300-1399)
Source1300:     rocky.1.gz

# rocky secureboot certs placeholder (1400-1499)
# 1400 is the root
# 1401-1420 are dedicated to the kernel
# 1421-1440 is dedicated to x86_64
# 1441-1460 is dedicated to aarch64
Source1400:     rocky-root-ca.der
Source1401:     rockydup1.x509
Source1402:     rockykpatch1.x509
Source1403:     rockydup1-aarch64.x509
Source1404:     rockykpatch1-aarch64.x509
Source1405:     rocky-nvidiagpuoot101.x509
Source1406:     rocky-nvidiagpuoot101-aarch64.x509
Source1407:     rocky-ima-ca.crt
Source1408:     rocky-imarelease.crt
# x86_64
Source1421:     rocky-fwupd.cer
Source1422:     rocky-grub2.cer
Source1423:     rocky-kernel.cer
Source1424:     rocky-shim.cer
Source1425:     rocky-uki-virt.cer
# x86_64 in der
Source1426:     rocky-fwupd.der
Source1427:     rocky-grub2.der
Source1428:     rocky-kernel.der
Source1429:     rocky-shim.der
Source1430:     rocky-uki-virt.der
# aarch64
Source1441:     rocky-fwupd-aarch64.cer
Source1442:     rocky-grub2-aarch64.cer
Source1443:     rocky-kernel-aarch64.cer
Source1444:     rocky-shim-aarch64.cer
Source1445:     rocky-uki-virt-aarch64.cer
# aarch64 in der
Source1446:     rocky-fwupd-aarch64.der
Source1447:     rocky-grub2-aarch64.der
Source1448:     rocky-kernel-aarch64.der
Source1449:     rocky-shim-aarch64.der
Source1450:     rocky-uki-virt-aarch64.der
 
%description
%{distro_name} release files.

%package     -n rocky-repos%{?rltype}
Summary:        %{distro_name} Package Repositories
License:        %{rpm_license}
Provides:       system-repos = %{version}-%{release}
Provides:       rocky-repos(%{major}) = %{full_release_version}
Requires:       system-release = %{version}-%{release}
Requires:       rocky-gpg-keys%{?rltype}
Conflicts:      %{name} < 8.0

%description -n rocky-repos%{?rltype}
%{distro_name} package repository files for yum/dnf

%package     -n rocky-gpg-keys%{?rltype}
Summary:        Rocky RPM GPG Keys
Conflicts:      %{name} < 8.0

%description -n rocky-gpg-keys%{?rltype}
This package provides the RPM signature keys for Rocky.

%package     -n rocky-sb-certs%{?rltype}
Summary:        %{distro_name} public secureboot certificates
Group:          System Environment/Base
Provides:       system-sb-certs = %{version}-%{release}
Provides:       redhat-sb-certs = %{version}-%{release}
Provides:       centos-sb-certs = %{version}-%{release}

%description -n rocky-sb-certs%{?rltype}
This package contains the %{distro_name} secureboot public certificates.

%prep
%if %{with rllookahead} && %{with rlbeta}
echo "!! WARNING !!"
echo "Both LookAhead and Beta were enabled. This is not supported."
echo "As a result: BUILD FAILED."
exit 1
%endif
echo Good.

%build
echo Good.

%install
# docs dir for license and contributors
mkdir ./docs
cp %{SOURCE201} %{SOURCE202} %{SOURCE203} ./docs

################################################################################
# system-release data
install -d -m 0755 %{buildroot}%{_sysconfdir}
echo "%{distro_name} release %{full_release_version}%{?rlstatement: %{rlstatement}} (%{distro_code})" > %{buildroot}%{_sysconfdir}/rocky-release
echo "Derived from Red Hat Enterprise Linux %{full_release_version}" > %{buildroot}%{_sysconfdir}/rocky-release-upstream
ln -s rocky-release %{buildroot}%{_sysconfdir}/system-release
ln -s rocky-release %{buildroot}%{_sysconfdir}/redhat-release
mkdir -p %{buildroot}%{_mandir}/man1
install -p -m 0644 %{SOURCE1300} %{buildroot}%{_mandir}/man1/

# Create the os-release file
install -d -m 0755 %{buildroot}%{_prefix}/lib
cat > %{buildroot}%{_prefix}/lib/os-release << EOF
NAME="%{distro_name}"
VERSION="%{full_release_version} (%{distro_code})"
ID="%{rlosid}"
ID_LIKE="rhel centos fedora"
VERSION_ID="%{full_release_version}"
PLATFORM_ID="platform:el%{major}"
PRETTY_NAME="%{distro_name} %{full_release_version}%{?rlstatement: %{rlstatement}} (%{distro_code})"
ANSI_COLOR="0;32"
LOGO="fedora-logo-icon"
CPE_NAME="cpe:/o:rocky:rocky:%{major}::baseos"
HOME_URL="%{home_url}"
VENDOR_NAME="%{dist_vendor}"
VENDOR_URL="%{vendor_url}"
BUG_REPORT_URL="%{bug_url}"
SUPPORT_END="%{support_end}"
ROCKY_SUPPORT_PRODUCT="%{os_bug_name}"
ROCKY_SUPPORT_PRODUCT_VERSION="%{full_release_version}%{?rlstatement:-%{rlstatement}}"
REDHAT_SUPPORT_PRODUCT="%{distro_name}"
REDHAT_SUPPORT_PRODUCT_VERSION="%{full_release_version}%{?rlstatement: %{rlstatement}}"
EOF

# Create the symlink for /etc/os-release
ln -s ../usr/lib/os-release %{buildroot}%{_sysconfdir}/os-release

# write cpe to /etc/system/release-cpe
echo "cpe:/o:rocky:rocky:%{major}::baseos" > %{buildroot}%{_sysconfdir}/system-release-cpe

# create /etc/issue and /etc/issue.net, /etc/issue.d
echo '\S' > %{buildroot}%{_sysconfdir}/issue
echo 'Kernel \r on \m' >> %{buildroot}%{_sysconfdir}/issue
cp %{buildroot}%{_sysconfdir}/issue{,.net}
echo >> %{buildroot}%{_sysconfdir}/issue
mkdir -p %{buildroot}%{_sysconfdir}/issue.d

# set up the dist tag macros
mkdir -p %{buildroot}%{_rpmmacrodir}
cat > %{buildroot}%{_rpmmacrodir}/macros.dist << EOF
# dist macros.

%%__bootstrap ~bootstrap
%%rocky_ver %{major}
%%rocky %{major}
%%centos_ver %{major}
%%centos %{major}
%%rhel %{major}
%%distcore .el%{major}
%%dist %%{!?distprefix0:%%{?distprefix}}%%{expand:%%{lua:for i=0,9999 do print("%%{?distprefix" .. i .."}") end}}%%{distcore}%%{?distsuffix}%%{?with_bootstrap:%{__bootstrap}}
%%el%{major} 1

%%dist_vendor         %{dist_vendor}
%%dist_name           %{distro}
%%dist_home_url       %{home_url}
%%dist_bug_report_url %{bug_url}
%%dist_debuginfod_url %{debug_url}
EOF

# Data directory
install -d -m 0755 %{buildroot}%{_datadir}/rocky-release
ln -s rocky-release %{buildroot}%{_datadir}/redhat-release
install -p -m 0644 %{SOURCE200} %{buildroot}%{_datadir}/rocky-release/

# end system-release data
################################################################################

################################################################################
# systemd section
install -d -m 0755 %{buildroot}%{_prefix}/lib/systemd/system-preset/
install -d -m 0755 %{buildroot}%{_prefix}/lib/systemd/user-preset/

install -m 0644 %{SOURCE300} %{buildroot}/%{_prefix}/lib/systemd/system-preset/
install -m 0644 %{SOURCE301} %{buildroot}/%{_prefix}/lib/systemd/system-preset/
install -m 0644 %{SOURCE302} %{buildroot}/%{_prefix}/lib/systemd/user-preset/

# same behavior for both presets
install -m 0644 %{SOURCE303} %{buildroot}/%{_prefix}/lib/systemd/system-preset/
install -m 0644 %{SOURCE303} %{buildroot}/%{_prefix}/lib/systemd/user-preset/

# sysctl presets
install -d -m 0755 %{buildroot}%{_prefix}/lib/sysctl.d/
install -m 0644 %{SOURCE304} %{buildroot}/%{_prefix}/lib/sysctl.d/
# systemd section
################################################################################

################################################################################
# start secureboot section
install -d -m 0755 %{buildroot}%{_sysconfdir}/pki/sb-certs/
install -d -m 0755 %{buildroot}%{_datadir}/pki/sb-certs/

# Backported certs for now
## root and kernel
install -m 0644 %{SOURCE1400} %{buildroot}%{_datadir}/pki/sb-certs/
install -m 0644 %{SOURCE1401} %{buildroot}%{_datadir}/pki/sb-certs/
install -m 0644 %{SOURCE1402} %{buildroot}%{_datadir}/pki/sb-certs/
install -m 0644 %{SOURCE1403} %{buildroot}%{_datadir}/pki/sb-certs/
install -m 0644 %{SOURCE1404} %{buildroot}%{_datadir}/pki/sb-certs/
install -m 0644 %{SOURCE1405} %{buildroot}%{_datadir}/pki/sb-certs/
install -m 0644 %{SOURCE1406} %{buildroot}%{_datadir}/pki/sb-certs/
install -m 0644 %{SOURCE1407} %{buildroot}%{_datadir}/pki/sb-certs/
install -m 0644 %{SOURCE1408} %{buildroot}%{_datadir}/pki/sb-certs/
## x86_64
# cer
install -m 0644 %{SOURCE1421} %{buildroot}%{_datadir}/pki/sb-certs/
install -m 0644 %{SOURCE1422} %{buildroot}%{_datadir}/pki/sb-certs/
install -m 0644 %{SOURCE1423} %{buildroot}%{_datadir}/pki/sb-certs/
install -m 0644 %{SOURCE1424} %{buildroot}%{_datadir}/pki/sb-certs/
install -m 0644 %{SOURCE1425} %{buildroot}%{_datadir}/pki/sb-certs/
# der
install -m 0644 %{SOURCE1426} %{buildroot}%{_datadir}/pki/sb-certs/
install -m 0644 %{SOURCE1427} %{buildroot}%{_datadir}/pki/sb-certs/
install -m 0644 %{SOURCE1428} %{buildroot}%{_datadir}/pki/sb-certs/
install -m 0644 %{SOURCE1429} %{buildroot}%{_datadir}/pki/sb-certs/
install -m 0644 %{SOURCE1430} %{buildroot}%{_datadir}/pki/sb-certs/
## aarch64
# cer
install -m 0644 %{SOURCE1441} %{buildroot}%{_datadir}/pki/sb-certs/
install -m 0644 %{SOURCE1442} %{buildroot}%{_datadir}/pki/sb-certs/
install -m 0644 %{SOURCE1443} %{buildroot}%{_datadir}/pki/sb-certs/
install -m 0644 %{SOURCE1444} %{buildroot}%{_datadir}/pki/sb-certs/
install -m 0644 %{SOURCE1445} %{buildroot}%{_datadir}/pki/sb-certs/
# der
install -m 0644 %{SOURCE1446} %{buildroot}%{_datadir}/pki/sb-certs/
install -m 0644 %{SOURCE1447} %{buildroot}%{_datadir}/pki/sb-certs/
install -m 0644 %{SOURCE1448} %{buildroot}%{_datadir}/pki/sb-certs/
install -m 0644 %{SOURCE1449} %{buildroot}%{_datadir}/pki/sb-certs/
install -m 0644 %{SOURCE1450} %{buildroot}%{_datadir}/pki/sb-certs/
 
# Placeholders
# x86_64
ln -sr %{buildroot}%{_datadir}/pki/sb-certs/rocky-root-ca.der %{buildroot}%{_datadir}/pki/sb-certs/secureboot-ca-x86_64.cer
ln -sr %{buildroot}%{_datadir}/pki/sb-certs/rocky-kernel.cer %{buildroot}%{_datadir}/pki/sb-certs/secureboot-kernel-x86_64.cer
ln -sr %{buildroot}%{_datadir}/pki/sb-certs/rocky-grub2.cer %{buildroot}%{_datadir}/pki/sb-certs/secureboot-grub2-x86_64.cer
ln -sr %{buildroot}%{_datadir}/pki/sb-certs/rocky-fwupd.cer %{buildroot}%{_datadir}/pki/sb-certs/secureboot-fwupd-x86_64.cer
ln -sr %{buildroot}%{_datadir}/pki/sb-certs/rocky-shim.cer %{buildroot}%{_datadir}/pki/sb-certs/secureboot-shim-x86_64.cer
ln -sr %{buildroot}%{_datadir}/pki/sb-certs/rocky-uki-virt.cer %{buildroot}%{_datadir}/pki/sb-certs/secureboot-uki-virt-x86_64.cer

# aarch64
ln -sr %{buildroot}%{_datadir}/pki/sb-certs/rocky-root-ca.der %{buildroot}%{_datadir}/pki/sb-certs/secureboot-ca-aarch64.cer
ln -sr %{buildroot}%{_datadir}/pki/sb-certs/rocky-kernel-aarch64.cer %{buildroot}%{_datadir}/pki/sb-certs/secureboot-kernel-aarch64.cer
ln -sr %{buildroot}%{_datadir}/pki/sb-certs/rocky-grub2-aarch64.cer %{buildroot}%{_datadir}/pki/sb-certs/secureboot-grub2-aarch64.cer
ln -sr %{buildroot}%{_datadir}/pki/sb-certs/rocky-fwupd-aarch64.cer %{buildroot}%{_datadir}/pki/sb-certs/secureboot-fwupd-aarch64.cer
ln -sr %{buildroot}%{_datadir}/pki/sb-certs/rocky-shim-aarch64.cer %{buildroot}%{_datadir}/pki/sb-certs/secureboot-shim-aarch64.cer
ln -sr %{buildroot}%{_datadir}/pki/sb-certs/rocky-uki-virt-aarch64.cer %{buildroot}%{_datadir}/pki/sb-certs/secureboot-uki-virt-aarch64.cer

# ppc64le
ln -sr %{buildroot}%{_datadir}/pki/sb-certs/rocky-root-ca.der %{buildroot}%{_datadir}/pki/sb-certs/secureboot-ca-ppc64le.cer
ln -sr %{buildroot}%{_datadir}/pki/sb-certs/rocky-kernel.der %{buildroot}%{_datadir}/pki/sb-certs/secureboot-kernel-ppc64le.cer
ln -sr %{buildroot}%{_datadir}/pki/sb-certs/rocky-grub2.der %{buildroot}%{_datadir}/pki/sb-certs/secureboot-grub2-ppc64le.cer
ln -sr %{buildroot}%{_datadir}/pki/sb-certs/rocky-fwupd.der %{buildroot}%{_datadir}/pki/sb-certs/secureboot-fwupd-ppc64le.cer
ln -sr %{buildroot}%{_datadir}/pki/sb-certs/rocky-shim.der %{buildroot}%{_datadir}/pki/sb-certs/secureboot-shim-ppc64le.cer
ln -sr %{buildroot}%{_datadir}/pki/sb-certs/rocky-uki-virt.cer %{buildroot}%{_datadir}/pki/sb-certs/secureboot-uki-virt-ppc64le.cer

# armhfp
ln -sr %{buildroot}%{_datadir}/pki/sb-certs/rocky-root-ca.der %{buildroot}%{_datadir}/pki/sb-certs/secureboot-ca-armhfp.cer
ln -sr %{buildroot}%{_datadir}/pki/sb-certs/rocky-kernel.cer %{buildroot}%{_datadir}/pki/sb-certs/secureboot-kernel-armhfp.cer
ln -sr %{buildroot}%{_datadir}/pki/sb-certs/rocky-grub2.cer %{buildroot}%{_datadir}/pki/sb-certs/secureboot-grub2-armhfp.cer
ln -sr %{buildroot}%{_datadir}/pki/sb-certs/rocky-fwupd.cer %{buildroot}%{_datadir}/pki/sb-certs/secureboot-fwupd-armhfp.cer
ln -sr %{buildroot}%{_datadir}/pki/sb-certs/rocky-shim.cer %{buildroot}%{_datadir}/pki/sb-certs/secureboot-shim-armhfp.cer
ln -sr %{buildroot}%{_datadir}/pki/sb-certs/rocky-uki-virt.cer %{buildroot}%{_datadir}/pki/sb-certs/secureboot-uki-virt-armhfp.cer

# s390x
ln -sr %{buildroot}%{_datadir}/pki/sb-certs/rocky-root-ca.der %{buildroot}%{_datadir}/pki/sb-certs/secureboot-ca-s390x.cer
ln -sr %{buildroot}%{_datadir}/pki/sb-certs/rocky-kernel.cer %{buildroot}%{_datadir}/pki/sb-certs/secureboot-kernel-s390x.cer
ln -sr %{buildroot}%{_datadir}/pki/sb-certs/rocky-grub2.cer %{buildroot}%{_datadir}/pki/sb-certs/secureboot-grub2-s390x.cer
ln -sr %{buildroot}%{_datadir}/pki/sb-certs/rocky-fwupd.cer %{buildroot}%{_datadir}/pki/sb-certs/secureboot-fwupd-s390x.cer
ln -sr %{buildroot}%{_datadir}/pki/sb-certs/rocky-shim.cer %{buildroot}%{_datadir}/pki/sb-certs/secureboot-shim-s390x.cer
ln -sr %{buildroot}%{_datadir}/pki/sb-certs/rocky-uki-virt.cer %{buildroot}%{_datadir}/pki/sb-certs/secureboot-uki-virt-s390x.cer

# symlinks for everybody
for x in $(ls %{buildroot}%{_datadir}/pki/sb-certs); do
  ln -sr %{buildroot}%{_datadir}/pki/sb-certs/${x} %{buildroot}%{_sysconfdir}/pki/sb-certs/${x}
done

# end secureboot section
################################################################################

################################################################################
# dnf repo section
install -d -m 0755 %{buildroot}%{_sysconfdir}/yum.repos.d
install -p -m 0644 %{SOURCE1200} %{buildroot}%{_sysconfdir}/yum.repos.d/
install -p -m 0644 %{SOURCE1201} %{buildroot}%{_sysconfdir}/yum.repos.d/
install -p -m 0644 %{SOURCE1202} %{buildroot}%{_sysconfdir}/yum.repos.d/
install -p -m 0644 %{SOURCE1203} %{buildroot}%{_sysconfdir}/yum.repos.d/

# dnf stuff
install -d -m 0755 %{buildroot}%{_sysconfdir}/dnf/vars
echo "%{contentdir}" > %{buildroot}%{_sysconfdir}/dnf/vars/contentdir
echo "%{sigcontent}" > %{buildroot}%{_sysconfdir}/dnf/vars/sigcontentdir
echo "%{?rltype}" > %{buildroot}%{_sysconfdir}/dnf/vars/rltype
echo "%{major}-stream" > %{buildroot}%{_sysconfdir}/dnf/vars/stream

# Copy out GPG keys
install -d -m 0755 %{buildroot}%{_sysconfdir}/pki/rpm-gpg
install -p -m 0644 %{SOURCE101} %{buildroot}%{_sysconfdir}/pki/rpm-gpg/
install -p -m 0644 %{SOURCE102} %{buildroot}%{_sysconfdir}/pki/rpm-gpg/
# end dnf repo section
################################################################################

################################################################################
# lookahead overrides
# TODO: Is there a cleaner way? 
%if %{with rllookahead}
install -m 0644 %{SOURCE400} %{buildroot}/%{_prefix}/lib/systemd/system-preset/85-display-manager.preset
install -m 0644 %{SOURCE401} %{buildroot}/%{_prefix}/lib/systemd/system-preset/90-default.preset
install -m 0644 %{SOURCE402} %{buildroot}/%{_prefix}/lib/systemd/user-preset/90-default-user.preset

install -m 0644 %{SOURCE403} %{buildroot}/%{_prefix}/lib/systemd/system-preset/99-default-disable.preset
install -m 0644 %{SOURCE403} %{buildroot}/%{_prefix}/lib/systemd/user-preset/99-default-disable.preset
install -m 0644 %{SOURCE404} %{buildroot}/%{_prefix}/lib/sysctl.d/50-redhat.conf
%endif
# lookahead replacements
################################################################################

%files
%license docs/LICENSE
%doc docs/Contributors docs/COMMUNITY-CHARTER
%dir %{_sysconfdir}/yum.repos.d
%{_sysconfdir}/redhat-release
%{_sysconfdir}/system-release
%{_sysconfdir}/rocky-release
%{_sysconfdir}/rocky-release-upstream
%config(noreplace) %{_sysconfdir}/os-release
%config %{_sysconfdir}/system-release-cpe
%config(noreplace) %{_sysconfdir}/issue
%config(noreplace) %{_sysconfdir}/issue.net
%dir %{_sysconfdir}/issue.d
%{_rpmmacrodir}/macros.dist
%{_datadir}/redhat-release
%{_datadir}/rocky-release
%{_prefix}/lib/os-release
%{_prefix}/lib/systemd/system-preset/*
%{_prefix}/lib/systemd/user-preset/*
%{_prefix}/lib/sysctl.d/50-redhat.conf
%{_mandir}/man1/rocky.1.gz

%files -n rocky-repos%{?rltype}
%license docs/LICENSE
%config(noreplace) %{_sysconfdir}/yum.repos.d/rocky.repo
%config(noreplace) %{_sysconfdir}/yum.repos.d/rocky-addons.repo
%config(noreplace) %{_sysconfdir}/yum.repos.d/rocky-extras.repo
%config(noreplace) %{_sysconfdir}/yum.repos.d/rocky-devel.repo
%config(noreplace) %{_sysconfdir}/dnf/vars/contentdir
%config(noreplace) %{_sysconfdir}/dnf/vars/sigcontentdir
%config(noreplace) %{_sysconfdir}/dnf/vars/rltype
%config(noreplace) %{_sysconfdir}/dnf/vars/stream

%files -n rocky-gpg-keys%{?rltype}
%{_sysconfdir}/pki/rpm-gpg/

%files -n rocky-sb-certs%{?rltype}
# care: resetting symlinks is intended
%dir %{_sysconfdir}/pki/sb-certs
%dir %{_datadir}/pki/sb-certs
%{_sysconfdir}/pki/sb-certs/*
%{_datadir}/pki/sb-certs/*

%changelog
* Fri Jul 18 2025 Louis Abel <label@resf.org> - 9.7-1.3
- Add releasever_major and minor

* Tue Jun 17 2025 Louis Abel <label@resf.org> - 9.7-1.2
- Enable mpa_registration.service
- Enable qgs.service

* Fri Apr 11 2025 Louis Abel <label@rockylinux.org> - 9.7-1.1
- Update SB certs
- Enable raid-check.timer
- Update IMA certificates

* Mon Feb 10 2025 Louis Abel <label@rockylinux.org> - 9.6-1.1
- Fix /etc/issue

* Mon May 27 2024 Louis Abel <label@rockylinux.org> - 9.5-1.2
- Backport distcore from 10
- Add vendor data for os-release

* Tue Apr 30 2024 Louis Abel <label@rockylinux.org> - 9.5-1.1
- Bump to 9.5

* Tue Apr 30 2024 Louis Abel <label@rockylinux.org> - 9.4-1.5
- Add nvidia SB certificates

* Sun Apr 07 2024 Louis Abel <label@rockylinux.org> - 9.4-1.3
- Add additional provides for rocky-sb-certs

* Wed Apr 03 2024 Louis Abel <label@rockylinux.org> - 9.4-1.2
- Update SB certs

* Wed Mar 27 2024 Louis Abel <label@rockylinux.org> - 9.4-1.1
- Preparation for 9.4

* Mon Mar 04 2024 Louis Abel <label@rockylinux.org> - 9.4-0.3
- Add kernel-bootcfg-boot-successful.service

* Fri Jan 12 2024 Louis Abel <label@rockylinux.org> - 9.4-0.2
- Improve presets for virtualization

* Fri Oct 20 2023 Louis Abel <label@rockylinux.org> - 9.4-0.1
- Bump to 9.4

* Fri Oct 20 2023 Louis Abel <label@rockylinux.org> - 9.3-0.6
- Add in true UKI-VIRT certificate
- Add aarch64 signing certificates
- Fix date in changelog

* Tue Sep 05 2023 Louis Abel <label@rockylinux.org> - 9.3-0.5
- Add placeholder certs for UKI-VIRT

* Sat Jun 10 2023 Louis Abel <label@rockylinux.org> - 9.3-0.4
- Define the distro macro

* Mon May 15 2023 Louis Abel <label@rockylinux.org> - 9.3-0.3
- Use DER format for ppc64le certificates for now

* Tue Apr 25 2023 Louis Abel <label@rockylinux.org> - 9.3-0.2
- Update secure boot certificates

* Thu Apr 06 2023 Louis Abel <label@rockylinux.org> - 9.3-0.1
- Bump main version to 9.3
- Enable obex

* Sun Jan 01 2023 Louis Abel <label@rockylinux.org> - 9.2-1.2
- Move macros.dist to a proper location

* Thu Dec 22 2022 Louis Abel <label@rockylinux.org> - 9.2-1.1
- Update devel repos (RLBT#0001354)
- Add SUPPORT_END with absolute EOL (See sig_core/#3)

* Wed Oct 19 2022 Louis Abel <label@rockylinux.org> - 9.1-1.10
- Change secure boot certificates

* Tue Oct 18 2022 Louis Abel <label@rockylinux.org> - 9.1-1.9
- Bump release version to match upstream

* Wed Sep 07 2022 Louis Abel <label@rockylinux.org> - 9.1-1.1
- Bump main version and prepare for upcoming beta

* Tue Aug 30 2022 Louis Abel <label@rockylinux.org> - 9.0-3.2
- Add stream dnf var

* Thu Jul 28 2022 Louis Abel <label@rockylinux.org> - 9.0-3.1
- Ensure distsuffix is part of disttag

* Wed Jul 20 2022 Louis Abel <label@rockylinux.org> - 9.0-2.2
- Fix mirrorlist URL for plus repository

* Thu Jun 30 2022 Louis Abel <label@rockylinux.org> - 9.0-2.1
- Prepare for release
- Ensure rltype is blank for stable releases

* Wed Jun 22 2022 Louis Abel <label@rockylinux.org> - 9.0-1.22
- Change to using mirrorlist

* Sun Jun 12 2022 Louis Abel <label@rockylinux.org> - 9.0-1.21
- Backport current SB certs for now
- Add logrotate timer and switcheroo
- Add missing macros
- Fix CPE values
- Remove /etc/centos-release file
- Add redhat and fix rocky tags in os-release
- Fix GPG key names to be consistent with SIG requirements
- Reduce number of repo files
- Change testing key to "testing" key from build system
- Add official "stable" key from build system
- List both GPG keys in repo files
- Fix rlpkg macro for gpg keys
- Add sig content dir
- Remove nplb as devel is technically it

* Mon Jan 10 2022 Louis Abel <label@rockylinux.org> - 9.0-1.1
- Add LOGO to /etc/os-release

* Tue Nov 30 2021 Louis Abel <label@rockylinux.org> - 9.0-1.0
- Init for Rocky Linux 9 (Blue Onyx)
- Sync with upstream
- Add direct LookAhead support
- Add direct Beta support
- Add spec file notes for packagers
- Add countme=1 to all base repos
