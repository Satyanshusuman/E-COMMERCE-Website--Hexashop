$('.fa-plus-square').click(function () {
    var id = $(this).attr("pid").toString();
	// console.log(id)
	  $.ajax({
		  type: 'get',
		  url: '/pluscart',
		  datatype:"text",
		  data: { 
				prod_id: id 
			},
		  success: function(data) {
			document.getElementById("amount").innerText= data.amount
			document.getElementById("totalamount").innerText=data.totalamount
			document.getElementById("total_qty").innerText=data.total_qty 

		  }
	  })
	})	


$('.fa-minus-square').click(function () {
	var id = $(this).attr("pid").toString();
	// console.log(id)
	$.ajax({
		type: 'get',
		url: '/minuscart',
		datatype:"text",
		data: { 
			  prod_id: id 
		  },
		success: function(data) {
		  document.getElementById("amount").innerText= data.amount
		  document.getElementById("totalamount").innerText=data.totalamount 
		  document.getElementById("total_qty").innerText=data.total_qty 

		}
		})
	})


	$('.fa-trash').click(function () {
		var id = $(this).attr("pid").toString();
		var eml= this
		$.ajax({
			type: 'get',
			url: '/delcart',
			datatype:"text",
			data: { 
				  prod_id: id 
			  },
			success: function(data) {
			  document.getElementById("amount").innerText= data.amount
			  document.getElementById("totalamount").innerText=data.totalamount 
			  document.getElementById("total_qty").innerText=data.total_qty 
			  eml.parentNode.parentNode.parentNode.remove()
			}
			})
		})