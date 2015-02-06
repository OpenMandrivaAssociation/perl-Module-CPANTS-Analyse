%define upstream_name    Module-CPANTS-Analyse
%define upstream_version 0.92

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Generate Kwalitee ratings for a distribution

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Module/Module-CPANTS-Analyse-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Archive::Any) >= 0.60.0
BuildRequires:	perl(Archive::Tar) >= 1.480.0
BuildRequires:	perl(Array::Diff) >= 0.40.0
BuildRequires:	perl(CPAN::DistnameInfo) >= 0.60.0
BuildRequires:	perl(Class::Accessor) >= 0.190.0
BuildRequires:	perl(Cwd)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(ExtUtils::Manifest)
BuildRequires:	perl(File::Find::Rule)
BuildRequires:	perl(File::Slurp)
BuildRequires:	perl(File::chdir)
BuildRequires:	perl(IO::Capture) >= 0.50.0
BuildRequires:	perl(LWP::Simple)
BuildRequires:	perl(List::MoreUtils)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Module::ExtractUse) >= 0.180.0
BuildRequires:	perl(Module::Pluggable) >= 2.960.0
BuildRequires:	perl(Module::Signature)
BuildRequires:	perl(Pod::Simple::Checker) >= 2.20.0
BuildRequires:	perl(Readonly)
BuildRequires:	perl(Set::Scalar)
BuildRequires:	perl(Software::License) >= 0.3.0
BuildRequires:	perl(Test::CPAN::Meta::YAML::Version)
BuildRequires:	perl(Test::Deep)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::NoWarnings)
BuildRequires:	perl(Test::Warn) >= 0.110.0
BuildRequires:	perl(Text::CSV_XS) >= 0.450.0
BuildRequires:	perl(YAML::Any) >= 0.810.0
BuildRequires:	perl(YAML::XS)
BuildRequires:	perl(version) >= 0.730.0
BuildArch:	noarch

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
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
#make test

%install
%makeinstall_std

%files
%doc AUTHORS Changes META.json META.yml MYMETA.yml README  TODO
%{_bindir}/*
%{perl_vendorlib}/Module
%{_mandir}/*/*



