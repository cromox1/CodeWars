def domain_name(url):
    if "//" in url:
        return url.split("//")[1].split("/")[0].replace("www.", "").split(".")[0]
    else:
        return url.split("/")[0].replace("www.", "").split(".")[0]

#### TDD TESTING
class Test:
    def assert_equals(value, expected):
        from nose.tools import assert_equal
        try:
            assert_equal(value, expected)
            print('EQUAL   --> got =', value, " ==  ex =", expected)
        except:
            print(' UNEQUAL !!!! // ### ')
            print('  v = ' + str(value))
            print('  x = ' + str(expected))
    @classmethod
    def describe(cls, param):
        print(param)

## TDD
Test.assert_equals(domain_name("http://github.com/carbonfive/raygun"), "github")
Test.assert_equals(domain_name("http://www.zombie-bites.com"), "zombie-bites")
Test.assert_equals(domain_name("https://www.cnet.com"), "cnet")