Name:		nginx-ldap-auth
Version:	0.0.3
Release:	1%{?dist}
Summary:	nginx LDAP authentication daemon

Group:		System Environment/Daemons
License:	2-clause BSD-like license
URL:		https://github.com/nginxinc/nginx-ldap-auth
Source0:	nginx-ldap-auth-%{version}.tar.gz

Requires:	python-ldap

%description
Reference implementation of method for authenticating users on behalf of
servers proxied by NGINX or NGINX Plus.

%prep
%setup -q

%install

echo RPM_BUILD_ROOT=$RPM_BUILD_ROOT
echo buildroot=%buildroot
echo _bindir=%_bindir
echo _unitdir=%_unitdir

mkdir -p %buildroot%_bindir
install -m755 nginx-ldap-auth-daemon.py %buildroot%_bindir/nginx-ldap-auth-daemon
mkdir -p %buildroot%_unitdir
mkdir -p %buildroot/etc/init.d
install -m755 nginx-ldap-auth-daemon-init.sh %buildroot/etc/init.d/nginx-ldap-auth-daemon

%files
%doc README.md nginx-ldap-auth.conf LICENSE
%_bindir/nginx-ldap-auth-daemon
/etc/init.d/nginx-ldap-auth-daemon

%post
#chkconfig --list nginx-ldap-auth-daemon

%changelog
* Thu Jan 12 2017 Sergei Hlupnov
- Removed systemd for amzn linux
* Wed Nov 02 2016 Konstantin Pavlov <thresh@nginx.com> 0.0.3-1
- Initial release
