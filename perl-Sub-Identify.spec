%define modname	Sub-Identify

Summary:	Retrieve names of code references
Name:		perl-%{modname}
Version:	0.14
Release:	2
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/pod/Sub::Identify
Source0:	http://www.cpan.org/modules/by-module/Sub/%{modname}-%{version}.tar.gz
BuildRequires:	perl-devel
BuildRequires:	perl(Test::More)

%description
Sub::Identify allows you to retrieve the real name of code references. For
this, it uses perl's introspection mechanism, provided by the B module.

%prep
%autosetup -p1 -n %{modname}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%make_install

%files
%doc Changes
%{perl_vendorarch}/Sub
%{perl_vendorarch}/auto/Sub
%{_mandir}/man3/*
