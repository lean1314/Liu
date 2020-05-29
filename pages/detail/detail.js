// pages/detail/detail.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    pinglun:"",
    detail:"",
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (detail) {
    var pid = detail.pid;
    console.log("商品ID是:"+pid);
    // console.log(detail)
    var that =this
          wx.request({
            url: 'http://192.168.0.105:5002/p',
            data:{},
            header:{
              "content-Type":"application/json"
            },
            success:function(res){
              that.setData({
                detail:res.data,
                pid:pid
              })
            }
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
  onShow: function (options) {
    var that =this
    wx.request({
      url: 'http://192.168.0.105:5002/c',
      data:{},
      header:{
        "content-Type":"application/json"
      },
      success:function(res){
        
        that.setData({
          pinglun:res.data
        });
      }
    
    })

  



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

  },

})