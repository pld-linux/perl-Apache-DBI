%include	/usr/lib/rpm/macros.perl
Summary:	Apache::DBI - Initiate a persistent database connection
Summary(pl):	Modu³ Apache::DBI - inicjuj±cy ci±g³e po³±czenie z baz±
Name:		perl-Apache-DBI
Version:	0.88
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/Apache/ApacheDBI-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module initiates a persistent database connection.

%description -l pl
Ten modu³ nawi±zuje ci±g³e po³±czenie z baz± danych.

%prep
%setup -q -n ApacheDBI-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes
%{perl_sitelib}/Apache/*.pm
%{_mandir}/man3/*
