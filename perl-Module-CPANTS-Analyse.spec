%define upstream_name    Module-CPANTS-Analyse
%define upstream_version 0.85

Name:           perl-%{upstream_name}
Version:        %perl_convert_version %{upstream_version}
Release:        %mkrel 1

Summary:        Generate Kwalitee ratings for a distribution
License:        GPL+ or Artistic
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%{upstream_name}
Source0:        http://www.cpan.org/modules/by-module/Module/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
BuildRequires:  perl(Archive::Any)
BuildRequires:  perl(Array::Diff)
BuildRequires:  perl(Class::Accessor)
BuildRequires:  perl(CPAN::DistnameInfo)
BuildRequires:  perl(File::Find::Rule)
BuildRequires:  perl(File::Slurp)
BuildRequires:  perl(IO::Capture::Stdout)
BuildRequires:  perl(IO::Zlib)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(LWP::Simple)
BuildRequires:  perl(Module::ExtractUse)
BuildRequires:  perl(Module::Pluggable)
BuildRequires:  perl(Pod::Simple)
BuildRequires:  perl(Readonly)
BuildRequires:  perl(Software::LicenseUtils)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(Test::YAML::Meta)
BuildRequires:  perl(Text::CSV_XS)
BuildRequires:  perl(YAML)
BuildRequires:  perl(YAML::Syck)
BuildRequires:  perl(version)
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

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
%setup -q -n %{upstream_name}-%{upstream_version}

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

