'''
A child is playing with a ball on the nth floor of a tall building. The height of this floor, h, is known.

He drops the ball out of the window. The ball bounces (for example), to two-thirds of its height (a bounce of 0.66).

His mother looks out of a window 1.5 meters from the ground.

How many times will the mother see the ball pass in front of her window (including when it's falling and bouncing?

Three conditions must be met for a valid experiment:
Float parameter "h" in meters must be greater than 0
Float parameter "bounce" must be greater than 0 and less than 1
Float parameter "window" must be less than h.
If all three conditions above are fulfilled, return a positive integer, otherwise return -1.

Note:
The ball can only be seen if the height of the rebounding ball is strictly greater than the window parameter.

Example:
- h = 3, bounce = 0.66, window = 1.5, result is 3
- h = 3, bounce = 1, window = 1.5, result is -1

(Condition 2) not fulfilled).

'''

def bouncing_ball(h, bounce, window):
    if h > window > 0 and 1 > bounce > 0:
        see = 1
        while h >= window:
            h = h*bounce
            if h > window:
                see += 2
            # elif h == window:
            #     see += 1
        return see
    else:
        return -1
### TDD
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

    @classmethod
    def it(cls, param):
        print(param)

Test.assert_equals(bouncing_ball(2, 0.5, 1), 1)
Test.assert_equals(bouncing_ball(3, 0.66, 1.5), 3)
Test.assert_equals(bouncing_ball(30, 0.66, 1.5), 15)
Test.assert_equals(bouncing_ball(30, 0.75, 1.5), 21)
Test.assert_equals(bouncing_ball(3, 0.5, 3.5), -1)
Test.assert_equals(bouncing_ball(3, 1, 1.5), -1)