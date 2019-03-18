#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-MatrixModels
Version  : 0.4.1
Release  : 49
URL      : https://cran.r-project.org/src/contrib/MatrixModels_0.4-1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/MatrixModels_0.4-1.tar.gz
Summary  : Modelling with Sparse And Dense Matrices
Group    : Development/Tools
License  : GPL-2.0+
BuildRequires : buildreq-R

%description
No detailed description available

%prep
%setup -q -c -n MatrixModels

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552769521

%install
export SOURCE_DATE_EPOCH=1552769521
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library MatrixModels
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library MatrixModels
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library MatrixModels
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  MatrixModels || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/MatrixModels/DESCRIPTION
/usr/lib64/R/library/MatrixModels/INDEX
/usr/lib64/R/library/MatrixModels/Meta/Rd.rds
/usr/lib64/R/library/MatrixModels/Meta/features.rds
/usr/lib64/R/library/MatrixModels/Meta/hsearch.rds
/usr/lib64/R/library/MatrixModels/Meta/links.rds
/usr/lib64/R/library/MatrixModels/Meta/nsInfo.rds
/usr/lib64/R/library/MatrixModels/Meta/package.rds
/usr/lib64/R/library/MatrixModels/NAMESPACE
/usr/lib64/R/library/MatrixModels/R/MatrixModels
/usr/lib64/R/library/MatrixModels/R/MatrixModels.rdb
/usr/lib64/R/library/MatrixModels/R/MatrixModels.rdx
/usr/lib64/R/library/MatrixModels/help/AnIndex
/usr/lib64/R/library/MatrixModels/help/MatrixModels.rdb
/usr/lib64/R/library/MatrixModels/help/MatrixModels.rdx
/usr/lib64/R/library/MatrixModels/help/aliases.rds
/usr/lib64/R/library/MatrixModels/help/paths.rds
/usr/lib64/R/library/MatrixModels/html/00Index.html
/usr/lib64/R/library/MatrixModels/html/R.css
/usr/lib64/R/library/MatrixModels/tests/MModels.R
