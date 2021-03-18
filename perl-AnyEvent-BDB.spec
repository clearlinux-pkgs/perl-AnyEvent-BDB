#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-AnyEvent-BDB
Version  : 1.1
Release  : 6
URL      : https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/AnyEvent-BDB-1.1.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/AnyEvent-BDB-1.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-AnyEvent-BDB-license = %{version}-%{release}
Requires: perl-AnyEvent-BDB-perl = %{version}-%{release}
Requires: perl(AnyEvent)
Requires: perl(BDB)
BuildRequires : buildreq-cpan
BuildRequires : perl(AnyEvent)
BuildRequires : perl(BDB)
BuildRequires : perl(common::sense)

%description
NAME
AnyEvent::BDB - truly asynchronous berkeley db access
SYNOPSIS
use AnyEvent::BDB;
use BDB;

%package dev
Summary: dev components for the perl-AnyEvent-BDB package.
Group: Development
Provides: perl-AnyEvent-BDB-devel = %{version}-%{release}
Requires: perl-AnyEvent-BDB = %{version}-%{release}

%description dev
dev components for the perl-AnyEvent-BDB package.


%package license
Summary: license components for the perl-AnyEvent-BDB package.
Group: Default

%description license
license components for the perl-AnyEvent-BDB package.


%package perl
Summary: perl components for the perl-AnyEvent-BDB package.
Group: Default
Requires: perl-AnyEvent-BDB = %{version}-%{release}

%description perl
perl components for the perl-AnyEvent-BDB package.


%prep
%setup -q -n AnyEvent-BDB-1.1
cd %{_builddir}/AnyEvent-BDB-1.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-AnyEvent-BDB
cp %{_builddir}/AnyEvent-BDB-1.1/COPYING %{buildroot}/usr/share/package-licenses/perl-AnyEvent-BDB/9a56f3b919dfc8fced3803e165a2e38de62646e5
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/AnyEvent::BDB.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-AnyEvent-BDB/9a56f3b919dfc8fced3803e165a2e38de62646e5

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.32.1/AnyEvent/BDB.pm
