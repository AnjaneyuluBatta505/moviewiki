$("document").ready(function(){
	$.each($('textarea'), function(index, obj){
		name = $(obj).attr("name");
		CKEDITOR.replace(name);
	});
	$.each($('select'), function(index, obj){
		$(obj).attr("style", "width:100%;")
	});
	$("select").select2({dropdownAutoWidth : true,
    width: 'auto'});
});