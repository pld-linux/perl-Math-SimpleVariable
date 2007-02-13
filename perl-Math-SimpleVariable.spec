#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Math
%define		pnam	SimpleVariable
Summary:	Math::SimpleVariable - simple representation of mathematical variables
Summary(pl.UTF-8):	Math::SimpleVariable - prosta reprezentacja zmiennych matematycznych
Name:		perl-Math-SimpleVariable
Version:	0.03
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0b7b45d71edab401e7aa64a0ad292eed
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math::SimpleVariable is a simple representation of mathematical
variables, with an obligatory name and an optional value. This class
on itself might not seem very useful at first sight, but you might
want to derive different types of variables for some application. That
way, objects of the derived variable class can be accessed
interchangeably with the here provided protocols.

%description -l pl.UTF-8
Math::SimpleVariable to prosta reprezentacja zmiennych matematycznych,
z obowiązkową nazwą i opcjonalną wartością. Ta klasa sama w sobie może
nie wydawać się zbyt przydatna, ale można z niej wyprowadzić różne
typy zmiennych dla aplikacji. W ten sposób, do obiektów tych nowych
klas można odwoływać się przy pomocy udostępnionych przez ten moduł
protokołów.

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
%doc Changes README
%{perl_vendorlib}/Math/SimpleVariable.pm
%{_mandir}/man3/*
