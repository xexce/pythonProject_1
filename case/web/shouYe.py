# coding=utf-8
from selenium import webdriver
from public.login import Mylogin
from selenium.webdriver.common.action_chains import  ActionChains
import unittest
import os
import time

class TestShouye(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()      #初始化一个driver
        self.driver.get("http://101.133.169.100/yuns/index.php")    #打开项目地址
        self.driver.maximize_window()         #初始窗口大小，使窗口最大化
        time.sleep(5)                         #初始网页等待时间，使窗口等待5s后执行
        print("starttime:" + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())))
                                              #初始化用例开始时间
    def tearDown(self):
        filedir = "G:/test/001/"              #定义一个路径地址，存储截屏
        if not os.path.exists(filedir):       #os是一个判断模块，判断以上有没有路径的存在
            os.makedirs(os.path.join('D:/', 'test', 'screenshot'))     #如果没有则创建一个新的路径
        print("endTime:" + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())))
                                              #print用例结束时间
        screen_name = filedir + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + ".png"
                                              #定义截图的时间，图片的名称和图片的格式
        self.driver.get_screenshot_as_file(screen_name)
                                              #通过get_screenshot执行上一步定义的截图要求
        self.driver.quit()                    #关闭浏览器


    def testShouye01_01(self):
        '''测试首页导航文案显示是否正常'''
        Mylogin(self.driver).login()
        firstPageNavi = self.driver.find_element_by_xpath("//div[@class='top']/span")
        loginText = self.driver.find_element_by_css_selector("div.login>a:nth-child(1)")
        regisText = self.driver.find_element_by_css_selector("div.login>a:nth-child(3)")

        self.assertEqual("亲，欢迎您来到云商系统商城！",firstPageNavi.text)
        self.assertEqual("134****0674", loginText.text)
        self.assertEqual("退出", regisText.text)
        # self.assertNotEqual("dd", regisText.text)
        #
        # self.assertIn("云商系统商城",firstPageNavi.text)
        #
        # self.assertTrue(self.driver.find_element_by_xpath("//div[@class='top']/span").is_displayed())
        # self.assertFalse(firstPageNavi.is_displayed())
        #
        # if loginText.text == "177****0979":
        #     print("等于")
        # else:
        #     print("不等于")
        #     self.driver.find_element_by_xpath("王麻子")



    def testShouye01_02(self):
        '''验证搜索内容无时，提示语是否正常'''
        Mylogin(self.driver).login()
        self.driver.find_element_by_xpath("/html/body/div/div/div/div/form/input[1]").send_keys("王麻子")
        self.driver.find_element_by_xpath("/html/body/div/div/div/div/form/input[2]").click()
        time.sleep(2)
        searchText = self.driver.find_element_by_xpath("//div[@class='nomsg']")
        self.assertEqual(searchText.text, "抱歉，没有找到相关的商品")

    def testShouye01_04(self):
        #验证首页秒杀按钮点击跳转是否正确
        self.driver.find_element_by_link_text('秒杀').click()
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[1])
        ATCL=self.driver.find_element_by_link_text("限时抢购")
        self.assertEqual(ATCL.text,"限时抢购")

    def testShouye01_05(self):
        #验证正待你秒杀信息似乎否正确
        test=self.driver.find_element_by_css_selector("body > div:nth-child(5) > div > div > div.name > div > a")
        print(test.text)
        self.assertEqual(test.text,"整点秒杀")


    def testShouye01_06(self):
        #验证首页商品导航栏是否正确
        shouye_tset=self.driver.find_element_by_css_selector('body > div.nav_bar > div > div.nav_pub > a:nth-child(1)')
        miaosha_test=self.driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/a[2]')
        youhuijuan_test=self.driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/a[3]')
        xiatian_tset=self.driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/a[4]")
        nanzhuang_test=self.driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/a[5]')
        self.assertEqual(shouye_tset.text,"首页")
        self.assertEqual(miaosha_test.text,'秒杀')
        self.assertEqual(youhuijuan_test.text,'优惠券')
        self.assertEqual(xiatian_tset.text,'夏天最热')
        self.assertEqual(nanzhuang_test.text,'男装活动')


    def testShouye01_07(self):
        #验证首页”精选商品分类“标题信息是否正确
        jingxuan_test=self.driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/span/em')
        self.assertEqual(jingxuan_test.text,"精选商品分类")

    def testShouye01_08(self):
        #验证精选商品分类中男装女装，二级分类菜单展示
        nan_01=self.driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/dl[1]/dt/div/span/a')
        ActionChains(self.driver).move_to_element(nan_01).perform()
        neiyi_test=self.driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/dl[1]/div/div[1]/div/a')
        fushi_test=self.driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/dl[1]/div/div[2]/div/a')
        neiyiwa_test=self.driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/dl[1]/div/div[3]/div/a')
        self.assertEqual(neiyi_test.text,'男士内衣')
        self.assertEqual(fushi_test.text,'服饰配件')
        self.assertEqual(neiyiwa_test.text,'内衣袜品')

    def testShouye01_08(self):
        #验证精选商品分类男装女装，中的男士二级菜单点击是否正确条状
        nan_01=self.driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/dl[1]/dt/div/span/a')
        ActionChains(self.driver).move_to_element(nan_01).perform()
        neiyi_test = self.driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/dl[1]/div/div[1]/div/a').click()
        RE=self.driver.find_element_by_xpath('/html/body/div[4]/div/div[3]/div[2]/div')
        self.assertEqual(RE.text,'抱歉，没有找到相关的商品')


    def testShouye01_09(self):
        #验证精选商品分类男装女装，中的女装二级菜单点击是否正确条状
        nan_01 = self.driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/dl[1]/dt/div/span/a')
        ActionChains(self.driver).move_to_element(nan_01).perform()
        nvzhuang_test = self.driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/dl[1]/div/div[5]/div/a').click()
        RE = self.driver.find_element_by_xpath('/html/body/div[4]/div/div[4]/div[2]')
        self.assertNotEqual(RE.text, '抱歉，没有找到相关的商品')

    def testShouye01_10(self):
        #验证秒杀界面”限时抢购“信息是否正确
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/a[2]').click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        xianshi_test=self.driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div/a[1]')
        self.assertEqual(xianshi_test.text,'限时抢购')

    # def testShouye01_11(self):
    #    # 验证将商品”dsa倒萨倒萨“，点击加入购物车，并在购物车里验证存在
    #         self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[1]/div[2]/a').click()
    #         self.driver.find_element_by_css_selector("//a[@data-id='9'and@title='紫']").click()
    #         self.driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div[2]/div[3]/dl[2]/dd/a[1]').click()
    #         self.driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div[2]/div[4]/div[2]/a[1]').click()
    #         self.driver.find_element_by_xpath('/html/div/div[2]/a[1]').click()
    #         self.driver.switch_to.window(self.driver.window_handles[1])
    #         shanchu_test=self.driver.find_element_by_class_name('cart_del del')
    #         self.assertEqual(shanchu_test.text,"删除")

    def testShouye01_12(self):
         #验证产品列表界面，品牌信息
        self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/div[2]/dl[1]/dd/a').click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        pinpai_test=self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/dl/dt')
        self.assertNotEqual(pinpai_test.text,"品牌")


    def testShouye01_13(self):
        #验证首页精选商品分类”鞋子包包二级展示正确
        bag=self.driver.find_element_by_link_text("鞋子包包")
        ActionChains(self.driver).move_to_element(bag).perform()
        Tbag=self.driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/dl[2]/div/div[1]/div/a')
        self.assertEqual(Tbag.text,"女鞋")

    def testShouye01_14(self):
        # 验证首页精选商品分类”家电数码二级展示正确
        shuma=self.driver.find_element_by_link_text("家电数码")
        ActionChains(self.driver).move_to_element(shuma).perform()
        jiadian=self.driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/dl[3]/div/div[1]/div/a')
        self.assertEqual(jiadian.text,"家电")

    def testShouye01_15(self):
        # 验证首页精选商品分类”美妆珠宝二级展示正确
        zhubao=self.driver.find_element_by_link_text("美妆珠宝")
        ActionChains(self.driver).move_to_element(zhubao).perform()
        meizhuang=self.driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/dl[4]/div/div[1]/div/a')
        self.assertEqual(meizhuang.text,"美妆")

    def testShouye01_16(self):
        #验证首页精选商品分类：家居纺织二级菜单展示是否正确
        jiaju=self.driver.find_element_by_link_text("家居纺织")
        ActionChains(self.driver).move_to_element(jiaju).perform()
        jiafang=self.driver.find_element_by_link_text('家纺')
        self.assertEqual(jiafang.text,"家纺")


    def testShouye01_17(self):
        # 验证首页精选商品分类：美食特产二级菜单展示是否正确
        meishi=self.driver.find_element_by_link_text("美食特产")
        ActionChains(self.driver).move_to_element(meishi).perform()
        shengxian=self.driver.find_element_by_link_text("生鲜")
        self.assertEqual("生鲜",shengxian.text)


    def testShouye01_18(self):
        # 验证首页精选商品分类：母婴玩具二级菜单展示是否正确
        muyin=self.driver.find_element_by_link_text("母婴玩具")
        ActionChains(self.driver).move_to_element(muyin).perform()
        fushi=self.driver.find_element_by_link_text("营养辅食")
        self.assertEqual("营养辅食",fushi.text)


    def testShouye01_19(self):
        # 验证首页精选商品分类：母婴玩具二级菜单展示是否正确
        sport=self.driver.find_element_by_link_text("运动健身")
        ActionChains(self.driver).move_to_element(sport).perform()
        music=self.driver.find_element_by_link_text("乐器")
        self.assertEqual("乐器",music.text)


    def testShouye01_20(self):
        #验证优惠券界面跳转是否正确
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/a[3]').click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        ready=self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div[3]/a")
        self.assertEqual(ready.text,"立即领取")


    def testShouye01_21(self):
        #验证夏天最热连接跳转是否正确
        self.driver.find_element_by_link_text("夏天最热").click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        Url=self.driver.current_url
        self.assertEqual(Url,"http://101.133.169.100/yuns/index.php/goods?cid=16")


    def testShouye01_22(self):
        #验证男装活动连接跳转是否正确
        self.driver.find_element_by_link_text("男装活动").click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        Url=self.driver.current_url
        self.assertEqual(Url,"http://101.133.169.100/yuns/index.php/goods/theme?id=6")

    def testShouye01_23(self):
        #验证品牌街连接跳转是否正确
        self.driver.find_element_by_link_text("品牌街").click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        Url=self.driver.current_url
        self.assertEqual(Url,'http://101.133.169.100/yuns/index.php/goods/brand.html')






if __name__ == "__main__":
    unittest.main()


