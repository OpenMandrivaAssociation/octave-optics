%global octpkg optics

Summary:	Functions covering various aspects of optics with Octave
Name:		octave-optics
Version:	0.1.4
Release:	2
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://packages.octave.org/optics/
Source0:	https://downloads.sourceforge.net/octave/optics-%{version}.tar.gz

BuildRequires:  octave-devel >= 3.2.0

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

BuildArch:	noarch

%description
Functions covering various aspects of optics.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

%build
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

