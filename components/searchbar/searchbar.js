// components/searchbar.js
Component({
  properties: {
    isnavigator: {
      type: Boolean,
      value: false
    }
  },

  data: {
    value: "",
  },
  methods: {
    inputxxx: function (e) {
      var value = e.detail.value;
      var detail = { "value": value };
      // var options = {};
      this.triggerEvent("searchinput", detail);

    },
  }
})
