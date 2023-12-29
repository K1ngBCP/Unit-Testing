import unittest

def kelpersegi(s):
    return 4*s 

def luaspersegi(s):
    return s * s

def kelpersegipanjang(p, l):
    return 2*(p + l)

def luaspersegipanjang(p, l):
    return p * l

def kellingkaran(r):
    return 2 * 3.14 * r

def luaslingkaran(r):
    return 3.14 * r * r

def kelsegitiga(s1,s2,s3):
    return s1 + s2 + s3

def luassegitiga(a, t):
    return 0.5 * (a * t)

def kelbelahketupat(s):
    return 4*s

def luasbelahketupat(d1, d2):
    return 0.5 * d1 * d2

def keljajargenjang(a, sm):
    return 2 * (a +sm)

def luasjajargenjang(a, t):
    return a * t

def keltrapesium(sa, sm,st,t):
    return sa + sm + st + t

def luastrapesium(sa, sb,t):
    return ((sa + sb) * t) * 0.5

def kellayanglayang(s1, s2):
    return 2 * (s1 + s2)

def luaslayanglayang(d1,d2):
    return (d1 * d2) * 0.5

class TestKalkulatorbangundatar(unittest.TestCase):
    def test_kelpersegi(self):
        hasil = kelpersegi(8)
        self.assertEqual(hasil, 32)

    def test_luaspersegi(self):
        hasil = luaspersegi(10)
        self.assertEqual(hasil, 100)

    def test_kelpersegipanjang(self):
        hasil = kelpersegipanjang(6, 2)
        self.assertEqual(hasil, 16)

    def test_luaspersegipanjang(self):
        hasil = luaspersegipanjang(8, 4)
        self.assertEqual(hasil, 32)

    def test_kellingkaran(self):
        hasil = kellingkaran(3)
        self.assertEqual(hasil, 18.84)

    def test_luaslingkaran(self):
        hasil = luaslingkaran(9)
        self.assertEqual(hasil, 254.34)

    def test_kelsegitiga(self):
        hasil = kelsegitiga(10, 4,  5)
        self.assertEqual(hasil, 19)

    def test_luassegitiga(self):
        hasil = luassegitiga(6, 2)
        self.assertEqual(hasil, 6)

    def test_kelbelahketupat(self):
        hasil = kelbelahketupat( 4)
        self.assertEqual(hasil, 16)

    def test_luasbelahketupat(self):
        hasil = luasbelahketupat(8, 3)
        self.assertEqual(hasil, 12)

    def test_keljajargenjang(self):
        hasil = keljajargenjang(10, 4)
        self.assertEqual(hasil, 28)

    def test_luasjajargenjang(self):
        hasil = luasjajargenjang(6, 2)
        self.assertEqual(hasil, 12)

    def test_keltrapesium(self):
        hasil = keltrapesium(8, 4,7,4)
        self.assertEqual(hasil, 23)

    def test_luastrapesium(self):
        hasil = luastrapesium(10, 4, 6)
        self.assertEqual(hasil, 42)

    def test_kellayanglayang(self):
        hasil = kellayanglayang(6, 2)
        self.assertEqual(hasil, 16)

    def test_luaslayanglayang(self):
        hasil = luaslayanglayang(8, 4)
        self.assertEqual(hasil, 16)

    def test_keltrapesium(self):
        hasil = keltrapesium(8, 4,7,4)
        self.assertEqual(hasil, 20)

    def test_luastrapesium(self):
        hasil = luastrapesium(10, 4, 6)
        self.assertEqual(hasil, 49)

    def test_kellayanglayang(self):
        hasil = kellayanglayang(6, 2)
        self.assertEqual(hasil, 18)

    def test_luaslayanglayang(self):
        hasil = luaslayanglayang(8, 4)
        self.assertEqual(hasil, 15)


if __name__ == '__main__':
    unittest.main()
