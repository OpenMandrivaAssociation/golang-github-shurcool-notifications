# Run tests in check section
%bcond_without check

%global goipath         github.com/shurcooL/notifications
%global commit          627ab5aea122bf029d0f8f6c3d44e614b4a33361

%global common_description %{expand:
Notifications service definition for Go.}

%gometa

Name:           %{goname}
Version:        0
Release:        0.3%{?dist}
Summary:        Notifications service definition for Go
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires: golang(dmitri.shuralyov.com/route/github)
BuildRequires: golang(github.com/google/go-github/github)
BuildRequires: golang(github.com/google/go-querystring/query)
BuildRequires: golang(github.com/gregjones/httpcache)
BuildRequires: golang(github.com/shurcooL/githubv4)
BuildRequires: golang(github.com/shurcooL/users)
BuildRequires: golang(github.com/shurcooL/webdavfs/vfsutil)
BuildRequires: golang(golang.org/x/net/webdav)

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%doc README.md


%changelog
* Fri Oct 26 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.3-20181026git627ab5a
- Bump to commit 627ab5aea122bf029d0f8f6c3d44e614b4a33361

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git3ad6f2c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 24 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20180420git3ad6f2c
- First package for Fedora

