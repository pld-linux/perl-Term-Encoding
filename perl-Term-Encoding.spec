#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Term
%define	pnam	Encoding
Summary:	Term::Encoding - Detect encoding of the current terminal
Summary(pl.UTF-8):	Term::Encoding - wykrywanie kodowania bieżącego terminala
Name:		perl-Term-Encoding
Version:	0.02
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Term/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	67b7fb38ec7779a3fb79a047fd7edbb5
URL:		http://search.cpan.org/dist/Term-Encoding/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Term::Encoding is a simple module to detect an encoding the current
terminal expects, in various ways.

%description -l pl.UTF-8
Term::Encoding to prosty moduł do wykrywania w różny sposób kodowania
oczekiwanego przez bieżący terminal.

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
%doc Changes
%{perl_vendorlib}/Term/*.pm
%{_mandir}/man3/*
