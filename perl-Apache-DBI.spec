%include	/usr/lib/rpm/macros.perl
%define	pdir	Apache
%define	pnam	DBI
Summary:	Apache::DBI - Initiate a persistent database connection
Summary(pl):	Modu³ Apache::DBI - inicjuj±cy ci±g³e po³±czenie z baz±
Name:		perl-%{pdir}-%{pnam}
Version:	0.89
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Apache::DBI and Apache::AuthDBI modules are supposed to be used with
the Apache server together with an embedded perl interpreter like
mod_perl. They provide support for basic authentication and
authorization as well as support for persistent database connections
via Perl's Database Independent Interface (DBI).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
%{perl_sitelib}/%{pdir}/*.pm
%{_mandir}/man3/*
