%include	/usr/lib/rpm/macros.perl
Summary:	Apache-DBI perl module
Summary(pl):	Modu³ perla Apache-DBI
Name:		perl-Apache-DBI
Version:	0.88
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	http://www.cpan.org/modules/by-module/Apache/ApacheDBI-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Apache-DBI perl module.

%description -l pl
Modu³ perla Apache-DBI.

%prep
%setup -q -n ApacheDBI-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README Changes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Apache/*.pm
%{_mandir}/man3/*
