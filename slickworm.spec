Summary:	Slickworm is a shoot-em-up game
Summary(pl):	Slickworm jest strzelank±
Name:		slickworm
Version:	0.2.0
Release:	1
License:	BSD
Group:		Applications/Games
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	ab074a53c76d55ec1807e64c4dd6dae4
Source1:	%{name}.desktop
Patch0:		%{name}-data.patch
URL:		http://slickworm.sourceforge.net/
BuildRequires:	OpenAL-devel
BuildRequires:	OpenGL-devel
Buildrequires:	SDL-devel >= 1.2.0
BuildRequires:	SDL_image-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libjpeg-devel
BuildRequires:	libvorbis-devel
BuildRequires:	ode-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_bindir	%{_prefix}/games
%define	_datadir	%{_prefix}/share/games
%define	_noautoreqdep	libGL.so.1 libGLU.so.1

%description
Slickworm is a shoot-em-up game. Not just any shoot-em-up, but one
that harks back to the shoot-em-ups of old that pitted one lone
combatant against swarms of increasingly tough little beasties.

%description -l pl
Slickworm jest strzelank± nawi±zuj±c± do starych gier, w których jeden
walczy przeciwko ca³emu mrowiu coraz trudniejszych ma³ych bestii.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-sound
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Games/Arcade

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games/Arcade

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_applnkdir}/Games/Arcade/*
