// pages/comment/comment.js
var util = require('../../utils/util.js');
Page({

  /**
   * 页面的初始数据
   */
  data: {
    contents:[],
    pingfena: "",
    pingjiaa: "",
    userid:1,
    productid:"",
    shijian:"",
    subvalue:"",
    // popErrorMsg: "",
  },
  /**
   * 获取input评分
   */
  inputpingfen: function (e) {
    this.setData({
      pingfena: e.detail.value,
    })
  },

  /**
   * 获取input评价
   */
  inputpingjia: function (e) {
    this.setData({
      pingjiaa: e.detail.value
    })
  },
  /**
   * 获取评价数据
   */
  formSubmit: function (e) {
    var that = this
    var userid=that.data.userid
    var productid=that.data.productid
    var time =util.formatTime(new Date())
    var shijian=time.toString()
    console.log("你的id是:"+userid+",商品id是:"+productid)
    var subValue = e.detail.value.pingfena
    var x = 1
      if (subValue == null || subValue == ""||!(/(^[0-9]*$)/.test(subValue))||subValue>10||subValue<0) {
        // x=x+1
        // that.data.x=x
        // wx.showToast({
        //   title:'请输入0～10的评分',
        //   duration:2000})
        console.log("输入错误")
        wx.showModal({
          title: '提示',
          content: '请输入0～10分的评分',
          success:function(res){
                if(res.confirm){
                  console.log('弹框后点确定')
                }else{
                    console.log('弹框后点取消')
                }
          }
        })
      //   that.setData(
      //    { popErrorMsg: "请输入0～10的评分"
      //   }
      //  ) 
      }
      else{
        wx.request({
          url: 'http://192.168.0.105:5002/ajax_post',
          method: "POST",
          data: {
            "pingfena": e.detail.value.pingfena,
             "pingjiaa": e.detail.value.pingjiaa,
             "userid":userid,
             "productid":productid,
             "shijian":shijian
             },
          header: {
            'content-type': 'application/json'
          },
          success: function (res) {
            console.log("啊啊啊成功啦,你的评分是:" + res.data.grade + "你的评价是:" + res.data.content+",此刻是"+res.data.date)
          }
        })
      }
    },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var that=this;
    that.setData({
      productid:that.options.pid,
    })
  },
  navigateBack: function () {
    var pages= getCurrentPages();
    if(pages.length>1){
      var prepage = pages[pages.length-2]
    }
    prepage.onShow()
    
    wx.navigateBack({
      delta:1
    });//返回上一页

  },
  

  
})