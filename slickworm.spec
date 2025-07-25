Summary:	Slickworm is a shoot-em-up game
Summary(pl.UTF-8):	Slickworm jest strzelanką
Name:		slickworm
Version:	0.4.1
Release:	0.1
License:	BSD
Group:		Applications/Games
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	c1a24992207fb4f1a1086bcff787ef6f
Source1:	%{name}.desktop
Patch0:		%{name}-data.patch
Patch1:		%{name}-include.patch
Patch2:		%{name}-graphicssystemopengl.patch
URL:		http://slickworm.sourceforge.net/
BuildRequires:	OpenAL-devel
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel >= 1.2.0
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

%description -l pl.UTF-8
Slickworm jest strzelanką nawiązującą do starych gier, w których jeden
walczy przeciwko całemu mrowiu coraz trudniejszych małych bestii.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-sound
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/slickworm.desktop
