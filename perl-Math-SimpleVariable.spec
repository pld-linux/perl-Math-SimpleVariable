#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Math
%define		pnam	SimpleVariable
Summary:	Math::SimpleVariable - simple representation of mathematical variables
Summary(pl):	Math::SimpleVariable - prosta reprezentacja zmiennych matematycznych
Name:		perl-Math-SimpleVariable
Version:	0.03
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math::SimpleVariable is a simple representation of mathematical
variables, with an obligatory name and an optional value. This class
on itself might not seem very useful at first sight, but you might
want to derive different types of variables for some application. That
way, objects of the derived variable class can be accessed
interchangeably with the here provided protocols.

%description -l pl
Math::SimpleVariable to prosta reprezentacja zmiennych matematycznych,
z obowi±zkow± nazw± i opcjonaln± warto¶ci±. Ta klasa sama w sobie mo¿e
nie wydawaæ siê zbyt przydatna, ale mo¿na z niej wyprowadziæ ró¿ne
typy zmiennych dla aplikacji. W ten sposób, do obiektów tych nowych
klas mo¿na odwo³ywaæ siê przy pomocy udostêpmionych przez ten modu³
protoko³ów.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/Math/SimpleVariable.pm
%{_mandir}/man3/*
