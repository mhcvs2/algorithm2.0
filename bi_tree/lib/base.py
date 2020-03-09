from .utils import *
from ..aaa import pre_order_traverse, in_order_traverse, post_order_traverse, level_traverse


class LoopType(object):
    PRE = 'pre_order_traverse'
    IN = 'in_order_traverse'
    POST = 'post_order_traverse'
    LEVEL = 'level_traverse'

    FUN_MAPS = {
        PRE: pre_order_traverse,
        IN: in_order_traverse,
        POST: post_order_traverse,
        LEVEL: level_traverse
    }


def get_loop_fun_by_type(loop_type=None):
    default_fun = LoopType.FUN_MAPS.get(LoopType.PRE)
    return LoopType.FUN_MAPS.get(loop_type, default_fun)


class BiTreeTestBase(TestCase):

    def _validate(self, _type, bi_tree, expected):
        loop_func = get_loop_fun_by_type(_type)
        actual = []
        loop_func(bi_tree, lambda node: actual.append(node.data))
        try:
            self.assertListEqual(expected, actual, 'loop type: %s' % _type)
        except AssertionError as e:
            print_red(("%s validate fail, \n%s (actual), \n%s (expected)" % (_type, str(actual), str(expected))))
        else:
            print_blue("%s validate success" % _type)

    def validate(self, bi_tree, pre_order=None, in_order=None, post_order=None, level=None):
        to_validate_types = {
            LoopType.PRE: pre_order,
            LoopType.IN: in_order,
            LoopType.POST: post_order,
            LoopType.LEVEL: level
        }
        for _type, expected in to_validate_types.items():
            if expected:
                self._validate(_type, bi_tree, expected)
