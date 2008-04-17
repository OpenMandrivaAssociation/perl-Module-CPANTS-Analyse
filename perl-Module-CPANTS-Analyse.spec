%define module  Module-CPANTS-Analyse
%define name    perl-%{module}
%define version 0.81
%define release %mkrel 1

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Generate Kwalitee ratings for a distribution
License:        GPL or Artistic
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Module/%{module}-%{version}.tar.gz
%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
BuildRequires:  perl-version
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::YAML::Meta)
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(Array::Diff)
BuildRequires:  perl(Archive::Any)
BuildRequires:  perl(Module::Pluggable)
BuildRequires:  perl(Module::ExtractUse)
BuildRequires:  perl(Pod::Simple)
BuildRequires:  perl(CPAN::DistnameInfo)
BuildRequires:  perl(Class::Accessor)
BuildRequires:  perl(IO::Capture::Stdout)
BuildRequires:  perl(YAML)
BuildRequires:  perl(YAML::Syck)
BuildRequires:  perl(IO::Zlib)
BuildRequires:  perl(Software::LicenseUtils)
BuildRequires:  perl(File::Find::Rule)
BuildRequires:  perl(List::MoreUtils)
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description 
Kwalitee is an automatically-measurable gauge of how good your software is.
That's very different from quality, which a computer really can't measure in a
general sense. (If you can, you've solved a hard problem in computer science.)

In the world of the CPAN, the CPANTS project (CPAN Testing Service; also a
funny acronym on its own) measures Kwalitee with several metrics. If you plan
to release a distribution to the CPAN -- or even within your own organization
-- testing its Kwalitee before creating a release can help you improve your
quality as well.

Test::Kwalitee and a short test file will do this for you automatically.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{_bindir}/*
%{perl_vendorlib}/Module
%{_mandir}/*/*


