// pages/list1/list1.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    thumbnail:"",
    pt:"",
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var that = this;
    console.log("商品类别是:"+options.pt);
    this.setData({
      pt:options.pt
    })
   /** if(pt == 1){
      var that =this
      wx.request({
        url: 'http://localhost:5002/p1',
        data:{},
        header:{
          "content-Type":"application/json"
        },
        success:function(res){
          that.setData({
            thumbnail:res.data
          })
        }
        })
    }
    else if(pt == 2){
      var that =this
      wx.request({
        url: 'http://localhost:5002/p2',
        data:{},
        header:{
          "content-Type":"application/json"
        },
        success:function(res){
          that.setData({
            thumbnail:res.data
          })
        }
        })
    }
    else if(pt == 3){
      var that =this
      wx.request({
        url: 'http://localhost:5002/p3',
        data:{},
        header:{
          "content-Type":"application/json"
        },
        success:function(res){
          that.setData({
            thumbnail:res.data
          })
        }
        })
    }
    else if(pt == 4){
      var that =this
      wx.request({
        url: 'http://localhost:5002/p4',
        data:{},
        header:{
          "content-Type":"application/json"
        },
        success:function(res){
          that.setData({
            thumbnail:res.data
          })
        }
        })
    }
    else if(pt == 5){
      var that =this
      wx.request({
        url: 'http://localhost:5002/p5',
        data:{},
        header:{
          "content-Type":"application/json"
        },
        success:function(res){
          that.setData({
            thumbnail:res.data
          })
        }
        })
    }
    else{
      var that =this
      wx.request({
        url: 'http://localhost:5002/p6',
        data:{},
        header:{
          "content-Type":"application/json"
        },
        success:function(res){
          that.setData({
            thumbnail:res.data
          })
        }
        })
    }*/
    wx:wx.request({
      url: 'http://192.168.0.105:5002/p',
      data: '',
      header: {
        "content-Type": "application/json"
      },
      success: function(res) {
        that.setData({
          thumbnail: res.data
        })
      },
      fail: function(res) {},
      complete: function(res) {},
    })
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})