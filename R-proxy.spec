%bcond_with bootstrap
%global packname  proxy
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.4_7
Release:          2
Summary:          Distance and Similarity Measures
Group:            Sciences/Mathematics
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.4-7.tar.gz
%if %{without bootstrap}
Requires:         R-cba
%endif
BuildRequires:    R-devel Rmath-devel texlive-collection-latex
%if %{without bootstrap}
BuildRequires:    R-cba
%endif

%description
Provides an extensible framework for the effcient calculation of auto- and
cross-proximities, along with implementations of the most popular ones.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%if %{without bootstrap}
%check
%{_bindir}/R CMD check %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
