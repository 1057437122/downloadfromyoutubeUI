var index_layer;
jQuery('#analysis_url').click(function(){
  url = jQuery('#origin_url').val();
alert(url);
  jQuery.ajax({
    url:'/get_video_info',
    type:'POST',
    data:{'url':url},
    success:function(res){
      layer.close(index_layer);
      index_layer = layer.open({
	  type: 1,
	  skin: 'layui-layer-rim', //加上边框
	  area: ['420px', '240px'], //宽高
	  content: res
	});
    },
    error:function(res){
      console.log(res);
    },
    beforeSend:function(res){
      //
    }
  });
})
