#
# Conditional build:
%bcond_with	tests	# perform "make test"
			# fail while DBD::mysql is present
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Apache
%define	pnam	DBI
Summary:	Apache::DBI - initiate a persistent database connection
Summary(pl):	Apache::DBI - inicjowanie trwa³ego po³±czenia z baz±
Name:		perl-Apache-DBI
Version:	0.94
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	70a90a6d96b3563a204996e0f8122e61
BuildRequires:	perl-devel >= 1:5.8.0
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
Modu³y Apache::DBI i Apache::AuthDBI s± przeznaczone do u¿ywania
³±cznie z serwerem Apache z wbudowanym interpreterem Perla takim jak
mod_perl. Zapewniaj± obs³ugê podstawowego uwierzytelnienia i
autoryzacji, a tak¿e obs³ugê ci±g³ych po³±czeñ z baz± danych poprzez
ogólny interfejs dostêpu do baz danych Perla (DBI).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
