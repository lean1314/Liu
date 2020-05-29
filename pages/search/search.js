// pages/search/search.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    thumbnail: ""
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var that = this
    wx.request({
      url: 'http://192.168.0.105:5002/p',
      data: {},
      header: {
        "content-Type": "application/json"
      },
      success: function (res) {
        that.setData({
          thumbnail: res.data,
        })
      }
    })
  },
  onsearchinputevent: function (e) {
    var value = e.detail.value;
    console.log(value);
    var that = this;
    that.setData({
      value: value
    })
  },




})