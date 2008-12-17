%define module	Sub-Identify
%define name	perl-%{module}
%define version	0.04
%define	release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Retrieve names of code references
License:	GPL or Artistic
Group:		Development/Perl
Url:		    http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Sub/%{module}-%{version}.tar.gz
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Sub::Identify allows you to retrieve the real name of code references. For
this, it uses perl's introspection mechanism, provided by the B module.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes
%{perl_vendorarch}/Sub
%{perl_vendorarch}/auto/Sub
%{_mandir}/*/*
