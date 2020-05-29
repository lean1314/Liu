
Page({

  /**
   * 页面的初始数据
   */
  data: {
    swiperCurrent: 0,
    indicatorDots: true,
    autoplay: true,
    interval: 3000,
    duration: 800,
    circular: true,
//  圆点样式
    indicatorCo:"#494949",
    indicatoraAC:"#ffffff",
    imgUrls: [
      'https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=1207305924,1848450926&fm=26&gp=0.jpg',
      'https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=1719740252,3807250852&fm=26&gp=0.jpg',
      'https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=869092693,2759062651&fm=26&gp=0.jpg'
    ]
  },
  // // 轮播图的切换事件
  swiperChange: function (e) {
    this.setData({
      swiperCurrent: e.detail.current
    })
  },
  // //点击指示点切换
  // chuangEvent: function (e) {
  //   this.setData({
  //     swiperCurrent: e.currentTarget.id
  //   })
  // },
  // //点击图片触发事件
  // swipclick: function (e) {
  //   console.log(this.data.swiperCurrent);
  //   wx.switchTab({
  //     url: this.data.links[this.data.swiperCurrent]
  //   })
  // },
 
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function () {
 

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