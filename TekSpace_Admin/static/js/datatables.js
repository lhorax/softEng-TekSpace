$(document).ready(function() {
	var table=$('#dataTable').DataTable( {
        dom: "<'row'<'col-sm-4'l><'col-sm-4 text-center'B><'col-sm-4'f>>" +
      "<'row'<'col-sm-12'tr>>" +
      "<'row'<'col-sm-5'i><'col-sm-7'p>>",
        buttons: [
			{	
				extend:'excelHtml5',
				text:'Excel File',
				className:'excelBtn',
				exportOptions: {
					columns: ':not(:last-child)',
				},
				title:'Student Report Summary'
			},
			{	
				extend: 'pdfHtml5',
				text: 'PDF File',
				exportOptions: {
					columns: ':not(:last-child)',
				},
				title:'Student Report Summary'
			}
        ],
		select:true
    } );
	$('#min').on('change', function() {
		table.draw();
	});
	$('#max').on('change',function () {
		table.draw();
	});
} );

$.fn.dataTable.ext.search.push(
	function (settings, data, dataIndex, rowData, counter) {
		if(settings.nTable.id!='dataTable'){return true;}
		var start = new Date($('#min').val());
		start.setHours(0);
		var end = new Date($('#max').val());
		end.setHours(0);
		var filter = new Date(data[0]);
		if (start == "Invalid Date" && end == "Invalid Date") { return true; }
		if (start == "Invalid Date" && filter <= end) { return true;}
		if(end == "Invalid Date" && filter >= start) {return true;}
		if (filter >= start && filter <= end) { return true; }
		return false;
	}
);