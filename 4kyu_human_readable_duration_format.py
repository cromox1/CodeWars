def format_duration(seconds):
    if seconds == 0:
        return 'now'
    elif seconds < 0:
        return 'Error - value error'
    else:
        # dict2 = secs_to_y_d_h_m_s(seconds)
        # dict1 = {k:v for k,v in dict2.items() if v != 0}
        dict1 = secs_to_yr_dy_hr_mn_sc(seconds)
        text = ''
        for k,v in dict1.items():
            if v == 1:
                text = text + ', ' + str(v) + ' ' + k
            elif v > 1:
                text = text + ', ' + str(v) + ' ' + k + 's'
        text2 = text[2:]
        if len(text2.split(',')) > 1:
            return ','.join(text2.split(',')[:-1]) + " and" + text2.split(',')[-1]
        else:
            return text2

def secs_to_yr_dy_hr_mn_sc(seconds):
    years = int(seconds/(365*24*60*60))
    days = int(seconds/(24*60*60)) - (years*365)
    hours = int(seconds/(60*60)) - (days*24) - (years*365*24)
    mins = int(seconds/60) - (hours*60) - (days*24*60) - (years*365*24*60)
    secs = seconds - (mins*60) - (hours*60*60) - (days*24*60*60) - (years*365*24*60*60)
    return {'year':years, 'day':days, 'hour':hours, 'minute':mins, 'second':secs}

#### TDD TESTING
class Test:
    def assert_equals(value, expected):
        from nose.tools import assert_equal
        try:
            assert_equal(value, expected)
            print('EQUAL   --> v =', value, " ==  x =", expected)
        except:
            message = ' // # ' + str(value) + ' should == ' + str(expected)
            print('UNEQUAL!! --> v =', value, " !=  x =", expected, message)

    @classmethod
    def describe(cls, param):
        print(param)

Test.assert_equals(format_duration(0), "now")
Test.assert_equals(format_duration(1), "1 second")
Test.assert_equals(format_duration(62), "1 minute and 2 seconds")
Test.assert_equals(format_duration(120), "2 minutes")
Test.assert_equals(format_duration(3600), "1 hour")
Test.assert_equals(format_duration(7200), "2 hours")
Test.assert_equals(format_duration(3662), "1 hour, 1 minute and 2 seconds")
Test.assert_equals(format_duration(1640467), "18 days, 23 hours, 41 minutes and 7 seconds")
Test.assert_equals(format_duration(33506460), "1 year, 22 days, 19 hours and 21 minutes")
Test.assert_equals(format_duration(31536001), "1 year and 1 second")
Test.assert_equals(format_duration(33501661), "1 year, 22 days, 18 hours, 1 minute and 1 second")
Test.assert_equals(format_duration(31626061), "1 year, 1 day, 1 hour, 1 minute and 1 second")
Test.assert_equals(format_duration(63252122), "2 years, 2 days, 2 hours, 2 minutes and 2 seconds")