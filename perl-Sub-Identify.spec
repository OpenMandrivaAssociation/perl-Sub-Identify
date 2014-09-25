%define modname	Sub-Identify
%define modver 0.08

Summary:	Retrieve names of code references
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Sub/%{modname}-%{modver}.tar.gz
BuildRequires:	perl-devel

%description
Sub::Identify allows you to retrieve the real name of code references. For
this, it uses perl's introspection mechanism, provided by the B module.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes
%{perl_vendorarch}/Sub
%{perl_vendorarch}/auto/Sub
%{_mandir}/man3/*
