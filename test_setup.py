
def setup_module():
    print("模块级别 setup")

def teardown_module():
    print("模块级别 teardown")

def setup_function():
    print("函数级别 setup")

def teardown_function():
    print("函数级别 teardown")

def test_func1():
    print("函数func1")

class TestDemo:

    def setup_class(self):
        print("类级别 setup")

    def teardown_class(self):
        print("类级别 teardown")
    def setup(self):
        print("方法级别 setup")

    def teardown(self):
        print("方法级别 teardowm")

    def test_demo1(self):
        print("测试方法test_demo1")

    def test_demo2(self):
        print("测试方法test_demo2")

class TestDemo2:

    def setup_class(self):
        print("类级别 setup")

    def teardown_class(self):
        print("类级别 teardown")
    def setup(self):
        print("方法级别 setup")

    def teardown(self):
        print("方法级别 teardowm")

    def test_demo1(self):
        print("测试方法test_demo1")

    def test_demo2(self):
        print("测试方法test_demo2")