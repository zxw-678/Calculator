import pytest
import yaml
from python_code.calc import Calculator

with open("./datas/calc.yaml") as f:
    datas = yaml.safe_load(f)['add']
    add_datas = datas['datas']
    print(add_datas)
    myid = datas['myid']
    print(myid)

with open("./datas/calc.yaml") as f:
    datas1 = yaml.safe_load(f)['div']
    div_datas = datas1['datas1']
    print(div_datas)
    myid1 = datas1['myid1']
    print(myid1)

# def test_a():
# #     print("测试用例a")

class TestCalc:
    def setup_class(self):
        print("开始计算")
        # 实例化计算器类
        self.calc = Calculator()
    def teardown_class(self):
        print("计算结束")

    @pytest.mark.parametrize(
        "a, b, expect",
        add_datas,ids=myid
    )
    def test_add(self, a, b, expect):
        # 实例化计算器类
        # calc = Calculator()
        # 调用add方法
        result = self.calc.add(a, b)
        if isinstance(result,float):
            result = round(result, 2)
        # 得到结果之后，需要写断言
        assert result == expect
        print(f"{a}+{b}={expect}")

    @pytest.mark.parametrize(
        "a, b, expect",
        div_datas, ids=myid1
    )
        # 除法
    def test_div(self, a, b, expect):
        result1 = self.calc.div(a, b)
        assert result1 == expect
        print(f"{a}/{b}={expect}")

    # def test_add2(self):
    #     result = self.calc.add(0.1, 0.2)
    #     assert round(result,2) == 0.3
    # def test_add1(self):
    #     # 实例化计算器类
    #     # calc = Calculator()
    #     # 调用add方法
    #     result = self.calc.add(0.1, 0.1)
    #     # 得到结果之后，需要写断言
    #     assert result == 0.2
    #
    # def test_add2(self):
    #     # b 实例化计算器类
    #     # calc = Calculator()
    #     # 调用add方法
    #     result = self.calc.add(-1, -2)
    #     # 得到结果之后，需要写断言
    #     assert result == -3

