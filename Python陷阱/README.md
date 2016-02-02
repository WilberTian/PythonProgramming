## 避免可变对象作为默认参数

在使用函数的过程中，经常会涉及默认参数。在Python中，当使用可变对象作为默认参数的时候，就可能产生非预期的结果。  

下面看一个例子：  

    def append_item(a = 1, b = []):
        b.append(a)
        print b
        
    append_item(a=1)
    append_item(a=3)
    append_item(a=5)  

结果为：

    [1]
    [1, 3]
    [1, 3, 5]
    
从结果中可以看到，当后面两次调用`append_item`函数的时候，函数参数b并没有被初始化为`[]`，而是保持了前面函数调用的值。  

之所以得到这个结果，是因为在Python中，**一个函数参数的默认值，仅仅在该函数定义的时候，被初始化一次**。    

下面看一个例子证明Python的这个特性：  

	class Test(object):  
	    def __init__(self):  
	        print("Init Test")  
	          
	def arg_init(a, b = Test()):  
	    print(a)  

    arg_init(1)  
	arg_init(3)  
	arg_init(5)  
    
    
结果为：

    Init Test
    1
    3
    5
	
    
从这个例子的结果就可以看到，`Test`类仅仅被实例化了一次，也就是说默认参数跟函数调用次数无关，仅仅在函数定义的时候被初始化一次。  

### 可变默认参数的正确使用
对于可变的默认参数，我们可以使用下面的模式来避免上面的非预期结果：

	def append_item(a = 1, b = None):
	    if b is None:
	        b = []
	    b.append(a)
	    print b
	    
	append_item(a=1)
	append_item(a=3)
	append_item(a=5)  
    
结果为：

	[1]
	[3]
	[5]


## Python中的作用域
Python的作用域解析顺序为Local、Enclosing、Global、Built-in，也就是说Python解释器会根据这个顺序解析变量。  

看一个简单的例子： 

	global_var = 0
	
	def outer_func():
	    outer_var = 1
	    
	    def inner_func():
	        inner_var = 2
	        
	        print "global_var is :", global_var
	        print "outer_var is :", outer_var
	        print "inner_var is :", inner_var
	        
	    inner_func()
	    
	outer_func()

结果为：

	global_var is : 0
	outer_var is : 1
	inner_var is : 2


在Python中，关于作用域有一点需要注意的是，**在一个作用域里面给一个变量赋值的时候，Python会认为这个变量是当前作用域的本地变量**。  

对于这一点也是比较容易理解的，对于下面代码`var_func`中给`num`变量进行了赋值，所以此处的`num`就是`var_func`作用域的本地变量。

	num = 0

	def var_func():
	    num = 1
	    print "num is :", num
	    
	var_func()

### 问题一
但是，当我们通过下面的方式使用变量的时候，就会产生问题了：

	num = 0
	
	def var_func():
	    print "num is :", num
	    num = 1
	    
	var_func()
    
结果如下，之所以产生这个错误，就是因为我们在`var_func`中给`num`变量进行了赋值，所以Python解释器会认为`num`是`var_func`作用域的本地变量，但是当代码执行到`print "num is :", num`语句的时候，`num`还是未定义。

	UnboundLocalError: local variable 'num' referenced before assignment

  

### 问题二
上面的错误还是比较明显的，还有一种比较隐蔽的错误形式如下：

	li = [1, 2, 3]
	
	def foo():
	    li.append(4)
	    print li
	    
	foo()
	
	def bar():
	    li +=[5]
	    print li
	    
	bar()
    
代码的结果为：

	[1, 2, 3, 4]
	UnboundLocalError: local variable 'li' referenced before assignment

在`foo`函数中，根据Python的作用域解析顺序，该函数中使用了全局的`li`变量；但是在`bar`函数中，对`li`变量进行了赋值，所以`li`会被当作`bar`作用域中的变量。

对于`bar`函数的这个问题，可以通过`global`关键字。

	li = [1, 2, 3]
	
	def foo():
	    li.append(4)
	    print li
	    
	foo()
	
	def bar():
	    global li
	    li +=[5]
	    print li
	    
	bar()
    
## 类属性隐藏
在Python中，有类属性和实例属性。类属性是属于类本身的，被所有的类实例共享。  

类属性可以通过类名访问和修改，也可以通过类实例进行访问和修改。但是，当实例定义了跟类同名的属性后，类属性就被隐藏了。  

看下面这个例子：

	class Student(object):
	    books = ["Python", "JavaScript", "CSS"]
	    def __init__(self, name, age):
	        self.name = name
	        self.age = age
	    pass
	    
	wilber = Student("Wilber", 27)
	print "%s is %d years old" %(wilber.name, wilber.age)
	
	print Student.books
	print wilber.books
	
	wilber.books = ["HTML", "AngularJS"]
	
	print Student.books
	print wilber.books
	
	del wilber.books
	
	print Student.books
	print wilber.books

