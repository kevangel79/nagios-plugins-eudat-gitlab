Name:		nagios-plugins-eudat-gitlab
Version:	1.0
Release:	2%{?dist}
Summary:	Nagios gitlab
License:	GPLv3+
Packager:	Themis Zamani <themiszamani@gmail.com>

Source:		%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

Requires:	util-linux
Requires:	wget
Requires:	jq

%description
Nagios probes to check functionality of cas server

%prep
%setup -q

%define _unpackaged_files_terminate_build 0 

%install

install -d %{buildroot}/%{_libexecdir}/argo-monitoring/probes/eudat-gitlab
install -d %{buildroot}/%{_sysconfdir}/nagios/plugins/eudat-gitlab
install -m 755 check_gitlab_liveness.sh %{buildroot}/%{_libexecdir}/argo-monitoring/probes/eudat-gitlab/check_gitlab_liveness.sh

%files
%dir /%{_libexecdir}/argo-monitoring
%dir /%{_libexecdir}/argo-monitoring/probes/
%dir /%{_libexecdir}/argo-monitoring/probes/eudat-gitlab

%attr(0755,root,root) /%{_libexecdir}/argo-monitoring/probes/eudat-gitlab/check_gitlab_liveness.sh

%changelog
* Wed Apr 17 2019 Themis Zamani <themiszamani@gmail.com> - 1.0-1
- Update package requirements, Kyriakos Gkinis <kyrginis@admin.grnet.gr> 
- Improve parsing of liveness JSON, Kyriakos Gkinis <kyrginis@admin.grnet.gr> 
- Added jq to the requirements, Kyriakos Gkinis <kyrginis@admin.grnet.gr> 

* Tue Jul 2 2018 Themis Zamani <themiszamani@gmail.com> - 1.0-1
- Initial version of the package. 


