_pkgname=astrosuite
pkgname=python+$_pkgname
pkgver=1.00-r
pkgrel=1
pkgdesc="Astronomy research-focused software collection written in Python"
arch=('any')
url="https://github.com/squimble/astrosuite/tree/main"
license=('MIT')
depends=('python')
makedepends=('git' 'python-build' 'python-installer' 'python-wheel' 'python-setup')
provides=("${pkgname%}")
conflicts=("${pkgname%}")
source=("git+%{https://github.com/squimble/astrosuite}.git#branch=main")
md5sums=('SKIP')

build(){
	cd "$_pkgname"
	python -m build --wheel --no-isolation

}

package(){
	cd "$_pkgname"
	python -m installer --destdir="$pkgdir" dist/*.whl

	install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

