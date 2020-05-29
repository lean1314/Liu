// components/stars/stars.js
Component({
  /**
   * 组件的属性列表
   */
  properties: {
    rate:{
      type:Number,
      value:0
    },
    starsize:{
      type:Number,
      value:25//rpx
    },
    fontsize:{
      type:Number,
      value:20//rpx
    },
    fontcolor:{
      type:String,
      value:"#494949"
    },
    istext:{
      type:Boolean,
      value:true
    }

  },

  /**
   * 组件的初始数据
   */
  data: {

  },

  /**
   * 组件的方法列表
   */
  methods: {

  },
  lifetimes:{
    attached:function(){
      var that = this;
      var rate = that.properties.rate;
      var intRate = parseInt(rate);
      var yellow = parseInt(intRate/2);
      var half = intRate%2;
      var grey = 5-yellow-half;
      var yellows = [];
      var halfs = [];
      var greys = [];
      for(var index=1;index<=yellow;index++){
        yellows.push(index);
      }
      for(var index=1;index<=half;index++){
        halfs.push(index);
      }
      for(var index=1;index<=grey;index++){
        greys.push(index);
      }
      var ratetext = rate && rate > 0 ? rate.toFixed(1):"未评分"
        that.setData({
        yellows:yellows,
        halfs:halfs,
        greys:greys,
        ratetext:ratetext,
      });
    }
  }
})