代码的结果如下，起初`wilber`实例可以直接访问类的`books`属性，但是当实例`wilber`定义了名称为`books`的实例属性之后，`wilber`实例的`books`属性就“隐藏”了类的`books`属性；当删除了`wilber`实例的`books`属性之后，`wilber.books`就又对应类的`books`属性了。

	Wilber is 27 years old
	['Python', 'JavaScript', 'CSS']
	['Python', 'JavaScript', 'CSS']
	['Python', 'JavaScript', 'CSS']
	['HTML', 'AngularJS']
	['Python', 'JavaScript', 'CSS']
	['Python', 'JavaScript', 'CSS']
    
当在Python值使用继承的时候，也要注意类属性的隐藏。对于一个类，可以通过类的`__dict__`属性来查看所有的类属性。   

当通过类名来访问一个类属性的时候，会首先查找类的`__dict__`属性，如果没有找到类属性，就会继续查找父类。但是，如果子类定义了跟父类同名的类属性后，子类的类属性就会隐藏父类的类属性。

看一个例子：

	class A(object):
	    count = 1
	    
	class B(A):
	    pass    
	    
	class C(A):
	    pass        
	    
	print A.count, B.count, C.count      
	
	B.count = 2
	
	print A.count, B.count, C.count      
	
	A.count = 3
	
	print A.count, B.count, C.count     
    print B.__dict__
	print C.__dict__
    
结果如下，当类`B`定义了`count`这个类属性之后，就会隐藏父类的`count`属性：

	1 1 1
	1 2 1
	3 2 3
    {'count': 2, '__module__': '__main__', '__doc__': None}
	{'__module__': '__main__', '__doc__': None}
    
    
## tuple是“可变的”    
在Python中，tuple是不可变对象，但是这里的不可变指的是tuple这个容器总的元素不可变（确切的说是元素的id），但是元素的值是可以改变的。

	tpl = (1, 2, 3, [4, 5, 6])
	
	print id(tpl)
	print id(tpl[3])
	
	tpl[3].extend([7, 8])
	
	print tpl
	print id(tpl)
	print id(tpl[3])
    
代码结果如下，对于`tpl`对象，它的每个元素都是不可变的，但是`tpl[3]`是一个`list`对象。也就是说，对于这个`tpl`对象，`id(tpl[3])`是不可变的，但是`tpl[3]`确是可变的。

	36764576
	38639896
	(1, 2, 3, [4, 5, 6, 7, 8])
	36764576
	38639896

## Python的深浅拷贝
在对Python对象进行赋值的操作中，一定要注意对象的深浅拷贝，一不小心就可能踩坑了。  

当使用下面的操作的时候，会产生浅拷贝的效果：

- 使用切片[:]操作
- 使用工厂函数（如list/dir/set）
- 使用copy模块中的copy()函数

使用copy模块里面的浅拷贝函数copy()：

	import copy
	
	will = ["Will", 28, ["Python", "C#", "JavaScript"]]
	wilber = copy.copy(will)
	
	print id(will)
	print will
	print [id(ele) for ele in will]
	print id(wilber)
	print wilber
	print [id(ele) for ele in wilber]
	
	will[0] = "Wilber"
	will[2].append("CSS")
	print id(will)
	print will
	print [id(ele) for ele in will]
	print id(wilber)
	print wilber
	print [id(ele) for ele in wilber]
    
使用copy模块里面的深拷贝函数deepcopy()：  

	import copy
	
	will = ["Will", 28, ["Python", "C#", "JavaScript"]]
	wilber = copy.deepcopy(will)
	
	print id(will)
	print will
	print [id(ele) for ele in will]
	print id(wilber)
	print wilber
	print [id(ele) for ele in wilber]
	
	will[0] = "Wilber"
	will[2].append("CSS")
	print id(will)
	print will
	print [id(ele) for ele in will]
	print id(wilber)
	print wilber
	print [id(ele) for ele in wilber]

## 模块循环依赖
在Python中使用`import`导入模块的时候，有的时候会产生模块循环依赖，例如下面的例子，`module_x`模块和`module_y`模块相互依赖，运行`module_y.py`的时候就会产生错误。

	# module_x.py
	import module_y
	    
	def inc_count():
	    module_y.count += 1
	    print module_y.count
        
        
    # module_y.py
	import module_x
	
	count = 10
	
	def run():
	    module_x.inc_count()
	    
	run()            

其实，在编码的过程中就应当避免循环依赖的情况，或者代码重构的过程中消除循环依赖。  

当然，上面的问题也是可以解决的，常用的解决办法就是把引用关系搞清楚，让某个模块在真正需要的时候再导入（一般放到函数里面）。  

对于上面的例子，就可以把`module_x.py`修改为如下形式，在函数内部导入`module_y`：


	# module_x.py
	def inc_count():
	    import module_y
	    module_y.count += 1
	    print module_y.count