%include	/usr/lib/rpm/macros.perl
%define	pdir	Apache
%define	pnam	DBI
Summary:	Apache::DBI - Initiate a persistent database connection
Summary(pl):	Modu� Apache::DBI - inicjuj�cy ci�g�e po��czenie z baz�
Name:		perl-%{pdir}-%{pnam}
Version:	0.93
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2ef8460467ef7d9adab9fd1ce388a6a6
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Apache::DBI and Apache::AuthDBI modules are supposed to be used with
the Apache server together with an embedded perl interpreter like
mod_perl. They provide support for basic authentication and
authorization as well as support for persistent database connections
via Perl's Database Independent Interface (DBI).

%description -l pl
Modu�y Apache::DBI i Apache::AuthDBI s� przeznaczone do u�ywania
��cznie z serwerem Apache z wbudowanym interpreterem Perla takim jak
mod_perl. Zapewniaj� obs�ug� podstawowego uwierzytelnienia i
autoryzacji, a tak�e obs�ug� ci�g�ych po��cze� z baz� danych poprzez
og�lny interfejs dost�pu do baz danych Perla (DBI).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
