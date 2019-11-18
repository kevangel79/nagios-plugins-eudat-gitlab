Name:		nagios-plugins-eudat-gitlab
Version:	1.1
Release:	1%{?dist}
Summary:	Nagios GitLab liveness probe
License:	GPLv3+
Packager:	Kyriakos Gkinis <kyrginis@admin.grnet.gr>

Source:		%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

Requires:	util-linux
Requires:	wget

%description
Nagios probe to check GitLab health by checking GitLab liveness endpoint

%prep
%setup -q

%define _unpackaged_files_terminate_build 0 

%install

install -d %{buildroot}/%{_libexecdir}/argo-monitoring/probes/eudat-gitlab
install -m 755 check_gitlab_liveness.sh %{buildroot}/%{_libexecdir}/argo-monitoring/probes/eudat-gitlab/check_gitlab_liveness.sh

%files
%dir /%{_libexecdir}/argo-monitoring
%dir /%{_libexecdir}/argo-monitoring/probes/
%dir /%{_libexecdir}/argo-monitoring/probes/eudat-gitlab

%attr(0755,root,root) /%{_libexecdir}/argo-monitoring/probes/eudat-gitlab/check_gitlab_liveness.sh

%changelog
* Mon Nov 18 2019 Kyriakos Gkinis <kyrginis@admin.grnet.gr> - 1.1-1
- Update probe to the new simpler Gitlab liveness response (after Gitlab 12.4).
- Remove jq dependency

* Fri Oct 27 2017 Kyriakos Gkinis <kyrginis@admin.grnet.gr> - 0.2-1
- Improve parsing of liveness JSON
- Added jq to the requirements

* Fri Oct 13 2017 Kyriakos Gkinis <kyrginis@admin.grnet.gr> - 0.1-1
- Initial version of the package
